# -*- coding: utf-8 -*-
"""Translate remaining English paragraphs in 016 - Managing Effects - Part 2."""
from pathlib import Path

TARGET = Path(__file__).resolve().parent.parent / "016 - Managing Effects - Part 2 - ui.dev.html"

REPLACEMENTS = [
    (
        '<p metastring="">Up until this point, all of our examples have been side effects that are local to the user\'s device –\u00a0getting their battery level, accessing local storage, changing the document\'s title. But when you think of side effects, especially as someone building for the web, the one that most likely comes to mind first is network requests.</p>',
        '<p metastring="">到目前为止，我们所有的例子都是仅限于用户设备本地的副作用——获取电池电量、访问 local storage、修改文档标题。但说到副作用，尤其是作为一个做 Web 开发的人，最先浮现在脑海里的往往是网络请求。</p>',
    ),
    (
        '<p metastring="">Third, this is "tutorial" code. We\'re pretending like loading and error states don\'t exist. Unfortunately, you can\'t write tutorial code at work, so let\'s fix that.</p>',
        '<p metastring="">第三，这是“教程代码”。我们在假装 loading 和 error 这两种状态不存在。可惜在实际工作里你不能这样写，所以我们来把它补上。</p>',
    ),
    (
        '<p metastring="">At this point, all we need to do is update the UI to both show our active Pokémon and allow the user (or the app itself) to change it via our Carousel. These components are extraneous to the point of this post, so I\'ll just paste them in and you can view them if you\'d like.</p>',
        '<p metastring="">到这里，我们只需要更新 UI 来显示当前的宝可梦，并让用户（或应用本身）通过 Carousel 去切换它。这些组件和本文要讲的主题关系不大，所以我就直接把它们贴出来，如果你感兴趣可以自己查看。</p>',
    ),
    (
        '<p metastring="">You can see this by scrolling back up and playing around with the app. Change the active Pokémon on the carousel as fast as you can.</p>',
        '<p metastring="">你可以滚动回上面玩一下这个应用来观察这个现象：尽你所能快速地在轮播上切换当前的宝可梦。</p>',
    ),
    (
        '<p metastring="">If you return a function from your effect, React will call that function each time before it ever calls your effect again, and then one final time when the component is removed from the DOM.</p>',
        '<p metastring="">如果你在 effect 中返回一个函数，React 会在每次再次调用该 effect 之前先调用这个函数，并在组件从 DOM 中被移除时最后再调用它一次。</p>',
    ),
    (
        '<p metastring="">Now play around with the app and notice the logs. Specifically, think of how we can leverage this knowledge of our cleanup function in order to ignore stale effects.</p>',
        '<p metastring="">现在玩一下这个应用并观察日志。具体来说，思考一下我们如何利用 cleanup 函数的这个特性，来忽略那些已经过期的 effect。</p>',
    ),
    (
        '<p metastring="">Now I know you\'re having the time of your life, but this\'ll be the last scenario we look at for now –\u00a0and it\'s one you\'ll see often.</p>',
        '<p metastring="">我知道你现在玩得很开心，但这将是我们目前要看的最后一个场景——而且这是你会经常遇到的一种场景。</p>',
    ),
    (
        '<p metastring="">Let\'s say we were writing software for a company that administers certifications for employees. To earn a certification, an employee must pass an online test by a certain percentage. Part of the test is that for every time the employee tabs away from the current window, they lose a percentage.</p>',
        '<p metastring="">假设我们正在为一家给员工做认证的公司开发软件。要获得认证，员工必须以一定的正确率通过在线测试。测试规则的一部分是：每次员工从当前窗口切走（tab away），都会被扣掉一部分分数。</p>',
    ),
    (
        '<p metastring="">How would we go about encapsulating this requirement into a React component, letting the student know how many times they\'ve tabbed away?</p>',
        '<p metastring="">我们要如何把这个需求封装进一个 React 组件里，并让学员知道自己一共切走过多少次？</p>',
    ),
    (
        '<p metastring="">The problem is every time React calls our effect, we\'re removing the previous event listener and adding a new one. That\'s... not ideal. We can see this in action if we add some logs to our effect and tab away and back to this page.</p>',
        '<p metastring="">问题在于：每次 React 调用我们的 effect 时，我们都会先移除之前的事件监听器，再添加一个新的。这……并不理想。如果我们在 effect 里加一些日志，然后切出去再切回这个页面，就能直观地看到这个问题。</p>',
    ),
    (
        '<p metastring="">Right now, and in almost every other scenario when you\'re updating state, you pass the state\'s updater function the value with which you want to replace the current state.</p>',
        '<p metastring="">目前，以及在你更新 state 的几乎所有其他场景里，你都是把"想要用来替换当前 state 的值"直接传给 state 的 updater 函数。</p>',
    ),
    (
        '<p metastring="">However, an often overlooked aspect of this API is you\'re also able to pass the state\'s updater function a function itself, and when React invokes that function, it\'ll pass it the current state. You can then use that state to calculate the new state.</p>',
        '<p metastring="">然而，这个 API 有一个经常被忽视的用法：你其实也可以把一个函数本身传给 state 的 updater 函数。当 React 调用这个函数时，会把当前的 state 作为参数传进去，你就可以基于这个 state 来计算新的 state。</p>',
    ),
    (
        '<p metastring="">Hopefully at this point you\'re starting to get a solid grasp of how you can use the rules we\'ve established to better establish a mental model for managing side effects in React.</p>',
        '<p metastring="">希望到这里，你已经开始扎实地掌握：如何利用我们建立的这些规则，来更好地搭建起一套在 React 中管理副作用的心理模型。</p>',
    ),
    (
        '<p metastring="">Now before you go, there are a few smaller details I want to point out that didn\'t fit into the normal narrative flow of these last few lessons, but I think are important to know.</p>',
        '<p metastring="">在你离开之前，还有几个较小的细节我想指出来——它们没能自然地融入前面几节课的叙事里，但我觉得了解一下很重要。</p>',
    ),
    (
        '<p class="text-center mt-4 text-2xl">If a side effect is synchronizing your component with some outside system and that side effect needs to run *before* the browser paints the screen, put that side effect inside useLayoutEffect</p>',
        '<p class="text-center mt-4 text-2xl">如果某个副作用是在把你的组件与某个外部系统同步，并且这个副作用必须在浏览器绘制屏幕<em>之前</em>运行，那就把它放进 useLayoutEffect 里。</p>',
    ),
]


def main():
    text = TARGET.read_text(encoding="utf-8")
    miss = []
    for src, dst in REPLACEMENTS:
        if src not in text:
            miss.append(src[:80])
            continue
        text = text.replace(src, dst, 1)
    if miss:
        print("MISSING:")
        for m in miss:
            print(" -", m)
        raise SystemExit(1)
    TARGET.write_text(text, encoding="utf-8")
    print(f"OK: applied {len(REPLACEMENTS)} replacements to {TARGET.name}")


if __name__ == "__main__":
    main()
