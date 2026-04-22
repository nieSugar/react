"""Extract translatable text from an HTML file for inspection."""
import os
import re
import sys
import json
from html.parser import HTMLParser

base = "D:/Personal/Downloads/react"


class TextExtractor(HTMLParser):
    SKIP_TAGS = {'script', 'style', 'svg', 'noscript', 'code', 'pre'}

    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.texts = []
        self.skip_depth = 0
        self.tag_stack = []

    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag)
        if tag in self.SKIP_TAGS:
            self.skip_depth += 1

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if self.tag_stack and self.tag_stack[-1] == tag:
            self.tag_stack.pop()
        if tag in self.SKIP_TAGS:
            self.skip_depth = max(0, self.skip_depth - 1)

    def handle_data(self, data):
        if self.skip_depth:
            return
        s = data
        stripped = s.strip()
        if not stripped:
            return
        # Only English-looking text
        if not re.search(r'[A-Za-z]', stripped):
            return
        # Skip single words that look like CSS/JS names
        parent = self.tag_stack[-1] if self.tag_stack else ''
        self.texts.append((parent, stripped))


def extract(path):
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    p = TextExtractor()
    p.feed(content)
    return p.texts


if __name__ == '__main__':
    fname = sys.argv[1] if len(sys.argv) > 1 else "007 - Props - ui.dev.html"
    path = os.path.join(base, fname)
    texts = extract(path)
    print(f"Total text fragments: {len(texts)}")
    # print only first 200 non-trivial
    shown = 0
    for parent, t in texts:
        if len(t) < 3:
            continue
        print(f"[{parent}] {t[:200]}")
        shown += 1
        if shown >= 150:
            break
