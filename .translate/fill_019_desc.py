# -*- coding: utf-8 -*-
"""Translate the two-part description under the 'Reducer 模式' section-header in 019.

The source markup renders as:

    Reducer 模式
    A functional programming pattern that takes a [累积器 popover]
    as input and returns a single value as output.
"""
from pathlib import Path

p = Path("019 - Complex State with useReducer - ui.dev.html")
text = p.read_text(encoding="utf-8")


# The description div is:
#   <div class="text-center mt-4 text-2xl">A functional programming pattern
#    that takes a <button>累积器<svg.../></button> as input and returns a
#    single value as output.</div>
#
# Rewrite both English fragments, keeping the button intact.
SRC_PREFIX = (
    '<div class="text-center mt-4 text-2xl">A functional programming pattern that '
    'takes a <button'
)
DST_PREFIX = (
    '<div class="text-center mt-4 text-2xl">一种函数式编程模式，接收一个<button'
)
if SRC_PREFIX not in text:
    raise SystemExit(f"Description prefix not found: {SRC_PREFIX[:80]}")
text = text.replace(SRC_PREFIX, DST_PREFIX, 1)

# Trailing fragment: "</button> as input and returns a single value as output.</div>"
SRC_SUFFIX = "</button> as input and returns a single value as output.</div>"
DST_SUFFIX = "</button>作为输入，并返回一个值作为输出。</div>"
if SRC_SUFFIX not in text:
    raise SystemExit(f"Description suffix not found: {SRC_SUFFIX[:80]}")
text = text.replace(SRC_SUFFIX, DST_SUFFIX, 1)

p.write_text(text, encoding="utf-8")
print("OK: 019 reducer-pattern description translated.")
