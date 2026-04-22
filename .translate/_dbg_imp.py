import json, sys
sys.stdout.reconfigure(encoding="utf-8")

PATH = r"D:\Personal\Downloads\react\.translate\inline\019 - Complex State with useReducer - ui.dev.json"
with open(PATH, "r", encoding="utf-8") as f:
    d = json.load(f)

targets = [k for k in d if "imperative solution" in k and not d[k]]
for k in targets:
    # Show exact bytes
    print("JSON KEY (repr):")
    print(repr(k))
    print()
    print("Length:", len(k))
    # Also list all non-ASCII chars
    print("Non-ASCII chars:")
    for i, c in enumerate(k):
        if ord(c) > 127:
            print(f"  pos {i}: {c!r}  U+{ord(c):04X}")