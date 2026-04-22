import os, json, sys
sys.stdout.reconfigure(encoding="utf-8")

INLINE = r"D:\Personal\Downloads\react\.translate\inline"

worklist = []
for jf in sorted(os.listdir(INLINE)):
    if not jf.endswith(".json"): continue
    stem = jf[:-5]
    with open(os.path.join(INLINE, jf), "r", encoding="utf-8") as f:
        d = json.load(f)
    for k, v in d.items():
        if not v:
            worklist.append({"file": stem, "en": k})

with open(r"D:\Personal\Downloads\react\.translate\worklist.json", "w", encoding="utf-8") as f:
    json.dump(worklist, f, ensure_ascii=False, indent=2)
print(f"Total entries: {len(worklist)}")