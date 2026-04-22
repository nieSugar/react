"""Batch E: 020 Referential Equality and Why It Matters (62 paragraphs)."""
import os, json, sys, re, unicodedata
sys.stdout.reconfigure(encoding="utf-8")

BASE = r"D:\Personal\Downloads\react\.translate\inline"

def norm(s):
    s = unicodedata.normalize("NFKC", s)
    s = s.replace("\u00a0", " ").replace("\u2013", "-").replace("\u2014", "-")
    s = s.replace("\u2018", "'").replace("\u2019", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = re.sub(r'aria-controls="radix-:[^"]+"', 'aria-controls=""', s)
    s = re.sub(r"\s+", " ", s).strip()
    return s

SVG_L = '<button aria-controls="" aria-expanded="false" aria-haspopup="dialog" class="Popover_children__8p5Di" data-state="closed" type="button"><span>'
SVG_R = '</span> <svg class="fill-brand-purple dark:fill-brand-yellow w-2 h-2 b-2 mx-0.5 mb-4" enable-background="new 0 0 455 455" version="1.1" viewbox="0 0 455 455" x="0" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" y="0"><path d="M347.49 227L454.5 165.212 394.508 61.288 287.5 123.077 287.5 0 167.5 0 167.5 123.077 60.492 61.288 0.499 165.212 107.51 227 0.5 288.788 60.492 392.712 167.5 330.923 167.5 455 287.5 455 287.5 330.923 394.508 392.712 454.501 288.788z"></path></svg></button>'

# The three sparkle wrappers in the 020 file (with specific positions).
SPARKLE_REF1 = '<span class="sparkle_wrapper__cL2jQ"><span class="sparkle_sparkle_wrapper__Izdcu" style="top:80%;left:46%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" height="10" viewbox="0 0 68 68" width="10"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" fill="var(--yellow)"></path></svg></span><span class="sparkle_sparkle_wrapper__Izdcu" style="top:85%;left:11%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" height="15" viewbox="0 0 68 68" width="15"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" fill="var(--yellow)"></path></svg></span><strong class="sparkle_child_wrapper__bem0y">'
SPARKLE_REF2 = '<span class="sparkle_wrapper__cL2jQ"><span class="sparkle_sparkle_wrapper__Izdcu" style="top:49%;left:44%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" height="15" viewbox="0 0 68 68" width="15"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" fill="var(--yellow)"></path></svg></span><span class="sparkle_sparkle_wrapper__Izdcu" style="top:3%;left:32%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" height="14" viewbox="0 0 68 68" width="14"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" fill="var(--yellow)"></path></svg></span><span class="sparkle_sparkle_wrapper__Izdcu" style="top:46%;left:7%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" height="19" viewbox="0 0 68 68" width="19"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" fill="var(--yellow)"></path></svg></span><strong class="sparkle_child_wrapper__bem0y">'
SPARKLE_REF3 = '<span class="sparkle_wrapper__cL2jQ"><span class="sparkle_sparkle_wrapper__Izdcu" style="top:51%;left:49%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" height="18" viewbox="0 0 68 68" width="18"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" fill="var(--yellow)"></path></svg></span><span class="sparkle_sparkle_wrapper__Izdcu" style="top:88%;left:36%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" height="10" viewbox="0 0 68 68" width="10"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" fill="var(--yellow)"></path></svg></span><strong class="sparkle_child_wrapper__bem0y">'
SPARKLE_REF4 = '<span class="sparkle_wrapper__cL2jQ"><span class="sparkle_sparkle_wrapper__Izdcu" style="top:83%;left:40%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" height="14" viewbox="0 0 68 68" width="14"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" fill="var(--yellow)"></path></svg></span><span class="sparkle_sparkle_wrapper__Izdcu" style="top:12%;left:19%"><svg class="sparkle_sparkle_svg__WdZ3Y" fill="none" height="13" viewbox="0 0 68 68" width="13"><path d="M 48 5 L 51 27 L 74 30 L 51 33 L 48 56 L 44 33 L 23 30 L 44 27 Z" fill="var(--yellow)"></path></svg></span><strong class="sparkle_child_wrapper__bem0y">'

TRANS = {
"020 - Referential Equality and Why It Matters - ui.dev": {
    f'It may seem strange, but one of the most fundamental steps on the road to mastering React is getting comfortable with the concept of {SPARKLE_REF1}referential equality</strong></span> in JavaScript.':
        f'听起来有点怪，但在掌握 React 的道路上，最基础的一步就是弄清 JavaScript 里的 {SPARKLE_REF1}引用相等（referential equality）</strong></span>这一概念。',
    'I know. If I was on a game show and had to come up with the most overcomplicated sentence I could, it\'d probably contain the words <em metastring="">referential equality in JavaScript</em> – but I promise it\'s not as bad as it sounds.':
        '我懂。如果让我在综艺节目上凑出一句最拗口的话，那里面十有八九会有“<em metastring="">JavaScript 里的引用相等</em>”这几个字 —— 但我保证，它没听起来那么可怕。',
    'Whenever you create a variable in JavaScript, that variable can store one of two types of data, a <strong metastring="">primitive</strong> value or a <strong metastring="">reference</strong> value. If the value is a <code>number</code>, <code>string</code>, <code>boolean</code>, <code>undefined</code>, <code>null</code>, or <code>symbol</code>, it\'s a <strong metastring="">primitive</strong> value. If it\'s anything else, it\'s a <strong metastring="">reference</strong> value.':
        '在 JavaScript 里创建变量时，它存储的值无非两种：<strong metastring="">原始</strong>值（primitive）或<strong metastring="">引用</strong>值（reference）。如果值是 <code>number</code>、<code>string</code>、<code>boolean</code>、<code>undefined</code>、<code>null</code> 或 <code>symbol</code>，就是<strong metastring="">原始</strong>值；除此之外都是<strong metastring="">引用</strong>值。',
    'If you looked at the in-memory value of a primitive, you\'d see the actual value itself (<code>28</code>, <code>\'Tyler\'</code>, <code>false</code>, etc.) If you looked at the in-memory value of a reference type, you\'d see a <em metastring="">reference</em> to a spot in memory. Or more specifically, you\'d see a memory address which pointed to a spot in memory where the value was stored.':
        '如果你看原始值在内存里的样子，看到的就是值本身（<code>28</code>、<code>\'Tyler\'</code>、<code>false</code> 等等）。如果你看引用类型在内存里的样子，看到的则是一个指向内存某处的<em metastring="">引用</em> —— 更具体地说，是一个指向存放实际值的那块内存地址。',
    'Though a little strange, this example demonstrates an important aspect of primitive values – that the in-memory value of a primitive is the value itself. Therefore, when we assign one primitive value to another, like we\'re doing with <code>displayName</code>, what we\'re really doing is copying the value from one spot in memory to another.':
        '虽然有点奇怪，但这个例子说明了原始值的一个重要特性：原始值在内存里的“值”就是它自己。所以当我们把一个原始值赋给另一个变量（就像我们对 <code>displayName</code> 做的那样），实际上是把值从内存的一个位置拷贝到了另一个位置。',
    'So even though <code>lastName</code> changes, and <code>displayName</code> uses <code>lastName</code>, <code>displayName</code> itself doesn\'t change because it <em metastring="">copied</em> the value of <code>lastName</code> when it was created.':
        '所以即便 <code>lastName</code> 变了，而 <code>displayName</code> 是基于 <code>lastName</code> 产生的，<code>displayName</code> 自己也不会变化 —— 因为它在创建时已经<em metastring="">拷贝</em>了 <code>lastName</code> 的值。',
    'Notice the difference? When we create a new variable and assign it to a reference value (like we\'re doing with <code>snoop</code>), what we\'re really doing is copying the <em metastring="">reference</em> to the spot in memory where the value is stored.':
        '注意到区别了吗？当我们创建新变量并把它赋为一个引用值（就像对 <code>snoop</code> 做的那样），实际上我们是把<em metastring="">指向那块内存的引用</em>拷贝过来了。',
    'Then, because both values point to the same spot in memory, when we modify the value at that location in memory, it\'ll effect both values that reference it, <code>snoop</code> and <code>leo</code>.':
        '接着，因为两个变量都指向内存的同一个位置，一旦我们修改了那个位置上的值，所有引用它的变量（<code>snoop</code> 和 <code>leo</code>）都会受到影响。',
    'Now there\'s one more interesting difference between primitive and reference values and that\'s how the identity operator (<code>===</code>) compares them.':
        '原始值和引用值之间还有一个有趣的区别：全等运算符（<code>===</code>）是怎么比较它们的。',
    'Here we see that because <code>name</code> and <code>friend</code> have the same value, <code>Tyler</code>, when comparing them, we get <code>true</code>. This probably seems obvious but it\'s important to realize that the reason we get <code>true</code> is because, with the identity operator, primitives are compared by their <strong metastring="">value</strong>. Since both values equal <code>Tyler</code>, comparing them evaluates to <code>true</code>.':
        '这里我们看到，因为 <code>name</code> 和 <code>friend</code> 的值都是 <code>Tyler</code>，比较结果是 <code>true</code>。这看起来显而易见，但关键是要意识到：之所以得到 <code>true</code>，是因为全等运算符对原始值按<strong metastring="">值</strong>比较。两者都等于 <code>Tyler</code>，所以比较结果为 <code>true</code>。',
    f'Even though <code>leo</code> and <code>leito</code> have the same properties and values, when comparing them with the identity operator, we get <code>false</code>. The reason for that is because, unlike primitive values which are compared by their value, reference values are compared by their location in memory. Unless two reference values have the same location in memory, the identity operator will say they\'re <code>false</code> – and therefore, not {SPARKLE_REF2}referentially equal</strong></span>.':
        f'尽管 <code>leo</code> 和 <code>leito</code> 拥有相同的属性和值，用全等运算符比较仍然会得到 <code>false</code>。原因是：与按值比较的原始值不同，引用值是按它们在内存中的位置比较的。除非两个引用值指向内存中的同一位置，否则全等运算符会判定它们为 <code>false</code> —— 也就是说它们不{SPARKLE_REF2}引用相等</strong></span>。',
    '<code>a === b</code> evaluates to <code>true</code> since both <code>a</code> and <code>b</code> point to the same spot in memory. When comparing reference values, the identity operator compares the memory address of the value, not the value itself.':
        '<code>a === b</code> 结果为 <code>true</code>，因为 <code>a</code> 和 <code>b</code> 指向内存中的同一位置。比较引用值时，全等运算符比较的是值的内存地址，而不是值本身。',
    '<code>{} === {}</code> evaluates to <code>false</code> since both objects are stored in different spots in memory. When comparing reference values, the identity operator compares the memory address of the value, not the value itself.':
        '<code>{} === {}</code> 结果为 <code>false</code>，因为这两个对象存在内存中不同的位置。比较引用值时，全等运算符比较的是值的内存地址，而不是值本身。',
    '<code>nope === noop</code> evaluates to <code>false</code> since both functions are stored in different spots in memory. When comparing reference values, the identity operator compares the memory address of the value, not the value itself.':
        '<code>nope === noop</code> 结果为 <code>false</code>，因为这两个函数存在内存中不同的位置。比较引用值时，全等运算符比较的是值的内存地址，而不是值本身。',
    '<code>c === d</code> evaluates to <code>true</code> since both <code>c</code> and <code>d</code> point to the same spot in memory. When comparing reference values, the identity operator compares the memory address of the value, not the value itself.':
        '<code>c === d</code> 结果为 <code>true</code>，因为 <code>c</code> 和 <code>d</code> 指向内存中的同一位置。比较引用值时，全等运算符比较的是值的内存地址，而不是值本身。',
    '<code>nope() === noop()</code> evaluates to <code>false</code> since both objects returned from our function invocations are stored in different spots in memory. When comparing reference values, the identity operator compares the memory address of the value, not the value itself.':
        '<code>nope() === noop()</code> 结果为 <code>false</code>，因为这两次函数调用各自返回的对象存在内存中不同的位置。比较引用值时，全等运算符比较的是值的内存地址，而不是值本身。',
    '<code>[] === []</code> evaluates to <code>false</code> since both arrays are stored in different spots in memory. When comparing reference values, the identity operator compares the memory address of the value, not the value itself.':
        '<code>[] === []</code> 结果为 <code>false</code>，因为这两个数组存在内存中不同的位置。比较引用值时，全等运算符比较的是值的内存地址，而不是值本身。',
    f'Now the question you\'ve been waiting for, what does {SPARKLE_REF3}referential equality</strong></span> have to do with React?':
        f'现在来到你一直在等的问题：{SPARKLE_REF3}引用相等</strong></span>和 React 有什么关系？',
    'If you remember, the way React works is that whenever state changes, it will re-render the component that owns that state <strong metastring="">and</strong> all of its child components – regardless of whether or not those child components accept any props.':
        '如果你还记得，React 的工作方式是：每当 state 变化时，它会重新渲染拥有该 state 的组件，<strong metastring="">以及</strong>它所有的子组件 —— 无论这些子组件是否接收 props。',
    'If you do have an expensive component and you want that component to opt out of this default behavior by <em metastring="">only</em> re-rendering when its props change, you can use React\'s <code>React.memo</code> higher-order component.':
        '如果你确实有个开销很大的组件，想让它退出这种默认行为，<em metastring="">仅</em>在 props 变化时才重新渲染，可以使用 React 的高阶组件 <code>React.memo</code>。',
    'You may remember this example which wraps our <code>Wave</code> component inside of <code>React.memo</code> so that it only re-renders when its props change – which as of right now is never since it has no props.':
        '你可能还记得这个例子：我们把 <code>Wave</code> 组件用 <code>React.memo</code> 包起来，这样它只会在 props 变化时重新渲染 —— 但目前它没有 props，所以它永远不会重新渲染。',
    'Now, regardless of how many times we click our <code>button</code>, <code>Wave</code> will only render once, on the initial render.':
        '现在不管我们点多少次 <code>button</code>，<code>Wave</code> 都只会在初次渲染时渲染一次。',
    'Now let\'s make our <code>Wave</code> component a little more configurable. Instead of receiving no props, let\'s pass it an <code>options</code> prop that we can use to configure the emoji. Specifically, we\'ll allow the consumer of <code>Wave</code> to be able to configure the emoji skin <code>tone</code> as well as if it\'s <code>animated</code>.':
        '现在我们让 <code>Wave</code> 组件更具可配置性。与其不接收 props，不如让它接收一个 <code>options</code> prop 来配置这个 emoji。具体来说，允许 <code>Wave</code> 的使用者配置 emoji 的肤色 <code>tone</code>，以及它是否 <code>animated</code>。',
    'Here\'s what our <code>Wave</code> component looks like now.':
        '现在 <code>Wave</code> 组件长这样。',
    'That works great, but can you spot the problem now? Change the greeting and see what happens. Even though we\'re using <code>React.memo</code>, our <code>Wave</code> component is back to the re-rendering every time <code>index</code> changes even though it doesn\'t rely on <code>index</code> at all.':
        '效果不错，不过你能看出现在的问题吗？改一下问候语，看看发生了什么。尽管我们用了 <code>React.memo</code>，但每次 <code>index</code> 变化时 <code>Wave</code> 都又会重新渲染 —— 哪怕它根本没用到 <code>index</code>。',
    f'Can you spot why that is? Here\'s a clue – it has to do with {SPARKLE_REF4}referential equality</strong></span>.':
        f'你能看出原因吗？给你一个线索 —— 和{SPARKLE_REF4}引用相等</strong></span>有关。',
    'The way <code>React.memo</code> works is it\'ll only re-render the component when its props change. But that brings up an interesting question, how exactly does React determine if the props have changed? Simple, with the <code>===</code> identity operator.':
        '<code>React.memo</code> 的工作方式是：只在 props 发生变化时才重新渲染组件。但这引出一个有意思的问题 —— React 到底怎么判断 props 是不是变了？很简单，用 <code>===</code> 全等运算符。',
    'OK technically it uses <code>Object.is</code> to check if the props have changed, but for all intents and purposes, you can think of them as being the same. The only difference is in their treatment of signed zeros and <code>NaN</code> values.':
        '严格来说它用 <code>Object.is</code> 来检查 props 是否变化，但就日常理解而言，你可以把两者看作一样。唯一的区别在于它们对有符号零（signed zero）和 <code>NaN</code> 的处理。',
    'The way our <code>Wave</code> component works is we\'re passing it an object (a reference value) as a prop.':
        '我们的 <code>Wave</code> 组件的工作方式是：我们把一个对象（引用值）作为 prop 传给它。',
    'As we saw earlier, because reference values are compared by their location in memory, even though the properties on our object never change, we\'re technically creating and passing a brand new object on every render – nullifying the benefits of <code>React.memo</code>.':
        '正如前面所说，引用值是按内存位置比较的，所以尽管对象上的属性始终没变，技术上我们每次渲染都在创建并传入一个全新的对象 —— 从而让 <code>React.memo</code> 的好处化为乌有。',
    'That works, as now our <code>Wave</code> component doesn\'t re-render when <code>index</code> changes, but it only works in this particular scenario where the properties and values on our object are static and don\'t depend on the context of our component.':
        '这样能用，<code>Wave</code> 组件在 <code>index</code> 变化时不再重新渲染。但它只在这种特定场景下有效 —— 对象上的属性和值都是静态的、不依赖组件上下文。',
    'What would happen if we wanted to make the <code>tone</code> property dynamic? Let\'s say we want to give the user the ability to update <code>tone</code> by clicking on the wave emoji.':
        '如果我们想让 <code>tone</code> 这个属性动态化会怎样？比如我们想让用户点击招手 emoji 来切换 <code>tone</code>。',
    'This works, but again, we\'re nullifying the benefits of <code>React.memo</code> since we\'re now re-creating a new object on every render. Not only that, but we\'re also re-creating the <code>handleWaveClick</code> function on every render as well.':
        '这样能用，但同样地，我们又让 <code>React.memo</code> 的好处化为乌有 —— 因为每次渲染都在重新创建一个新对象。不仅如此，我们每次渲染还在重新创建 <code>handleWaveClick</code> 函数。',
    f'What we really want to do is figure out a way to {SVG_L}memoize{SVG_R} both our <code>options</code> object and our <code>handleClick</code> function so that their references only change when <code>tone</code> does. That way when <code>React.memo</code> uses <code>Object.is</code> to compare props, it\'ll work as we want.':
        f'我们真正要做的是想办法{SVG_L}把这个 <code>options</code> 对象和 <code>handleClick</code> 函数 memo 起来{SVG_R}，让它们的引用只在 <code>tone</code> 变化时才变化。这样当 <code>React.memo</code> 用 <code>Object.is</code> 比较 props 时，就会按我们的预期工作。',
    'Thankfully, React comes with a built-in hook that does exactly this called <code>useMemo</code>.':
        '好在 React 自带了一个专干这事儿的 hook —— <code>useMemo</code>。',
    'Defined, <code>useMemo</code> lets you cache the result of a calculation between renders.':
        '简单来说，<code>useMemo</code> 让你把一次计算的结果在多次渲染间缓存下来。',
    'The first argument is a function that returns the value you want to cache. The second argument is, similar to <code>useEffect</code>, an array of dependencies the function depends on. If any of the dependencies change, the cached value will be recalculated.':
        '第一个参数是一个返回你想缓存的值的函数。第二个参数和 <code>useEffect</code> 类似，是该函数依赖的一组依赖项数组。任何一个依赖项变化时，缓存的值就会重新计算。',
    'To memoize our <code>options</code> object, we can do something like this.':
        '要 memo 化我们的 <code>options</code> 对象，可以像下面这样做。',
    'Now, unless <code>waveIndex</code> changes, the <code>options</code> object will be referentially identical across renders.':
        '现在，只要 <code>waveIndex</code> 不变，<code>options</code> 对象在多次渲染间就保持同一个引用。',
    'We can do something similar for our <code>handleWaveClick</code> function as well, except instead of caching an object, we\'ll cache a function.':
        '对 <code>handleWaveClick</code> 函数我们也可以做类似的事，只不过这次缓存的不是对象，而是函数。',
    'We can even refactor this a bit to not have that <code>waveIndex</code> dependency. Instead of relying on the <code>waveIndex</code> state via closures, we can pass <code>setWaveIndex</code> a function and get access to it there.':
        '甚至可以稍微重构一下，去掉对 <code>waveIndex</code> 的依赖。与其通过闭包依赖 <code>waveIndex</code> state，我们可以给 <code>setWaveIndex</code> 传一个函数，在那里拿到当前值。',
    'Now if we throw both of those in our app, notice that when we change our greeting, <code>Wave</code> no longer re-renders since both of its props are referentially identical as the previous render.':
        '现在把这两处都用上，你会发现改变问候语时 <code>Wave</code> 不再重新渲染 —— 因为它的两个 props 的引用与上一次渲染完全相同。',
    'Whenever you need to memoize a function, instead of returning a function from <code>useMemo</code> as we did above, you can use React\'s <code>useCallback</code> hook to make it a little easier.':
        '每当你需要 memo 化一个函数时，比起像上面那样从 <code>useMemo</code> 返回一个函数，你可以改用 React 的 <code>useCallback</code> hook，更省事。',
    'It works exactly the same as <code>useMemo</code>, except instead of caching the <em metastring="">result</em> of calling a function, it caches the function itself.':
        '它和 <code>useMemo</code> 的工作方式完全一样，只不过缓存的不是调用函数的<em metastring="">结果</em>，而是函数本身。',
    'If we refactor our <code>handleWaveClick</code> function, it\'ll now look like this.':
        '如果把我们的 <code>handleWaveClick</code> 函数重构一下，就会变成下面这样。',
    '<code>useCallback</code> is really just a simple abstraction over <code>useMemo</code>. You can think of it like this.':
        '<code>useCallback</code> 说白了就是对 <code>useMemo</code> 的一层简单封装。你可以把它理解成下面这样。',
    'In my opinion, it shouldn\'t exist since you can just use <code>useMemo</code>. But it does, so you might as well use it.':
        '在我看来，它根本不该存在，因为你用 <code>useMemo</code> 就够了。不过它既然存在了，那就用它吧。',
    'Now if we add our new <code>handleWaveClick</code> function to our app, you\'ll notice it behaves the same as before.':
        '现在把新的 <code>handleWaveClick</code> 加回应用里，你会发现它的行为和之前一样。',
    f'You\'ll often hear about <code>useMemo</code> and <code>useCallback</code> as ways to {SVG_L}increase performance{SVG_R} of a React app – and though that\'s (mostly) true, in practice, I\'ve found that it\'s much more common to use them as ways to create referentially consistent values.':
        f'你经常听说 <code>useMemo</code> 和 <code>useCallback</code> 是提升 React 应用{SVG_L}性能{SVG_R}的方式 —— 这（大致上）没错，但在实践中，我发现更常见的用法是：用它们来创建引用上稳定的值。',
    'This is a natural byproduct of so many Hooks (<code>useEffect</code>, <code>useMemo</code>, <code>useCallback</code>) utilizing a dependency array to determine what values have changed between renders':
        '这是众多 Hook（<code>useEffect</code>、<code>useMemo</code>、<code>useCallback</code>）都通过依赖数组来判断多次渲染之间哪些值发生了变化 —— 带来的一个自然副产物。',
    'let <span style="color:var(--blue)">age</span> = 31; // <span style="color:var(--blue)">number</span>':
        'let <span style="color:var(--blue)">age</span> = 31; // <span style="color:var(--blue)">number</span>',
    'let <span style="color:var(--orange)">name</span> = "Tyler"; // <span style="color:var(--orange)">string</span>':
        'let <span style="color:var(--orange)">name</span> = "Tyler"; // <span style="color:var(--orange)">string</span>',
    'let <span style="color:var(--pink)">loading</span> = false; // <span style="color:var(--pink)">boolean</span>':
        'let <span style="color:var(--pink)">loading</span> = false; // <span style="color:var(--pink)">boolean</span>',
    'let <span style="color:var(--yellow)">permissions</span>; // <span style="color:var(--yellow)">undefined</span>':
        'let <span style="color:var(--yellow)">permissions</span>; // <span style="color:var(--yellow)">undefined</span>',
    'let <span style="color:var(--green)">response</span> = null; // <span style="color:var(--green)">null</span>':
        'let <span style="color:var(--green)">response</span> = null; // <span style="color:var(--green)">null</span>',
    'let <span style="color:var(--purple)">counter</span> = Symbol("c"); // <span style="color:var(--purple)">symbol</span>':
        'let <span style="color:var(--purple)">counter</span> = Symbol("c"); // <span style="color:var(--purple)">symbol</span>',
    'let <span style="color:var(--blue)">me</span> = { name: "Tyler" }; // <span style="color:var(--blue)">object</span>':
        'let <span style="color:var(--blue)">me</span> = { name: "Tyler" }; // <span style="color:var(--blue)">object</span>',
    'let <span style="color:var(--orange)">friends</span> = ["Ben", "Lynn"]; // <span style="color:var(--orange)">array</span>':
        'let <span style="color:var(--orange)">friends</span> = ["Ben", "Lynn"]; // <span style="color:var(--orange)">array</span>',
    'let <span style="color:var(--pink)">add</span> = (a, b) =&gt; a + b; // <span style="color:var(--pink)">function</span>':
        'let <span style="color:var(--pink)">add</span> = (a, b) =&gt; a + b; // <span style="color:var(--pink)">function</span>',
    'That\'s cool, but in practice, what difference does it make? Let\'s take a look at some <span style="color:rgb(165,154,157);letter-spacing:-0.07em;font-weight:100">contrived</span> examples.':
        '挺酷的，但在实践中它到底造成什么差别？来看几个<span style="color:rgb(165,154,157);letter-spacing:-0.07em;font-weight:100">刻意构造</span>的例子。',
    f'So how do we fix this? Well, we need to figure out a way for the object we pass as a prop to be {SVG_L}referentially consistent {SVG_R} across renders.':
        f'那我们怎么修？我们需要想办法让作为 prop 传入的对象在多次渲染之间{SVG_L}引用保持一致{SVG_R}。',
    '<strong>Turtles all the way down</strong>':
        '<strong>一层套一层，永无止境</strong>',
}
}

for stem, mapping in TRANS.items():
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