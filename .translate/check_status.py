import os, json, re
base = r"D:\Personal\Downloads\react\.translate\extracted"
for f in sorted(os.listdir(base)):
    if not f.endswith('.json'): continue
    p = os.path.join(base, f)
    with open(p, 'r', encoding='utf-8') as fp:
        d = json.load(fp)
    total = len(d)
    done = sum(1 for v in d.values() if v and v != '')
    print(f"{total:4d} total, {done:4d} translated -> {f}")
