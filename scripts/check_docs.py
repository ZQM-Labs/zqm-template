#!/usr/bin/env python3
"""Dependency-free documentation checks for ZQM repositories."""
from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
REPO = os.environ.get("GITHUB_REPOSITORY", "").lower()
errors: list[str] = []
warnings: list[str] = []

markdown_files = [
    p for p in ROOT.rglob("*.md")
    if ".git" not in p.parts and "node_modules" not in p.parts
]
readme = ROOT / "README.md"
if not readme.is_file():
    errors.append("Repository root README.md is missing.")
else:
    text = readme.read_text(encoding="utf-8")
    if len(text.strip()) < 200:
        errors.append("README.md is unexpectedly short; add purpose and usage context.")
    headings = {m.group(1).strip().lower() for m in re.finditer(r"^#{1,6}\s+(.+)$", text, re.M)}
    if not any(re.search(r"quick.?start|installation|getting started|setup", h) for h in headings):
        errors.append("README.md needs a Quickstart, Installation, Getting Started, or Setup section.")
    if not any(re.search(r"validation|tests?|testing|continuous integration|\bci\b", h) for h in headings):
        errors.append("README.md needs a Validation, Tests, Testing, or CI section.")

# Counts in prose drift quickly. Prefer generated inventories or omit counts.
count_pattern = re.compile(r"\b\d+\s+(?:public|private|archived)\s+(?:repos?|repositories)\b", re.I)
for path in markdown_files:
    text = path.read_text(encoding="utf-8", errors="replace")
    for line_no, line in enumerate(text.splitlines(), 1):
        if count_pattern.search(line) and not line.lstrip().startswith("<!--"):
            errors.append(f"{path.relative_to(ROOT)}:{line_no}: hard-coded repository count; generate it or remove it.")

# Validate relative Markdown links, including links to files in this repository.
link_pattern = re.compile(r"!?(?:\[[^\]]*\])\((<[^>]+>|[^)]+)\)")
for source in markdown_files:
    source_text = source.read_text(encoding="utf-8", errors="replace")
    for match in link_pattern.finditer(source_text):
        raw = match.group(1).strip().strip("<>")
        if not raw or raw.startswith("#"):
            continue
        parsed = urlsplit(raw)
        if parsed.scheme or parsed.netloc:
            continue
        target = unquote(parsed.path)
        if not target:
            target_path = source
        else:
            target_path = (source.parent / target).resolve()
        if not target_path.exists():
            line_no = source_text.count("\n", 0, match.start()) + 1
            errors.append(f"{source.relative_to(ROOT)}:{line_no}: broken relative link: {raw}")

# Catch badge URLs that look like this repository but use a different slug.
if REPO:
    owner, _, repo_name = REPO.partition("/")
    badge_pattern = re.compile(r"!\[[^\]]*\]\((https?://[^)]+)\)")
    for source in markdown_files:
        source_text = source.read_text(encoding="utf-8", errors="replace")
        for match in badge_pattern.finditer(source_text):
            url = match.group(1)
            parsed = urlsplit(url)
            path = parsed.path.lower()
            # Shields and GitHub Actions badges have a recognizable owner/repo pair.
            pair = re.search(r"/" + re.escape(owner) + r"/([^/]+)/actions(?:/|$)", path)
            if pair and pair.group(1) != repo_name:
                line_no = source_text.count("\n", 0, match.start()) + 1
                errors.append(
                    f"{source.relative_to(ROOT)}:{line_no}: workflow badge points at "
                    f"{owner}/{pair.group(1)}, but this repository is {REPO}."
                )

if warnings:
    for item in warnings:
        print(f"WARNING: {item}")
if errors:
    print("Documentation checks failed:")
    for item in errors:
        print(f" - {item}")
    sys.exit(1)

print(
    f"Documentation checks passed: {len(markdown_files)} Markdown files scanned; "
    "root README sections, relative links, repository counts, and workflow badge identities checked."
)
