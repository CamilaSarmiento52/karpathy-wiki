---
type: source
raw_path: raw/github/karpathy__rendergit.md
published: 2025-08-21
medium: github
summary: "README of rendergit, his vibe-coded tool that flattens a GitHub repo into one static HTML page with a Human view for browsing and an LLM view for pasting into a chatbot."
url: https://github.com/karpathy/rendergit
title: rendergit README
---
# rendergit README
Raw: [[raw/github/karpathy__rendergit]] · Original: https://github.com/karpathy/rendergit

Dated by the README's commit (14d7a58). Locations: `§intro` (tagline and the paragraph under the title), `§Basic usage`, `§Features`, `§Contributing`, `§License`.

## Summary
rendergit flattens any GitHub repository into a single static HTML page with syntax highlighting, Markdown rendering and sidebar navigation, pitched at people tired of clicking through file hierarchies and for code review, exploration and Ctrl+F search (§intro). It clones the repo to a temporary directory, renders the source into one temporary HTML file and opens it in the browser (§Basic usage). The page toggles between a Human View for browsing and an LLM View that gives the whole codebase as CXML text to paste into Claude, ChatGPT and similar (§Basic usage, §Features). It skips binaries and oversized files and adds a directory tree, file sizes and a mobile-friendly layout (§Features). He says he vibe coded it a few months earlier, keeps using it often, and is sharing it without intending to maintain or support it (§Contributing).

## Key points
- What the tool does and its two views → [[rendergit]]
- An LLM View that turns a repo into one pasteable text → [[building-for-agents]]
- A vibe-coded utility he keeps using → [[vibe-coding]]

## Fed pages
- [[rendergit]]
- [[building-for-agents]]
- [[vibe-coding]]
