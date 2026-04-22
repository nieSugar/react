import json, sys
sys.stdout.reconfigure(encoding="utf-8")

hp = r"D:\Personal\Downloads\react\019 - Complex State with useReducer - ui.dev.html"
with open(hp, "r", encoding="utf-8", errors="replace") as f:
    h = f.read()

for needle in [
    "gets a little trickier",
    "a little trickier",
    "specify different types of actions",
    "For resetting",
    "reset the count",
    "add that to state",
    "whatever was passed to dispatch",
]:
    idx = h.find(needle)
    print("HTML", repr(needle), "->", idx)

print()
p = r"D:\Personal\Downloads\react\.translate\extracted\019 - Complex State with useReducer - ui.dev.json"
with open(p, "r", encoding="utf-8") as f:
    d = json.load(f)

for needle in ["trickier", "For resetting", "reset the count", "add that to state"]:
    hits = [(k, d[k]) for k in d.keys() if needle.lower() in k.lower()]
    print("JSON", repr(needle), "->", len(hits), "keys")
    for k, v in hits:
        vv = v if v else "(empty)"
        print("   KEY:", repr(k[:200]))
        print("   VAL:", repr(vv[:150]))