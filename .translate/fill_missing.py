"""Fill in missing translations across the 5 partially-done JSON files.

Strategy:
- Pure code/identifier/CSS entries -> value = key (will be filtered out of
  apply step, but counted as "done" by check_status).
- Prose entries -> Chinese translation respecting GLOSSARY.md.
"""
import json, os, sys, io
sys.stdout.reconfigure(encoding="utf-8")

BASE = r"D:\Personal\Downloads\react\.translate\extracted"

# Helper: entries where we keep the original English (code, CSS names, short identifiers).
# Using the raw key from the JSON (before any unescaping).
KEEP = {
    "&lt;": "&lt;",
    "&gt;": "&gt;",
    "&lt;/": "&lt;/",
    "=&gt;": "=&gt;",
    "\"react\"": "\"react\"",
    "\"./utils\"": "\"./utils\"",
    "'var(--red)'": "'var(--red)'",
    "'var(--green)'": "'var(--green)'",
    "'Stop'": "'Stop'",
    "'Start'": "'Start'",
    "border-radius": "border-radius",
    "background-color": "background-color",
    "--charcoal": "--charcoal",
    "flex-direction": "flex-direction",
    "align-items": "align-items",
    "text-align": "text-align",
    # 019 extras
    "\"Ben\"": "\"Ben\"",
    "\"Tyler\"": "\"Tyler\"",
    "\"Lynn\"": "\"Lynn\"",
    "\"Alex\"": "\"Alex\"",
    "`Hello,": "`Hello,",
    "Hello, Ben.": "Hello, Ben.",
    "Hello, Tyler.": "Hello, Tyler.",
    "Hello, Lynn.": "Hello, Lynn.",
    "Hello, Alex.": "Hello, Alex.",
    "state: 12": "state: 12",
}

# Long technical error message from 006 (React sandbox error). Keep verbatim.
ERR_006 = (
    "Cannot assign to read only property 'message' of object 'SyntaxError: "
    "/App.jsx: Adjacent JSX elements must be wrapped in an enclosing tag. "
    "Did you want a JSX fragment &lt;&gt;...&lt;/&gt;? (4:4)\n\n"
    "  2 |   return (\n  3 |     &lt;h2&gt;Authors&lt;/h2&gt;\n&gt; 4 |     &lt;ul&gt;\n    "
    "|     ^\n  5 |       &lt;li&gt;Tyler McGinnis&lt;/li&gt;\n  6 |       &lt;li&gt;Ben Adam&lt;/li&gt;\n"
    "  7 |       &lt;li&gt;Alex Brown&lt;/li&gt;'"
)
KEEP[ERR_006] = ERR_006

# Translations for 019 (Complex State with useReducer) prose.
TRANS_019 = {
    "Complex State with useReducer - ui.dev": "使用 useReducer 管理复杂状态 - ui.dev",
    "Next Lesson": "下一章",
    "Complex State with useReducer": "使用 useReducer 管理复杂状态",
    "media loading": "媒体加载中",
    "The Green Bay Packers, fresh off a devastating loss in the Super Bowl the previous season, had convened for the first day of training camp in July of 1961. T...":
        "1961 年 7 月，绿湾包装工队（Green Bay Packers）刚刚在上一个赛季的超级碗中经历了一场惨痛的失利，迎来了训练营的第一天。教练文斯·隆巴迪走进房间，手里拿着一个橄榄球。",
    "He began the team meeting with a simple and now fabled statement: \"Gentlemen, this is a football.\"":
        "他用一句简单却如今已成为传奇的话开启了这次队会：“先生们，这是一个橄榄球。”",
    "Every season, regardless of the team's prior success, would start in the same way – with a deep emphasis on the fundamentals.":
        "每个赛季，不管球队之前有多辉煌，都以同样的方式开始 —— 深入强调基础。",
    "I want to start this lesson off in a similar manner by looking at what I would consider to be the most fundamental array method in JavaScript – readers, this...":
        "我想用类似的方式开启这一课 —— 来看看我认为 JavaScript 中最基础的数组方法 —— 读者朋友们，这就是 `forEach`。",
    "=&gt;": "=&gt;",
    "`Hello,": "`Hello,",
    "Console (4)": "Console (4)",
    "Hello, Ben.": "Hello, Ben.",
    "Hello, Tyler.": "Hello, Tyler.",
    "Hello, Lynn.": "Hello, Lynn.",
    "Hello, Alex.": "Hello, Alex.",
    "The whole purpose of SKIP#143 is it allows you to invoke a provided function for each element in an array.":
        "SKIP#143 的全部作用，就是让你对数组中的每个元素调用你提供的函数。",
    "Now, say we had an array of numbers instead of strings. Using SKIP#144, how would we add all of the numbers together to get a single value?":
        "现在，假设我们有一个数字数组而不是字符串数组。使用 SKIP#144，我们怎么把所有数字加起来得到一个总和？",
    "Odds are, you'd do probably do something like this.":
        "大概率你会这么写：",
    "Console (1)": "Console (1)",
    "state: 12": "state: 12",
    "Notice that in order to add up all of the values, we needed to add another value, SKIP#148, and mutate it on each iteration.":
        "注意，为了把所有值加起来，我们不得不额外引入一个变量 SKIP#148，并在每次迭代中对它进行修改。",
    "reducer pattern": "reducer 模式",
    "Reducer Pattern": "Reducer 模式",
    "In JavaScript, the most common use of the reducer pattern is the SKIP#154 method that all Arrays have access to. If we refactored our example from earlier ...":
        "在 JavaScript 里，reducer 模式最常见的用法就是所有数组都能访问到的 SKIP#154 方法。如果我们用它重写前面的例子，就会像下面这样。",
    "The way it does this is, for each element in the collection, it invokes a reducer function passing it two arguments, the accumulated state and the current el...":
        "它的工作方式是：对集合中的每个元素，调用一个 reducer 函数，并向它传入两个参数 —— 累积的状态（accumulator）和当前元素。",
    "What the reducer function returns will be passed as the first argument to the next invocation of the reducer until there are no more elements left, in which ...":
        "reducer 函数返回的值会作为下一次调用时的第一个参数，直到没有更多元素为止，此时整条链条最终返回的值就是最终结果。",
    "That was a lot of words. We can see this in action if we add some logs to our SKIP#163.":
        "上面说了一大堆。我们给 SKIP#163 加几行日志，直观地看看它是怎么执行的。",
    "So here's what we know so far. The reducer pattern is a functional programming pattern that takes a collection as input and returns a single value as output....":
        "目前我们知道的是：reducer 模式是一种函数式编程模式，它接收一个集合作为输入，返回一个单一的值作为输出。",
    "Now, instead of using this pattern to transform a collection into a value, how can we use it to accomplish the main goal of this course, creating a better, m...":
        "那么，除了用这种模式把集合变成一个值之外，我们怎么才能用它来实现本课程的主要目标 —— 创建一个更好、更可预测的 UI？",
    "Let's reframe it a bit. What if instead of our collection being an array, it was a collection of user actions that happened over time? Then, whenever a new u...":
        "我们换个角度看。假设我们的“集合”不再是一个数组，而是一连串随时间发生的用户操作呢？那每当有新的用户操作发生时，我们就可以调用 reducer 函数，把当前状态和这次操作传给它，让它计算出新的状态。",
    "Check this out. Don't worry about the details yet, just know that we're using the exact same SKIP#167 function, but instead of invoking it manually, we're ...":
        "看看这段代码。先不用纠结细节，只要知道我们用的还是同一个 SKIP#167 函数，只不过这次不是手动调用，而是由每次按钮点击这个动作来触发它。",
    "It might seem strange, but since this is just a pattern, there's no reason we can't utilize it to create a more predictable interface. Now the question is, h...":
        "看起来有点奇怪，但既然这只是一种模式，我们没理由不借助它来打造一个更可预测的接口。现在的问题是，怎么把它和 React 结合起来？",
    "Because it's such a helpful pattern, React comes with a built-in Hook called SKIP#169 that functionally behaves like SKIP#170, but allows you to manage y...":
        "因为 reducer 是一种非常有用的模式，React 专门提供了一个内置 Hook —— SKIP#169。它的行为上类似 SKIP#170，但允许你以 reducer 的方式来管理组件状态。",
    "What's different is instead of returning an updater function, it returns a function called SKIP#175 that when called, will invoke the SKIP#176 function.":
        "不同之处在于，它返回的不是更新函数，而是一个叫 SKIP#175 的函数 —— 调用它时会触发 SKIP#176 函数的执行。",
    "Putting it all together, here's what it looks like. Again, notice our SKIP#178 is still the exact same.":
        "把这些拼在一起，效果就是下面这样。再次注意，我们的 SKIP#178 还是和之前完全一致。",
    "The only difference is that instead of the SKIP#181 getting the SKIP#182 from an array, it's getting it from whatever is passed to SKIP#183 – in our ex...":
        "唯一的区别在于：SKIP#181 不再从数组里拿到 SKIP#182，而是从传给 SKIP#183 的值中拿到 —— 在我们的例子中，就是传给 dispatch 的字符串。",
    "Said differently, when invoked, whatever you pass to SKIP#185 will be passed as the second argument to the SKIP#186 function (which we've been calling S...":
        "换句话说，调用时你传给 SKIP#185 的任何值，都会作为 SKIP#186 函数（也就是我们一直在叫的 SKIP#187）的第二个参数。",
    "Again, everything is the exact same as what we saw with JavaScript's SKIP#190, but now it's a user event that triggers the reducer function.":
        "同样，一切和 JavaScript 的 SKIP#190 完全一致，只不过现在是由用户事件来触发 reducer 函数。",
    "Instead of just incrementing SKIP#193, let's add two more buttons - one to decrement it and one to reset it to SKIP#194.":
        "我们不只让 SKIP#193 自增，再加两个按钮 —— 一个用来递减，一个用来把它重置为 SKIP#194。",
    "For decrementing, all we need to do is pass SKIP#195 to dispatch, because math.":
        "对于递减，我们只需要把 SKIP#195 传给 dispatch —— 因为数学嘛。",
    "With the current functionality of our app, we'll have three different action types, SKIP#209, SKIP#210, and SKIP#211.":
        "基于应用当前的功能，我们会有三种不同的 action 类型：SKIP#209、SKIP#210 和 SKIP#211。",
    "Now, inside of our SKIP#213, we can change how we update the SKIP#214 based on those action types. Instead of naming our second parameter SKIP#215, let...":
        "现在，在 SKIP#213 内部，我们可以根据这些 action 类型来决定如何更新 SKIP#214。把第二个参数的名字从 SKIP#215 改为 action 会更贴切 —— 因为它确实代表一次 action。",
    "This is where we start to see SKIP#220 shine. You may not have noticed it, but we've completely decoupled the logic for managing SKIP#221 from the compon...":
        "这正是 SKIP#220 开始大放异彩的地方。你可能没察觉，我们已经把管理 SKIP#221 的逻辑完全从组件中解耦出来了。",
    "This means all the component has to do is SKIP#222 what action occurred and how the state changes in response to that action is an implementation detail of...":
        "这意味着组件只需要 SKIP#222 说一声“发生了什么 action”，而状态到底如何变化则是 reducer 的实现细节 —— 组件根本不用关心。",
    "Let's keep going.": "我们继续。",
    "Before you continue...": "在你继续之前……",
    "Instead of just incrementing and decrementing SKIP#223 by SKIP#224, let's let the user decide via a slider. The final result being something like this.":
        "我们不再只让 SKIP#223 固定按 SKIP#224 递增/递减，而是让用户通过一个滑块来决定。最终效果大致如下：",
    "To accomplish this, imagine we had a SKIP#226 component that took in 3 props, SKIP#227, SKIP#228, and SKIP#229.":
        "为此，想象我们有一个 SKIP#226 组件，它接收三个 props：SKIP#227、SKIP#228 和 SKIP#229。",
    "The way we get the value of the slider is via the SKIP#231's SKIP#232 prop. Knowing this, and knowing that its the value of the slider that will decide b...":
        "我们通过 SKIP#231 的 SKIP#232 prop 来获得滑块的值。了解了这一点，并且知道滑块的值决定了每次按钮点击会让计数增加或减少多少，我们就可以相应地实现它。",
    "Right now the SKIP#234 for our SKIP#235 is an integer which represents the SKIP#236.":
        "目前 SKIP#235 的 SKIP#234 是一个整数，代表 SKIP#236。",
    "This worked previously, but now instead of just managing SKIP#238, we also want our SKIP#239 to manage another piece of state – SKIP#240, which we get ...":
        "这之前没问题，但现在我们不再只管理 SKIP#238，还希望 SKIP#239 管理另一块状态 —— SKIP#240，也就是从滑块拿到的值。",
    "Instead of SKIP#242 just being an integer, let's refactor it to be an object. This way, any new values that our SKIP#243 needs to manage (like our new S...":
        "与其让 SKIP#242 只是一个整数，我们把它重构成一个对象。这样，SKIP#243 将来要管理的任何新值（比如这次的 SKIP#244）都可以作为对象上的属性。",
    "Now, since our SKIP#247 is no longer an integer but an object with SKIP#248 and SKIP#249 properties, we'll need to update our SKIP#250 to account for...":
        "现在 SKIP#247 不再是一个整数，而是一个带有 SKIP#248 和 SKIP#249 属性的对象，我们需要相应地更新 SKIP#250。",
    "Notice that we always return an object with the same shape, and now we're accessing SKIP#252 as a property on that SKIP#253 object. Also notice that in a...":
        "注意我们每次都返回结构相同的对象，而且现在是从 SKIP#253 对象上访问 SKIP#252 属性。另外还要注意，在每个分支里，我们都用展开语法把现有状态先拷贝过来，然后再覆盖要改的字段。",
    "So now that our SKIP#259 is updated to work with the new shape of our state, the next thing we need to do is update SKIP#260 whenever the user moves the ...":
        "既然 SKIP#259 已经能处理新的状态结构，下一步就是在用户移动滑块时更新 SKIP#260。",
    "Whenever the user moves the slider, the SKIP#264 function will be called with the new value of the slider, giving us the opportunity to update the SKIP#26...":
        "每当用户移动滑块，SKIP#264 函数就会被调用并带上滑块的新值，这正好给了我们机会去更新 SKIP#265。",
    "Up until this point, we've been able to SKIP#267 the type of action that occurred (SKIP#268, SKIP#269, and SKIP#270). This worked fine, but we're now...":
        "到目前为止，我们只 SKIP#267 发生的 action 类型（SKIP#268、SKIP#269 和 SKIP#270）。这之前没问题，但现在有了新的需求。",
    "Along with the action SKIP#271, we also need to pass along some other data – specifically in our case, we want to pass along the SKIP#272 of the slider s...":
        "除了 action SKIP#271 之外，我们还需要带上一些额外的数据 —— 具体来说，我们想带上滑块的 SKIP#272，这样 reducer 才能用它来更新状态。",
    "You might be tempted to do something like this, where you pass any extra data as a second argument to SKIP#274.":
        "你可能会想这样写 —— 把任何额外数据作为第二个参数传给 SKIP#274。",
    "Unfortunately, this won't work because the SKIP#276 function only accepts a single argument. To work around this, what if instead of dispatching a string, ...":
        "可惜这样行不通，因为 SKIP#276 函数只接受一个参数。要绕过这个问题，我们可以不 dispatch 字符串，而是 dispatch 一个包含所需全部信息的对象。",
    "Here's what our existing event handlers would look like if we did that – notice that each object we dispatch has a SKIP#277 property to represent that type...":
        "如果这样做，我们现有的事件处理器会变成下面这样 —— 注意每个 dispatch 出去的对象都有一个 SKIP#277 属性，用来表示 action 类型。",
    "And here's a new event handler we could pass to our SKIP#279's SKIP#280 prop.":
        "下面是我们可以传给 SKIP#279 的 SKIP#280 prop 的新事件处理器。",
    "Notice that we're passing along the SKIP#282 value as a property on the SKIP#283 object.":
        "注意我们把 SKIP#282 的值作为 SKIP#283 对象上的一个属性一起传过去。",
    "Now that we've updated what we're dispatching to be an object instead of a string, there are three changes we need to make to our SKIP#284.":
        "既然我们把 dispatch 的内容从字符串改成了对象，就需要对 SKIP#284 做三处改动。",
    "First, we need to refactor all of our conditional statements to check for SKIP#285 instead of just SKIP#286.":
        "第一，我们需要把所有条件判断都改成检查 SKIP#285，而不是只检查 SKIP#286。",
    "Second, we need to add another conditional for our new action type, SKIP#288.":
        "第二，我们需要给新的 action 类型 SKIP#288 再加一个分支。",
    "Notice that we're using SKIP#290 in order to update the SKIP#291 property on our state. This was the whole reason we needed to refactor SKIP#292 to be ...":
        "注意我们在用 SKIP#290 来更新状态上的 SKIP#291 属性。这也是我们一开始要把 SKIP#292 重构成对象的全部原因。",
    "And finally, we need to update SKIP#293 and SKIP#294 to adjust the SKIP#295 based on the SKIP#296 property instead of SKIP#297.":
        "最后，我们还需要更新 SKIP#293 和 SKIP#294 —— 让它们根据 SKIP#296 属性来调整 SKIP#295，而不是根据 SKIP#297。",
    "With that, we see another subtle but powerful benefit of SKIP#301 you might have missed. Because the SKIP#302 function is passed the current SKIP#303 a...":
        "由此，我们看到 SKIP#301 一个你可能忽略了的微妙却强大的好处。因为 SKIP#302 函数会被传入当前的 SKIP#303，所以你可以基于当前状态来计算下一个状态 —— 这正是在使用 SKIP#304 时很容易搞错的地方。",
    "In fact, I'd go as far as to say whenever updating one piece of state depends on the value of another piece of state, reach for SKIP#306.":
        "事实上，我甚至可以说：只要更新某一块状态依赖于另一块状态的值，就应该考虑使用 SKIP#306。",
    "At this point, we've seen both how SKIP#307 works and some of the advantages it gives us. Now, let's dive a little deeper into those advantages and answer ...":
        "到这里，我们已经看到 SKIP#307 怎么用，以及它带来的一些好处。现在让我们更深入地聊一下这些好处，回答一个自然会冒出来的问题：什么时候应该用 SKIP#308，什么时候应该用 SKIP#309？",
    "Fundamentally, SKIP#310 and SKIP#311 accomplish the same thing - they both allow you to add state to a component that will be preserved across renders an...":
        "从根本上讲，SKIP#310 和 SKIP#311 能做的事是一样的 —— 它们都让你在组件里添加会跨渲染保留下来的状态，状态变化时还会触发重新渲染。但在某些场景下，用 SKIP#312 会让代码更可读、更可维护。",
    "Here's one example. Imagine we were creating a component that was responsible for allowing a user to register for our newsletter. This form needs to collect ...":
        "举个例子。想象我们在做一个让用户订阅新闻简报的组件。这个表单需要收集用户的邮箱和姓名。",
    "For UX purposes, we'll also need two more pieces of state, SKIP#314 and SKIP#315.":
        "为了更好的用户体验，我们还需要另外两块状态：SKIP#314 和 SKIP#315。",
    "Using SKIP#316, here's one approach for how we'd accomplish this.":
        "用 SKIP#316 来实现，可以这样写：",
    "First, there's nothing technically wrong with this code. It works just fine.":
        "首先，这段代码从技术上讲没有任何问题，它能正常工作。",
    "The reason SKIP#322 can be more declarative is because it allows us to map actions to state transitions. This means, instead of having a collection of SKI...":
        "SKIP#322 之所以能更声明式，是因为它让我们能把 action 映射到状态转换。这意味着我们不再需要一堆散落的 SKIP#323 调用，而是可以把状态的变化集中到一个 reducer 里。",
    "To see what this looks like, let's assume we've already set up our SKIP#326 and we're updating our SKIP#327 function we saw above. Here's what that would...":
        "为了看它长什么样，我们先假设已经写好了 SKIP#326，然后更新前面看到的 SKIP#327 函数。效果如下：",
    "The rest of the code isn't particularly interesting or covering anything new, but we'll quickly walk through it for completeness.":
        "剩下的代码没什么特别新鲜的，但为了完整性我们快速过一遍。",
    "First we'll build out our SKIP#332, updating our state based on those three actions.":
        "先实现 SKIP#332，根据这三种 action 更新状态。",
    "Then we'll update our SKIP#334 component to use SKIP#335 instead of SKIP#336.":
        "然后更新 SKIP#334 组件，用 SKIP#335 替换 SKIP#336。",
    "If you ever find yourself needing a more declarative approach to updating your component state, give SKIP#340 a shot since it allows you to map actions dir...":
        "如果你发现自己需要一种更声明式的方式来更新组件状态，不妨试试 SKIP#340 —— 它让你能把 action 直接映射到状态转换。",
    "Now before we end, let's take a look at one more use case where SKIP#341 works better than SKIP#342. To make it fun, I want to offer it as a challenge.":
        "在结束之前，我们再看一个 SKIP#341 比 SKIP#342 更合适的场景。为了好玩，我把它作为一个小挑战留给你。",
    "Here's our counter implementation we saw earlier but implemented with SKIP#343 instead of SKIP#344.":
        "下面是我们之前看到的计数器实现，不过这次用 SKIP#343 而不是 SKIP#344。",
    "Really, give it a shot. Scroll down when you're ready.":
        "真的，试一下。准备好之后再往下滚动。",
    "Alright let me guess the steps you went through. First, you probably started with something like this.":
        "好，让我来猜猜你经历了怎样的思考过程。首先，你可能会这样开始：",
    "That's clean – and aggressively wrong. Remember, SKIP#353 uses SKIP#354 and SKIP#355, which means you need to declare them in your dependency array. Th...":
        "看起来很整洁 —— 但错得彻底。记住，SKIP#353 用到了 SKIP#354 和 SKIP#355，这意味着你必须把它们声明到依赖数组里。一旦这样做，每次 SKIP#356 变化时 effect 都会重新跑，完全不符合你的预期。",
    "From there, you probably remembered that if you pass a function to an updater function, you'll get access to the current state without needing to pass it int...":
        "接着你可能想起来，如果把函数传给更新函数，就可以拿到当前状态，而不用把它作为 effect 的依赖传进去。",
    "Believe it or not, as of this writing, the only way to solve a problem like this is to use SKIP#363.":
        "信不信由你，截至本文撰写时，解决这类问题唯一的办法就是用 SKIP#363。",
    "Again, with SKIP#364 we decouple how the state is updated from the action that triggered the update. This means that we can trigger a state change from ins...":
        "再次强调，SKIP#364 把“状态如何更新”和“触发更新的 action”解耦开来。这意味着我们可以从 effect 内部触发状态变化，而不必把 effect 依赖在某一块具体的状态上。",
    "Check it out.": "看看下面：",
    "Now our effect is only called once, regardless of how many times SKIP#369 or SKIP#370 change.":
        "现在不管 SKIP#369 或 SKIP#370 变化多少次，我们的 effect 都只会被调用一次。",
    "To recap, like SKIP#371, SKIP#372 allows you to add state to a component that will be preserved across renders and trigger a re-render when it changes. U...":
        "简要回顾一下：和 SKIP#371 一样，SKIP#372 让你给组件添加跨渲染保留的状态，并在状态变化时触发重新渲染。但不同的是，它不返回更新函数，而是返回一个 SKIP#373 函数，调用它会运行你的 SKIP#374。",
    "SKIP#375 also offers a bit more flexibility than SKIP#376 since it allows you to decouple how the state is updated from the action that triggered the upd...":
        "SKIP#375 也比 SKIP#376 多一些灵活性，因为它让你把“状态如何更新”和“触发更新的 action”解耦开来。",
    "If different pieces of state update independently from one another (SKIP#377, SKIP#378, etc.), SKIP#379 should work fine. If your state tends to be upd...":
        "如果各块状态之间相互独立地更新（SKIP#377、SKIP#378 等等），SKIP#379 就够用了。但如果你的状态倾向于整块一起更新，或者某块状态的更新依赖于另一块，那就用 SKIP#380。",
}

def process(filename, extra_trans=None):
    path = os.path.join(BASE, filename)
    with open(path, "r", encoding="utf-8") as f:
        # Preserve order AND allow duplicate keys by using a list of pairs.
        pairs = json.load(f, object_pairs_hook=list)

    filled = 0
    remaining = 0
    out = []
    for k, v in pairs:
        if v:
            out.append((k, v))
            continue
        new_v = None
        if extra_trans and k in extra_trans:
            new_v = extra_trans[k]
        elif k in KEEP:
            new_v = KEEP[k]
        if new_v is None:
            remaining += 1
            out.append((k, v))
        else:
            filled += 1
            out.append((k, new_v))

    # Since JSON doesn't allow duplicate keys, keep the LAST value per key
    # (but we only have distinct keys in practice per file, plus dup 'reducer pattern' variants).
    d = {}
    for k, v in out:
        d[k] = v  # later duplicates override earlier — fine for our purposes.

    with open(path, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=2)
    print(f"  {filename[:3]}  filled={filled}  remaining-missing={remaining}")

process("006 - JSX - ui.dev.json")
process("009 - Elements vs Components - ui.dev + styles.css.json")
process("010 - Handling Events - ui.dev.json")
process("017 - Preserving Values with useRef - ui.dev.json")
process("019 - Complex State with useReducer - ui.dev.json", extra_trans=TRANS_019)
