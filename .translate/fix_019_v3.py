"""Final fill: handle \x00 sentinels around SKIP# placeholders in JSON keys."""
import json, sys, ast, unicodedata, re
sys.stdout.reconfigure(encoding="utf-8")

SRC = r"D:\Personal\Downloads\react\.translate\fill_missing.py"
PATH = r"D:\Personal\Downloads\react\.translate\extracted\019 - Complex State with useReducer - ui.dev.json"

with open(SRC, "r", encoding="utf-8") as f:
    tree = ast.parse(f.read())
TRANS = None
for node in ast.walk(tree):
    if isinstance(node, ast.Assign) and any(
        isinstance(t, ast.Name) and t.id == "TRANS_019" for t in node.targets
    ):
        TRANS = ast.literal_eval(node.value)
        break

QUOTES = str.maketrans({
    "\u2018": "'", "\u2019": "'",
    "\u201c": '"', "\u201d": '"',
    "\u2013": "-", "\u2014": "-",
    "\u2026": "...",
})

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.translate(QUOTES)
    s = s.replace("\x00", "")          # strip null sentinels
    s = re.sub(r"\s+", " ", s).strip()  # collapse whitespace
    return s

# Also: for the **Chinese translation**, we need to keep the SKIP placeholders intact.
# The JSON key contains \x00SKIP#N\x00; our translation contains bare "SKIP#N".
# When translate_tool.apply() applies it, it replaces the inner text, so the
# user's Chinese text won't include the \x00 markers — that's fine because the
# apply() runs on already-SKIP-masked HTML. Our translation strings should
# use the same sentinel form as the HTML keys for perfect re-substitution.
#
# So wrap our bare SKIP#N references with \x00 too, so apply() can re-mask them
# consistently with the masked HTML.
SENTINEL = re.compile(r"SKIP#(\d+)")

def wrap_skip(text):
    return SENTINEL.sub(lambda m: f"\x00SKIP#{m.group(1)}\x00", text)

# Build normalized prefix -> wrapped-translation map.
entries = []
for k, v in TRANS.items():
    nk = norm(k)
    wv = wrap_skip(v)
    is_prefix = nk.endswith("...")
    if is_prefix:
        entries.append((nk[:-3], wv, True))
    else:
        entries.append((nk, wv, False))

with open(PATH, "r", encoding="utf-8") as f:
    d = json.load(f)

filled = 0
unmatched = []
for k, v in list(d.items()):
    if v:
        continue
    nk = norm(k)
    best = None
    best_len = -1
    for pref, trans, is_pre in entries:
        if is_pre:
            if nk.startswith(pref) and len(pref) > best_len:
                best = trans
                best_len = len(pref)
        else:
            if nk == pref and len(pref) > best_len:
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
    print("Still unmatched sample:")
    for k in unmatched[:5]:
        print(" ", repr(k[:200]))
