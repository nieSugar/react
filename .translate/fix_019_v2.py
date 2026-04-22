"""Third pass: fuzzy-match remaining missing 019 entries by normalizing
curly quotes / apostrophes / en-dashes and retrying the lookup.
"""
import json, sys, ast, unicodedata
sys.stdout.reconfigure(encoding="utf-8")

SRC = r"D:\Personal\Downloads\react\.translate\fill_missing.py"
PATH = r"D:\Personal\Downloads\react\.translate\extracted\019 - Complex State with useReducer - ui.dev.json"

# Parse TRANS_019 from source.
with open(SRC, "r", encoding="utf-8") as f:
    tree = ast.parse(f.read())
TRANS = None
for node in ast.walk(tree):
    if isinstance(node, ast.Assign) and any(
        isinstance(t, ast.Name) and t.id == "TRANS_019" for t in node.targets
    ):
        TRANS = ast.literal_eval(node.value)
        break
assert TRANS is not None

TABLE = str.maketrans({
    "\u2018": "'", "\u2019": "'",
    "\u201c": '"', "\u201d": '"',
    "\u2013": "-", "\u2014": "-",
    "\u2026": "...",
})
def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.translate(TABLE)
    return s

# Build normalized prefix -> translation map.
prefix_map = []
for k, v in TRANS.items():
    nk = norm(k)
    if nk.endswith("..."):
        prefix_map.append((nk[:-3], v))
    else:
        prefix_map.append((nk, v))

with open(PATH, "r", encoding="utf-8") as f:
    d = json.load(f)

filled = 0
unmatched = []
for k, v in list(d.items()):
    if v:
        continue
    nk = norm(k)
    best = None
    best_len = 0
    for pref, trans in prefix_map:
        if nk.startswith(pref) and len(pref) > best_len:
            best = trans
            best_len = len(pref)
    if best:
        d[k] = best
        filled += 1
    else:
        unmatched.append(k)

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

remaining = sum(1 for v in d.values() if not v)
print(f"Filled: {filled}, still missing: {remaining}")
if unmatched:
    print("Still unmatched:")
    for k in unmatched:
        print(" ", k[:200])
