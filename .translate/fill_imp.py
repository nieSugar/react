import json, sys, re, unicodedata
sys.stdout.reconfigure(encoding="utf-8")

PATH = r"D:\Personal\Downloads\react\.translate\inline\019 - Complex State with useReducer - ui.dev.json"

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("\u00a0", " ")   # NBSP
    s = s.replace("\u2013", "-").replace("\u2014", "-")
    s = s.replace("\u2018", "'").replace("\u2019", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = re.sub(r"\s+", " ", s).strip()
    return s

TRANS_IMP = {
    "However, it is an imperative solution to the problem. We're operationally describing <strong metastring=\"\">how</strong> we want to submit the user's email - with <strong metastring=\"\">lots</strong> of <code>setX</code> invocations. Instead, what if we took a more declarative approach?":
        "不过，这是一种命令式的解法。我们是在一步步描述<strong metastring=\"\">怎样</strong>提交用户的邮箱 —— 通过<strong metastring=\"\">大量</strong>的 <code>setX</code> 调用来完成。那如果我们采用更声明式的方式呢？",
}

norm_map = {norm(k): v for k, v in TRANS_IMP.items()}

with open(PATH, "r", encoding="utf-8") as f:
    d = json.load(f)

filled = 0
for k in list(d.keys()):
    if d[k]: continue
    nk = norm(k)
    if nk in norm_map:
        d[k] = norm_map[nk]
        filled += 1

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

remaining = sum(1 for v in d.values() if not v)
print(f"Filled: {filled}, remaining: {remaining}")