# -*- coding: utf-8 -*-
"""Translate the remaining English fragments in 008 - Elements vs Components.

The file mixes Chinese and English inside the same <p> (via inline <em>/<code>/<span>
tags), so our simple `<p>…</p>` prose-only scanner missed them. This script
handles each unique fragment as an exact (src, dst) replacement.
"""
from pathlib import Path

TARGET = Path("008 - Elements vs Components - ui.dev.html")


# NOTE: the "If this is called a 函数定义,", "this is called a 函数调用.",
# and "If this is called a component 定义," paragraphs appear TWICE each:
# once in the opening question (lines ~364/366/368) and once again when
# the author recaps the question near the end (lines ~450/452/454). We
# intentionally apply the same translation in both places, using str.replace()
# without a count limit.
PAIRS = [
    # Intro: "Here's a question for you. If this is called a 函数定义,"
    (
        '<p metastring="">Here\'s a question for you. If this is called a '
        '<em metastring="">函数定义</em>,</p>',
        '<p metastring="">给你出个小问题。如果这被称为<em metastring="">函数定义</em>，</p>',
    ),
    # "this is called a 函数调用." — appears twice
    (
        '<p metastring="">this is called a <em metastring="">函数调用</em>.</p>',
        '<p metastring="">那这个就叫做<em metastring="">函数调用</em>。</p>',
    ),
    # "If this is called a component 定义," — appears twice
    (
        '<p metastring="">If this is called a <em metastring="">component 定义</em>,</p>',
        '<p metastring="">如果这被称为 <em metastring="">component 定义</em>，</p>',
    ),
    # "If this is called a 函数定义," (the recap version, no "Here's a question")
    (
        '<p metastring="">If this is called a <em metastring="">函数定义</em>,</p>',
        '<p metastring="">如果这被称为<em metastring="">函数定义</em>，</p>',
    ),
    # Definition paragraph with embedded <em>不是</em>
    (
        '<p metastring="">This definition gives us some interesting insight into how React '
        'works under the hood. An element <em metastring="">不是</em> a DOM node, instead '
        "it's an object representation of it.</p>",
        '<p metastring="">这个定义让我们对 React 底层的工作方式有了一些有趣的洞察。'
        '一个 element <em metastring="">并不是</em>一个 DOM 节点，'
        '而是这个 DOM 节点的<strong>对象表示</strong>。</p>',
    ),
    # "Notice there's no JSX – it's <sparkle>就是 JavaScript™</sparkle>."
    #
    # Only the leading and trailing English bits need translation; the sparkle
    # span in the middle is already Chinese, so we keep it byte-for-byte.
    # In the source HTML the en-dash is followed by a non-breaking space
    # (U+00A0), not a regular space.
    (
        '<p metastring="">Notice there\'s no JSX \u2013\u00a0it\'s ',
        '<p metastring="">注意这里完全没有 JSX\u2014\u2014它',
    ),
    # ...and the trailing ".</p>" right after the sparkle span on the same line.
    # We anchor the replacement on the closing </span>. Keep it ultra-narrow
    # so we don't match any other sparkle in the file.
    (
        'class="sparkle_child_wrapper__bem0y">就是 JavaScript\u2122</strong></span>.</p>',
        'class="sparkle_child_wrapper__bem0y">就是 JavaScript\u2122</strong></span>。</p>',
    ),
    # The long "What's interesting about learning React..." paragraph.
    # en-dash is followed by U+00A0 in the source.
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
    # Final recap: "We call it 创建一个 element, because after the JSX is compiled
    # and <code>jsx</code> is invoked, that's what we get back – an element."
    # en-dash is followed by U+00A0 in the source.
    (
        '<p metastring="">We call it <em metastring="">创建一个 element</em>, because '
        'after the JSX is compiled and <code>jsx</code> is invoked, that\u2019s what '
        'we get back \u2013\u00a0an element.</p>',
        '<p metastring="">我们把它叫做<em metastring="">创建一个 element</em>，'
        '因为在 JSX 被编译、<code>jsx</code> 被调用之后，我们拿回来的正是一个 element。</p>',
    ),
]


def main() -> None:
    text = TARGET.read_text(encoding="utf-8")
    total = 0
    missing = []
    for src, dst in PAIRS:
        count = text.count(src)
        if count == 0:
            missing.append(src[:80])
            continue
        text = text.replace(src, dst)
        total += count
    if missing:
        print("MISSING:")
        for m in missing:
            print(" -", m)
        raise SystemExit(1)
    TARGET.write_text(text, encoding="utf-8")
    print(f"OK: applied {total} replacements from {len(PAIRS)} patterns.")


if __name__ == "__main__":
    main()
