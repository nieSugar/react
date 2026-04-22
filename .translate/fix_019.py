"""Second pass: fix the 71 items still missing in 019 by matching the
translated entries from fill_missing.py (whose keys have trailing `...`)
against the actual full keys via prefix match.
"""
import json, os, sys, importlib.util
sys.stdout.reconfigure(encoding="utf-8")

# Re-import TRANS_019 from fill_missing.py
spec = importlib.util.spec_from_file_location(
    "fill_missing", r"D:\Personal\Downloads\react\.translate\fill_missing.py"
)
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
TRANS_019 = mod.TRANS_019

path = r"D:\Personal\Downloads\react\.translate\extracted\019 - Complex State with useReducer - ui.dev.json"
with open(path, "r", encoding="utf-8") as f:
    d = json.load(f)

# Build a list of (prefix_of_translated_key_without_ellipsis, translation) pairs.
prefix_map = []
for k, v in TRANS_019.items():
    if k.endswith("..."):
        prefix_map.append((k[:-3], v))   # prefix that the full key must start with
    else:
        prefix_map.append((k, v))

filled = 0
for k, v in list(d.items()):
    if v:
        continue
    # Find a matching translation by prefix (the longest prefix that matches).
    best = None
    best_len = 0
    for pref, trans in prefix_map:
        if k.startswith(pref) and len(pref) > best_len:
            best = trans
            best_len = len(pref)
    if best is not None:
        d[k] = best
        filled += 1

with open(path, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

remaining = sum(1 for v in d.values() if not v)
print(f"Filled: {filled}, still missing: {remaining}")
