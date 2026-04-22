"""
Translation tool for ui.dev React lesson HTML files.

Usage:
  python translate_tool.py extract <file>      # produce JSON of English strings
  python translate_tool.py apply <file> <json> # apply translations from JSON

Strategy:
  We work directly on the raw HTML as text, using precisely-delimited
  regex replacements based on tag boundaries. We never re-serialize the
  HTML (SingleFile output is huge and whitespace-sensitive), we only
  replace the inner text of specific leaf elements.

  Elements we translate:
    <p>, <li>, <h1..h6>, <span>, <strong>, <em>, <a>,
    <button>, <label>, <option>, <title>, <small>, <div>,
    <figcaption>, <blockquote>, <th>, <td>, <summary>

  We do NOT translate:
    text inside <code>, <pre>, <script>, <style>, <svg>, <noscript>
    URLs, attribute values (except title/alt/placeholder – handled specially),
    or text that is only code symbols / contains no letters.
"""
import os
import re
import sys
import json
import html
from collections import OrderedDict

BASE = "D:/Personal/Downloads/react"

# Tags whose *direct* text we translate (leaf-only text nodes).
TRANSLATABLE_TAGS = [
    'p', 'li', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'span', 'strong', 'em', 'b', 'i', 'u',
    'a', 'button', 'label', 'option', 'title', 'small', 'div',
    'figcaption', 'blockquote', 'th', 'td', 'summary',
    'dt', 'dd', 'caption',
]

# Regions we must never descend into.
SKIP_REGION_RE = re.compile(
    r'<(script|style|svg|noscript|code|pre)\b[^>]*>.*?</\1\s*>',
    re.DOTALL | re.IGNORECASE,
)

# Self-closing script/style are extremely rare in this corpus, ignore.


def mask_skip_regions(text):
    """Replace <script>/<style>/... with placeholders so we don't touch them.

    Returns (masked_text, placeholders_list) where masked_text contains
    \x00SKIP#N\x00 markers.
    """
    placeholders = []

    def repl(m):
        placeholders.append(m.group(0))
        return f"\x00SKIP#{len(placeholders)-1}\x00"

    masked = SKIP_REGION_RE.sub(repl, text)
    return masked, placeholders


def unmask(text, placeholders):
    def repl(m):
        idx = int(m.group(1))
        return placeholders[idx]
    return re.sub(r'\x00SKIP#(\d+)\x00', repl, text)


# Pattern to find simple <tag ...>TEXT</tag> pairs where TEXT has no '<'.
LEAF_RE = re.compile(
    r'(<(' + '|'.join(TRANSLATABLE_TAGS) + r')\b[^>]*>)'  # opening tag
    r'([^<]+?)'                                           # plain text content
    r'(</\2\s*>)',                                        # matching close
    re.IGNORECASE,
)


SKIP_RE = re.compile(r'\x00SKIP#\d+\x00')


def is_translatable(s):
    stripped = s.strip()
    if not stripped:
        return False
    # Strip away SKIP placeholders – if nothing meaningful remains, skip.
    without_skips = SKIP_RE.sub('', stripped).strip()
    if not without_skips:
        return False
    # Needs at least one ASCII letter.
    if not re.search(r'[A-Za-z]', without_skips):
        return False
    # Avoid single identifier-looking tokens.
    if re.fullmatch(r'[A-Za-z_][\w.]*', without_skips):
        return False
    # Skip numbers + letters (e.g. "1080p", "720p").
    if re.fullmatch(r'\d+[A-Za-z]+', without_skips):
        return False
    # Skip obvious file names.
    if re.fullmatch(r'[\w.]+\.(html|jsx?|tsx?|css|json|md)', without_skips):
        return False
    return True


def extract_fragments(html_text):
    """Return ordered unique list of translatable fragments preserving order."""
    masked, placeholders = mask_skip_regions(html_text)
    seen = OrderedDict()
    for m in LEAF_RE.finditer(masked):
        raw = m.group(3)
        if is_translatable(raw):
            # Normalize leading/trailing whitespace as separate for re-insertion,
            # but key stores the stripped content.
            key = raw.strip()
            if key not in seen:
                seen[key] = True
    return list(seen.keys())


def apply_translations(html_text, translations):
    """Replace translatable text inside leaf tags with translations.

    translations: dict mapping English stripped text -> Chinese translation.
    """
    masked, placeholders = mask_skip_regions(html_text)

    def repl(m):
        open_tag = m.group(1)
        text = m.group(3)
        close_tag = m.group(4)
        stripped = text.strip()
        if not is_translatable(stripped):
            return m.group(0)
        if stripped in translations:
            new_inner = translations[stripped]
            # Preserve leading/trailing whitespace around text.
            lead = text[:len(text) - len(text.lstrip())]
            tail = text[len(text.rstrip()):]
            return f"{open_tag}{lead}{new_inner}{tail}{close_tag}"
        return m.group(0)

    replaced = LEAF_RE.sub(repl, masked)
    return unmask(replaced, placeholders)


def cmd_extract(path, out_json):
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    frags = extract_fragments(content)
    # Write as {en: ""} for human translation.
    obj = OrderedDict()
    for f in frags:
        obj[f] = ""
    with open(out_json, 'w', encoding='utf-8') as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
    print(f"Extracted {len(frags)} fragments -> {out_json}")


def cmd_apply(path, json_path):
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    with open(json_path, 'r', encoding='utf-8') as f:
        trans = json.load(f)
    # Only use entries with non-empty translation.
    trans = {k: v for k, v in trans.items() if v and v != k}
    new_content = apply_translations(content, trans)
    if new_content == content:
        print("No changes applied.")
        return
    with open(path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Applied {len(trans)} translations to {path}")


def cmd_extract_all(out_dir):
    os.makedirs(out_dir, exist_ok=True)
    files = sorted(
        f for f in os.listdir(BASE)
        if re.match(r'\d{3} - .*\.html$', f)
    )
    for fname in files:
        src = os.path.join(BASE, fname)
        out = os.path.join(out_dir, fname.replace('.html', '.json'))
        cmd_extract(src, out)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)
    cmd = sys.argv[1]
    if cmd == 'extract':
        path = os.path.join(BASE, sys.argv[2]) if not os.path.isabs(sys.argv[2]) else sys.argv[2]
        out = sys.argv[3] if len(sys.argv) > 3 else path.replace('.html', '.json')
        cmd_extract(path, out)
    elif cmd == 'apply':
        path = os.path.join(BASE, sys.argv[2]) if not os.path.isabs(sys.argv[2]) else sys.argv[2]
        jp = sys.argv[3]
        cmd_apply(path, jp)
    elif cmd == 'extract_all':
        cmd_extract_all(sys.argv[2] if len(sys.argv) > 2 else './extracted')
    else:
        print("Unknown command")
        sys.exit(1)
