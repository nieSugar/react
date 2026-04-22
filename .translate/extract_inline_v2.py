"""Comprehensive inline-tag extractor.

Covers <p>, <li>, <h1>-<h6>, <blockquote>, <td>, <th>, <summary>,
<figcaption>, <dd>, <dt>, <caption> — i.e. any block/table element
that might wrap translatable prose with nested inline tags
(<code>, <em>, <strong>, <a>, <b>, <i>, <u>, <span>).

Also re-scans files previously processed and FILTERS OUT entries already
translated (either in the existing inline JSON or not containing English).
"""
import os, re, sys, json, html as htmllib
sys.stdout.reconfigure(encoding="utf-8")

BASE = r"D:\Personal\Downloads\react"
OUT = os.path.join(BASE, ".translate", "inline")
os.makedirs(OUT, exist_ok=True)

BLOCK_TAGS = ("p","li","h1","h2","h3","h4","h5","h6",
              "blockquote","td","th","summary","figcaption",
              "dd","dt","caption")
BLOCK_RE = re.compile(
    r"<(" + "|".join(BLOCK_TAGS) + r")\b[^>]*>(.*?)</\1\s*>",
    re.DOTALL | re.IGNORECASE,
)
# Inline tags that, when found inside a block, trigger the "missed by LEAF" case.
INLINE = re.compile(r"<(?:code|em|strong|a|b|i|u|span)\b", re.IGNORECASE)
STRIP_TAG = re.compile(r"<[^>]+>")
CJK = re.compile(r"[\u4e00-\u9fff]")

stats = []
total_new = 0
total_still_missing = 0

for fname in sorted(os.listdir(BASE)):
    if not re.match(r"\d{3} - .*\.html$", fname):
        continue
    stem = fname[:-5]
    full = os.path.join(BASE, fname)
    with open(full, "r", encoding="utf-8", errors="replace") as f:
        h = f.read()

    existing = {}
    jpath = os.path.join(OUT, stem + ".json")
    if os.path.exists(jpath):
        with open(jpath, "r", encoding="utf-8") as jf:
            existing = json.load(jf)

    still_missing = 0
    added = 0
    for m in BLOCK_RE.finditer(h):
        inner = m.group(2)
        if not INLINE.search(inner):
            continue
        txt = htmllib.unescape(STRIP_TAG.sub("", inner)).strip()
        if len(txt) < 20: continue
        if CJK.search(txt): continue
        if not re.search(r"[A-Za-z]", txt): continue
        if inner not in existing:
            existing[inner] = ""
            added += 1

    still_missing = sum(1 for v in existing.values() if not v)
    with open(jpath, "w", encoding="utf-8") as f:
        json.dump(existing, f, ensure_ascii=False, indent=2)
    stats.append((fname[:3], len(existing), still_missing, added))
    total_new += added
    total_still_missing += still_missing

for n, total, missing, added in stats:
    if total > 0:
        print(f"  {n}  total={total:>3}  missing={missing:>3}  new-this-scan=+{added}")
print(f"\nTotal NEW from wider scan: {total_new}")
print(f"TOTAL STILL MISSING: {total_still_missing}")