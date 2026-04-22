"""Extract <p>/<li> elements whose inner HTML has nested inline tags
(code/em/strong/a/b/i/u) that the existing LEAF-only extractor missed.
Output per-file JSON: { inner_html: "" } for translation.
"""
import os, re, sys, json, html as htmllib
sys.stdout.reconfigure(encoding="utf-8")

BASE = r"D:\Personal\Downloads\react"
OUT = r"D:\Personal\Downloads\react\.translate\inline"
os.makedirs(OUT, exist_ok=True)

PARA_RE = re.compile(r"<(p|li)\b[^>]*>(.*?)</\1\s*>", re.DOTALL | re.IGNORECASE)
INLINE = re.compile(r"<(?:code|em|strong|a|b|i|u)\b", re.IGNORECASE)
STRIP_TAG = re.compile(r"<[^>]+>")
CJK = re.compile(r"[\u4e00-\u9fff]")

total = 0
file_stats = []

for fname in sorted(os.listdir(BASE)):
    if not re.match(r"\d{3} - .*\.html$", fname):
        continue
    full = os.path.join(BASE, fname)
    with open(full, "r", encoding="utf-8", errors="replace") as f:
        h = f.read()

    entries = {}
    for m in PARA_RE.finditer(h):
        inner = m.group(2)
        if not INLINE.search(inner):
            continue
        txt = htmllib.unescape(STRIP_TAG.sub("", inner)).strip()
        if len(txt) < 30: continue
        if CJK.search(txt): continue
        if not re.search(r"[A-Za-z]", txt): continue
        entries[inner] = ""

    if entries:
        # Save inline JSON
        outf = os.path.join(OUT, fname.replace(".html", ".json"))
        with open(outf, "w", encoding="utf-8") as f:
            json.dump(entries, f, ensure_ascii=False, indent=2)
        file_stats.append((fname, len(entries)))
        total += len(entries)

for f, n in file_stats:
    print(f"  {f[:3]}  {n}")
print(f"\nTotal: {total}")