import json, sys
sys.stdout.reconfigure(encoding="utf-8")

PATH = r"D:\Personal\Downloads\react\.translate\inline\019 - Complex State with useReducer - ui.dev.json"

# Translations for 019's 12 missed inline-tag paragraphs.
# IMPORTANT: keys must match the inner HTML exactly (incl. nested tags & attrs).
TRANS = {
    "This works, but it's not ideal for a few different reasons. First, it's dependent on the state of our application. Second, it's modifying state outside of its own scope. By definition, this makes <code>forEach</code> an <span class=\"font-black tracking-wider\" style=\"color:currentcolor\">impure</span> function.":
        "这样写能用，但理由其实并不理想。首先，它依赖应用的外部状态；其次，它修改了自身作用域之外的状态。按定义来说，这让 <code>forEach</code> 成为一个<span class=\"font-black tracking-wider\" style=\"color:currentcolor\">不纯的</span>函数。",

    "The key difference between <code>reduce</code> and <code>forEach</code> is that <code>reduce</code> is able to keep track of the accumulated <code>state</code> <em metastring=\"\">internally</em> without relying upon or modifying state outside of its own scope - that's what makes it pure.":
        "<code>reduce</code> 和 <code>forEach</code> 的关键区别在于：<code>reduce</code> 能够<em metastring=\"\">在内部</em>追踪累积的 <code>state</code>，而不依赖或修改自身作用域之外的状态 —— 这正是它保持纯函数的原因。",

    "The API for <code>useReducer</code> is similar to what we saw earlier with <code>Array.reduce</code>, but with one big difference. Instead of just returning the state, similar to <code>useState</code>, <code>useReducer</code> also returns a way to <em metastring=\"\">update</em> that state.":
        "<code>useReducer</code> 的 API 和我们之前看到的 <code>Array.reduce</code> 类似，但有一个重大差别。它不只是返回 state，和 <code>useState</code> 一样，<code>useReducer</code> 还会返回一种<em metastring=\"\">更新</em>该 state 的方式。",

    "So at this point you've seen how <code>useReducer</code> works in its most <strong metastring=\"\">basic</strong> form. What you haven't seen yet is an example of <code>useReducer</code> that resembles anything close to what you'd see in the real-world. To get closer to that, let's add a little bit more functionality to our app.":
        "到这里，你已经看过了 <code>useReducer</code> 最<strong metastring=\"\">基础</strong>的用法。但你还没看到一个足够贴近真实场景的 <code>useReducer</code> 例子。为了更接近现实，我们给应用再加一些功能。",

    "For resetting the <code>count</code> to <code>0</code>, it gets a little trickier. Right now with how we've set up our <code>reducer</code> function, there's no way to specify different <em metastring=\"\">types</em> of actions that can occur to update our state. We only accept a <code>value</code> (which we get from whatever was passed to <code>dispatch</code>) and add that to <code>state</code>.":
        "要把 <code>count</code> 重置为 <code>0</code>，情况就有点棘手了。按我们目前的 <code>reducer</code> 函数写法，根本没有办法表示更新 state 时可能发生的不同<em metastring=\"\">类型</em>的 action。我们只接受一个 <code>value</code>（也就是传给 <code>dispatch</code> 的任何值），然后把它加到 <code>state</code> 上。",

    "What if instead of <code>dispatch</code>ing the value directly, we <code>dispatch</code> the <strong metastring=\"\">type</strong> of action that occurred? That way, based on that action type, our <code>reducer</code> can decide how to update the state.":
        "如果我们不直接 <code>dispatch</code> 值，而是 <code>dispatch</code> 所发生 action 的<strong metastring=\"\">类型</strong>会怎么样？这样 <code>reducer</code> 就能根据 action 类型决定如何更新 state。",

    "If this lesson has felt <em metastring=\"\">slow</em> so far, this is where it'll start to pick up. If this lesson hasn't felt slow (that's fine), make sure you're comfortable with everything we've covered so far before moving on.":
        "如果你之前觉得这节课节奏比较<em metastring=\"\">慢</em>，从这里开始就会加速。如果你并不觉得慢（也没关系），在继续之前请确认你已经熟练掌握了前面讲到的所有内容。",

    "However, it is an imperative solution to the problem. We're operationally describing <strong metastring=\"\">how</strong> we want to submit the user's email – with <strong metastring=\"\">lots</strong> of <code>setX</code> invocations. Instead, what if we took a more declarative approach?":
        "不过，这是一种命令式的解法。我们是在一步步描述<strong metastring=\"\">怎样</strong>提交用户的邮箱 —— 通过<strong metastring=\"\">大量</strong>的 <code>setX</code> 调用来完成。那如果我们采用更声明式的方式呢？",

    "Instead of <strong metastring=\"\">how</strong>, let's describe <strong metastring=\"\">what</strong> we're trying to accomplish. We can do this by leveraging <code>useReducer</code>.":
        "不去描述<strong metastring=\"\">怎么做</strong>，而是描述我们<strong metastring=\"\">想做什么</strong>。借助 <code>useReducer</code> 就能做到这一点。",

    "Notice that we're describing <strong metastring=\"\">what</strong> we want to do - <code>submit</code>. Then, based on that result, <code>success</code> or <code>error</code>. That's a lot cleaner and easier to reason about than our imperative solution.":
        "注意我们描述的是<strong metastring=\"\">想做什么</strong> —— <code>submit</code>，然后根据结果是 <code>success</code> 还是 <code>error</code>。这比命令式写法干净得多，也更容易推理。",

    "What I want you to do is, using <code>useEffect</code> and <code>setInterval</code>, increment the counter by <code>step</code> every second. So <code>count</code> will change both whenever the user clicks a button <strong metastring=\"\">or</strong> every second.":
        "我希望你用 <code>useEffect</code> 和 <code>setInterval</code>，让计数器每秒钟按 <code>step</code> 自增一次。也就是说，<code>count</code> 会在用户点击按钮时变化，<strong metastring=\"\">或者</strong>每隔一秒也会变化。",

    "Nice. That <em metastring=\"\">seems</em> like it works, but can you spot the problem with it? Try changing <code>step</code>. It's the same problem we ran into before. Every time <code>step</code> changes, we're clearing and establishing a new interval. Better, but still not ideal.":
        "不错。这<em metastring=\"\">看起来</em>能跑，但你能看出问题在哪吗？试着改一下 <code>step</code>。这就是我们之前遇到过的同一个问题。每次 <code>step</code> 变化，我们都会清掉并重新建立一个 interval。比之前好一点，但还是不理想。",
}

with open(PATH, "r", encoding="utf-8") as f:
    d = json.load(f)

filled = 0
unmatched = []
for k in list(d.keys()):
    if k in TRANS and not d[k]:
        d[k] = TRANS[k]
        filled += 1
    elif not d[k]:
        unmatched.append(k)

with open(PATH, "w", encoding="utf-8") as f:
    json.dump(d, f, ensure_ascii=False, indent=2)

print(f"Filled: {filled}")
if unmatched:
    print(f"Unmatched ({len(unmatched)}):")
    for k in unmatched:
        print(" ", k[:200])