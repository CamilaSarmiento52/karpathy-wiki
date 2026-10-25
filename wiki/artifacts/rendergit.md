---
type: artifact
repo_url: https://github.com/karpathy/rendergit
language: Python
status: active
sources: ["[[github-2025-08-21-rendergit-readme]]"]
aliases: [render git]
---
# rendergit
His tool that flattens a GitHub repository into a single static HTML page with syntax highlighting, Markdown rendering and sidebar navigation, under the tagline "Just show me the code." ([[github-2025-08-21-rendergit-readme]] §intro).

## What it demonstrates
- **Who it is for.** People tired of clicking around the file hierarchies of GitHub repos who want all the code on one page, for code review, exploration and an instant Ctrl+F search across every file ([[github-2025-08-21-rendergit-readme]] §intro, §Features).
- **How it runs.** Install with `uv tool install` or clone and `pip install -e .`, then pass a repo URL; his example is nanoGPT ([[github-2025-08-21-rendergit-readme]] §Basic usage). It clones the repo to a temporary directory, renders the source into one temporary HTML file and opens it in the browser ([[github-2025-08-21-rendergit-readme]] §Basic usage).
- **Two views of one repo.** A Human View for browsing with syntax highlighting, sidebar navigation and "visual goodies", and an LLM View that gives the entire codebase as raw CXML text to copy into Claude, ChatGPT and the like for code analysis ([[github-2025-08-21-rendergit-readme]] §Basic usage, §Features).
- **Features.** Highlighting via Pygments, Markdown rendering for READMEs and docs, skipping of binaries and oversized files, a directory tree at the top, file sizes in the sidebar, and a layout that works on mobile ([[github-2025-08-21-rendergit-readme]] §Features).
- **Vibe coded, shared, not maintained.** He says he vibe coded it a few months before the README and keeps using it very often, so he is sharing it, but "I don't super intend to maintain or support it though." ([[github-2025-08-21-rendergit-readme]] §Contributing). The licence is BSD0 ([[github-2025-08-21-rendergit-readme]] §License).
- **Note:** `status: active` because he says he keeps using it and nothing marks it deprecated, despite the maintenance disclaimer; `language: Python` is inferred from the pip and uv install and Pygments, since the README does not name the language ([[github-2025-08-21-rendergit-readme]] §Basic usage, §Contributing).

## Related
- [[building-for-agents]] — the LLM View makes a repo readable to an LLM, like the gitingest and DeepWiki tools he praises
- [[vibe-coding]] — how he built it
- [[nanogpt]] — the repo in his usage example
