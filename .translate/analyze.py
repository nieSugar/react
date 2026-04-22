"""Analyze HTML file structure to find translatable text."""
import os
import re
import sys
from html.parser import HTMLParser
from collections import Counter

files = [
    "001 - Getting Started - ui.dev.html",
    "002 - Why React_ - ui.dev.html",
    "003 - Imperative vs Declarative Programming - ui.dev.html",
    "004 - Pure Functions - ui.dev.html",
    "005 - Components - ui.dev.html",
    "006 - JSX - ui.dev.html",
    "007 - Props - ui.dev.html",
    "008 - Elements vs Components - ui.dev.html",
    "009 - Elements vs Components - ui.dev + styles.css.html",
    "010 - Handling Events - ui.dev.html",
    "011 - Preserving Values with useState - ui.dev.html",
    "012 - Using useState - ui.dev.html",
    "013 - Why React Renders - ui.dev.html",
    "014 - Reality Check - ui.dev.html",
    "015 - Managing Effects - ui.dev.html",
    "016 - Managing Effects - Part 2 - ui.dev.html",
    "017 - Preserving Values with useRef - ui.dev.html",
    "018 - Teleportation with Context - ui.dev.html",
    "019 - Complex State with useReducer - ui.dev.html",
    "020 - Referential Equality and Why It Matters - ui.dev.html",
    "021 - Managing Advanced Effects - ui.dev.html",
    "022 - Abstracting Reactive Values with useEffectEvent - ui.dev.html",
    "023 - Creating Custom Hooks - ui.dev.html",
    "024 - Rebuilding useHooks - ui.dev.html"
]

base = "D:/Personal/Downloads/react"

class TextExtractor(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=False)
        self.skip_stack = []
        self.texts = []
        self.in_skip = 0
        self.current_tag = None
        self.tag_stack = []
        self.classes_stack = []

    def handle_starttag(self, tag, attrs):
        self.tag_stack.append(tag)
        attrs_d = dict(attrs)
        cls = attrs_d.get('class', '')
        self.classes_stack.append(cls)
        if tag in ('script', 'style', 'svg', 'noscript'):
            self.in_skip += 1

    def handle_endtag(self, tag):
        if tag in ('script', 'style', 'svg', 'noscript'):
            self.in_skip = max(0, self.in_skip - 1)
        if self.tag_stack:
            self.tag_stack.pop()
            self.classes_stack.pop()

    def handle_data(self, data):
        if self.in_skip:
            return
        s = data.strip()
        if not s:
            return
        # Skip mostly punctuation / code-like
        if len(s) < 2:
            return
        parent = self.tag_stack[-1] if self.tag_stack else ''
        cls = self.classes_stack[-1] if self.classes_stack else ''
        self.texts.append((parent, cls, s[:120]))


def analyze_file(path):
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    p = TextExtractor()
    try:
        p.feed(content)
    except Exception as e:
        print(f"  Parse error: {e}")
    return p.texts, len(content)


if __name__ == '__main__':
    total_size = 0
    for fname in files:
        path = os.path.join(base, fname)
        if not os.path.exists(path):
            print(f"MISSING: {fname}")
            continue
        size = os.path.getsize(path)
        total_size += size
        print(f"{fname}: {size/1024:.0f} KB")
    print(f"Total: {total_size/1024/1024:.1f} MB")
