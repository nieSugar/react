# -*- coding: utf-8 -*-
"""Round 2: translate remaining English paragraphs in 001/005/018/020.

All en-dashes "–" in this codebase are followed by a non-breaking space
(U+00A0), so we use that literal form in the source strings below.
"""
from pathlib import Path

NBSP = "\u00a0"
DASH = "\u2013"  # en-dash
D = DASH + NBSP   # shortcut used across originals


# { filename: [ (src, dst), ... ] }
JOBS = {
    "001 - Getting Started - ui.dev.html": [
        (
            f'<p metastring="">First, despite the dopamine rush you got when you gave us money, '
            f"you haven't actually accomplished anything yet. I beg of you {D}don't let this course "
            f"collect dust with all those Udemy courses you've purchased over the years.</p>",
            '<p metastring="">第一，虽然你在给我们付钱的那一刻获得了一阵多巴胺的快感，'
            '但你其实还什么都没完成。我求你——不要让这门课像你这些年在 Udemy 上买过的那些课一样，'
            '最终只是躺在那里吃灰。</p>',
        ),
        (
            f'<p metastring="">Second, learning new things is hard. We\'ve tried our best to make this '
            f"course as simple and as enjoyable as possible {D}but at the end of the day, you're going "
            f"to have to sit down and put in the work. It'll be hard, but if you do, and you're able to "
            f"get through the course, I promise you you'll know more React than most senior React developers.</p>",
            '<p metastring="">第二，学习新东西本来就难。我们已经尽最大努力把这门课做得简单、'
            '有趣——但归根到底，你还是得坐下来，花时间投入进去。过程会很难，但只要你肯投入、'
            '并顺利完成这门课，我保证你对 React 的了解会比大多数资深 React 开发者还要多。</p>',
        ),
    ],
    "005 - Components - ui.dev.html": [
        (
            f'<p metastring="">The primary benefit of HTML is that it allows us to create rich, '
            f'structured markup in a declarative way. In contrast, the primary benefit of JavaScript '
            f'is that it gives us a set of tools for managing the complexity of building an '
            f'application {D}namely through features like the module system, scopes, closures, and '
            f"anything else you'd expect from an actual programming language.</p>",
            '<p metastring="">HTML 的核心好处是：它让我们能用声明式的方式，写出结构丰富的标记。'
            '相比之下，JavaScript 的核心好处则是：它提供了一整套用来管理应用复杂度的工具——'
            '包括模块系统、作用域、闭包，以及你对一门真正的编程语言所期望的一切特性。</p>',
        ),
        (
            f'<p metastring="">There\'s a lot happening under the hood between when JavaScript reads '
            f'the component and when the browser paints the UI to the screen, but know that the final '
            f"output is probably what you'd expect {D}where React replaces the component with the "
            f'description of the UI the component returns.</p>',
            '<p metastring="">从 JavaScript 读到组件，到浏览器把 UI 真正绘制到屏幕上，'
            '中间其实发生了很多事情；但你可以放心：最终的结果和你预期的基本一致——'
            'React 会用组件返回的那段 UI 描述，去替换组件本身。</p>',
        ),
    ],
    "018 - Teleportation with Context - ui.dev.html": [
        (
            '<p metastring="">Whenever you have an app that is a collection of components, there\'s a '
            'linear relationship between the size of your application and how difficult it is to share '
            'state across that application.</p>',
            '<p metastring="">只要你的应用是由一堆组件组成的，那么应用规模，'
            '和在整个应用里共享 state 的难度之间，就会呈线性关系。</p>',
        ),
        (
            '<p metastring="">It\'s rare, but there are times when passing props through intermediate '
            'components can become overly redundant at best, or completely unmanageable at worst.</p>',
            '<p metastring="">虽然不多见，但确实会有这种时刻：通过中间层组件一路传递 props，'
            '往轻了说是过于冗余，往重了说则是完全没法管理。</p>',
        ),
        (
            '<p metastring="">Take a library like React Router. Even if you\'ve never used React Router '
            "before, it's probably not surprising to you that in order to work, it needs the ability to "
            'pass routing data to any component in the component tree, regardless of how deeply nested '
            'the components are.</p>',
            '<p metastring="">以 React Router 这样的库为例。即便你从没用过 React Router，'
            '你大概也不会感到意外：为了能正常工作，它必须能把路由数据传递给组件树中的任意一个组件，'
            '不管这个组件嵌套得多深。</p>',
        ),
        (
            f'<p metastring="">That\'s literally all it does {D}it\'s the Wormhole, Einstein-Rosen '
            f'bridge, TARDIS, Stargate, Portkey, DeLorean of React.</p>',
            '<p metastring="">它做的事情就只有这些——它是 React 世界里的虫洞、爱因斯坦-罗森桥、'
            'TARDIS、星际之门、门钥匙和德罗宁时光车。</p>',
        ),
        (
            '<p metastring="">Now the question becomes, how do we use it?</p>',
            '<p metastring="">那么问题来了：我们到底该怎么用它？</p>',
        ),
        (
            '<p metastring="">Well if you think about it, there are really just a few things you need '
            'to know for a feature like this.</p>',
            '<p metastring="">其实仔细想一想，对于这样一个特性，我们真正需要知道的就只有几件事。</p>',
        ),
        (
            '<p metastring="">Next is deciding what we want to teleport and to which part of our app '
            "we want to make it available. What's nice about Context is it gives you granular control "
            "over which parts of your component tree have access to the data that you're teleporting.</p>",
            '<p metastring="">接下来要决定的是：我们想要“传送”的是什么，以及希望它在应用的哪一部分可用。'
            'Context 的一个好处是：它让你可以非常精细地控制——组件树中的哪些部分才能访问你正在传送的这份数据。</p>',
        ),
        (
            f'<p metastring="">In a way, you can kind of think of using Context as creating "shadow '
            f'props" {D}where you\'re making data available to a component, just without having to '
            f'explicitly pass it down.</p>',
            '<p metastring="">从某种角度看，使用 Context 有点像是在创建一套“影子 props”——'
            '你让某个组件能够拿到这些数据，只是不必再一层层显式地把它传下去。</p>',
        ),
        (
            f'<p metastring="">The reason I chose this example is because it demonstrate how Context '
            f'works without having to worry about "managing" state, and in fact, as we saw {D}it has '
            f'nothing to do with state at all. Context is purely just a mechanism for teleporting data.</p>',
            '<p metastring="">我之所以选这个例子，是因为它演示了 Context 是如何工作的，'
            '同时又不需要我们去操心“管理” state。而且正如你所见——它和 state 其实毫无关系。'
            'Context 只是一种用来“传送数据”的机制，仅此而已。</p>',
        ),
        (
            f'<p metastring="">This is a huge misconception when it comes to Context. Whether what '
            f"you're teleporting is a static object, function, state, or anything else {D}it doesn't "
            f'change that fact that Context is a teleporter, not a manager of state.</p>',
            '<p metastring="">这是人们对 Context 一个很大的误解。无论你传送的是静态对象、'
            '函数、state 还是别的任何东西——都改变不了一个事实：Context 是一个“传送器”，'
            '而不是一个 state 的“管理器”。</p>',
        ),
        (
            '<p metastring="">This also makes Context a little difficult to teach. It\'s not that '
            "Context itself is difficult, as you saw. It's that Context is most appropriately used in "
            'large applications with deeply nested component architectures where passing props '
            "becomes unreasonable. So, by definition, it's hard to create a small demo app that "
            'represents that use case.</p>',
            '<p metastring="">这也让 Context 有点不好讲。你也看到了，Context 本身并不难。'
            '难在于：它真正适合用在那些组件结构层层嵌套、靠 props 一层层往下传已经不合理的大型应用里。'
            '所以从定义上讲，就很难用一个小小的 demo 应用，把这种场景完整地还原出来。</p>',
        ),
        (
            '<p metastring="">The only other question we have left to answer is how does React handle '
            're-rendering when the data we\'re teleporting changes?</p>',
            '<p metastring="">我们还剩下的唯一一个问题是：当我们传送的数据发生变化时，'
            'React 是怎么处理重新渲染的？</p>',
        ),
        (
            f'<p metastring="">The answer is satisfyingly simple {D}React re-renders the same way it '
            f'always does, when state changes.</p>',
            '<p metastring="">答案简单得令人满意——React 的重新渲染方式和它一贯的做法完全一样：'
            '只要 state 发生变化，它就会重新渲染。</p>',
        ),
        (
            '<p metastring="">OK I lied there is one more question we need to answer but it\'s not '
            'as important.</p>',
            '<p metastring="">好吧，我撒谎了，其实还有一个问题需要回答，只是它没有前面的那么重要。</p>',
        ),
        (
            "<p metastring=\"\">When you're a hammer, everything looks like a nail. Typically when "
            "you first learn about Context, it appears like it's the solution to a lot of your "
            "problems. Just remember, there's nothing wrong with passing props down multiple "
            'levels, that\'s literally how React was designed. I don\'t have a universal rule for '
            "when you should and shouldn't use Context, just be mindful that it's common to overuse it.</p>",
            '<p metastring="">“手里拿着锤子，看什么都像钉子。”通常来说，你第一次接触 Context 时，'
            '会觉得它好像是你许多问题的万能解。但请记住：把 props 一层层往下传并没有什么错，'
            'React 本来就是这么设计的。关于“什么时候该用、什么时候不该用 Context”，'
            '我没有一条通用的规则——只是提醒你一下：Context 被过度使用是非常常见的情况。</p>',
        ),
    ],
    "020 - Referential Equality and Why It Matters - ui.dev.html": [
        (
            f'<p metastring="">To help us understand it, and therefore help us take one of the final '
            f'steps in mastering React, we first have to take a step back and talk about what is '
            f'arguably the most fundamental aspect of JavaScript {D}value types.</p>',
            '<p metastring="">为了帮助我们理解这一点，也就是帮助我们走出掌握 React 的最后几步，'
            '我们得先退一步，聊一聊 JavaScript 中可以说是最基础的一个话题——值的类型。</p>',
        ),
        (
            '<p metastring="">On the surface primitive values and reference values look the same, '
            'but under the hood they behave much differently. The key difference can be seen in '
            'how they store their value in memory.</p>',
            '<p metastring="">从表面上看，原始值（primitive value）和引用值（reference value）'
            '看起来差不多，但在底层它们的行为有很大不同。最关键的差异体现在它们是如何把自己的值存进内存里的。</p>',
        ),
        (
            "<p metastring=\"\">Now let's look at a similar example but instead of using a primitive "
            "value, let's use a reference value.</p>",
            '<p metastring="">接下来我们看一个类似的例子，不过这次用的不是原始值，而是引用值。</p>',
        ),
        (
            '<p metastring="">Here\'s an example of using the identity operator to compare two '
            'primitive values.</p>',
            '<p metastring="">下面是一个使用“恒等运算符”来比较两个原始值的例子。</p>',
        ),
        (
            '<p metastring="">Now before we get to why this knowledge is fundamental to mastering '
            "React, let's stress test your understanding a little bit. Go through these questions, "
            'then click "Click to Reveal" when you think you got it.</p>',
            '<p metastring="">在讲为什么这些知识对掌握 React 如此重要之前，我们先来小小地压力测试一下你的理解。'
            '看完下面这些题目，当你觉得自己想明白了，再点击 “Click to Reveal”。</p>',
        ),
        (
            "<p metastring=\"\">You're going to be awesome at the next JavaScript bar trivia night.</p>",
            '<p metastring="">下次参加 JavaScript 主题的酒吧知识竞猜，你一定会表现得非常出色。</p>',
        ),
        (
            '<p metastring="">One simple option would be to just move our object outside of the '
            'component. That way it will be created once when the module is loaded, but not '
            're-created on every render.</p>',
            '<p metastring="">一个简单的办法是：直接把这个对象移到组件外面。'
            '这样它只会在模块被加载时创建一次，而不会在每次渲染时都被重新创建。</p>',
        ),
        (
            "<p metastring=\"\">To do that, we'd have to move our object back into our component. "
            "Something like this.</p>",
            '<p metastring="">要做到这一点，我们就得把这个对象重新搬回组件内部，大概像下面这样。</p>',
        ),
        (
            "<p metastring=\"\">Now there is one more refactor we can make to our code, but it's "
            "purely syntactic.</p>",
            '<p metastring="">我们还可以对代码做最后一次重构，但这一次纯粹是语法层面的优化。</p>',
        ),
    ],
}


def main():
    total = 0
    missing_any = False
    for fname, pairs in JOBS.items():
        path = Path(fname)
        text = path.read_text(encoding="utf-8")
        applied = 0
        for src, dst in pairs:
            if src in text:
                text = text.replace(src, dst, 1)
                applied += 1
            else:
                missing_any = True
                print(f"[MISS] {fname}: {src[:90]!r}")
        if applied:
            path.write_text(text, encoding="utf-8")
        print(f"{fname}: applied {applied}/{len(pairs)}")
        total += applied
    if missing_any:
        raise SystemExit(1)
    print(f"\nTOTAL applied: {total}")


if __name__ == "__main__":
    main()
