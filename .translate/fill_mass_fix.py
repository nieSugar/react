# -*- coding: utf-8 -*-
"""Fix the 7 <p> blocks that fill_mass.py couldn't match because of en-dash +
U+00A0 non-breaking space patterns in the source HTML.

We build the source string with the exact \xa0 (NBSP) after each en-dash,
which matches the byte pattern found by `_miss_bytes.py`.
"""
from pathlib import Path

NBSP = "\u00a0"
EN = "\u2013"  # en-dash


# ------------------------------------------------------------------
# Shared popover/button markup that appears inside the patched blocks
# ------------------------------------------------------------------

def btn(aria_id: str, label: str) -> str:
    return (
        f'<button aria-controls="radix-:{aria_id}:" aria-expanded="false" '
        f'aria-haspopup="dialog" class="Popover_children__8p5Di" '
        f'data-state="closed" type="button"><span>{label}</span> '
        '<svg class="fill-brand-purple dark:fill-brand-yellow w-2 h-2 b-2 '
        'mx-0.5 mb-4" enable-background="new 0 0 455 455" version="1.1" '
        'viewbox="0 0 455 455" x="0" xml:space="preserve" '
        'xmlns="http://www.w3.org/2000/svg" y="0"><path '
        'd="M347.49 227L454.5 165.212 394.508 61.288 287.5 123.077 287.5 0 '
        '167.5 0 167.5 123.077 60.492 61.288 0.499 165.212 107.51 227 0.5 '
        '288.788 60.492 392.712 167.5 330.923 167.5 455 287.5 455 287.5 '
        '330.923 394.508 392.712 454.501 288.788z"></path></svg></button>'
    )


def fb(color: str, txt: str) -> str:
    return (
        f'<span class="font-black tracking-wider" style="color:var(--{color})">'
        f'{txt}</span>'
    )


JOBS: dict[str, list[tuple[str, str]]] = {}


# -------- 003 --------
# NOTE: the source file uses NFD for "Beyoncé" (`e` + U+0301 combining
# acute), not the precomposed U+00E9.
JOBS["003 - Imperative vs Declarative Programming - ui.dev.html"] = [
    (
        '<p metastring="">You decide that you\u2019ve been spending too much time '
        'arguing about <em metastring="">JavaScript \u75b2\u52b3</em>\u2122 and your '
        'husband deserves a nice date. You choose to go to Red Lobster since '
        'you\u2019ve been listening to a lot of Beyonce\u0301 lately. You arrive at '
        'Red Lobster, approach the front desk and say\u2026</p>',
        '<p metastring="">你觉得自己在争论<em metastring="">JavaScript \u75b2\u52b3'
        '</em>\u2122上花的时间太多了，你老公值得一次好好的约会。因为最近你一直在循环碧昂丝的歌，'
        '你决定去 Red Lobster。到了 Red Lobster，你走到前台说……</p>',
    ),
]

# -------- 013 --------
JOBS["013 - Why React Renders - ui.dev.html"] = [
    (
        f'<p metastring="">Now whenever our <code>button</code> is clicked, our '
        f'<code>handleClick</code> {fb("pink","\u4e8b\u4ef6\u5904\u7406\u51fd\u6570")} '
        f'will run. The {fb("blue","state")} (<code>index</code>) inside of '
        '<code>handleClick</code> will be the same as the state in the most recent '
        "snapshot. From there, React sees there's a call to <code>setIndex</code> "
        "and that the value passed to it is different than the state in the "
        f"snapshot {EN}{NBSP}triggering a re-render.</p>",
        f'<p metastring="">现在每当我们的 <code>button</code> 被点击时，我们的 '
        f'<code>handleClick</code> {fb("pink","事件处理函数")}就会执行。'
        f'<code>handleClick</code> 内部的 {fb("blue","state")}（<code>index</code>）'
        '会和最近一次快照里的 state 一致。接下来 React 看到里面调用了 <code>setIndex</code>，'
        '而且传进去的值和快照中的 state 不同——于是触发一次重新渲染。</p>',
    ),
]

# -------- 015 --------
BTN15_RULE1 = btn("rkd", "规则 #1")
JOBS["015 - Managing Effects - ui.dev.html"] = [
    (
        f'<p metastring="">从概念上讲，这是有意义的，特别是当与 {BTN15_RULE1}. '
        'React can maximize the speed and predictability of rendering by enforcing '
        f'rules around when side effects can run {EN}{NBSP}either when an event '
        'occurs (Rule #1) or after the component has rendered (Rule #2).</p>',
        f'<p metastring="">从概念上讲，这是说得通的，尤其是和 {BTN15_RULE1}结合起来看。'
        'React 通过规定副作用可以何时运行来最大化渲染的速度与可预测性——要么在事件发生时（规则 #1），'
        '要么在 component 渲染之后（规则 #2）。</p>',
    ),
]

# -------- 017 --------
JOBS["017 - Preserving Values with useRef - ui.dev.html"] = [
    (
        '<p metastring="">Because CSS is doing a lot of the heavy lifting, we don\'t '
        'have a <em metastring="">ton</em> of options for how to solve this. One '
        'approach that I think is <em metastring="">差不多就行\u2122</em> is to disable '
        "the toggle switch for a short period of time after it's been clicked "
        f"{EN}{NBSP}say 1300ms.</p>",
        '<p metastring="">因为大部分重活都交给了 CSS，我们在解决这个问题时并没有'
        '<em metastring="">太多</em>选择。我觉得一个<em metastring="">差不多就行\u2122</em>'
        '的做法是：点击之后，把切换开关临时禁用一小段时间——比如 1300ms。</p>',
    ),
    (
        '<p metastring="">Now, there is one thing that\'s been eating me up since '
        'earlier. It was this line when we were discussing how to disable our toggle '
        'button until after all our CSS animations had finished - "One approach that '
        'I think is <em metastring="">差不多就行\u2122</em> is to disable the toggle '
        f'switch for a short period of time after it\'s been clicked {EN}{NBSP}say '
        '1300ms."</p>',
        '<p metastring="">还有件事，从前面开始就一直在我心里挠痒痒。那就是在讨论"等 CSS '
        '动画全部结束后再启用切换开关"时我写下的一句话——"我觉得一个<em metastring="">'
        '差不多就行\u2122</em>的做法是：点击之后，把切换开关临时禁用一小段时间——比如 1300ms。"</p>',
    ),
]

# -------- 021 --------
JOBS["021 - Managing Advanced Effects - ui.dev.html"] = [
    (
        '<p metastring="">If you take a peek into the dark crevices of the React API, '
        'you\'ll find two of these specialized <del metastring="">hooks</del> tools '
        f"{EN}{NBSP}each designed to solve advanced use cases around managing "
        "effects in React.</p>",
        '<p metastring="">如果你往 React API 的幽暗角落里看一眼，你会发现两个这样的专用 '
        '<del metastring="">hook</del> 工具——每一个都是为了解决 React 中管理 effect 的某种'
        '高级场景而设计的。</p>',
    ),
]

# -------- 022 --------
BTN22_REACTIVE = btn("rtn", "响应式值")
JOBS["022 - Abstracting Reactive Values with useEffectEvent - ui.dev.html"] = [
    (
        f'<p metastring="">All we\'re wanting to do is pass along some '
        f'<code>state</code> information for our analytics. However, because '
        f'<code>state</code> is a {BTN22_REACTIVE}, we need to include it in the '
        f"dependency array {EN}{NBSP}if we don't, React will complain.</p>",
        f'<p metastring="">我们想做的事情其实很简单：把一些 <code>state</code> 信息传给'
        f'我们的统计。但因为 <code>state</code> 是一个{BTN22_REACTIVE}，'
        '我们必须把它放进依赖数组里——否则 React 会报错。</p>',
    ),
]


def main() -> None:
    total = 0
    had_miss = False
    for fname, pairs in JOBS.items():
        p = Path(fname)
        text = p.read_text(encoding="utf-8")
        applied = 0
        for src, dst in pairs:
            cnt = text.count(src)
            if cnt == 0:
                had_miss = True
                print(f"[{fname}] STILL MISS: {src[:100]}")
                continue
            text = text.replace(src, dst)
            applied += cnt
        if applied:
            p.write_text(text, encoding="utf-8")
            print(f"[{fname}] applied {applied} (from {len(pairs)}).")
            total += applied
    print(f"\nTOTAL: {total}")
    if had_miss:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
