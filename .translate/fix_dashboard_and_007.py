# -*- coding: utf-8 -*-
"""
Two tasks in one:

1. Rewrite the ui.dev "Dashboard" link in every lesson HTML so that it points
   to our local /index.html navigation page instead of the external ui.dev
   dashboard (https://ui.dev/c/react). Also translate the label to "目录" so
   it matches the floating nav bar.

2. Translate the last untranslated sentence in 007 - Props:
   "One thing you may have noticed is that sometimes we have to wrap what
    we're passing in inside of <花括号>, {}. Can you spot why that is?"
"""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parent.parent

# ---------- Task 1: Dashboard → 目录 → /index.html ----------
# The original anchor exact form (as found in every lesson HTML):
#
#   <a class="..."
#      href="https://ui.dev/c/react">
#     <svg ...><path .../></svg> Dashboard</a>
#
# We don't want to depend on the class string, which is long and identical
# across files. Use a tolerant regex that anchors on the href and the literal
# " Dashboard</a>" suffix.
DASHBOARD_RE = re.compile(
    r'(<a\b[^>]*?href=")https://ui\.dev/c/react("[^>]*>.*?)\sDashboard</a>',
    re.DOTALL,
)


def rewrite_dashboard(text: str) -> tuple[str, int]:
    """Replace the external Dashboard href + label in `text`."""
    new_text, count = DASHBOARD_RE.subn(
        r'\1/index.html\2 目录</a>',
        text,
    )
    return new_text, count


# ---------- Task 2: 007 Props "花括号" sentence ----------
PROPS_FILE = ROOT / "007 - Props - ui.dev.html"

PROPS_SRC = (
    '<p metastring="">One thing you may have noticed is that sometimes we have '
    'to wrap what we\'re passing in inside of '
    '<span class="highlight-trigger font-medium underline decoration-brand-blue '
    '!cursor-help" style="display:inline-block;white-space:nowrap">花括号</span>, '
    '<code>{}</code>. Can you spot why that is?</p>'
)

PROPS_DST = (
    '<p metastring="">你可能已经注意到，有时候我们需要把传入的值用一对'
    '<span class="highlight-trigger font-medium underline decoration-brand-blue '
    '!cursor-help" style="display:inline-block;white-space:nowrap">花括号</span> '
    '<code>{}</code> 包起来。你能看出这是为什么吗？</p>'
)


def main() -> None:
    # --- Task 2: 007 props sentence ---
    text = PROPS_FILE.read_text(encoding="utf-8")
    if PROPS_SRC in text:
        text = text.replace(PROPS_SRC, PROPS_DST, 1)
        PROPS_FILE.write_text(text, encoding="utf-8")
        print(f"[007] props '花括号' sentence translated.")
    else:
        print(f"[007] !! props sentence not found, skipped.")

    # --- Task 1: Dashboard link in every lesson file ---
    total_files = 0
    total_hits = 0
    for path in sorted(ROOT.glob("0*.html")):
        txt = path.read_text(encoding="utf-8")
        new_txt, count = rewrite_dashboard(txt)
        if count > 0:
            path.write_text(new_txt, encoding="utf-8")
            total_files += 1
            total_hits += count
            print(f"  [{path.name}] rewrote {count} Dashboard link(s)")
    print(f"\nDashboard rewrites: {total_hits} link(s) across {total_files} files.")


if __name__ == "__main__":
    main()
