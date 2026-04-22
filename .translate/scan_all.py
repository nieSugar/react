# -*- coding: utf-8 -*-
"""Scan ALL lesson HTML files for text segments that look like untranslated
English prose (>=20 chars, contains spaces/words, no Chinese characters).

Ignores <script>/<style>/<svg> blocks and obvious non-prose (URLs, class
names, filenames, etc.) via some simple heuristics.
"""
import re
from pathlib import Path

ROOT = Path(".")


def scan(path: Path):
    text = path.read_text(encoding="utf-8")
    # Strip opaque blocks
    text = re.sub(r"<script\b[^>]*>.*?</script>", "", text, flags=re.DOTALL | re.I)
    text = re.sub(r"<style\b[^>]*>.*?</style>", "", text, flags=re.DOTALL | re.I)
    text = re.sub(r"<svg\b[^>]*>.*?</svg>", "", text, flags=re.DOTALL | re.I)
    # Also strip <pre class="prism-code..."> code blocks AND <pre class="sp-...">
    text = re.sub(
        r'<pre\s[^>]*class="[^"]*(?:prism-code|sp-)[^"]*"[^>]*>.*?</pre>',
        "",
        text,
        flags=re.DOTALL | re.I,
    )
    # Strip <template> blocks (shadow DOM media player innards)
    text = re.sub(r"<template\b[^>]*>.*?</template>", "", text, flags=re.DOTALL | re.I)
    # Strip the file meta <head>
    text = re.sub(r"<head\b.*?</head>", "", text, flags=re.DOTALL | re.I)
    # Collect text between tags
    segs = re.findall(r">([^<]+)<", text)

    hits = []
    for s in segs:
        s2 = s.strip()
        if len(s2) < 20:
            continue
        # Skip if contains any Chinese
        if re.search(r"[\u4e00-\u9fff]", s2):
            continue
        # Must contain at least one ASCII space (prose)
        if " " not in s2:
            continue
        # Skip if looks like a URL / filename / code identifier
        if re.search(r"\b(?:https?:|www\.|\.html|\.css|\.js|\.png|\.jpg)\b", s2):
            continue
        # Must contain actual English words (>= 2 alphabet-only tokens)
        words = re.findall(r"[A-Za-z]{3,}", s2)
        if len(words) < 3:
            continue
        # Common "noise" segments to ignore
        if re.fullmatch(r"[A-Z][A-Z0-9_\- ]+", s2):
            continue
        hits.append(s2)
    return hits


def main():
    any_hits = False
    for p in sorted(ROOT.glob("0*.html")):
        hits = scan(p)
        # Dedup while preserving order
        seen = set()
        uniq = []
        for h in hits:
            if h not in seen:
                seen.add(h)
                uniq.append(h)
        if uniq:
            any_hits = True
            print(f"\n=== {p.name} ({len(uniq)} unique hit(s)) ===")
            for h in uniq:
                print(f"  - {h[:240]}")
    if not any_hits:
        print("ALL CLEAN -- no untranslated English prose detected.")


if __name__ == "__main__":
    main()
