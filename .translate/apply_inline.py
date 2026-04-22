"""Apply inline-paragraph translations to the HTML files.

For each translated entry in .translate/inline/<stem>.json, find the matching
<p>/<li> element whose inner HTML == the key, and replace with the Chinese
translation (which preserves the same inline tags).
"""
import os, re, sys, json
sys.stdout.reconfigure(encoding="utf-8")

BASE = r"D:\Personal\Downloads\react"
INLINE = os.path.join(BASE, ".translate", "inline")

PARA_RE = re.compile(r"(<(p|li)\b[^>]*>)(.*?)(</\2\s*>)", re.DOTALL | re.IGNORECASE)

def apply_one(html_path, json_path):
    with open(json_path, "r", encoding="utf-8") as f:
        trans = json.load(f)
    # Only use entries with a non-empty Chinese translation.
    trans = {k: v for k, v in trans.items() if v and v != k}
    if not trans:
        return 0

    with open(html_path, "r", encoding="utf-8", errors="replace") as f:
        html = f.read()

    applied = 0
    def repl(m):
        nonlocal applied
        open_tag = m.group(1)
        inner = m.group(3)
        close_tag = m.group(4)
        if inner in trans:
            applied += 1
            return f"{open_tag}{trans[inner]}{close_tag}"
        return m.group(0)

    new_html = PARA_RE.sub(repl, html)
    if applied:
        with open(html_path, "w", encoding="utf-8") as f:
            f.write(new_html)
    return applied

def main():
    total = 0
    for jf in sorted(os.listdir(INLINE)):
        if not jf.endswith(".json"): continue
        stem = jf[:-5]
        html_path = os.path.join(BASE, stem + ".html")
        if not os.path.exists(html_path):
            continue
        n = apply_one(html_path, os.path.join(INLINE, jf))
        if n:
            print(f"  {stem[:3]}  applied {n}")
            total += n
    print(f"\nTotal applied: {total}")

main()