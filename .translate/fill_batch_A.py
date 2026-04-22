"""Batch A: fill inline translations for 001, 002, 003, 004, 005, 006, 007, 008, 009, 011, 014."""
import os, json, sys, re, unicodedata
sys.stdout.reconfigure(encoding="utf-8")

BASE = r"D:\Personal\Downloads\react\.translate\inline"

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("\u00a0", " ")
    s = s.replace("\u2013", "-").replace("\u2014", "-")
    s = s.replace("\u2018", "'").replace("\u2019", "'")
    s = s.replace("\u201c", '"').replace("\u201d", '"')
    s = re.sub(r"\s+", " ", s).strip()
    return s

# file stem -> dict of { english inner HTML : chinese inner HTML }
TRANS = {}

TRANS["001 - Getting Started - ui.dev"] = {
    "- <a href=\"https://twitter.com/tylermcginnis\" metastring=\"\">Tyler</a>, <a href=\"https://twitter.com/lynnandtonic\" metastring=\"\">Lynn</a>, <a href=\"https://twitter.com/benadam11\" metastring=\"\">Ben</a>, and <a href=\"https://twitter.com/alexbrown40\" metastring=\"\">Alex</a>":
        "- <a href=\"https://twitter.com/tylermcginnis\" metastring=\"\">Tyler</a>、<a href=\"https://twitter.com/lynnandtonic\" metastring=\"\">Lynn</a>、<a href=\"https://twitter.com/benadam11\" metastring=\"\">Ben</a> 和 <a href=\"https://twitter.com/alexbrown40\" metastring=\"\">Alex</a>",
}

TRANS["002 - Why React_ - ui.dev"] = {
    "So the question is, how in the world did React go from sentiments like this, to being universally loved and <i>mostly</i> respected?":
        "所以问题来了：React 是怎么从当年那种评价，变成今天普遍被喜爱、<i>大多数时候</i>也被尊重的框架的？",
    "jQuery revolutionized building for the web by both creating a simple <em metastring=\"\">and</em> unified abstraction over manipulating the DOM that worked in <em metastring=\"\">any</em> browser - regardless of typical browser compatibility issues.":
        "jQuery 革新了 Web 开发方式 —— 它在操作 DOM 之上提供了一层既简单<em metastring=\"\">又</em>统一的抽象，而且在<em metastring=\"\">任何</em>浏览器上都能工作，屏蔽了那些常见的兼容性问题。",
    "What jQuery needed was something that encouraged a little more structure. Something that gave a <em metastring=\"\">backbone</em> 😎 to our applications.":
        "jQuery 需要的是某种更能约束代码结构的东西 —— 能给我们的应用一套<em metastring=\"\">骨架</em> 😎 的东西。",
    "In theory, this was nice because you didn't have to worry about doing manual DOM manipulation yourself. In practice, well, implicit state changes usually lead to code that is both hard to follow <em metastring=\"\">and</em> hard to debug. It also led to performance issues since Angular.js had to constantly scan your app looking for state changes.":
        "理论上很不错，因为你不必再手动操作 DOM。但实际情况是，隐式的状态变更往往会让代码既难以跟踪<em metastring=\"\">又</em>难以调试。同时也带来了性能问题 —— Angular.js 必须不停扫描你的应用以发现状态变化。",
    "What has changed though, is <em metastring=\"\">how</em> React is used. From about 2014 - 2020, React was used (in conjunction with React Router), to primarily create single page applications. More recently, React has taken on a different role – that of a UI primitive.":
        "真正变化的是 React <em metastring=\"\">使用方式</em>。从 2014 年到 2020 年前后，React（通常配合 React Router）主要被用来构建单页应用。最近几年，React 扮演起了另一种角色 —— 作为一种 UI 基础构件（primitive）。",
    "I know it seems strange, but \"metaframeworks\" like <a href=\"https://nextjs.dev/\" metastring=\"\">Next.js</a>, <a href=\"https://remix.dev/\" metastring=\"\">Remix</a>, and <a href=\"https://astro.build/\" metastring=\"\">Astro</a> have gained popularity by treating React as a sort of UI primitive and building on top of it with new features like server side rendering, intelligent bundling, route pre-fetching, and more.":
        "我知道这听起来有点奇怪，但像 <a href=\"https://nextjs.dev/\" metastring=\"\">Next.js</a>、<a href=\"https://remix.dev/\" metastring=\"\">Remix</a>、<a href=\"https://astro.build/\" metastring=\"\">Astro</a> 这类“元框架”正是把 React 当作一种 UI 基础构件来对待，并在其之上加入服务端渲染、智能打包、路由预取等新特性，因而大受欢迎。",
    "But regardless of <em metastring=\"\">how</em> you use React, this course was designed to teach you React from first principles, so you'll be able to use it in any context.":
        "但无论你<em metastring=\"\">怎样</em>使用 React，本课程的设计都是从第一性原理出发去讲解 React，让你能在任意场景下把它用好。",
    "Developers <span class=\"font-black tracking-wider\" style=\"color:var(--blue)\">really</span> didn't like it. And at first glance, why would they? It was drastically different than anything that had come before it.":
        "开发者<span class=\"font-black tracking-wider\" style=\"color:var(--blue)\">真的</span>不喜欢它。乍看之下也正常 —— 它和之前的一切都截然不同。",
    "With jQuery, what started out as a simple way to update DOM state, typically devolved into a mess of <span class=\"font-black tracking-wider\" style=\"color:var(--orange)\">spaghetti</span> like mutations that were both hard to predict and keep track of if you weren't careful.":
        "用 jQuery 时，最初只是想简单地更新一下 DOM 状态，但稍不留神就会演变成一团<span class=\"font-black tracking-wider\" style=\"color:var(--orange)\">意大利面</span>式的状态改动 —— 既难以预测也难以追踪。",
}

TRANS["003 - Imperative vs Declarative Programming - ui.dev"] = {
    "You won't get very far into learning React until you hear it – <em metastring=\"\">React is <span class=\"sparkle_wrapper__cL2jQ\"><span class=\"sparkle_sparkle_wrapper__Izdcu\" style=\"top:74%;left:48%\"><svg class=\"sparkle_sparkle_svg__WdZ3Y\" fill=\"none\" height=\"17\" viewbox=\"0 0 68 68\" width=\"17\"><path d=\"M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z\" fill=\"var(--yellow)\"></path></svg></span><span class=\"sparkle_sparkle_wrapper__Izdcu\" style=\"top:50%;left:24%\"><svg class=\"sparkle_sparkle_svg__WdZ3Y\" fill=\"none\" height=\"15\" viewbox=\"0 0 68 68\" width=\"15\"><path d=\"M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z\" fill=\"var(--yellow)\"></path></svg></span><strong class=\"sparkle_child_wrapper__bem0y\">declarative</strong></span></em>. But, what does that even mean? If you try to dive deeper, you inevitably come across a definition that looks something like this, comparing it to imperative programming.":
        "学 React 没多久你就会听到这样一句话 —— <em metastring=\"\"><span class=\"sparkle_wrapper__cL2jQ\"><span class=\"sparkle_sparkle_wrapper__Izdcu\" style=\"top:74%;left:48%\"><svg class=\"sparkle_sparkle_svg__WdZ3Y\" fill=\"none\" height=\"17\" viewbox=\"0 0 68 68\" width=\"17\"><path d=\"M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z\" fill=\"var(--yellow)\"></path></svg></span><span class=\"sparkle_sparkle_wrapper__Izdcu\" style=\"top:50%;left:24%\"><svg class=\"sparkle_sparkle_svg__WdZ3Y\" fill=\"none\" height=\"15\" viewbox=\"0 0 68 68\" width=\"15\"><path d=\"M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z\" fill=\"var(--yellow)\"></path></svg></span><strong class=\"sparkle_child_wrapper__bem0y\">React 是声明式的</strong></span></em>。但这到底是什么意思？如果你试着深挖，迟早会看到类似这样的定义 —— 把它和命令式编程对比：",
    "Imperative programming is <b>how</b> you do something, and declarative programming is more like <b>what</b> you do.":
        "命令式编程描述的是<b>怎么</b>做某件事，而声明式编程更像是在描述<b>要做什么</b>。",
    "The hard part about this topic is, as my friend <a href=\"https://twitter.com/iammerrick/status/699373002249498624\" metastring=\"\">Merrick</a> has observed, it's one of those things you have an intuition about, but can’t seem to explain. Vibe driven development, if you will.":
        "正如我的朋友 <a href=\"https://twitter.com/iammerrick/status/699373002249498624\" metastring=\"\">Merrick</a> 观察到的，这个话题的难点在于：你对它有种直觉，却怎么也说不清楚。非要说的话，这就是「凭感觉驱动的开发」。",
    "I’m going to ask you a question. I want you to think of both an <strong metastring=\"\">imperative</strong> response and a <strong metastring=\"\">declarative</strong> response.":
        "我来问你一个问题。我希望你同时想一个<strong metastring=\"\">命令式</strong>的回答和一个<strong metastring=\"\">声明式</strong>的回答。",
    "Regardless of how I get to your house, what really matters is the car I drive. Am I going to drive an <em metastring=\"\">imperative</em> stick shift car or a <em metastring=\"\">declarative</em> automatic car? Enough metaphors?":
        "其实不管我怎么到你家，真正重要的是我开的是哪辆车。我是开一辆<em metastring=\"\">命令式</em>的手动挡，还是一辆<em metastring=\"\">声明式</em>的自动挡？比喻够多了吧？",
    "<span class=\"text-brand-purple dark:text-brand-yellow font-bold font-mono\">1.</span> <span>The most obvious commonality is that they’re describing <b>HOW</b> to do something. In each example, we’re either explicitly iterating over an array or explicitly laying out steps for how to implement the functionality we want.</span>":
        "<span class=\"text-brand-purple dark:text-brand-yellow font-bold font-mono\">1.</span> <span>最明显的共同点是它们都在描述<b>怎么做</b>。每个例子里，我们要么显式地遍历一个数组，要么显式地列出实现目标功能的每一步。</span>",
    "<span class=\"text-brand-purple dark:text-brand-yellow font-bold font-mono\">2.</span> <span>This one might not be as obvious if you’re not used to thinking in the <i>declarative</i> or even more specifically <i>functional</i> way. In each example, we’re mutating some piece of state.</span>":
        "<span class=\"text-brand-purple dark:text-brand-yellow font-bold font-mono\">2.</span> <span>如果你不太习惯<i>声明式</i>、甚至更具体的<i>函数式</i>思维，这一点可能不太明显。每个例子中，我们都在修改某一块状态。</span>",
    "In every example we’re describing <span class=\"font-black tracking-wider\" style=\"color:var(--green)\">what</span> we want to happen rather than <span class=\"font-black tracking-wider\" style=\"color:var(--pink)\">how</span> (we don’t know how map and reduce are implemented, we also probably don’t care). We’re not mutating any state. All of the mutations are abstracted inside of <code>map</code> and <code>reduce</code>. It’s also more readable (once you get used to <code>map</code> and <code>reduce</code>, of course).":
        "在每个例子里，我们都在描述我们希望<span class=\"font-black tracking-wider\" style=\"color:var(--green)\">发生什么</span>，而不是<span class=\"font-black tracking-wider\" style=\"color:var(--pink)\">怎么做</span>（我们不知道 map 和 reduce 内部是怎么实现的，大概率也不关心）。我们没有修改任何状态，所有的修改都被封装在 <code>map</code> 和 <code>reduce</code> 里。而且（一旦你习惯了 <code>map</code> 和 <code>reduce</code>）它读起来也更清晰。",
    "The imperative approach is concerned with <span class=\"font-black tracking-wider\" style=\"color:var(--pink)\">how</span> you’re actually going to get a seat. You need to list out the steps to be able to show <span class=\"font-black tracking-wider\" style=\"color:var(--pink)\">how</span> you’re going to get a table. The declarative approach is more concerned with <span class=\"font-black tracking-wider\" style=\"color:var(--green)\">what</span> you want, a table for two.":
        "命令式关心的是你<span class=\"font-black tracking-wider\" style=\"color:var(--pink)\">怎么</span>真正拿到一张桌子。你需要把所有步骤列出来，来展示你<span class=\"font-black tracking-wider\" style=\"color:var(--pink)\">如何</span>拿到桌子。而声明式更关心你<span class=\"font-black tracking-wider\" style=\"color:var(--green)\">想要什么</span> —— 一张两人的桌子。",
    "By glancing at both examples, you have a clear understanding of what is going on. They’re both declarative. They’re concerned with <span class=\"font-black tracking-wider\" style=\"color:var(--green)\">what</span> you want to be done, rather than <span class=\"font-black tracking-wider\" style=\"color:var(--pink)\">how</span> you want it done.":
        "扫一眼这两个例子，你就能清楚地知道在发生什么。它们都是声明式的 —— 关心的是你<span class=\"font-black tracking-wider\" style=\"color:var(--green)\">想做什么</span>，而不是你想<span class=\"font-black tracking-wider\" style=\"color:var(--pink)\">怎么做</span>。",
    "Here are 3 interview type questions. We're going to answer them <span class=\"font-black tracking-wider\" style=\"color:var(--pink)\">imperatively</span>, as if we're focused on <span class=\"font-black tracking-wider\" style=\"color:var(--pink)\">how</span>.":
        "下面是三道类似面试题的问题。我们要用<span class=\"font-black tracking-wider\" style=\"color:var(--pink)\">命令式</span>方式来回答，也就是把注意力放在<span class=\"font-black tracking-wider\" style=\"color:var(--pink)\">怎么做</span>上。",
    "Now, let's take a look at some <span class=\"font-black tracking-wider\" style=\"color:var(--green)\">declarative</span> examples. The goal is to fix all the problems from above. So each example needs to describe <span class=\"font-black tracking-wider\" style=\"color:var(--green)\">what</span> is happening, can’t mutate state, and should be readable at a glance.":
        "现在来看几个<span class=\"font-black tracking-wider\" style=\"color:var(--green)\">声明式</span>的例子。目标是修掉上面所有的问题，所以每个例子都需要描述<span class=\"font-black tracking-wider\" style=\"color:var(--green)\">发生了什么</span>、不能修改状态、而且一眼就能读懂。",
    "Well, I cheated a little bit and am using React — but note that all three imperative mistakes are still fixed. The real beauty of React is that you can create <span class=\"font-black tracking-wider\" style=\"color:var(--green)\">declarative</span> user interfaces – simply by describing <span class=\"font-black tracking-wider\" style=\"color:var(--green)\">what</span> you want your UI to look like based on your state.":
        "好吧，我作弊了一点，用了 React —— 不过注意，之前命令式的那三个问题依然被解决了。React 真正的魅力就在于：你可以打造<span class=\"font-black tracking-wider\" style=\"color:var(--green)\">声明式</span>的用户界面 —— 只需根据 state 描述你<span class=\"font-black tracking-wider\" style=\"color:var(--green)\">希望</span> UI 长什么样即可。",
}

TRANS["004 - Pure Functions - ui.dev"] = {
    "Any time a function does <strong metastring=\"\">anything</strong> other than this, whether through relying on state other than the input value it receives or creating an observable change to the program itself, it's said to have a side effect.":
        "只要一个函数做了<strong metastring=\"\">除此之外</strong>的任何事情 —— 不管是依赖它接收的输入值以外的状态，还是对程序本身产生了可观察的改动 —— 就可以说它有副作用。",
    "So why are side effects bad? Well, they're not <em metastring=\"\">bad</em> – they're just unpredictable.":
        "那副作用为什么不好？其实它们并不<em metastring=\"\">坏</em> —— 只是不可预测而已。",
}

TRANS["005 - Components - ui.dev"] = {
    "React, of course, is a lovechild of the two – giving you the declarative-ness of HTML with the feature set of JavaScript. But, what does that <em metastring=\"\">actually</em> look like.":
        "当然，React 正是这两者的结合体 —— 给你 HTML 的声明式写法，同时具备 JavaScript 的全部能力。那它<em metastring=\"\">实际</em>长什么样呢？",
    "The <em metastring=\"\">only</em> change we need to make it a true React component is to capitalize the first letter of our function.":
        "要把它变成一个真正的 React component，我们<em metastring=\"\">唯一</em>需要做的，就是把函数名首字母大写。",
    "The reason you need to capitalize the first letter of your component is so React knows it's a React component and not a normal DOM <code>element</code> – i.e. <span class=\"font-mono tracking-tight px-1 py-0.5 font-semibold text-[16px] bg-gray-75 dark:bg-brand-charcoal rounded text-brand-blue\">Footer</span> vs <span class=\"font-mono tracking-tight px-1 py-0.5 font-semibold text-[16px] bg-gray-75 dark:bg-brand-charcoal rounded text-brand-green\">footer</span>.":
        "之所以要把 component 的首字母大写，是为了让 React 知道它是一个 React component，而不是普通的 DOM <code>element</code> —— 也就是 <span class=\"font-mono tracking-tight px-1 py-0.5 font-semibold text-[16px] bg-gray-75 dark:bg-brand-charcoal rounded text-brand-blue\">Footer</span> 与 <span class=\"font-mono tracking-tight px-1 py-0.5 font-semibold text-[16px] bg-gray-75 dark:bg-brand-charcoal rounded text-brand-green\">footer</span> 的区别。",
    "Notice that we don't invoke <code>Authors</code> as if it's a normal function – i.e. <code>Authors()</code>. Instead, we treat it as if it were an HTML element, wrapping it in angle brackets – i.e. <code>&lt;Authors /&gt;</code>.":
        "注意我们并不像调用普通函数那样去调用 <code>Authors</code>（即 <code>Authors()</code>），而是把它当作一个 HTML 元素来用，用尖括号包起来 —— 也就是 <code>&lt;Authors /&gt;</code>。",
    "For example, we can refactor the code above like so – assuming <code>Timeline</code>, <code>Trending</code>, and <code>Follow</code> are only used inside of this <code>Home</code> component.":
        "比如，假设 <code>Timeline</code>、<code>Trending</code> 和 <code>Follow</code> 只在这个 <code>Home</code> component 里用到，我们可以把上面的代码重构成下面这样。",
}

TRANS["006 - JSX - ui.dev"] = {
    "For the former to be true, we'd have to be returning literal HTML. Clearly that's not the case because we can't <em metastring=\"\">literally</em> have HTML inside of a JavaScript file. But if we're not returning HTML, what exactly are we returning?":
        "如果是前者，那我们就得真的返回 HTML。显然不是这样，因为我们不可能在 JavaScript 文件里<em metastring=\"\">字面上</em>写 HTML。但如果返回的不是 HTML，我们到底在返回什么？",
    "For the most part, writing JSX should feel pretty natural. It's <em metastring=\"\">mostly</em> just like HTML, but there are a few things to be aware of. We'll spend the rest of this post exploring some of those gotchas as well as some tips and tricks when it comes to JSX.":
        "大多数时候，写 JSX 会感觉相当自然。它<em metastring=\"\">基本上</em>就像 HTML，但有几点需要留意。这篇文章剩下的部分就用来探讨这些陷阱，以及写 JSX 时的一些小技巧。",
    "There also exists a shorthand syntax for React Fragment (<code>&lt;&gt;</code>), but it feels a little <em metastring=\"\">too</em> magical to me, so I don't use it much.":
        "React Fragment 还有一种简写形式（<code>&lt;&gt;</code>），不过在我看来有点<em metastring=\"\">太</em>魔法了，所以我用得不多。",
    "Unfortunately, we're not quite done yet. There's just one small addition we need to make to our code. Whenever you use <code>.map</code> to create a list in React, you need to make sure that you add a <strong metastring=\"\">unique</strong> <code>key</code> prop to each list item.":
        "可惜还没完。我们还需要在代码里做一个小小的补充。每当你在 React 里用 <code>.map</code> 来生成列表时，都必须给每个列表项加上一个<strong metastring=\"\">唯一</strong>的 <code>key</code> prop。",
    "It's React's job to make rendering the list as fast as possible. When you give each list item a <strong metastring=\"\">unique</strong> <code>key</code> prop, it helps React know which items, if any, change throughout different renders of that component.":
        "让列表渲染尽可能快是 React 的职责。当你给每个列表项一个<strong metastring=\"\">唯一</strong>的 <code>key</code> prop，就能帮助 React 在组件多次渲染之间识别出哪些项发生了变化。",
    "For the curious amongst you, you're probably wondering how JSX <em metastring=\"\">actually</em> works. We have an entire bonus section later on dedicated to this question, but here's a quick teaser.":
        "好奇心重的同学可能已经在想：JSX <em metastring=\"\">到底</em>是怎么工作的？后面我们有一整节附加内容专门讲这个问题，这里先给你一个预告。",
}

TRANS["007 - Props - ui.dev"] = {
    "Without the ability to pass data, in this case <span class=\"highlight-trigger font-medium underline decoration-brand-blue !cursor-help\" style=\"display:inline-block;white-space:nowrap\"><code>username</code></span>, to each of our of functions, our composition would break down.":
        "如果没办法把数据（这里是 <span class=\"highlight-trigger font-medium underline decoration-brand-blue !cursor-help\" style=\"display:inline-block;white-space:nowrap\"><code>username</code></span>）传给每一个函数，我们的组合就没法成立。",
    "Similarly, because React relies heavily on composition, there needs to exist a way to pass data <strong metastring=\"\">into</strong> components. This brings us to our next important React concept, <code>props</code>.":
        "同样地，因为 React 严重依赖组合，就必须有一种方式能把数据<strong metastring=\"\">传入</strong> component。这就引出了 React 下一个重要的概念 —— <code>props</code>。",
}

TRANS["008 - Elements vs Components - ui.dev"] = {
    "The primary reason for the confusion is because there's an important but subtle step between when React evaluates your code, and the browser sees it. This makes sense. The browser can only understand JavaScript – and though JSX is a syntax <em metastring=\"\">extension</em> to JavaScript, it's still not browser compatible JavaScript.":
        "造成这种困惑的主要原因在于：React 执行你的代码与浏览器最终看到结果之间，有一步重要却不起眼的中间过程。这其实合理 —— 浏览器只懂 JavaScript，而 JSX 只是 JavaScript 的一种语法<em metastring=\"\">扩展</em>，本身并不是浏览器能直接理解的 JavaScript。",
    "The answer lies in what React calls an <strong metastring=\"\">element</strong>.":
        "答案就藏在 React 所说的 <strong metastring=\"\">element</strong> 里。",
    "This problem isn't anything new. We've been <button aria-controls=\"radix-:rab:\" aria-expanded=\"false\" aria-haspopup=\"dialog\" class=\"Popover_children__8p5Di\" data-state=\"closed\" type=\"button\"><span>compiling</span> <svg class=\"fill-brand-purple dark:fill-brand-yellow w-2 h-2 b-2 mx-0.5 mb-4\" enable-background=\"new 0 0 455 455\" version=\"1.1\" viewbox=\"0 0 455 455\" x=\"0\" xml:space=\"preserve\" xmlns=\"http://www.w3.org/2000/svg\" y=\"0\"><path d=\"M347.49 227L454.5 165.212 394.508 61.288 287.5 123.077 287.5 0 167.5 0 167.5 123.077 60.492 61.288 0.499 165.212 107.51 227 0.5 288.788 60.492 392.712 167.5 330.923 167.5 455 287.5 455 287.5 330.923 394.508 392.712 454.501 288.788z\"></path></svg></button> non-browser-compatible syntax (Elm, TypeScript, CoffeeScript, etc.) to JavaScript for years.":
        "这个问题并不新鲜。多年来我们一直在把浏览器无法直接理解的语法（Elm、TypeScript、CoffeeScript 等等）<button aria-controls=\"radix-:rab:\" aria-expanded=\"false\" aria-haspopup=\"dialog\" class=\"Popover_children__8p5Di\" data-state=\"closed\" type=\"button\"><span>编译</span> <svg class=\"fill-brand-purple dark:fill-brand-yellow w-2 h-2 b-2 mx-0.5 mb-4\" enable-background=\"new 0 0 455 455\" version=\"1.1\" viewbox=\"0 0 455 455\" x=\"0\" xml:space=\"preserve\" xmlns=\"http://www.w3.org/2000/svg\" y=\"0\"><path d=\"M347.49 227L454.5 165.212 394.508 61.288 287.5 123.077 287.5 0 167.5 0 167.5 123.077 60.492 61.288 0.499 165.212 107.51 227 0.5 288.788 60.492 392.712 167.5 330.923 167.5 455 287.5 455 287.5 330.923 394.508 392.712 454.501 288.788z\"></path></svg></button>成 JavaScript。",
}

# 009 shares the exact same 3 paragraphs as 008 — reuse the same translations.
TRANS["009 - Elements vs Components - ui.dev + styles.css"] = dict(TRANS["008 - Elements vs Components - ui.dev"])

TRANS["011 - Preserving Values with useState - ui.dev"] = {
    "So what does adding state to a component look like? Let's say we were building a simple <strong metastring=\"\">counter</strong> app that keeps track of how many times a user has clicked a button.":
        "那给 component 加上 state 是什么样子？假设我们要写一个简单的<strong metastring=\"\">计数器</strong>应用，用来记录用户点了多少次按钮。",
    "Ironically, it won't work for the same reason, because React <em metastring=\"\">is</em> just JavaScript – and that's not how JavaScript works.":
        "讽刺的是，它不会起作用，原因和之前一样：React <em metastring=\"\">就是</em> JavaScript —— 而 JavaScript 本来就不是这么工作的。",
    "Well, we need some help from React. Specifically, we need a way to tell React to preserve the value of <code>count</code> between different invocations of our <code>Counter</code> function (React refers to these function component invocations as <em metastring=\"\">renders</em>).":
        "这时候就得请 React 帮忙了。具体来说，我们需要一种方式告诉 React 在我们的 <code>Counter</code> 函数多次调用之间保留 <code>count</code> 的值（React 把函数组件的这些调用称为<em metastring=\"\">渲染</em>）。",
    "Lucky for us, React comes with a <span class=\"font-black tracking-wider\" style=\"color:var(--brand-orange)\">hook</span> that does exactly this called <code>useState</code>.":
        "幸运的是，React 自带了一个正好干这件事的 <span class=\"font-black tracking-wider\" style=\"color:var(--brand-orange)\">hook</span>，叫做 <code>useState</code>。",
    "\"Hooks are functions, but it’s helpful to think of them as unconditional declarations about your component’s needs. You <em metastring=\"\">use</em> React features at the top of your component similar to how you <em metastring=\"\">import</em> modules at the top of your file.\" - React docs":
        "“Hook 是函数，但把它们看作对组件需求的无条件声明会更有帮助。你在组件顶部<em metastring=\"\">使用（use）</em>React 的能力，就像在文件顶部<em metastring=\"\">引入（import）</em>模块一样。” —— React 官方文档",
    "Now that we know the purpose of <code>useState</code> as well as how it works, let's update our <code>Counter</code> example from earlier to <em metastring=\"\">use</em> it.":
        "现在我们知道了 <code>useState</code> 的用途和工作方式，就用它来更新一下前面那个 <code>Counter</code> 示例。",
    "Now, regardless of how many times React renders our <code>Counter</code> component, the value of <code>count</code> will persist across all of those renders. But this brings up an interesting question, when <em metastring=\"\">does</em> React render our components exactly?":
        "现在，不管 React 渲染多少次 <code>Counter</code>，<code>count</code> 的值都会在所有渲染之间保留下来。但这就引出一个有意思的问题：React 到底<em metastring=\"\">什么时候</em>会渲染我们的组件？",
    "If we break it down, we've seen how you create your <span class=\"font-black tracking-wider\" style=\"color:var(--yellow)\">View</span> with JSX, and how you encapsulate that View inside of a <span class=\"font-black tracking-wider\" style=\"color:var(--green)\">function</span> to get your component. But there's still one piece of the formula we need to talk about, <span class=\"font-black tracking-wider\" style=\"color:var(--blue)\">state</span>.":
        "拆开来看，我们已经见过如何用 JSX 搭出 <span class=\"font-black tracking-wider\" style=\"color:var(--yellow)\">View</span>，以及如何把 View 封装到<span class=\"font-black tracking-wider\" style=\"color:var(--green)\">函数</span>里得到 component。但这个公式里还有一块没讲 —— <span class=\"font-black tracking-wider\" style=\"color:var(--blue)\">state</span>。",
}

TRANS["014 - Reality Check - ui.dev"] = {
    "In the real world, it's not uncommon to need to do things <em metastring=\"\">outside</em> of React. Fetching data from a server, interacting directly with the DOM, or even using native browser APIs like <code>setTimeout</code> or <code>localStorage</code> are all examples of real world use cases that don't fit neatly into the React's model.":
        "在真实项目里，经常需要做一些<em metastring=\"\">React 之外</em>的事。比如从服务器获取数据、直接和 DOM 交互、甚至使用 <code>setTimeout</code> 或 <code>localStorage</code> 这类浏览器原生 API —— 这些场景都没法完全套进 React 的模型里。",
}

def fill(stem, mapping):
    path = os.path.join(BASE, stem + ".json")
    if not os.path.exists(path):
        print(f"SKIP (no file): {stem}")
        return
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