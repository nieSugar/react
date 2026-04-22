# -*- coding: utf-8 -*-
"""Mass translation of leftover mixed EN/ZH <p>/<h3>/<h4>/<li>/<div> blocks
across the remaining 17 files, in one coordinated script.

All sparkle-wrapper / button-popover inner markup is copied byte-for-byte from
the original HTML so rendering is preserved; only the surrounding English prose
is rewritten into Chinese.
"""
from pathlib import Path


# Helper constants for the long sparkle-span stretches that appear several
# times. Each SPARKLE_* is the EXACT inner HTML (the 3-nested-span block
# including the SVG sparkle particles) lifted directly from the source file.

S_WHY_NOT_WORK = (
    '<span class="sparkle_wrapper__cL2jQ"><span class="sparkle_sparkle_wrapper__Izdcu" '
    'style="top:22%;left:4%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" '
    'height="12" viewbox="0 0 68 68" width="12"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" '
    'fill="var(--yellow)"></path></svg></span><span class="sparkle_sparkle_wrapper__Izdcu" '
    'style="top:55%;left:28%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" '
    'height="13" viewbox="0 0 68 68" width="13"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" '
    'fill="var(--yellow)"></path></svg></span><span class="sparkle_sparkle_wrapper__Izdcu" '
    'style="top:40%;left:63%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" '
    'height="19" viewbox="0 0 68 68" width="19"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" '
    'fill="var(--yellow)"></path></svg></span><strong class="sparkle_child_wrapper__bem0y">'
    "为什么不行？</strong></span>"
)


# === file -> list of (src, dst) ===
JOBS: dict[str, list[tuple[str, str]]] = {}


# -------- 002 Why React --------
JOBS["002 - Why React_ - ui.dev.html"] = [
    (
        '<p metastring="">Ironically, jQuery\'s biggest blessing was also its biggest curse. '
        'Turns out, relying on shared mutable state was a '
        '<a href="https://twitter.com/teozaurus/status/518071391959388160" metastring="">'
        '糟糕的主意</a>.</p>',
        '<p metastring="">讽刺的是，jQuery 最大的加分项同时也是它最大的祸根。事实证明，'
        '依赖共享的可变状态，是一个'
        '<a href="https://twitter.com/teozaurus/status/518071391959388160" metastring="">'
        '糟糕的主意</a>。</p>',
    ),
    (
        '<p metastring="">Not only that, but by embracing both JSX and React\'s component '
        'based API, all of a sudden what used to require imperative, operational like code, '
        'could be abstracted behind a declarative API. This not only enabled a better '
        'developer experience, but also a vibrant ecosystem of '
        '<a href="https://github.com/brillout/awesome-react-components" metastring="">'
        '第三方 component</a>.</p>',
        '<p metastring="">不仅如此，借助 JSX 和 React 基于 component 的 API，原本那些需要大量命令式、'
        '操作式代码才能完成的工作，突然之间就可以被封装到一套声明式 API 背后。这不仅带来了更好的开发体验，'
        '也催生出了一个繁荣的'
        '<a href="https://github.com/brillout/awesome-react-components" metastring="">'
        '第三方 component</a> 生态。</p>',
    ),
    (
        f'<p metastring="">{S_WHY_NOT_WORK} This thinking led to the creation of JSX - '
        "a wonderful lovechild of HTML and JavaScript that allows you to write HTML-ish "
        "looking syntax directly inside of JavaScript.</p>",
        f'<p metastring="">{S_WHY_NOT_WORK}正是这种想法催生了 JSX——HTML 和 JavaScript '
        '完美结合的产物，它让你可以直接在 JavaScript 里写出类似 HTML 的语法。</p>',
    ),
    (
        '<p metastring="">Believe it or not, when React first launched, it was... '
        '<a href="https://news.ycombinator.com/item?id=5789055" metastring="">反响并不好</a>.</p>',
        '<p metastring="">信不信由你，React 最初发布的时候……'
        '<a href="https://news.ycombinator.com/item?id=5789055" metastring="">反响并不好</a>。</p>',
    ),
]


# -------- 003 Imperative vs Declarative Programming --------
# sparkle 现实生活
S_REAL_LIFE = (
    '<span class="sparkle_wrapper__cL2jQ"><span class="sparkle_sparkle_wrapper__Izdcu" '
    'style="top:38%;left:22%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" '
    'height="12" viewbox="0 0 68 68" width="12"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" '
    'fill="var(--yellow)"></path></svg></span><span class="sparkle_sparkle_wrapper__Izdcu" '
    'style="top:87%;left:26%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" '
    'height="10" viewbox="0 0 68 68" width="10"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" '
    'fill="var(--yellow)"></path></svg></span>'
    '<strong class="sparkle_child_wrapper__bem0y">现实生活</strong></span>'
)

JOBS["003 - Imperative vs Declarative Programming - ui.dev.html"] = [
    (
        '<p metastring="">There\u2019s actually <em metastring="">some</em> good information '
        "hidden in here. Let\u2019s first see the merit in this definition by taking it out "
        f'of the context of programming and look at a {S_REAL_LIFE} example.</p>',
        '<p metastring="">其实这里面藏着<em metastring="">一些</em>有用的信息。'
        f'我们先跳出编程的语境，看一个 {S_REAL_LIFE} 的例子，来体会一下这个定义的价值。</p>',
    ),
    (
        '<p metastring="">You decide that you\u2019ve been spending too much time arguing '
        'about <em metastring="">JavaScript 疲劳</em>\u2122 and your husband deserves a nice '
        "date. You choose to go to Red Lobster since you\u2019ve been listening to a lot of "
        'Beyonc\u00e9 lately. You arrive at Red Lobster, approach the front desk and say\u2026</p>',
        '<p metastring="">你觉得自己在争论<em metastring="">JavaScript 疲劳</em>\u2122上花的时间太多了，'
        '你老公值得一次好好的约会。因为最近你一直在循环碧昂丝的歌，你决定去 Red Lobster。'
        '到了 Red Lobster，你走到前台说……</p>',
    ),
    (
        '<p metastring="">It\u2019s like trying to answer <em metastring="">到底是先有鸡还是'
        '先有蛋？</em> except everyone seems to think the chicken did, but you don\u2019t '
        "even like eggs, and you\u2019re confused. Combine this frustration with the "
        'bastardization of the actual word \u201cdeclarative\u201d to basically just mean '
        '<a href="https://twitter.com/jergason/status/699379381127368704" metastring="">'
        'good</a> and all of a sudden your imposter syndrome is tap dancing on your '
        "confidence, and you realize you don\u2019t even like programming that much.</p>",
        '<p metastring="">这就像在回答<em metastring="">到底是先有鸡还是先有蛋？</em>——'
        '只不过所有人好像都觉得是鸡先，可你偏偏又不爱吃蛋，整个人彻底懵了。再加上 '
        '\u201cdeclarative\u201d 这个词被滥用到基本只剩'
        '<a href="https://twitter.com/jergason/status/699379381127368704" metastring="">'
        'good</a>的意思，于是突然之间你的冒名顶替综合征就在你的自信心上跳起了踢踏舞，'
        '你甚至开始怀疑：自己是不是其实根本就没那么喜欢编程。</p>',
    ),
]


# -------- 004 Pure Functions --------
# sparkle blocks we need verbatim for 004
S_PURE_FN = (
    '<span class="sparkle_wrapper__cL2jQ"><span class="sparkle_sparkle_wrapper__Izdcu" '
    'style="top:15%;left:82%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" '
    'height="19" viewbox="0 0 68 68" width="19"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" '
    'fill="var(--yellow)"></path></svg></span><span class="sparkle_sparkle_wrapper__Izdcu" '
    'style="top:49%;left:73%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" '
    'height="18" viewbox="0 0 68 68" width="18"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" '
    'fill="var(--yellow)"></path></svg></span><span class="sparkle_sparkle_wrapper__Izdcu" '
    'style="top:18%;left:57%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" '
    'height="10" viewbox="0 0 68 68" width="10"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" '
    'fill="var(--yellow)"></path></svg></span>'
    '<strong class="sparkle_child_wrapper__bem0y">纯函数</strong></span>'
)
S_SIDE_EFFECT = (
    '<span class="sparkle_wrapper__cL2jQ"><span class="sparkle_sparkle_wrapper__Izdcu" '
    'style="top:95%;left:22%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" '
    'height="11" viewbox="0 0 68 68" width="11"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" '
    'fill="var(--yellow)"></path></svg></span><span class="sparkle_sparkle_wrapper__Izdcu" '
    'style="top:23%;left:20%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" '
    'height="16" viewbox="0 0 68 68" width="16"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" '
    'fill="var(--yellow)"></path></svg></span>'
    '<strong class="sparkle_child_wrapper__bem0y">副作用</strong></span>'
)
S_INCONSIST = (
    '<span class="sparkle_wrapper__cL2jQ"><span class="sparkle_sparkle_wrapper__Izdcu" '
    'style="top:20%;left:93%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" '
    'height="16" viewbox="0 0 68 68" width="16"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" '
    'fill="var(--yellow)"></path></svg></span><span class="sparkle_sparkle_wrapper__Izdcu" '
    'style="top:82%;left:82%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" '
    'height="15" viewbox="0 0 68 68" width="15"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" '
    'fill="var(--yellow)"></path></svg></span>'
    '<strong class="sparkle_child_wrapper__bem0y">不一致的输出。</strong></span>'
)
S_DEP_STATE = (
    '<span class="highlight-trigger font-medium underline decoration-brand-blue '
    '!cursor-help" style="display:inline-block;white-space:nowrap">依赖 state</span>'
)
S_RECEIVED = (
    '<span class="highlight-trigger font-medium underline decoration-brand-blue '
    '!cursor-help" style="display:inline-block;white-space:nowrap">它接收到的</span>'
)
S_STATE_HIGHLIGHT = (
    '<span class="highlight-trigger font-medium underline decoration-brand-blue '
    '!cursor-help" style="display:inline-block;white-space:nowrap">state</span>'
)
S_INPUT_VAL = (
    '<span class="highlight-trigger font-medium underline decoration-brand-blue '
    '!cursor-help" style="display:inline-block;white-space:nowrap">输入值</span>'
)
S_OBSERVABLE = (
    '<span class="highlight-trigger font-medium underline decoration-brand-blue '
    '!cursor-help" style="display:inline-block;white-space:nowrap">可观察的变化</span>'
)

JOBS["004 - Pure Functions - ui.dev.html"] = [
    (
        '<p metastring="">And worse, if something does go wrong, there are a variety of '
        'other things that <em metastring="">并不是</em> the user\'s profile that might get '
        'returned.</p>',
        '<p metastring="">更糟的是，一旦出点什么差错，有各种各样其他的东西可能被返回回来，'
        '而它们<em metastring="">并不是</em>用户的 profile。</p>',
    ),
    (
        f'<p metastring="">It both {S_DEP_STATE} other than the input value '
        f'{S_RECEIVED}, and it creates an observable change to the program itself '
        '(by mutating <code>todos</code>) \u2013 therefore, it has a side effect.</p>',
        f'<p metastring="">它既{S_DEP_STATE}——也就是{S_RECEIVED}输入值以外的 state——'
        '又对程序本身造成了可观察到的变化（它修改了 <code>todos</code>）。'
        '所以，它存在副作用。</p>',
    ),
    (
        '<p metastring="">To better figure this out, I think it would be beneficial to '
        'narrow our scope. <em metastring="">让应用更可预测</em> is too broad of a goal to '
        "be of any practical use. Instead, I think it's safe to assume that we can make our "
        "apps more predictable by making the individual pieces that make up our app more "
        "predictable \u2013 and what are those pieces? Usually they're functions.</p>",
        '<p metastring="">为了把这件事想清楚，我们最好先把范围缩小一点。'
        '<em metastring="">让应用更可预测</em>这个目标太泛，几乎没什么实操价值。相反，'
        '我们可以合理地假设：要让整个应用更可预测，可以通过让组成应用的每一个小单元都更可预测来实现——'
        '而这些小单元是什么？通常来说，就是函数。</p>',
    ),
    (
        '<p metastring="">Say we had an expensive <code>isPrime</code> function that '
        "calculated if a given number (<code>n</code>) was a "
        '<a href="https://en.wikipedia.org/wiki/Prime_number" metastring="">质数</a>.</p>',
        '<p metastring="">假设我们有一个开销比较大的 <code>isPrime</code> 函数，'
        '它用来判断给定的数字（<code>n</code>）是不是'
        '<a href="https://en.wikipedia.org/wiki/Prime_number" metastring="">质数</a>。</p>',
    ),
    (
        '<p metastring="">It doesn\'t create an observable change to the program, but it '
        f'does rely on {S_STATE_HIGHLIGHT} other than the {S_INPUT_VAL} it receives '
        "(state from an external API still counts). Therefore, this function has a side "
        'effect.</p>',
        f'<p metastring="">它并没有对程序本身造成可观察到的变化，但它依赖了 {S_STATE_HIGHLIGHT}，'
        f'而这些 state 并不是它接收到的 {S_INPUT_VAL}（来自外部 API 的 state 也算）。'
        '因此，这个函数存在副作用。</p>',
    ),
    (
        f'<p metastring="">If it\'s not already obvious, this idea isn\'t a new concept '
        "that we've invented. Instead, we've essentially re-created the functional "
        f'programming principle of {S_PURE_FN}. A function is considered pure if it '
        'contains no side effects and if, given the same input, it always returns the '
        'same output.</p>',
        f'<p metastring="">如果这还不够明显——这个想法并不是我们新发明的什么概念。事实上，'
        f'我们不过是重新得出了函数式编程里所说的 {S_PURE_FN} 原则：一个函数如果不包含任何副作用，'
        '并且对于相同的输入总是返回相同的输出，就被认为是纯函数。</p>',
    ),
    (
        '<p metastring="">You probably get the idea by now. We\'re not relying on state '
        f'other than the input value it receives, but we are creating an {S_OBSERVABLE} '
        'to the program itself. Therefore, another side effect.</p>',
        '<p metastring="">到这里你大概已经明白意思了。我们虽然没有依赖输入值以外的 state，'
        f'但我们对程序本身造成了{S_OBSERVABLE}。所以，这又是一个副作用。</p>',
    ),
    (
        f'<p metastring="">In my opinion, there are two big offenders \u2013 {S_SIDE_EFFECT} '
        f'and {S_INCONSIST}</p>',
        f'<p metastring="">在我看来，真正的元凶有两个——{S_SIDE_EFFECT}和{S_INCONSIST}</p>',
    ),
    (
        '<p metastring="">Earlier we defined a function as <em metastring="">一个接收输入'
        '（参数）并计算出输出（返回值）的过程。</em></p>',
        '<p metastring="">前面我们把函数定义为<em metastring="">一个接收输入（参数）并计算出'
        '输出（返回值）的过程。</em></p>',
    ),
]


# -------- 005 Components --------
JOBS["005 - Components - ui.dev.html"] = [
    (
        '<p metastring="">If you don\'t yet have that intuition, following the '
        '<a href="https://en.wikipedia.org/wiki/Single-responsibility_principle" '
        'metastring="">单一职责原则</a> is a decent barometer for when and where to create '
        'components. Namely, components (and functions) should do just one thing.</p>',
        '<p metastring="">如果你还没建立起那种直觉，那么遵循'
        '<a href="https://en.wikipedia.org/wiki/Single-responsibility_principle" '
        'metastring="">单一职责原则</a>是一条不错的参考线，可以帮你判断什么时候、在哪里该创建新的 '
        'component。简单来说就是：component（和函数）应该只做一件事。</p>',
    ),
    (
        '<p metastring="">One thing I love about React is that it feels like it\'s the '
        'answer to the question, <em metastring="">如果 HTML 是在今天才被发明的，它会是什么样子？'
        '</em></p>',
        '<p metastring="">我很喜欢 React 的一点是：它给人的感觉，像是在回答这样一个问题——'
        '<em metastring="">如果 HTML 是在今天才被发明的，它会是什么样子？</em></p>',
    ),
]


# -------- 009 Elements vs Components (duplicate of 008) --------
# Reuse the same translations we already applied to 008.
S_JS_SPARKLE_009 = (
    '<span class="sparkle_wrapper__cL2jQ"><span class="sparkle_sparkle_wrapper__Izdcu" '
    'style="top:20%;left:15%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" '
    'height="14" viewbox="0 0 68 68" width="14"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" '
    'fill="var(--yellow)"></path></svg></span><span class="sparkle_sparkle_wrapper__Izdcu" '
    'style="top:59%;left:71%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" '
    'height="16" viewbox="0 0 68 68" width="16"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" '
    'fill="var(--yellow)"></path></svg></span>'
    '<strong class="sparkle_child_wrapper__bem0y">就是 JavaScript\u2122</strong></span>'
)
JOBS["009 - Elements vs Components - ui.dev + styles.css.html"] = [
    (
        '<p metastring="">Here\'s a question for you. If this is called a '
        '<em metastring="">函数定义</em>,</p>',
        '<p metastring="">给你出个小问题。如果这被称为<em metastring="">函数定义</em>，</p>',
    ),
    (
        '<p metastring="">This definition gives us some interesting insight into how React '
        'works under the hood. An element <em metastring="">不是</em> a DOM node, instead '
        "it's an object representation of it.</p>",
        '<p metastring="">这个定义让我们对 React 底层的工作方式有了一些有趣的洞察。'
        '一个 element <em metastring="">并不是</em>一个 DOM 节点，'
        '而是这个 DOM 节点的<strong>对象表示</strong>。</p>',
    ),
    (
        f'<p metastring="">Notice there\'s no JSX \u2013\u00a0it\'s {S_JS_SPARKLE_009}.</p>',
        f'<p metastring="">注意这里完全没有 JSX\u2014\u2014它{S_JS_SPARKLE_009}。</p>',
    ),
    (
        '<p metastring="">What\u2019s interesting about learning React is that typically '
        "one of the first things you're taught are components and that "
        '<em metastring="">component 是 React 的基础构建块</em>. As we can see, '
        "that's not true \u2013\u00a0elements are the true building blocks of React. "
        'Components, by definition, are just functions that optionally accept input '
        'via props, and return a React element.</p>',
        '<p metastring="">学 React 时有一件很有意思的事：你最先被教的内容之一就是 component，'
        '而且会被告知 <em metastring="">component 是 React 的基础构建块</em>。但正如我们看到的，'
        '这并不对——element 才是 React 真正的基础构建块。按定义来说，component 不过是一些函数：'
        '它们可以通过 props 接收输入（可选），并返回一个 React element。</p>',
    ),
    (
        '<p metastring="">We call it <em metastring="">创建一个 element</em>, because '
        'after the JSX is compiled and <code>jsx</code> is invoked, that\u2019s what '
        'we get back \u2013\u00a0an element.</p>',
        '<p metastring="">我们把它叫做<em metastring="">创建一个 element</em>，'
        '因为在 JSX 被编译、<code>jsx</code> 被调用之后，我们拿回来的正是一个 element。</p>',
    ),
]


# -------- 010 Handling Events --------
JOBS["010 - Handling Events - ui.dev.html"] = [
    (
        '<p metastring="">Turns out, JavaScript is <em metastring="">really</em> good at '
        "creating and destroying functions. To the point where it's usually a non-issue. "
        'For the <em metastring="">极少数</em> edge cases where this isn\'t true, we have '
        'some options we\'ll learn about later in the course.</p>',
        '<p metastring="">事实证明，JavaScript 在创建和销毁函数这件事上<em metastring="">真的</em>'
        '非常在行，在行到这通常根本就不是个问题。对于那些<em metastring="">极少数</em>'
        '真的会成为问题的边界情况，我们也有一些办法可用——这些后面课程里会讲到。</p>',
    ),
]


# -------- 011 Preserving Values with useState --------
S_ONLY_JS = (
    '<span class="sparkle_wrapper__cL2jQ"><span class="sparkle_sparkle_wrapper__Izdcu" '
    'style="top:65%;left:2%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" '
    'height="12" viewbox="0 0 68 68" width="12"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" '
    'fill="var(--yellow)"></path></svg></span><span class="sparkle_sparkle_wrapper__Izdcu" '
    'style="top:21%;left:35%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" '
    'height="15" viewbox="0 0 68 68" width="15"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" '
    'fill="var(--yellow)"></path></svg></span>'
    '<strong class="sparkle_child_wrapper__bem0y">只是 JavaScript</strong></span>'
)
JOBS["011 - Preserving Values with useState - ui.dev.html"] = [
    (
        f'<p metastring="">After all, React is {S_ONLY_JS}, right? And the way you add '
        "state to a function is by creating a variable. Unfortunately, this won't work. "
        "Can you spot why?</p>",
        f'<p metastring="">毕竟，React {S_ONLY_JS}，对吧？而给一个函数加入"状态"的方式，'
        '就是去创建一个变量。可惜，这样写并不管用。你能看出是为什么吗？</p>',
    ),
]


# -------- 012 Using useState --------
def CH(label):
    return f'<span class="ch-section-link" data-active="false">{label}</span>'


JOBS["012 - Using useState - ui.dev.html"] = [
    (
        f'<p metastring="">Whenever the state you\'re updating lives in a '
        f'{CH("不同的位置")} from the {CH("事件处理函数")} that update that state, '
        f'you\'ll create an {CH("更新函数")} in the component where the state lives '
        f'and you\'ll {CH("调用那个函数")} from the component where the event '
        'handlers live.</p>',
        f'<p metastring="">每当你要更新的 state 和更新它的{CH("事件处理函数")}处于'
        f'{CH("不同的位置")}时，你就会在 state 所在的 component 里创建一个'
        f'{CH("更新函数")}，然后在事件处理函数所在的 component 里{CH("调用那个函数")}。</p>',
    ),
    (
        '<p metastring="">To <strong metastring="">更新一个元素</strong>, use '
        "JavaScript's <code>map</code> method to create a new array, updating the "
        'specific element where appropriate.</p>',
        '<p metastring="">要<strong metastring="">更新一个元素</strong>，使用 JavaScript '
        '的 <code>map</code> 方法创建一个新数组，并在合适的位置更新目标元素。</p>',
    ),
    (
        f'<p metastring="">To do that, we\'ll add some {CH("state")} to the component to '
        f'keep track of the status of the todo item, add {CH("一个事件处理函数")} to update '
        f'that state, then hook the event handler up to our {CH("input")} via its '
        f'{CH("onChange")} prop.</p>',
        f'<p metastring="">为此，我们会给 component 加一些 {CH("state")} 来跟踪 todo 项的状态，'
        f'再加{CH("一个事件处理函数")}来更新这段 state，然后通过 {CH("input")} 的 '
        f'{CH("onChange")} prop 把事件处理函数挂上去。</p>',
    ),
    (
        '<p metastring="">To <strong metastring="">添加一个元素</strong> to an array, use '
        "JavaScript's spread operator (<code>...</code>) to spread all the existing "
        'elements onto a new array with the new element.</p>',
        '<p metastring="">要往数组里<strong metastring="">添加一个元素</strong>，使用 '
        'JavaScript 的展开运算符（<code>...</code>）把所有已有元素连同新元素一起展开到一个'
        '新数组里。</p>',
    ),
    (
        '<p metastring="">To <strong metastring="">删除一个元素</strong> from an array, use '
        "JavaScript's <code>filter</code> method to create a new array, filtering out the "
        'element that should be removed.</p>',
        '<p metastring="">要从数组里<strong metastring="">删除一个元素</strong>，使用 '
        'JavaScript 的 <code>filter</code> 方法创建一个新数组，并把要删除的那个元素过滤掉。</p>',
    ),
    (
        f'<p metastring="">At this point our app is progressing nicely, but you may '
        f'notice something a little strange. Currently, we have {CH("多段 state")} '
        "representing one todo item. That works, but it won't scale well when we add "
        'more todo items.</p>',
        f'<p metastring="">到这一步我们的应用已经做得挺不错了，但你可能注意到一件有点奇怪的事：'
        f'目前我们用{CH("多段 state")}来表示同一个 todo 项。现在能跑起来，但一旦 todo 项变多，'
        '这样组织就扩展不开了。</p>',
    ),
    (
        f'<p metastring="">In our case, the state of our app {CH("lives")} inside of '
        'the parent <code>TodoList</code> component. Therefore, any time we want to '
        f'update that state, we need to do so {CH("它所在的位置")} \u2013 in '
        '<code>TodoList</code>.</p>',
        f'<p metastring="">在我们这个例子里，应用的 state 就{CH("lives")}在父 component '
        f'<code>TodoList</code> 里。所以每次要更新这段 state 时，我们都得在'
        f'{CH("它所在的位置")}——也就是 <code>TodoList</code> 里——去更新。</p>',
    ),
    (
        '<p metastring="">You can break the process of updating arrays down into three '
        'use cases: <strong metastring="">添加元素</strong>, <strong metastring="">删除'
        '元素</strong>, and <strong metastring="">更新元素</strong>.</p>',
        '<p metastring="">更新数组的过程可以拆成三种场景：<strong metastring="">添加元素'
        '</strong>、<strong metastring="">删除元素</strong>、<strong metastring="">'
        '更新元素</strong>。</p>',
    ),
    (
        f'<p metastring="">At this point whenever the user clicks on our {CH("Edit")} '
        f'button, the {CH("todo 项")} will be replaced with an {CH("input")} '
        'element.</p>',
        f'<p metastring="">到这一步，每当用户点击我们的 {CH("Edit")} 按钮，对应的'
        f'{CH("todo 项")}就会被一个 {CH("input")} 元素替换掉。</p>',
    ),
]


# -------- 013 Why React Renders --------
def FB(color, text):
    return f'<span class="font-black tracking-wider" style="color:var(--{color})">{text}</span>'


S_HL13_3rd = (
    '<span class="highlight-trigger font-medium underline decoration-brand-blue '
    '!cursor-help" style="display:inline-block;white-space:nowrap">第三次调用</span>'
)
S_HL13_2nd = (
    '<span class="highlight-trigger font-medium underline decoration-brand-blue '
    '!cursor-help" style="display:inline-block;white-space:nowrap">第二次调用</span>'
)
BUTTON13_WHEN = (
    '<button aria-controls="radix-:rik:" aria-expanded="false" '
    'aria-haspopup="dialog" class="Popover_children__8p5Di" data-state="closed" '
    'type="button"><span>被创建时</span> <svg class="fill-brand-purple '
    'dark:fill-brand-yellow w-2 h-2 b-2 mx-0.5 mb-4" enable-background="new 0 0 455 '
    '455" version="1.1" viewbox="0 0 455 455" x="0" xml:space="preserve" '
    'xmlns="http://www.w3.org/2000/svg" y="0"><path d="M347.49 227L454.5 165.212 '
    '394.508 61.288 287.5 123.077 287.5 0 167.5 0 167.5 123.077 60.492 61.288 '
    '0.499 165.212 107.51 227 0.5 288.788 60.492 392.712 167.5 330.923 167.5 '
    '455 287.5 455 287.5 330.923 394.508 392.712 454.501 288.788z"></path></svg></button>'
)
JOBS["013 - Why React Renders - ui.dev.html"] = [
    (
        f'<p metastring="">Now whenever our <code>button</code> is clicked, our '
        f'<code>handleClick</code> {FB("pink","事件处理函数")} will run. The '
        f'{FB("blue","state")} (<code>index</code>) inside of <code>handleClick</code> '
        'will be the same as the state in the most recent snapshot. From there, React '
        "sees there's a call to <code>setIndex</code> and that the value passed to it "
        'is different than the state in the snapshot \u2013 triggering a re-render.</p>',
        f'<p metastring="">现在每当我们的 <code>button</code> 被点击时，我们的 '
        f'<code>handleClick</code> {FB("pink","事件处理函数")}就会执行。'
        f'<code>handleClick</code> 内部的 {FB("blue","state")}（<code>index</code>）'
        '会和最近一次快照里的 state 一致。接下来 React 看到里面调用了 <code>setIndex</code>，'
        '而且传进去的值和快照中的 state 不同——于是触发一次重新渲染。</p>',
    ),
    (
        f'<p metastring="">Notice that we don\'t use <code>4</code> in the '
        f'{S_HL13_3rd} even though that\'s what was returned in the {S_HL13_2nd}. '
        "That's because we're just telling React to forget everything it knew and use "
        '<code>7</code> as the new state.</p>',
        f'<p metastring="">注意，{S_HL13_3rd}里我们并没有用 <code>4</code>，'
        f'尽管它正是{S_HL13_2nd}返回的值。原因是：我们只是在告诉 React：忘掉它之前知道的一切，'
        '把 <code>7</code> 当作新的 state 就行。</p>',
    ),
    (
        f'<p metastring="">When an {FB("pink","事件处理函数")} is invoked, that event '
        f'handler has access to the {FB("orange","props")} and {FB("blue","state")} '
        'as they were in the moment in time when the snapshot '
        f'{BUTTON13_WHEN}.</p>',
        f'<p metastring="">当一个{FB("pink","事件处理函数")}被调用时，它能拿到的 '
        f'{FB("orange","props")} 和 {FB("blue","state")}，都是快照{BUTTON13_WHEN}那一刻的值。</p>',
    ),
]


# -------- 014 Reality Check --------
JOBS["014 - Reality Check - ui.dev.html"] = [
    (
        '<p metastring="">For React to be of any practical use and not just a theoretical '
        'tool we learn about in Computer Science programs, it needs to handle these '
        '<em metastring="">外部世界</em> use cases \u2013 and do so in a way that doesn\'t '
        'completely destroy the simplicity of the mental model.</p>',
        '<p metastring="">要让 React 具备真正的实用价值，而不只是计算机科学课堂上的一个'
        '理论工具，它就必须能处理这些<em metastring="">外部世界</em>的使用场景——'
        '而且还得用一种不会把整套心智模型的简洁性彻底毁掉的方式来实现。</p>',
    ),
]


# -------- 015 Managing Effects --------
BTN15_RULE1 = (
    '<button aria-controls="radix-:rkd:" aria-expanded="false" aria-haspopup="dialog" '
    'class="Popover_children__8p5Di" data-state="closed" type="button"><span>规则 #1'
    '</span> <svg class="fill-brand-purple dark:fill-brand-yellow w-2 h-2 b-2 mx-0.5 '
    'mb-4" enable-background="new 0 0 455 455" version="1.1" viewbox="0 0 455 455" '
    'x="0" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" y="0"><path '
    'd="M347.49 227L454.5 165.212 394.508 61.288 287.5 123.077 287.5 0 167.5 0 '
    '167.5 123.077 60.492 61.288 0.499 165.212 107.51 227 0.5 288.788 60.492 '
    '392.712 167.5 330.923 167.5 455 287.5 455 287.5 330.923 394.508 392.712 '
    '454.501 288.788z"></path></svg></button>'
)
BTN15_NATURE = (
    '<button aria-controls="radix-:rkf:" aria-expanded="false" aria-haspopup="dialog" '
    'class="Popover_children__8p5Di" data-state="closed" type="button"><span>自然会认为'
    '</span> <svg class="fill-brand-purple dark:fill-brand-yellow w-2 h-2 b-2 mx-0.5 '
    'mb-4" enable-background="new 0 0 455 455" version="1.1" viewbox="0 0 455 455" '
    'x="0" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" y="0"><path '
    'd="M347.49 227L454.5 165.212 394.508 61.288 287.5 123.077 287.5 0 167.5 0 '
    '167.5 123.077 60.492 61.288 0.499 165.212 107.51 227 0.5 288.788 60.492 '
    '392.712 167.5 330.923 167.5 455 287.5 455 287.5 330.923 394.508 392.712 '
    '454.501 288.788z"></path></svg></button>'
)
JOBS["015 - Managing Effects - ui.dev.html"] = [
    (
        f'<p metastring="">从概念上讲，这是有意义的，特别是当与 {BTN15_RULE1}. '
        'React can maximize the speed and predictability of rendering by enforcing '
        'rules around when side effects can run \u2013 either when an event occurs '
        '(Rule #1) or after the component has rendered (Rule #2).</p>',
        f'<p metastring="">从概念上讲，这是说得通的，尤其是和 {BTN15_RULE1}结合起来看。'
        'React 通过规定副作用可以何时运行来最大化渲染的速度与可预测性——要么在事件发生时（规则 #1），'
        '要么在 component 渲染之后（规则 #2）。</p>',
    ),
    (
        f'<p metastring="">This is how everyone {BTN15_NATURE} 关于第二个参数的说法，'
        '但这是错误的。与其告诉React <strong metastring="">when</strong> 要调用该effect，'
        '你给React <strong metastring="">所有依赖项</strong> 那个effect需要运行——像这样。</p>',
        f'<p metastring="">这就是人人{BTN15_NATURE}关于第二个参数的理解，但这是错误的。'
        '与其告诉 React <strong metastring="">什么时候</strong>要调用这个 effect，'
        '不如把这个 effect 运行时需要的<strong metastring="">所有依赖项</strong>告诉它——'
        '就像这样。</p>',
    ),
]


# -------- 017 Preserving Values with useRef --------
S_VERY_REACT = (
    '<span class="sparkle_wrapper__cL2jQ"><span class="sparkle_sparkle_wrapper__Izdcu" '
    'style="top:26%;left:97%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" '
    'height="15" viewbox="0 0 68 68" width="15"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" '
    'fill="var(--yellow)"></path></svg></span><span class="sparkle_sparkle_wrapper__Izdcu" '
    'style="top:1%;left:10%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" '
    'height="19" viewbox="0 0 68 68" width="19"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" '
    'fill="var(--yellow)"></path></svg></span><span class="sparkle_sparkle_wrapper__Izdcu" '
    'style="top:7%;left:26%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" '
    'height="12" viewbox="0 0 68 68" width="12"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" '
    'fill="var(--yellow)"></path></svg></span><span class="sparkle_sparkle_wrapper__Izdcu" '
    'style="top:18%;left:1%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" '
    'height="14" viewbox="0 0 68 68" width="14"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" '
    'fill="var(--yellow)"></path></svg></span>'
    '<strong class="sparkle_child_wrapper__bem0y">很 React 的方式</strong></span>'
)
BTN17_HINT = (
    '<button aria-controls="radix-:rnr:" aria-expanded="false" aria-haspopup="dialog" '
    'class="Popover_children__8p5Di" data-state="closed" type="button"><span>给你个提示'
    '</span> <svg class="fill-brand-purple dark:fill-brand-yellow w-2 h-2 b-2 mx-0.5 '
    'mb-4" enable-background="new 0 0 455 455" version="1.1" viewbox="0 0 455 455" '
    'x="0" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" y="0"><path '
    'd="M347.49 227L454.5 165.212 394.508 61.288 287.5 123.077 287.5 0 167.5 0 '
    '167.5 123.077 60.492 61.288 0.499 165.212 107.51 227 0.5 288.788 60.492 '
    '392.712 167.5 330.923 167.5 455 287.5 455 287.5 330.923 394.508 392.712 '
    '454.501 288.788z"></path></svg></button>'
)
JOBS["017 - Preserving Values with useRef - ui.dev.html"] = [
    (
        f'<p metastring="">This actually works, but it\'s brittle, unnecessarily '
        f'dependant on string matching, and not very {S_VERY_REACT}. In fact, it kind '
        "of feels like we're giving React the \U0001F595 since we're bypassing it "
        'directly and going straight to the DOM.</p>',
        f'<p metastring="">这样确实能跑，但它很脆弱，不必要地依赖字符串匹配，也不是'
        f'{S_VERY_REACT}。实际上感觉有点像是在对 React 比 \U0001F595，因为我们绕过了它，'
        '直接去动 DOM。</p>',
    ),
    (
        '<p metastring="">Because CSS is doing a lot of the heavy lifting, we don\'t '
        'have a <em metastring="">ton</em> of options for how to solve this. One '
        'approach that I think is <em metastring="">差不多就行\u2122</em> is to disable '
        'the toggle switch for a short period of time after it\'s been clicked \u2013 '
        'say 1300ms.</p>',
        '<p metastring="">因为大部分重活都交给了 CSS，我们在解决这个问题时并没有'
        '<em metastring="">太多</em>选择。我觉得一个<em metastring="">差不多就行\u2122</em>'
        '的做法是：点击之后，把切换开关临时禁用一小段时间——比如 1300ms。</p>',
    ),
    (
        '<p metastring="">Now I know it seems weird, isn\'t the whole point of React '
        'to create an abstraction over the view (DOM) so you <strong metastring="">'
        '不要</strong> have to directly interact with it? Yes, mostly. But again, '
        "they're called escape hatches for a reason.</p>",
        '<p metastring="">我知道这看起来有点奇怪——React 的整个意义不就是在视图（DOM）'
        '之上建一层抽象，让你<strong metastring="">不要</strong>直接去动它吗？大体上是的，'
        '但反过来说，它们之所以被叫做"逃生舱"，总是有它的道理。</p>',
    ),
    (
        '<p metastring="">Now, there is one thing that\'s been eating me up since '
        'earlier. It was this line when we were discussing how to disable our toggle '
        'button until after all our CSS animations had finished - "One approach that '
        'I think is <em metastring="">差不多就行\u2122</em> is to disable the toggle '
        'switch for a short period of time after it\'s been clicked \u2013 say 1300ms.'
        '"</p>',
        '<p metastring="">还有件事，从前面开始就一直在我心里挠痒痒。那就是在讨论"等 CSS '
        '动画全部结束后再启用切换开关"时我写下的一句话——"我觉得一个<em metastring="">'
        '差不多就行\u2122</em>的做法是：点击之后，把切换开关临时禁用一小段时间——比如 1300ms。"</p>',
    ),
    (
        f'<p metastring="">Did you spot the bug? If not, {BTN17_HINT}.</p>',
        f'<p metastring="">你发现 bug 了吗？如果没有，{BTN17_HINT}。</p>',
    ),
]


# -------- 018 Teleportation with Context --------
JOBS["018 - Teleportation with Context - ui.dev.html"] = [
    (
        '<h3 metastring="">One more thing, again...</h3>',
        '<h3 metastring="">再多说一件事……</h3>',
    ),
    (
        '<p metastring="">And adapted to our example.</p>',
        '<p metastring="">把它套到我们的例子上。</p>',
    ),
]


# -------- 019 Complex State with useReducer --------
S_REDUCER_PATTERN = (
    '<span class="sparkle_wrapper__cL2jQ"><span class="sparkle_sparkle_wrapper__Izdcu" '
    'style="top:51%;left:11%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" '
    'height="13" viewbox="0 0 68 68" width="13"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" '
    'fill="var(--yellow)"></path></svg></span><span class="sparkle_sparkle_wrapper__Izdcu" '
    'style="top:26%;left:38%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" '
    'height="11" viewbox="0 0 68 68" width="11"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" '
    'fill="var(--yellow)"></path></svg></span><span class="sparkle_sparkle_wrapper__Izdcu" '
    'style="top:79%;left:42%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" '
    'height="10" viewbox="0 0 68 68" width="10"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" '
    'fill="var(--yellow)"></path></svg></span>'
    '<strong class="sparkle_child_wrapper__bem0y">reducer 模式</strong></span>'
)
JOBS["019 - Complex State with useReducer - ui.dev.html"] = [
    (
        f"<p metastring=\"\">While not always bad, it's best to avoid impure functions "
        'when you can. To accomplish the same functionality with a <span class="'
        'font-black tracking-wider" style="color:currentcolor">pure</span> function, '
        f"we can use what's called the {S_REDUCER_PATTERN}.</p>",
        f'<p metastring="">虽然不纯的函数也不总是坏事，但能避免就尽量避免。要用一个'
        f'<span class="font-black tracking-wider" style="color:currentcolor">纯</span>'
        f'函数来实现同样的功能，我们可以借助所谓的 {S_REDUCER_PATTERN}。</p>',
    ),
]


# -------- 020 Referential Equality and Why It Matters --------
JOBS["020 - Referential Equality and Why It Matters - ui.dev.html"] = [
    (
        '<p metastring="">Now, what about reference values?</p>',
        '<p metastring="">那引用值（reference value）呢？</p>',
    ),
    (
        '<p metastring="">Here\'s how it works.</p>',
        '<p metastring="">下面我们来看看它是怎么运作的。</p>',
    ),
    (
        '<p metastring="">Let\'s answer that with an example.</p>',
        '<p metastring="">我们用一个例子来回答这个问题。</p>',
    ),
    (
        '<h4 class="text-2xl mt-0" style="color:var(--brand-yellow)"><strong>Turtles '
        'all the way down</strong></h4>',
        '<h4 class="text-2xl mt-0" style="color:var(--brand-yellow)"><strong>'
        '一层套一层，一直套下去</strong></h4>',
    ),
]


# -------- 021 Managing Advanced Effects --------
BTN21_REASON = (
    '<button aria-controls="radix-:rsu:" aria-expanded="false" aria-haspopup="dialog" '
    'class="Popover_children__8p5Di" data-state="closed" type="button"><span>某种原因'
    '</span> <svg class="fill-brand-purple dark:fill-brand-yellow w-2 h-2 b-2 mx-0.5 '
    'mb-4" enable-background="new 0 0 455 455" version="1.1" viewbox="0 0 455 455" '
    'x="0" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" y="0"><path '
    'd="M347.49 227L454.5 165.212 394.508 61.288 287.5 123.077 287.5 0 167.5 0 '
    '167.5 123.077 60.492 61.288 0.499 165.212 107.51 227 0.5 288.788 60.492 '
    '392.712 167.5 330.923 167.5 455 287.5 455 287.5 330.923 394.508 392.712 '
    '454.501 288.788z"></path></svg></button>'
)
JOBS["021 - Managing Advanced Effects - ui.dev.html"] = [
    (
        '<p metastring="">This works, but there\'s a <em metastring="">有个小问题</em>.</p>',
        '<p metastring="">这样能跑，但<em metastring="">有个小问题</em>。</p>',
    ),
    (
        '<p metastring="">If you take a peek into the dark crevices of the React API, '
        'you\'ll find two of these specialized <del metastring="">hooks</del> tools '
        '\u2013 each designed to solve advanced use cases around managing effects in '
        'React.</p>',
        '<p metastring="">如果你往 React API 的幽暗角落里看一眼，你会发现两个这样的专用 '
        '<del metastring="">hook</del> 工具——每一个都是为了解决 React 中管理 effect 的某种'
        '高级场景而设计的。</p>',
    ),
    (
        f'<p metastring="">The solution is to either move <code>subscribe</code> '
        'outside of the component as we did earlier so it never changes, or, if you '
        f'need to keep it inside of the component for {BTN21_REASON}, you can use '
        '<code>useCallback</code> so its reference is stable.</p>',
        f'<p metastring="">解决办法有两种：要么像前面那样把 <code>subscribe</code> '
        f'移到 component 外面，让它永远不变；要么如果出于{BTN21_REASON}你必须把它留在 '
        'component 内部，那就用 <code>useCallback</code> 来让它的引用保持稳定。</p>',
    ),
]


# -------- 022 Abstracting Reactive Values with useEffectEvent --------
BTN22_REACTIVE = (
    '<button aria-controls="radix-:rtn:" aria-expanded="false" aria-haspopup="dialog" '
    'class="Popover_children__8p5Di" data-state="closed" type="button"><span>响应式值'
    '</span> <svg class="fill-brand-purple dark:fill-brand-yellow w-2 h-2 b-2 mx-0.5 '
    'mb-4" enable-background="new 0 0 455 455" version="1.1" viewbox="0 0 455 455" '
    'x="0" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" y="0"><path '
    'd="M347.49 227L454.5 165.212 394.508 61.288 287.5 123.077 287.5 0 167.5 0 '
    '167.5 123.077 60.492 61.288 0.499 165.212 107.51 227 0.5 288.788 60.492 '
    '392.712 167.5 330.923 167.5 455 287.5 455 287.5 330.923 394.508 392.712 '
    '454.501 288.788z"></path></svg></button>'
)
BTN22_ALPHA = (
    '<button aria-controls="radix-:rtm:" aria-expanded="false" aria-haspopup="dialog" '
    'class="Popover_children__8p5Di" data-state="closed" type="button"><span>在 alpha '
    '中稳定</span> <svg class="fill-brand-purple dark:fill-brand-yellow w-2 h-2 b-2 mx-0.5 '
    'mb-4" enable-background="new 0 0 455 455" version="1.1" viewbox="0 0 455 455" '
    'x="0" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" y="0"><path '
    'd="M347.49 227L454.5 165.212 394.508 61.288 287.5 123.077 287.5 0 167.5 0 '
    '167.5 123.077 60.492 61.288 0.499 165.212 107.51 227 0.5 288.788 60.492 '
    '392.712 167.5 330.923 167.5 455 287.5 455 287.5 330.923 394.508 392.712 '
    '454.501 288.788z"></path></svg></button>'
)
JOBS["022 - Abstracting Reactive Values with useEffectEvent - ui.dev.html"] = [
    (
        f'<p metastring="">All we\'re wanting to do is pass along some <code>state</code> '
        f'information for our analytics. However, because <code>state</code> is a '
        f"{BTN22_REACTIVE}, we need to include it in the dependency array \u2013 if we "
        "don't, React will complain.</p>",
        f'<p metastring="">我们想做的事情其实很简单：把一些 <code>state</code> 信息传给'
        f'我们的统计。但因为 <code>state</code> 是一个{BTN22_REACTIVE}，'
        '我们必须把它放进依赖数组里——否则 React 会报错。</p>',
    ),
    (
        f"<p metastring=\"\">That said, it's been {BTN22_ALPHA} for a while, it's "
        'incredibly helpful, and we rely heavily on it throughout the remainder of this '
        'course.</p>',
        f'<p metastring="">话虽如此，它其实已经{BTN22_ALPHA}一段时间了，而且非常有用，'
        '本课程余下的内容也会大量依赖它。</p>',
    ),
]


# -------- 024 Rebuilding useHooks --------
JOBS["024 - Rebuilding useHooks - ui.dev.html"] = [
    (
        "<p metastring=\"\">My running theory is it's because it's the most generic, "
        'widely applicable advice that is certain to be true. You do get better by '
        '<em metastring="">\u201c动手去做\u201d</em>. The problem is the most widely '
        'applicable approach is almost never the most efficient one.</p>',
        '<p metastring="">我的猜测是：因为它是最通用、适用面最广、也一定不会错的那种建议。'
        '你确实会因为<em metastring="">\u201c动手去做\u201d</em>而变得更好，问题在于：'
        '最通用的做法，几乎从来都不是最高效的做法。</p>',
    ),
    (
        '<p metastring="">I know this seems controversial, but you would never tell a '
        'professional basketball player to <em metastring="">\u201c去玩就完了\u201d</em> '
        '\u2013 so why is "just build things" such a common trope when it comes to '
        'learning technical topics?</p>',
        '<p metastring="">我知道这听起来挺反直觉的，但你绝不会去告诉一个职业篮球运动员：'
        '<em metastring="">\u201c去玩就完了\u201d</em>——那为什么一谈到学习技术话题时，'
        '"just build things"就成了一句几乎所有人都在说的套话呢？</p>',
    ),
    (
        '<p metastring="">This is the <em metastring="">\u201c你不可能靠读书学会骑自行车'
        '\u201d</em> approach to developer education. That\'s fantastic advice, if '
        'you\'re a 4 year old. In reality, professional cyclists <em metastring="">do'
        '</em> learn all about riding, both the physical act and how to most efficiently '
        'train, from reading.</p>',
        '<p metastring="">这就是开发者教育里的<em metastring="">\u201c你不可能靠读书'
        '学会骑自行车\u201d</em>派。如果你是个 4 岁小孩，这建议还挺棒的。但现实是：'
        '职业自行车手<em metastring="">其实</em>就是通过阅读来学习与骑行相关的一切——'
        '既包括怎么骑，也包括怎么最高效地训练。</p>',
    ),
]


def main() -> None:
    grand_total = 0
    had_miss = False
    for fname, pairs in JOBS.items():
        p = Path(fname)
        text = p.read_text(encoding="utf-8")
        applied = 0
        missing = []
        for src, dst in pairs:
            cnt = text.count(src)
            if cnt == 0:
                missing.append(src[:120])
                continue
            text = text.replace(src, dst)
            applied += cnt
        if missing:
            had_miss = True
            print(f"[{fname}] MISS {len(missing)}/{len(pairs)}:")
            for m in missing:
                print(f"  - {m}")
        if applied:
            p.write_text(text, encoding="utf-8")
            print(f"[{fname}] applied {applied} (from {len(pairs)} patterns).")
            grand_total += applied
    print(f"\nGRAND TOTAL: {grand_total} replacements.")
    if had_miss:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
