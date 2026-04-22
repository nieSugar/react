import json, sys
sys.stdout.reconfigure(encoding="utf-8")

p = r"D:\Personal\Downloads\react\.translate\extracted\019 - Complex State with useReducer - ui.dev.json"
with open(p, "r", encoding="utf-8") as f:
    d = json.load(f)

needle = "resetting the count"
print(f'=== JSON entries containing "{needle}" ===')
hits = 0
for k, v in d.items():
    kl = k.lower()
    vl = (v or "").lower()
    if needle in kl or needle in vl:
        hits += 1
        vshow = v if v else "(empty)"
        print(f"KEY: {k[:280]!r}")
        print(f"VAL: {vshow[:200]!r}")
        print()
print(f"Hits in JSON: {hits}")

print()
print("=== HTML: paragraph location ===")
hp = r"D:\Personal\Downloads\react\019 - Complex State with useReducer - ui.dev.html"
with open(hp, "r", encoding="utf-8", errors="replace") as f:
    h = f.read()
idx = h.find("resetting the count to 0")
if idx >= 0:
    print(f"Found at idx {idx}")
    print("--- 300 chars before ---")
    print(repr(h[max(0,idx-300):idx]))
    print("--- paragraph + 500 ---")
    print(repr(h[idx:idx+500]))
else:
    print("Not found in HTML.")
