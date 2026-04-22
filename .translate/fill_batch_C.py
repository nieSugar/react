"""Batch C: 015, 017, 018, 021, 022, 023, 024."""
import os, json, sys, re, unicodedata
sys.stdout.reconfigure(encoding="utf-8")

BASE = r"D:\Personal\Downloads\react\.translate\inline"

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("\u00a0", " ").replace("\u2013", "-").replace("\u2014", "-")
    s = s.replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = re.sub(r"\s+", " ", s).strip()
    return s

SVG_BTN_HELP_L = "<button aria-controls=\"radix-:rke:\" aria-expanded=\"false\" aria-haspopup=\"dialog\" class=\"Popover_children__8p5Di\" data-state=\"closed\" type=\"button\"><span>"
SVG_BTN_HELP_R = "</span> <svg class=\"fill-brand-purple dark:fill-brand-yellow w-2 h-2 b-2 mx-0.5 mb-4\" enable-background=\"new 0 0 455 455\" version=\"1.1\" viewbox=\"0 0 455 455\" x=\"0\" xml:space=\"preserve\" xmlns=\"http://www.w3.org/2000/svg\" y=\"0\"><path d=\"M347.49 227L454.5 165.212 394.508 61.288 287.5 123.077 287.5 0 167.5 0 167.5 123.077 60.492 61.288 0.499 165.212 107.51 227 0.5 288.788 60.492 392.712 167.5 330.923 167.5 455 287.5 455 287.5 330.923 394.508 392.712 454.501 288.788z\"></path></svg></button>"

TRANS = {}

TRANS["015 - Managing Effects - ui.dev"] = {
    "A not so often talked about aspect of this formula is one simple but requisite rule in React – that the <span class=\"font-black tracking-wider\" style=\"color:var(--green)\">function</span> which calculates the <span class=\"font-black tracking-wider\" style=\"color:var(--yellow)\">View</span> needs to be a <span class=\"sparkle_wrapper__cL2jQ\"><span class=\"sparkle_sparkle_wrapper__Izdcu\" style=\"top:12%;left:98%\"><svg class=\"sparkle_sparkle_svg__WdZ3Y\" fill=\"none\" height=\"10\" viewbox=\"0 0 68 68\" width=\"10\"><path d=\"M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z\" fill=\"var(--yellow)\"></path></svg></span><span class=\"sparkle_sparkle_wrapper__Izdcu\" style=\"top:65%;left:0%\"><svg class=\"sparkle_sparkle_svg__WdZ3Y\" fill=\"none\" height=\"10\" viewbox=\"0 0 68 68\" width=\"10\"><path d=\"M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z\" fill=\"var(--yellow)\"></path></svg></span><span class=\"sparkle_sparkle_wrapper__Izdcu\" style=\"top:63%;left:93%\"><svg class=\"sparkle_sparkle_svg__WdZ3Y\" fill=\"none\" height=\"18\" viewbox=\"0 0 68 68\" width=\"18\"><path d=\"M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z\" fill=\"var(--yellow)\"></path></svg></span><strong class=\"sparkle_child_wrapper__bem0y\">pure</strong></span> calculation.":
        "这个公式里有一点不太常被讨论，但却是 React 中一条简单而必要的规则 —— 用来计算<span class=\"font-black tracking-wider\" style=\"color:var(--yellow)\">View</span> 的那个<span class=\"font-black tracking-wider\" style=\"color:var(--green)\">函数</span>必须是一次<span class=\"sparkle_wrapper__cL2jQ\"><span class=\"sparkle_sparkle_wrapper__Izdcu\" style=\"top:12%;left:98%\"><svg class=\"sparkle_sparkle_svg__WdZ3Y\" fill=\"none\" height=\"10\" viewbox=\"0 0 68 68\" width=\"10\"><path d=\"M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z\" fill=\"var(--yellow)\"></path></svg></span><span class=\"sparkle_sparkle_wrapper__Izdcu\" style=\"top:65%;left:0%\"><svg class=\"sparkle_sparkle_svg__WdZ3Y\" fill=\"none\" height=\"10\" viewbox=\"0 0 68 68\" width=\"10\"><path d=\"M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z\" fill=\"var(--yellow)\"></path></svg></span><span class=\"sparkle_sparkle_wrapper__Izdcu\" style=\"top:63%;left:93%\"><svg class=\"sparkle_sparkle_svg__WdZ3Y\" fill=\"none\" height=\"18\" viewbox=\"0 0 68 68\" width=\"18\"><path d=\"M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z\" fill=\"var(--yellow)\"></path></svg></span><strong class=\"sparkle_child_wrapper__bem0y\">纯</strong></span>计算。",
    "Now I know what you might be thinking, surely this isn't <strong metastring=\"\">that</strong> big of deal, right? Getting a single item out of local storage is plenty fast. Even if it <em metastring=\"\">slightly</em> slows down the initial render, does it really matter?":
        "我知道你可能会想：这应该没<strong metastring=\"\">那么</strong>严重吧？从 localStorage 里读一个值已经够快了。就算它<em metastring=\"\">稍微</em>拖慢一点初次渲染，又有什么关系？",
    "<code>useEffect</code> is a hook that comes with React that, as our definition suggests, allows you to run a side effect that synchronizes your component with some outside system. <code>useEffect</code> works by removing the side effect from React's rendering flow and delaying its execution until <strong metastring=\"\">after</strong> the component has rendered.":
        "<code>useEffect</code> 是 React 自带的 hook。正如定义所说，它允许你执行一个把 component 和外部系统同步起来的副作用。<code>useEffect</code> 的原理是把副作用从 React 的渲染流程中抽离出来，把它的执行推迟到组件渲染<strong metastring=\"\">之后</strong>。",
    "As a gentle example of <code>useEffect</code>, here's a component that show's the user's current battery level. We'll use <code>useEffect</code> since we want to <em metastring=\"\">synchronize</em> the component's state with some outside system (the battery level on the user's device).":
        "作为 <code>useEffect</code> 的一个温和示例，这里是一个显示用户当前电量的组件。我们用 <code>useEffect</code>，因为我们想把组件 state 与一个外部系统（用户设备的电量）<em metastring=\"\">同步</em>起来。",
    f"First, as mentioned earlier, our {SVG_BTN_HELP_L}effect{SVG_BTN_HELP_R} gets invoked <strong metastring=\"\">after</strong> React renders. You can see this by the fact that <code>Rendering</code> gets logged before <code>Getting battery level...</code>.":
        f"首先，正如前面提到的，我们的 {SVG_BTN_HELP_L}effect{SVG_BTN_HELP_R} 会在 React 渲染<strong metastring=\"\">之后</strong>才被调用。你可以从 <code>Rendering</code> 先于 <code>Getting battery level...</code> 打印这件事看出来。",
    "Second, and this may come as a surprise to you, by default, our effect gets invoked after <strong metastring=\"\">every</strong> re-render. This is why the console output looks the way it does.":
        "其次，可能有点出乎你意料：默认情况下，effect 会在<strong metastring=\"\">每次</strong>重新渲染之后都被调用。这也就是控制台输出长那样的原因。",
    "On the initial render we set the <code>level</code> state is to <code>0</code> and we log <code>Rendering</code>. Then, <strong metastring=\"\">after</strong> rendering, React calls our effect which logs <code>Getting battery level...</code> before asynchronously fetching our device's battery level. Once it has it, if the battery level is different than our initial state of <code>0</code> (which is a safe assumption), React re-renders with the new battery level.":
        "初次渲染时，我们把 <code>level</code> state 设为 <code>0</code> 并打印 <code>Rendering</code>。然后在渲染<strong metastring=\"\">之后</strong>，React 调用我们的 effect，它先打印 <code>Getting battery level...</code>，再异步获取设备电量。一旦拿到电量，如果它不等于初始的 <code>0</code>（基本可以这么假设），React 就会用新的电量重新渲染。",
    "On the re-render, <code>Rendering</code> gets logged and then, <strong metastring=\"\">after</strong> React has finished rendering, our effect is called. The effect logs <code>Getting battery level...</code> before asynchronously fetching the battery level, again. Since this time the battery level is the same as the previous render, our effect ends and React is done.":
        "这次重新渲染时，<code>Rendering</code> 又被打印。<strong metastring=\"\">之后</strong>，等 React 渲染完毕，我们的 effect 又被调用。它先打印 <code>Getting battery level...</code>，再次异步获取电量。由于这次电量和上次一样，effect 执行完就结束，React 也就完成了。",
    "Admittedly, the default behavior of React calling the effect after <strong metastring=\"\">every</strong> render might seem a little strange. In both of our examples, that's not ideal.":
        "说实话，React 默认在<strong metastring=\"\">每次</strong>渲染后都调用 effect 的行为，看起来有点怪。在我们上面的两个例子里，这都不是理想的行为。",
    "Because I presume you have a normal human brain, what you're probably expecting is something like this, where our second argument to <code>useEffect</code> tells React <strong metastring=\"\">when</strong> to invoke the effect.":
        "因为我假设你有一颗正常人的脑子，你大概期望的是这样：给 <code>useEffect</code> 传第二个参数，告诉 React <strong metastring=\"\">什么时候</strong>应该调用 effect。",
    f"Now, whenever {SVG_BTN_HELP_L}<code>name</code> changes{SVG_BTN_HELP_R}, React will re-run the effect.":
        f"现在，每当 {SVG_BTN_HELP_L}<code>name</code> 变化{SVG_BTN_HELP_R}，React 就会重新运行 effect。",
    "It may seem strange, but this default makes sense if you think about it in the context of the goal of <code>useEffect</code>. The whole goal of <code>useEffect</code> is to synchronize your component with some external system. Whenever <strong metastring=\"\">any</strong> of the dependencies that the effect needs in order to synchronize change, React, should resynchronize.":
        "看起来奇怪，但如果从 <code>useEffect</code> 的目标角度来想，这个默认行为其实是合理的。<code>useEffect</code> 的全部目标就是把组件和某个外部系统同步起来。只要 effect 进行同步时依赖的<strong metastring=\"\">任何</strong>一个值发生变化，React 就应该再同步一次。",
    "Notice that our effect only gets invoked <strong metastring=\"\">once</strong>, after the initial render. This makes sense. We've told React that the effect doesn't depend on any values outside of the effect, so it never needs to re-run (or <em metastring=\"\">resync</em>).":
        "注意 effect 只在初次渲染之后被调用<strong metastring=\"\">一次</strong>。这是合理的：我们告诉了 React 这个 effect 不依赖外部的任何值，所以它永远不需要重新运行（也就不需要<em metastring=\"\">重新同步</em>）。",
    f"{SVG_BTN_HELP_L}Hydration{SVG_BTN_HELP_R} failed because the initial UI does not match what was rendered on the server.":
        f"{SVG_BTN_HELP_L}Hydration{SVG_BTN_HELP_R} 失败 —— 因为初始 UI 与服务端渲染的结果不一致。",
}

TRANS["017 - Preserving Values with useRef - ui.dev"] = {
    f"Let's walk through it. We know in order to keep track of how much time has passed, we need the right combination of component state with a {SVG_BTN_HELP_L}<code>setInterval</code>{SVG_BTN_HELP_R} side effect. Because <code>setInterval</code> is a side effect that's triggered by an event, we've put it inside of an event handler.":
        f"我们来过一遍。要追踪已经过去了多少时间，我们需要在组件 state 与 {SVG_BTN_HELP_L}<code>setInterval</code>{SVG_BTN_HELP_R} 这个副作用之间找到正确的组合。因为 <code>setInterval</code> 是由事件触发的副作用，我们把它放在了事件处理函数里。",
    "To fix this, instead of re-creating <code>id</code> on every render, what we want to do is tell React to <strong metastring=\"\">preserve</strong> <code>id</code> across renders. Isn't this is the exact use case that <code>useState</code> was created for?":
        "要解决这个问题，我们不应该每次渲染都重新创建 <code>id</code>，而是让 React 在多次渲染间<strong metastring=\"\">保留</strong> <code>id</code>。这不就是 <code>useState</code> 被创造出来要解决的场景吗？",
    "Yes, our app <em metastring=\"\">technically</em> does work. And I'm not even mad, more just disappointed. Throughout this whole course you've been taught, nauseatingly, that in React, your view is simply a function of your state.":
        "是的，我们的应用<em metastring=\"\">技术上</em>确实能跑。我也不生气，只是有点失望。整门课我们一直近乎啰嗦地在强调：在 React 里，view 就是 state 的一个函数。",
    "As is, our app breaks this mental model. We've introduced state that has <strong metastring=\"\">nothing</strong> to do with our view, we're simply using it as a way to preserve a value across renders. That's what we in the biz call <span class=\"sparkle_wrapper__cL2jQ\"><span class=\"sparkle_sparkle_wrapper__Izdcu\" style=\"top:60%;left:82%\"><svg class=\"sparkle_sparkle_svg__WdZ3Y\" fill=\"none\" height=\"17\" viewbox=\"0 0 68 68\" width=\"17\"><path d=\"M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z\" fill=\"var(--yellow)\"></path></svg></span><span class=\"sparkle_sparkle_wrapper__Izdcu\" style=\"top:88%;left:87%\"><svg class=\"sparkle_sparkle_svg__WdZ3Y\" fill=\"none\" height=\"19\" viewbox=\"0 0 68 68\" width=\"19\"><path d=\"M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z\" fill=\"var(--yellow)\"></path></svg></span><strong class=\"sparkle_child_wrapper__bem0y\">hacky</strong></span>.":
        "但眼下我们的应用打破了这个心智模型。我们引入了一块<strong metastring=\"\">跟视图毫无关系</strong>的 state，纯粹只是为了跨渲染保留一个值。这种写法在行话里叫<span class=\"sparkle_wrapper__cL2jQ\"><span class=\"sparkle_sparkle_wrapper__Izdcu\" style=\"top:60%;left:82%\"><svg class=\"sparkle_sparkle_svg__WdZ3Y\" fill=\"none\" height=\"17\" viewbox=\"0 0 68 68\" width=\"17\"><path d=\"M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z\" fill=\"var(--yellow)\"></path></svg></span><span class=\"sparkle_sparkle_wrapper__Izdcu\" style=\"top:88%;left:87%\"><svg class=\"sparkle_sparkle_svg__WdZ3Y\" fill=\"none\" height=\"19\" viewbox=\"0 0 68 68\" width=\"19\"><path d=\"M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z\" fill=\"var(--yellow)\"></path></svg></span><strong class=\"sparkle_child_wrapper__bem0y\">hacky（歪招）</strong></span>。",
    "The API is fairly simple. When you call <code>useRef</code>, what you get back is a <span class=\"font-mono\">ref</span> – an object with a mutable <code>current</code> property whose value will be preserved across renders.":
        "API 相当简单。调用 <code>useRef</code> 得到的是一个 <span class=\"font-mono\">ref</span> —— 一个对象，带有可变的 <code>current</code> 属性，它的值会在多次渲染间保留下来。",
    f"Unlike <code>useState</code>, this <code>current</code> property is {SVG_BTN_HELP_L}mutable{SVG_BTN_HELP_R} and doesn't have a special mutation API. This means you can mutate it just like you'd mutate any other value, and doing so won't trigger a re-render.":
        f"与 <code>useState</code> 不同，这个 <code>current</code> 属性是{SVG_BTN_HELP_L}可变的{SVG_BTN_HELP_R}，而且没有专门的修改 API。你可以像修改任何普通值那样直接修改它，而且这样做不会触发重新渲染。",
    "You'll notice that our app is <em metastring=\"\">mostly</em> fine, but there's one thing I think we can improve on. If you click on the toggle switch repeatedly, over and over, the experience breaks down. It still works, but I think the better UX is to only allow the user to toggle when the animation has finished running.":
        "你会发现我们的应用<em metastring=\"\">大体上</em>没问题，但有一点可以改进：如果你反复点击那个切换开关，体验会崩掉。它还能用，但我觉得更好的 UX 是：只有在动画跑完后，才允许用户再次切换。",
    "There is just <em metastring=\"\">one</em> more side effect that we haven't talked about yet, and it's crucial for building on the web – interacting <em metastring=\"\">directly</em> with the DOM.":
        "还有<em metastring=\"\">一个</em>我们没讲过的副作用，它对于在 Web 上开发至关重要 —— 也就是<em metastring=\"\">直接</em>操作 DOM。",
    "This <em metastring=\"\">worked</em>, but it too was brittle. If a designer tweaked how long our animations took to run, it wouldn't behave as expected.":
        "这样<em metastring=\"\">能用</em>，但同样很脆弱。如果设计师调整了动画的时长，它就不会按预期工作了。",
    "Before we go on, I want to say that I would consider everything below this to be <strong metastring=\"\">advanced</strong>. Don't get down on yourself if it's a little confusing at first. I've been writing React since 2014 and it even took me a little while to get a solution I was happy with.":
        "继续之前我想说：下面的内容我认为都属于<strong metastring=\"\">进阶</strong>。如果一开始觉得有点绕，不必沮丧。我从 2014 年就开始写 React 了，想出一个自己满意的方案都还花了些时间。",
    "So we're good, right? At this point in the course you probably know that if I ask that question, we are definitely <span class=\"font-black tracking-wider\" style=\"color:var(--red)\">not</span> good.":
        "所以我们就搞定了，对吧？学到这里你大概也知道：只要我这样问，那我们肯定<span class=\"font-black tracking-wider\" style=\"color:var(--red)\">还没</span>搞定。",
    f"Much better. We no longer have any state that isn't used to update the view, and more importantly, we're potentially {SVG_BTN_HELP_L}saving{SVG_BTN_HELP_R} React some work since our app no longer re-renders when we store the id.":
        f"好多了。我们不再有任何“没用于更新视图”的 state，更重要的是，我们还可能给 React {SVG_BTN_HELP_L}省下了{SVG_BTN_HELP_R}一些工作 —— 因为存 id 时我们的应用不再触发重新渲染。",
    "To get data <span class=\"font-bold relative m-px\" style=\"bottom:3px\">d</span><span class=\"font-bold relative m-px\" style=\"bottom:2px\">o</span><span class=\"font-bold relative m-px\" style=\"bottom:1px\">w</span><span class=\"font-bold relative m-px\" style=\"bottom:0px\">n</span> the component tree, you use props. To get data <span class=\"font-bold relative m-px\" style=\"bottom:0px\">u</span><span class=\"font-bold relative m-px\" style=\"bottom:1px\">p</span> the component tree, you use callbacks.":
        "要把数据<span class=\"font-bold relative m-px\" style=\"bottom:3px\">往</span><span class=\"font-bold relative m-px\" style=\"bottom:2px\">下</span><span class=\"font-bold relative m-px\" style=\"bottom:1px\">传</span><span class=\"font-bold relative m-px\" style=\"bottom:0px\">递</span>组件树，用 props；要把数据<span class=\"font-bold relative m-px\" style=\"bottom:0px\">往</span><span class=\"font-bold relative m-px\" style=\"bottom:1px\">上</span>传，用回调。",
}

TRANS["018 - Teleportation with Context - ui.dev"] = {
    "This works... <strong metastring=\"\">most</strong> of the time. But what happens if instead of your app looking like that, it looked like this?":
        "这种方式<strong metastring=\"\">大多数</strong>时候都管用。但如果你的应用长得不是那样，而是像下面这样呢？",
    "Or <code>react-intl</code>, a library for handling internationalization and localization that needs to be able to pass locale data to any component in the component tree, again, regardless of how deeply nested the components are.":
        "再比如 <code>react-intl</code>，一个负责国际化和本地化的库 —— 它同样需要能把 locale 数据传递给组件树中任意一个组件，无论嵌套多深。",
    "Because this is such an obvious limitation of a component based architecture, React comes with a built-in API to solve it called Context. You can think of Context as giving you the ability to teleport data <em metastring=\"\">anywhere</em> in your component tree, without needing to pass props.":
        "由于这是组件化架构一个很明显的局限，React 自带了一个叫做 Context 的内置 API 来解决它。你可以把 Context 想象成一种“传送”能力：把数据传到组件树<em metastring=\"\">任意位置</em>，而不需要一层层传 props。",
    "The one is pretty simple. You can create a Context by calling <code>React.createContext</code>.":
        "这一步相当简单。你可以通过调用 <code>React.createContext</code> 创建一个 Context。",
    "Here's how it works. When you create a new Context, what React gives you is an object with a <code>Provider</code> property.":
        "它的工作方式是这样的。当你创建一个新的 Context 时，React 会给你一个对象，对象上有一个 <code>Provider</code> 属性。",
    "<code>Provider</code> accepts a <code>value</code> prop which is the data that you want to teleport to any component in <code>Provider</code>'s subtree.":
        "<code>Provider</code> 接收一个 <code>value</code> prop —— 它就是你想“传送”给 <code>Provider</code> 子树中任意组件的数据。",
    "Now, because we've wrapped our entire app in <code>Provider</code>, any component, regardless of how nested it is, can get access to what we passed to <code>value</code>, <code>marty</code>.":
        "因为我们已经把整个应用包在 <code>Provider</code> 里了，任何组件（无论嵌套多深）都能拿到传给 <code>value</code> 的数据，也就是 <code>marty</code>。",
    "To get access to what was passed to the <code>Provider</code>'s <code>value</code> prop, you use React's <code>useContext</code> hook, passing it the Context as the first argument.":
        "要拿到 <code>Provider</code> 的 <code>value</code> prop 所传入的数据，你使用 React 的 <code>useContext</code> hook，并把 Context 作为第一个参数传给它。",
    "Notice that even though our <code>Cafe80s</code> component is a few layers deep and doesn't receive any props, we can still access the <code>marty</code> object via <code>useContext</code>.":
        "注意，尽管 <code>Cafe80s</code> 嵌了好几层、也没有接收任何 props，我们仍然能通过 <code>useContext</code> 拿到 <code>marty</code> 对象。",
    "Now admittedly there is one thing strange about this demo you may have noticed. Since <code>marty</code> is just a static object, why don't we just <code>export</code> it from a module and <code>import</code> it wherever we need it? There's not really a need for Context in this scenario.":
        "老实说，这个 demo 里确实有一点你可能已经注意到的怪事：既然 <code>marty</code> 只是一个静态对象，我们为什么不把它从某个模块 <code>export</code> 出来，需要时再 <code>import</code> 进来？在这个场景里确实用不到 Context。",
    "With that said, let's move our example a little <em metastring=\"\">closer to</em> reality by teleporting state instead of just a static object.":
        "话虽如此，我们把例子往<em metastring=\"\">更贴近</em>真实情况挪一步 —— 传送的不再是一个静态对象，而是 state。",
    "More specifically, let's move <code>marty</code> into an array, add in his friend Doc, and then teleport that array of <code>passengers</code>.":
        "具体来说，我们把 <code>marty</code> 放进一个数组，再加上他的朋友 Doc，然后传送这整个 <code>passengers</code> 数组。",
    "Note that after updating what we're teleporting to be an array, we also needed to update where we're consuming that data, in this case, the <code>Cafe80s</code> component.":
        "注意把传送的内容改为数组之后，我们也得同步更新消费这份数据的地方 —— 也就是 <code>Cafe80s</code> 组件。",
    "But other than that, notice <em metastring=\"\">nothing</em> else changed. One more time for those in the back, Context isn't a way to manage state, it's a way to teleport data. The \"management\" of our state is done by <code>useState</code>, not Context.":
        "除此之外，注意<em metastring=\"\">别的</em>什么都没变。给后排再强调一遍：Context 不是管理 state 的方式，而是传送数据的方式。真正“管理”state 的是 <code>useState</code>，不是 Context。",
    "In our example, <code>passengers</code> is located at the root of our application. Therefor, whenever it changes, React will re-render the entire tree, passing the new <code>passengers</code> as the value of the Context.":
        "在这个例子里，<code>passengers</code> 位于应用的根节点。所以每当它变化时，React 都会重新渲染整棵树，把新的 <code>passengers</code> 作为 Context 的值传下去。",
    "Whenever you invoke <code>useContext</code> passing it a Context object, it'll return whatever you passed to the <code>value</code> prop of the nearest <code>Provider</code> component of the same Context.":
        "每当你调用 <code>useContext</code> 并传入一个 Context 对象，它会返回该 Context 对应的、<em>最近一层</em> <code>Provider</code> 上 <code>value</code> prop 所传入的值。",
    "However, what if there is no <code>Provider</code> component above it in the component tree? In that case, it'll get its value from the first argument that was passed to <code>createContext</code> when the Context object was created.":
        "那如果组件树上方根本没有对应的 <code>Provider</code> 呢？这种情况下，它会取创建 Context 时传给 <code>createContext</code> 的第一个参数作为值。",
    "Now, if we invoke <code>useContext(delorean)</code> without previously rendering a <code>&lt;delorean.Provider&gt;</code> component, the return value will be the array we supplied to <code>createContext</code>.":
        "现在，如果我们调用 <code>useContext(delorean)</code> 之前并没有渲染过 <code>&lt;delorean.Provider&gt;</code>，返回值就会是我们当初传给 <code>createContext</code> 的那个数组。",
    "Notice that our app still works the same, even though we no longer have state inside of our <code>App</code> component.":
        "注意，即便我们的 <code>App</code> 组件里不再有 state，应用依然能正常工作。",
    "Admittedly this isn't very practical since now our app will never re-render if <code>passengers</code> changes, but it does demonstrate how to use the default value of <code>createContext</code>.":
        "坦白说这样并不太实用，因为现在 <code>passengers</code> 变化时应用也不会重新渲染，但它确实演示了 <code>createContext</code> 默认值的用法。",
    "In reality, you'll almost always just duplicate the data – once for the default value and once for when you set it to state. Doing this assures that <code>useContext</code> will be able to supply a value if it doesn't have an associated <code>Provider</code> higher up in the tree, but also that your app will re-render when the value on state changes.":
        "实际上，你几乎总会把数据写两份 —— 一份作为默认值，一份放到 state 里。这样既能保证在没有上层 <code>Provider</code> 时 <code>useContext</code> 也能拿到值，又能保证 state 改变时应用能重新渲染。",
    "Here's a very clever example my good friend <a href=\"https://twitter.com/chantastic/status/979480237279928320\" metastring=\"\">chantastic</a> came up with for a situation in which you can take advantage of this. I've modified it a bit, but the core idea is the same.":
        "这里有一个相当巧妙的例子，来自我的好友 <a href=\"https://twitter.com/chantastic/status/979480237279928320\" metastring=\"\">chantastic</a>，展示了什么场景下可以利用这一点。我做了点小改动，但核心思路是一样的。",
    "Can you follow what's going on? First, we create a new Context and set its default value to <code>shit</code>. Then we render two components, <code>VisitFriendsHouse</code> and <code>VisitGrandmasHouse</code>.":
        "你能跟上这里发生了什么吗？首先我们新建了一个 Context，并把它的默认值设为 <code>shit</code>。然后渲染两个组件：<code>VisitFriendsHouse</code> 和 <code>VisitGrandmasHouse</code>。",
    "Because we're not allowed to swear at our Grandma's house, we use <code>expletive.Provider</code> to supply a value of <code>darn</code> as the value we're teleporting. That way, inside of <code>ContextualExclamation</code>, when <code>useContext</code> looks for the <code>value</code> of its nearest <code>Provider</code>, it'll find it, <code>darn</code>.":
        "因为在奶奶家不允许骂脏话，我们用 <code>expletive.Provider</code> 把要传送的值设为 <code>darn</code>。这样在 <code>ContextualExclamation</code> 里，<code>useContext</code> 会找到最近一层 <code>Provider</code> 的 <code>value</code>，也就是 <code>darn</code>。",
    "Unlike at Grandmas, with our friend, <del metastring=\"\">we're allowed to swear</del> Grandma can't hear us. So instead of wrapping it in <code>expletive.Provider</code>, we leave that off so that way, inside of <code>ContextualExclamation</code>, when <code>useContext</code> looks for the <code>value</code> of its nearest <code>Provider</code>, it won't find it and instead it'll use the default value, <code>shit</code>.":
        "和在奶奶家不同，在朋友家里，<del metastring=\"\">我们可以爆粗</del>奶奶反正听不见。所以我们不再用 <code>expletive.Provider</code> 包裹 —— 这样在 <code>ContextualExclamation</code> 里，<code>useContext</code> 找不到最近的 <code>Provider</code> 的 <code>value</code>，就会退而求其次用默认值 <code>shit</code>。",
    "Take this scenario, for example. What you've been taught is that whenever you have state that multiple components depend on, you'll want to <span class=\"font-bold relative m-px\" style=\"bottom:0px\">l</span><span class=\"font-bold relative m-px\" style=\"bottom:1px\">i</span><span class=\"font-bold relative m-px\" style=\"bottom:2px\">f</span><span class=\"font-bold relative m-px\" style=\"bottom:3px\">t</span> that state up to the nearest parent component and then pass it <span class=\"font-bold relative m-px\" style=\"bottom:3px\">d</span><span class=\"font-bold relative m-px\" style=\"bottom:2px\">o</span><span class=\"font-bold relative m-px\" style=\"bottom:1px\">w</span><span class=\"font-bold relative m-px\" style=\"bottom:0px\">n</span> via props.":
        "拿这个场景举例。你之前学到的是：当多个组件依赖同一块 state 时，就把它<span class=\"font-bold relative m-px\" style=\"bottom:0px\">提</span><span class=\"font-bold relative m-px\" style=\"bottom:1px\">升</span><span class=\"font-bold relative m-px\" style=\"bottom:2px\">到</span><span class=\"font-bold relative m-px\" style=\"bottom:3px\">上</span>级最近的共同父组件，然后通过 props <span class=\"font-bold relative m-px\" style=\"bottom:3px\">往</span><span class=\"font-bold relative m-px\" style=\"bottom:2px\">下</span><span class=\"font-bold relative m-px\" style=\"bottom:1px\">传</span><span class=\"font-bold relative m-px\" style=\"bottom:0px\">递</span>。",
    "<span class=\"text-brand-purple dark:text-brand-yellow font-bold font-mono\">1.</span> <span><span>Creating the <del>teleporter</del> Context<span></span></span></span>":
        "<span class=\"text-brand-purple dark:text-brand-yellow font-bold font-mono\">1.</span> <span><span>创建<del>传送器</del> Context<span></span></span></span>",
    "<span class=\"text-brand-purple dark:text-brand-yellow font-bold font-mono\">2.</span> <span>Deciding what we want to teleport and to where</span>":
        "<span class=\"text-brand-purple dark:text-brand-yellow font-bold font-mono\">2.</span> <span>决定要传送什么、传送到哪里</span>",
    "<span class=\"text-brand-purple dark:text-brand-yellow font-bold font-mono\">3.</span> <span>Getting what we teleported from inside a component</span>":
        "<span class=\"text-brand-purple dark:text-brand-yellow font-bold font-mono\">3.</span> <span>在组件内部拿到我们所传送的数据</span>",
}

TRANS["021 - Managing Advanced Effects - ui.dev"] = {
    "Now I get it. Yes, we've already had a few lessons on managing side effects in React and yes, those were the <em metastring=\"\">longest</em> ones in the course. Mastery is fun, effects are hard. Let's keep going.":
        "我懂。是的，我们已经讲了好几节关于管理副作用的课，而且它们是整个课程里<em metastring=\"\">最长</em>的几节。精通很爽，但 effect 真的难。我们继续。",
    "For a <em metastring=\"\">micro</em>second, until our effect runs and updates the state, the browser dimensions are <code>null</code>. This means that on the initial render of our app, anywhere we use <code>size.width</code> or <code>size.height</code> won't render properly.":
        "有<em metastring=\"\">一瞬间</em>（直到 effect 跑起来并更新 state 之前），浏览器尺寸的值是 <code>null</code>。也就是说在应用初次渲染时，任何用到 <code>size.width</code> 或 <code>size.height</code> 的地方都不会正确渲染。",
    "The primary reason this happens is because <code>useEffect</code> runs <em metastring=\"\">asynchronously</em> <em metastring=\"\">after</em> render. This is <em metastring=\"\">almost</em> always what you want, as it optimizes for showing the UI to the user as quickly as possible. However, in this scenario, we actually want our effect to run <em metastring=\"\">synchronously</em> <em metastring=\"\">before</em> React shows <em metastring=\"\">anything</em> to the user.":
        "出现这种情况的主要原因是：<code>useEffect</code> 会在渲染<em metastring=\"\">之后</em>以<em metastring=\"\">异步</em>方式运行。大多数时候这正是你想要的，能尽快把 UI 展示给用户。但在这个场景里，我们其实希望 effect 在 React 向用户展示<em metastring=\"\">任何东西</em><em metastring=\"\">之前</em>就<em metastring=\"\">同步</em>运行。",
    "This is exactly the use case that <code>React.useLayoutEffect</code> was designed for. React guarantees that the code inside <code>useLayoutEffect</code> and any state updates scheduled inside it will be processed <em metastring=\"\">before</em> the browser repaints the screen. This lets your component use layout information for rendering – as we're doing in our example with the browser's dimensions.":
        "这正是 <code>React.useLayoutEffect</code> 的设计场景。React 保证 <code>useLayoutEffect</code> 里的代码以及其中安排的任何 state 更新，都会在浏览器重绘屏幕<em metastring=\"\">之前</em>处理完。这让你的组件可以用布局信息来渲染 —— 就像我们例子里用到浏览器尺寸一样。",
    "Our artificial delay is still in place, but notice that now, React doesn't show anything to the user until <em metastring=\"\">after</em> its ran <code>useLayoutEffect</code> and updated our state. This way, the first time the user sees anything, it'll be with the layout information.":
        "我们人为加的延迟还在，但注意现在 React 直到 <em metastring=\"\">跑完</em> <code>useLayoutEffect</code>、更新完 state 之后才会向用户展示任何东西。这样用户第一次看到的画面就已经带有布局信息了。",
    "Now this works, and there's nothing <em metastring=\"\">wrong</em> with it – but there is some duplication here.":
        "这样能跑，也没有什么<em metastring=\"\">错</em> —— 但这里存在一点重复。",
    "Essentially all we're trying to do is subscribe to the browser's internal <code>navigator.onLine</code> state. However, in order to do that, we're creating and then managing <em metastring=\"\">another</em> piece of state, <code>networkStatus</code>, inside our component. That seems redundant.":
        "本质上我们想做的就是订阅浏览器内部的 <code>navigator.onLine</code> 状态。但为此我们又在组件里新建并管理了<em metastring=\"\">另一</em>块 state，<code>networkStatus</code>。感觉有点冗余。",
    "You'll notice that in our example above, both <code>subscribe</code> and <code>getSnapshot</code> live <em metastring=\"\">outside</em> of our component. This is convenient because it allows us to decouple our subscription logic from our component – but there's also another, more practical benefit to it as well.":
        "你会注意到上面的例子里，<code>subscribe</code> 和 <code>getSnapshot</code> 都住在组件<em metastring=\"\">外面</em>。这样做一方面让订阅逻辑和组件解耦，另一方面还带来一个更实际的好处。",
    f"And how does React define <em metastring=\"\">change</em>? The same way it always does, with {SVG_BTN_HELP_L}<code>Object.is</code>{SVG_BTN_HELP_R}.":
        f"那 React 如何定义“<em metastring=\"\">变化</em>”？和它一贯的做法一样，用 {SVG_BTN_HELP_L}<code>Object.is</code>{SVG_BTN_HELP_R}。",
}

TRANS["022 - Abstracting Reactive Values with useEffectEvent - ui.dev"] = {
    "Because \"Don't Repeat Yourself\" (DRY) is a principle of software development and <strong metastring=\"\">not</strong> one of education, let's recap everything we know about React's <code>useEffect</code> hook one last time.":
        "因为“Don't Repeat Yourself（DRY）”是软件开发的原则，<strong metastring=\"\">而不是</strong>教学的原则，所以我们再来最后总结一次关于 React 的 <code>useEffect</code> hook 的全部要点。",
    "The whole purpose of <code>useEffect</code> is to encapsulate a side effect that synchronizes your component with some outside system. It works by removing the side effect from React's rendering flow and delaying its execution until it's safe to do so, <strong metastring=\"\">after</strong> the component has rendered.":
        "<code>useEffect</code> 的全部目的，就是封装一个把组件与外部系统同步的副作用。它通过把副作用从 React 的渲染流程中抽离出来，并推迟到可以安全执行（也就是组件渲染<strong metastring=\"\">之后</strong>）时再运行。",
    "What we really need in this moment is a way to tell React that we want to use a reactive value inside of <code>useEffect</code>, but that reactive value has <em metastring=\"\">nothing</em> to do with synchronizing the component, and therefore, shouldn't need to be included in the dependency array.":
        "这时我们真正需要的，是一种方式告诉 React：我想在 <code>useEffect</code> 里使用某个响应式值，但这个值和“同步组件”<em metastring=\"\">毫无关系</em>，因此不应该被放进依赖数组里。",
    "The biggest thing to notice is that <code>url</code> is still included in the dependency array <strong metastring=\"\">and</strong> we're passing it as an argument to <code>onPageView</code>. This is good practice as it makes it explicit which values are synchronizing (<code>url</code>) and which aren't (<code>state</code>).":
        "最需要注意的是：<code>url</code> 依然在依赖数组里，<strong metastring=\"\">而且</strong>我们把它作为参数传给了 <code>onPageView</code>。这是个不错的习惯，因为它明确地区分了哪些值参与同步（<code>url</code>）、哪些不参与（<code>state</code>）。",
}

TRANS["023 - Creating Custom Hooks - ui.dev"] = {
    "React is a library for building user interfaces. With React, your View a function of your application's State – <code>v = f(s)</code>. All you have to do is worry about how the state in your application changes, and React handles the rest.":
        "React 是一个构建用户界面的库。在 React 里，你的 View 是应用 State 的一个函数 —— <code>v = f(s)</code>。你只需要关心应用里 state 如何变化，剩下的交给 React。",
    "Now here's a question I want you to think through. Let's say we wanted to display the user's network status in <em metastring=\"\">another</em> part of our app. How would you go about doing that?":
        "这里有一个问题想让你好好想想。假设我们想在应用的<em metastring=\"\">另外一处</em>也显示用户的网络状态，你会怎么做？",
    "What if, just like React comes with its own set of hooks, we were also able to make our own <em metastring=\"\">custom</em> hooks? In that scenario, a custom <code>useNetworkStatus</code> hook would be awfully convenient.":
        "假如我们也能像 React 自带 hook 那样，写自己的<em metastring=\"\">自定义</em> hook 会怎样？在这个场景里，一个自定义的 <code>useNetworkStatus</code> hook 会非常方便。",
    "One question you may have is <em metastring=\"\">why</em> exactly does a hook need to start with <code>use</code>? That seems overly restrictive.":
        "你可能会有一个问题：hook <em metastring=\"\">为什么</em>一定要以 <code>use</code> 开头？这看起来过于死板了吧？",
    "Now the only question left is <strong metastring=\"\">when</strong> is it appropriate to create a custom hook? The answer, as with most things in React, is to rely on your intuition. The same intuition you've developed about functions and when to create them can be directly applied to creating hooks. Mostly, you'll know it when you see it.":
        "现在剩下的唯一问题就是：<strong metastring=\"\">什么时候</strong>适合创建一个自定义 hook？答案和 React 里大多数事情一样，靠你的直觉。你在“什么时候创建函数”上已有的直觉，基本可以直接套用到创建 hook 上。很多时候，你一看到就知道该不该抽。",
    "A custom hook is a function that starts with <span class=\"font-mono\">use</span> and calls other hooks inside of it":
        "自定义 hook 就是一个以 <span class=\"font-mono\">use</span> 开头、并在函数体内部调用其他 hook 的函数",
}

TRANS["024 - Rebuilding useHooks - ui.dev"] = {
    "When we started working on <a href=\"https://react.gg/\" metastring=\"\">react.gg</a>, a primary focus of ours was figuring out how to get students comfortable working with \"production\" level React code, without the burden or context of needing to dive into a fully fledged project.":
        "我们开始做 <a href=\"https://react.gg/\" metastring=\"\">react.gg</a> 时，最重要的关注点之一，就是如何让学员在不必背上“整套真实项目”的负担的情况下，依然能从容地处理“生产级别”的 React 代码。",
    "I'm sure you've experienced it before. In an attempt to make the course \"hands-on\", the instructor has you clone a <em metastring=\"\">starter</em> project from Github, <code>npm install</code> two dozen packages, and then you spend the next 14 hours watching them glue it together.":
        "你肯定有过这种体验 —— 为了让课程“够实战”，老师让你从 GitHub 克隆一个<em metastring=\"\">起始</em>项目，<code>npm install</code> 两打依赖，然后你接下来 14 小时都在看他把这些东西粘在一起。",
    "When we built react.gg, <strong metastring=\"\">this</strong> is the experience we wanted to recreate.":
        "做 react.gg 时，我们想重现的正是<strong metastring=\"\">这种</strong>体验。",
    "The tradeoff here, of course, is that a \"real-world <em metastring=\"\">simulated</em> environment\" is still just that – simulated.":
        "当然，这里有个取舍：一个“<em metastring=\"\">模拟</em>的真实世界环境”终归是模拟的。",
    "The course was still, despite our best effort, missing <em metastring=\"\">something</em> that would allow you to get comfortable with the <em metastring=\"\">actual</em> code you'll see in the <em metastring=\"\">actual</em> projects you'll work on.":
        "尽管我们尽了最大努力，这门课程仍然<em metastring=\"\">缺少</em>某种东西 —— 一种能让你熟悉你<em metastring=\"\">真正</em>会在<em metastring=\"\">真正</em>项目里看到的那种代码的东西。",
    "Then we had an idea. If we wanted you to get real-world experience, what better way than to have you build a real-world React library. Naturally, this led us to the creation of <a href=\"https://usehooks.com/\" metastring=\"\">useHooks</a> - a library of 50 modern, real-world, production ready React hooks that as of this writing gets more than <a href=\"https://npmjs.com/package/@uidotdev/usehooks\" metastring=\"\">20,000</a> downloads a week.":
        "后来我们有了一个想法：如果想让你获得真实世界的经验，还有什么比让你亲手做一个真实世界的 React 库更合适的？于是顺理成章地，我们做出了 <a href=\"https://usehooks.com/\" metastring=\"\">useHooks</a> —— 一个包含 50 个现代、实战、生产就绪的 React hook 的库，截至撰写本文时，它每周的下载量超过 <a href=\"https://npmjs.com/package/@uidotdev/usehooks\" metastring=\"\">20,000</a> 次。",
    "What I love about useHooks, and what's impossible to do with traditional course projects, is that <em metastring=\"\">everything</em> we've covered in the course so far is used in the library. There isn't one thing you've learned that you won't see again in one form or another in useHooks. Not only that, but by the nature of building reusable hooks, you'll also get more familiar with fundamental browser APIs like <code>localStorage</code>, <code>matchMedia</code>, and <code>IntersectionObserver</code> to name a few.":
        "我喜欢 useHooks 的地方、也是传统课程项目做不到的地方，是我们课程里讲过的<em metastring=\"\">所有</em>内容都会在这个库里被用到。你学过的任何一样东西，都会在 useHooks 中以某种形式再次出现。不仅如此，由于你在构建可复用的 hook，还会更熟悉 <code>localStorage</code>、<code>matchMedia</code>、<code>IntersectionObserver</code> 这类基础的浏览器 API。",
}

def fill(stem, mapping):
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

for stem, mapping in TRANS.items():
    fill(stem, mapping)