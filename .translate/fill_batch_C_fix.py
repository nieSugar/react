"""Finishing touches for batch C: SVG 'help' button paragraphs with differing
Radix aria-controls ids. Translate by stripping the id during matching."""
import os, json, sys, re, unicodedata
sys.stdout.reconfigure(encoding="utf-8")

BASE = r"D:\Personal\Downloads\react\.translate\inline"

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("\u00a0", " ").replace("\u2013", "-").replace("\u2014", "-")
    s = s.replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    # Strip volatile Radix popover aria-controls ids:
    s = re.sub(r'aria-controls="radix-:[^"]+"', 'aria-controls=""', s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

# Use "aria-controls=\"\"" (empty) as the canonical placeholder for our translated keys.
SVG_L = '<button aria-controls="" aria-expanded="false" aria-haspopup="dialog" class="Popover_children__8p5Di" data-state="closed" type="button"><span>'
SVG_R = '</span> <svg class="fill-brand-purple dark:fill-brand-yellow w-2 h-2 b-2 mx-0.5 mb-4" enable-background="new 0 0 455 455" version="1.1" viewbox="0 0 455 455" x="0" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" y="0"><path d="M347.49 227L454.5 165.212 394.508 61.288 287.5 123.077 287.5 0 167.5 0 167.5 123.077 60.492 61.288 0.499 165.212 107.51 227 0.5 288.788 60.492 392.712 167.5 330.923 167.5 455 287.5 455 287.5 330.923 394.508 392.712 454.501 288.788z"></path></svg></button>'

FIXES = {
    "015 - Managing Effects - ui.dev": {
        f'Now, whenever {SVG_L}<code>name</code> changes{SVG_R}, React will re-run the effect.':
            f'现在，每当 {SVG_L}<code>name</code> 变化{SVG_R}，React 就会重新运行 effect。',
        f'{SVG_L}Hydration{SVG_R} failed because the initial UI does not match what was rendered on the server.':
            f'{SVG_L}Hydration{SVG_R} 失败 —— 因为初始 UI 与服务端渲染的结果不一致。',
    },
    "017 - Preserving Values with useRef - ui.dev": {
        f'Let\u2019s walk through it. We know in order to keep track of how much time has passed, we need the right combination of component state with a {SVG_L}<code>setInterval</code>{SVG_R} side effect. Because <code>setInterval</code> is a side effect that\u2019s triggered by an event, we\u2019ve put it inside of an event handler.':
            f'我们来过一遍。要追踪已经过去了多少时间，我们需要在组件 state 与 {SVG_L}<code>setInterval</code>{SVG_R} 这个副作用之间找到正确的组合。因为 <code>setInterval</code> 是由事件触发的副作用，我们把它放在了事件处理函数里。',
        f'Unlike <code>useState</code>, this <code>current</code> property is {SVG_L}mutable{SVG_R} and doesn\u2019t have a special mutation API. This means you can mutate it just like you\u2019d mutate any other value, and doing so won\u2019t trigger a re-render.':
            f'与 <code>useState</code> 不同，这个 <code>current</code> 属性是{SVG_L}可变的{SVG_R}，而且没有专门的修改 API。你可以像修改任何普通值那样直接修改它，而且这样做不会触发重新渲染。',
        f'Much better. We no longer have any state that isn\u2019t used to update the view, and more importantly, we\u2019re potentially {SVG_L}saving{SVG_R} React some work since our app no longer re-renders when we store the id.':
            f'好多了。我们不再有任何“没用于更新视图”的 state，更重要的是，我们还可能给 React {SVG_L}省下了{SVG_R}一些工作 —— 因为存 id 时我们的应用不再触发重新渲染。',
    },
    "021 - Managing Advanced Effects - ui.dev": {
        f'And how does React define <em metastring="">change</em>? The same way it always does, with {SVG_L}<code>Object.is</code>{SVG_R}.':
            f'那 React 如何定义“<em metastring="">变化</em>”？和它一贯的做法一样，用 {SVG_L}<code>Object.is</code>{SVG_R}。',
    },
}

for stem, mapping in FIXES.items():
    path = os.path.join(BASE, stem + ".json")
    with open(path, "r", encoding="utf-8") as f:
        d = json.load(f)
    norm_map = {norm(k): v for k, v in mapping.items()}
    filled = 0
    for k in list(d.keys()):
        if d[k]: continue
        nk = norm(k)
        if nk in norm_map:
            d[k] = norm_map[nk]
            filled += 1
    with open(path, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    missing = sum(1 for v in d.values() if not v)
    print(f"  {stem[:3]}  filled={filled}  still-missing={missing}")