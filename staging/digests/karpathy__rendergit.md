# Digest: rendergit README
- raw: raw/github/karpathy__rendergit.md · published: 2025-08-21 · medium: github · words: 316 (frontmatter); 339 by wc
- source slug: github-2025-08-21-rendergit-readme
- commit: 14d7a58c0f4d815a3447f25e9ef1088c7e9ade84

Locations: `§intro` (tagline and paragraph under `# rendergit`), `§Basic usage`, `§Features`,
`§Contributing`, `§License`.

## Source page
```
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

Dated by the README's commit (14d7a58).

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
- [[vibe-coding-over-time]]
```

## Candidates

### artifact: rendergit
- existing: no
- aliases: [render git]
- frontmatter: repo_url https://github.com/karpathy/rendergit · language Python (installed with uv or `pip install -e .`; Pygments for highlighting) · status: active is defensible (he keeps using it), but he says he does not intend to maintain it; see notes.
- statements:
  - Tagline: "Just show me the code." (§intro)
  - It flattens any GitHub repository into one static HTML page with syntax highlighting, Markdown rendering and sidebar navigation, for code review, exploration and Ctrl+F search across all files (§intro, §Features).
  - Usage: install with `uv tool install` or clone and `pip install -e .`, then run `rendergit <repo url>`; his example URL is nanoGPT (§Basic usage).
  - It clones the repo to a temporary directory, renders the source into a single temporary HTML file and opens it in the browser (§Basic usage).
  - Human View: syntax highlighting, sidebar navigation, "visual goodies"; LLM View: the whole codebase as raw CXML text to copy into Claude or ChatGPT for code analysis (§Basic usage, §Features).
  - It highlights code with Pygments, renders README and docs Markdown, skips binaries and oversized files, shows a directory tree at the top and file sizes in the sidebar, and works on mobile (§Features).
  - He vibe coded it a few months before this README, keeps using it very often, and does not really intend to maintain or support it (§Contributing).
  - Licence BSD0 (§License).
- relation: none to claim pages.

### topic: building-for-agents (existing) — the connection asked about
- Yes, it connects, with care about what the source says. The topic is his argument that infrastructure should be readable for LLMs as well as humans, and its page already cites him liking tools such as gitingest and DeepWiki that make a GitHub repo LLM-readable by changing the URL (youtube-2025-06-19-software-is-changing @36:40, @37:12). rendergit does the same job with an explicit two-audience design: a Human View and an LLM View of the same repo (§Basic usage, §Features).
- statement to add: his rendergit renders a repo two ways, a browsable Human View and an LLM View of the whole codebase as CXML text to paste into Claude or ChatGPT (github-2025-08-21-rendergit-readme §Features).
- caveat: the README says LLM, Claude and ChatGPT, not "agents", and gives no argument; it is an example, not a restatement of the thesis. Put it in `sources` with that one sentence, or in `context` with a **Note:** if merge reads the topic as strictly about agents.

### topic: vibe-coding (existing) and timeline: vibe-coding-over-time (existing)
- statement: he says he vibe coded rendergit, still uses it very often, and shared it without plans to maintain it (§Contributing).
- timeline entry: **2025-08-21** — Shares rendergit, a utility he vibe coded and keeps using, without plans to maintain it ([[github-2025-08-21-rendergit-readme]] §Contributing).
- relation to claims: none. It is not a position. **Note:** it sits between the weekend-projects claim (throwaway use) and later professional uses: a tool he uses often but will not maintain. That reading is mine; do not set `supports`/`extends` on it.
- Do not write "a few months ago" as a date; the README's own phrase can be quoted, but no date for the vibe coding session follows from it.

**Note (not proposed as a link):** the two views echo [[llm-gui]]'s point that text suits LLMs and visuals suit people; my reading only.

## Quotes
- "Just show me the code." (§intro)
- "Flatten any GitHub repository into a single, static HTML page" (§intro)
- "Perfect for code review, exploration, and an instant Ctrl+F experience." (§intro)
- "Copy the entire codebase as CXML text to paste into Claude, ChatGPT, etc." (§Basic usage)
- "I vibe coded this utility a few months ago" (§Contributing)
- "I don't super intend to maintain or support it though." (§Contributing)

## Notes for merge
- `status`: he keeps using it but does not intend to maintain or support it. `active` (not deprecated, in use) or `archived` (unmaintained) are both arguable; nothing says superseded. I lean `active` with a sentence quoting the maintenance disclaimer.
- `language`: Python is inferred from the pip/uv install and Pygments; the README does not say "Python". State it as the install method, or let merge check.
- CXML is named but not defined in the README; do not expand it.
- His usage example points at karpathy/nanogpt (lowercase in the uv example, nanoGPT in the pip example); a mention, not a link to [[nanogpt]]'s content.
- "BSD0 go nuts" is the licence line verbatim.
