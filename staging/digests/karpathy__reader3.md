# Digest: reader3 README
- raw: raw/github/karpathy__reader3.md · published: 2025-11-18 · medium: github · words: 215 (frontmatter); 238 by wc
- source slug: github-2025-11-18-reader3-readme
- commit: 64960f99d8d3c2eaaec56c6765b4c1aeae14c80b

Locations: `§intro` (text under `# reader 3`), `§Usage`, `§License`.

## Source page
```
---
type: source
raw_path: raw/github/karpathy__reader3.md
published: 2025-11-18
medium: github
summary: "README of reader3, a small self-hosted EPUB reader he mostly vibe coded to show how to read books one chapter at a time alongside an LLM."
url: https://github.com/karpathy/reader3
title: reader3 README
---
# reader3 README
Raw: [[raw/github/karpathy__reader3]] · Original: https://github.com/karpathy/reader3

Dated by the README's commit (64960f9).

## Summary
reader3 is a lightweight, self-hosted EPUB reader that shows a book one chapter at a time, so the chapter text is easy to copy into an LLM and read along with it; he suggests Project Gutenberg as a source of EPUBs (§intro). He says it was 90% vibe coded to illustrate how easily one can read books together with LLMs, linking his post on that habit (§intro). He will not support or improve it, offers it as inspiration, and says code is ephemeral now and libraries are over, so readers should ask their LLM to change it (§intro). Usage: run `reader3.py` on an EPUB to register it in a local library folder, then run `server.py` and browse the library on localhost (§Usage). He says it is not supposed to be complicated (§Usage).

## Key points
- A chapter-at-a-time EPUB reader for copy-pasting into an LLM → [[reader3]], [[read-with-an-llm]]
- 90% vibe coded, unsupported → [[vibe-coding]], [[vibe-coding-over-time]]
- Code is ephemeral, libraries are over → [[code-is-ephemeral-now-and-libraries-are-over]]

## Fed pages
- [[reader3]]
- [[read-with-an-llm]]
- [[vibe-coding]]
- [[vibe-coding-over-time]]
- [[code-is-ephemeral-now-and-libraries-are-over]]
```

## Candidates

### artifact: reader3
- existing: no
- aliases: [reader 3]
- frontmatter: repo_url https://github.com/karpathy/reader3 · language: Python (inferred from `uv run reader3.py` and `server.py`; the README does not say "Python") · status: `active` arguable (not deprecated) but he will not support or improve it; same call as [[rendergit]].
- statements:
  - A lightweight, self-hosted EPUB reader that lets you read EPUB books one chapter at a time, which makes it easy to copy a chapter into an LLM and read along (§intro).
  - His suggested flow: get EPUB books (Project Gutenberg has many), open them in the reader, copy text to your favourite LLM, and read together (§intro).
  - 90% vibe coded, to illustrate how easily one can read books together with LLMs (§intro).
  - He is not going to support it, provides it as is for inspiration, and does not intend to improve it (§intro).
  - Usage: `uv run reader3.py dracula.epub` creates `dracula_data`, registering the book in the local library; `uv run server.py` serves the library at localhost:8123; deleting a book's folder removes it (§Usage).
  - Licence MIT (§License).
- relation: none to claim pages.

### method: read-with-an-llm (existing)
- statement: reader3 exists to make the copy-paste step easy: it shows one chapter at a time so its text can be pasted into an LLM to read along (§intro).
- **Note:** the method page records that on 2025-02-27 he found the copy-paste back and forth clunky and knew of no tool for it (youtube-2025-02-27-how-i-use-llms @58:28, per that page). reader3 is his own tool for the paste step; it does not add highlight-and-ask. A connection, not something the README says.

### topic: vibe-coding (existing) and timeline: vibe-coding-over-time (existing)
- statement: he says reader3 was 90% vibe coded to illustrate an idea, and he will not support or improve it (§intro).
- timeline entry: **2025-11-18** — Shares reader3, 90% vibe coded, unsupported; says code is ephemeral now and libraries are over → [[code-is-ephemeral-now-and-libraries-are-over]] ([[github-2025-11-18-reader3-readme]] §intro)
- year-in-review link: the 2025-12-19 review lists reader3, llm-council and HN time capsule among projects he vibe coded as quick app demos ([[blog-2025-12-19-year-in-review-2025]] §5). Dates only.

### claim: code-is-ephemeral-now-and-libraries-are-over
- existing: no
- title: "Code is ephemeral now and libraries are over"; `stated_on: 2025-11-18`, `confidence: stated`, topic [[vibe-coding]].
- quote: "Code is ephemeral now and libraries are over" (§intro)
- statements:
  - Said as the reason he will not maintain reader3: users should ask their LLM to change the code however they like (§intro).
  - The same two sentences appear in the llm-council README (github-2025-11-22-llm-council-readme §Vibe Code Alert); a repeat in a second README, not independent evidence.
- relations:
  - **supports [[vibe-coding-will-terraform-software]]** (candidate): the 2025-12-19 review calls code "suddenly free, ephemeral, malleable, discardable after single use" and says vibe coding will terraform software ([[blog-2025-12-19-year-in-review-2025]] §5); the 2025-11-18 README says code is ephemeral and libraries are over (§intro). Same idea, two dates; not `extends` (the review adds jobs and professional use, the README adds nothing beyond it). Dates only.
  - **Note** to [[small-hackable-educational-code]]: that method is about code people read and learn from; here he tells users not to read but to ask an LLM to change it. Different purposes (a demo vs a teaching repo), not a contradiction; do not link.
  - Note for [[vibe-coding-is-for-throwaway-weekend-projects]]: none set; a shared, unsupported demo is consistent with it.

## Quotes
- "lets you read through EPUB books one chapter at a time" (§intro)
- "copy paste text around to your favorite LLM, and read together and along" (§intro)
- "This project was 90% vibe coded" (§intro)
- "I'm not going to support it in any way" (§intro)
- "Code is ephemeral now and libraries are over" (§intro)
- "It's not supposed to be complicated or complex." (§Usage)

## Notes for merge
- The H1 is "reader 3" with a space; the repo is reader3. Use `reader3` as slug, alias "reader 3".
- His link "read books together with LLMs" points to x.com/karpathy/status/1990577951671509438, the raw `raw/x/1990577951671509438.md` (same published date, 2025-11-18). Link the two source pages to each other; no order between them can be stated from dates.
- Dracula from Project Gutenberg is the example book; a mention.
- Port 8123 is in the README; uv is the package manager.
