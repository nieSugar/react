# -*- coding: utf-8 -*-
"""Apply the Chinese text replacements from _translated.html to the original 015."""
from pathlib import Path

TARGET = Path('015 - Managing Effects - ui.dev.html')

# (original English fragment, Chinese translation)
# Preserve surrounding punctuation and whitespace as seen in the file.
REPLACEMENTS = [
    ("This is better, as our side effect will only get called once on the initial render. Unfortunately, even if it's just once, we're still violating",
     "这样更好，因为我们的副作用只会在初始渲染时调用一次。遗憾的是，即使只有一次，我们仍然违反了"),
    ("This example is now the perfect representation of our 3 rules. We've successfully moved all of our side effects out of React's",
     "这个例子现在完美代表了我们的3条规则。我们已经成功地把所有副作用从React的"),
    ("Notice our side effect is still part of our component, we've just abstracted it to a part of our component that's",
     "注意我们的副作用仍然是组件的一部分，我们只是把它抽象到组件中一个"),
    ("any time it does anything other than take some input, an argument, and calculate some output, a return value.",
     "任何时候它除了接收某些输入（参数）并计算某些输出（返回值）之外还做任何事情。"),
    ("work how you're expecting it to. This is such a common misconception, I want to call it out explicitly.",
     "按你的预期工作。这是一个非常常见的误解，我想明确指出这一点。"),
    ("we could get around this, or we could just follow our rules and avoid the problem entirely.",
     "我们可以绕过这个问题，或者我们可以遵循我们的规则并完全避免这个问题。"),
    (", it should be able to get a description of the UI without running into any side effects.",
     "，它应该能够获得UI的描述，而不会遇到任何副作用。"),
    (", but that doesn't get us anywhere closer to knowing where to put our side effect.",
     "，但这并没有让我们更接近了解在哪里放置我们的副作用。"),
    ("With that said, we still don't really have a rule for this scenario. We know what",
     "话虽如此，我们对这个场景仍然没有真正的规则。我们知道"),
    ("That sounds fancy, but in the context of React, it just means that when React",
     "这听起来很花哨，但在React的背景下，这只是意味着当React"),
    (", but what's inside of it, side effects or not, are irrelevant during render.",
     "，但其中的内容，无论是否有副作用，在渲染时都无关紧要。"),
    ("This seems like a reasonable solution, and it might be, if it didn't violate",
     "这看起来像是一个合理的解决方案，也许是的，如果它没有违反"),
    ("about the second argument, but it's wrong. Instead of telling React",
     "关于第二个参数的说法，但这是错误的。与其告诉React"),
    ("Now before we dive into it, I want to warn you that it probably",
     "在深入研究之前，我想警告你它可能"),
    ("This seems lik a reasonable solution, but again, it violates",
     "这看起来像是一个合理的解决方案，但同样，它违反了"),
    ("Conceptually this makes sense, especially when combined with",
     "从概念上讲，这是有意义的，特别是当与"),
    (". Not only that, but it technically violates Rule #0 on",
     "。不仅如此，它在技术上也违反了第0条规则"),
    ("Diagram showing that view = function(state)",
     "显示view = function(state)的图表"),
    ("that effect needs to run – like this.",
     "那个effect需要运行——像这样。"),
    ("to invoke the effect, you give React",
     "要调用该effect，你给React"),
    ("posts all dedicated to this topic.",
     "都有专门讨论这个主题的文章。"),
    ("Even the official React docs",
     "即使是官方React文档"),
    ('"Getting battery level..."',
     '"正在获取电池电量..."'),
    (". React is still aware of",
     "。React仍然知道"),
    ("Getting battery level...",
     "正在获取电池电量..."),
]


def main():
    text = TARGET.read_text(encoding="utf-8")
    applied = 0
    missing = []
    for src, dst in REPLACEMENTS:
        count = text.count(src)
        if count == 0:
            missing.append(src[:80])
            continue
        text = text.replace(src, dst)
        applied += count
    if missing:
        print("MISSING:")
        for m in missing:
            print(" -", m)
    TARGET.write_text(text, encoding="utf-8")
    print(f"OK: applied {applied} replacements (from {len(REPLACEMENTS)} patterns)")


if __name__ == "__main__":
    main()
