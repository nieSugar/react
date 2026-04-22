"""Scan all 24 HTML files for <p> and <li> elements that contain nested
inline tags (code/em/strong/a/b/i/u) and therefore were MISSED by the
text-only LEAF extractor.
"""
import os, re, sys, html as htmllib
sys.stdout.reconfigure(encoding="utf-8")

BASE = r"D:\Personal\Downloads\react"

# Match <p ...>...</p> and <li ...>...</li> (non-greedy, allowing nested content).
# We use a greedy search for the CLOSING tag that comes after skipping
# nothing — only matches short-ish paragraphs to be safe.
PARA_RE = re.compile(r"<(p|li)\b[^>]*>(.*?)</\1\s*>", re.DOTALL | re.IGNORECASE)
HAS_NESTED = re.compile(r"<(?:code|em|strong|a|b|i|u)\b", re.IGNORECASE)
# Strip inline tags to get the plain text.
STRIP_TAG = re.compile(r"<[^>]+>")
# Chinese detection:
CJK = re.compile(r"[\u4e00-\u9fff]")

missed_all = {}

for fname in sorted(os.listdir(BASE)):
    if not re.match(r"\d{3} - .*\.html$", fname):
        continue
    full = os.path.join(BASE, fname)
    with open(full, "r", encoding="utf-8", errors="replace") as f:
        h = f.read()

    missed = []
    for m in PARA_RE.finditer(h):
        inner = m.group(2)
        if not HAS_NESTED.search(inner):
            continue  # pure leaf handled already
        # Get plain text
        txt = STRIP_TAG.sub("", inner)
        txt = htmllib.unescape(txt).strip()
        if len(txt) < 30:       # short ones likely code labels, skip
            continue
        # If text has CJK chars, it's already translated.
        if CJK.search(txt):
            continue
        # English-looking with at least one letter.
        if not re.search(r"[A-Za-z]", txt):
            continue
        missed.append(txt[:250])

    if missed:
        missed_all[fname] = missed

for fname, items in missed_all.items():
    print(f"=== {fname} : {len(items)} missed ===")
    for i, t in enumerate(items, 1):
        print(f"  [{i}] {t}")
    print()

total = sum(len(v) for v in missed_all.values())
print(f"TOTAL missed English paragraphs: {total} across {len(missed_all)} files")