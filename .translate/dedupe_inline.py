import os, json, re, sys, hashlib
sys.stdout.reconfigure(encoding="utf-8")
INLINE = r"D:\Personal\Downloads\react\.translate\inline"
remaining = []
for jf in sorted(os.listdir(INLINE)):
    if not jf.endswith('.json'):
        continue
    stem = jf[:-5]
    with open(os.path.join(INLINE, jf), 'r', encoding='utf-8') as f:
        d = json.load(f)
    for k, v in d.items():
        if not v:
            remaining.append((stem, k))
print('remaining entries:', len(remaining))
uniq = {}
for stem, k in remaining:
    uniq.setdefault(k, []).append(stem)
print('unique keys:', len(uniq))
# show duplicates
dups = [(k, stems) for k, stems in uniq.items() if len(stems) > 1]
print('duplicate keys:', len(dups))
for k, stems in sorted(dups, key=lambda x: (-len(x[1]), x[1][0]))[:30]:
    print('\nCOUNT', len(stems), 'FILES', sorted(stems))
    print(k[:220].replace('\n',' '))