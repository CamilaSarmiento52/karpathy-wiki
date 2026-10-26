---
type: artifact
repo_url: https://github.com/karpathy/reader3
language: Python
status: active
sources: ["[[github-2025-11-18-reader3-readme]]", "[[blog-2025-12-19-year-in-review-2025]]", "[[x-2025-11-18-reading-with-llms]]"]
aliases: [reader 3]
---
# reader3
His lightweight, self-hosted EPUB reader that shows a book one chapter at a time, which makes it easy to copy a chapter into an LLM and read along ([[github-2025-11-18-reader3-readme]] §intro).

## What it demonstrates
- **Reading together with an LLM.** His suggested flow: get EPUB books (Project Gutenberg has many), open them in the reader, copy text to your favourite LLM, and read together and along; the habit is [[read-with-an-llm]] ([[github-2025-11-18-reader3-readme]] §intro). The README links his X post of the same date on reading everything with LLMs in three passes ([[github-2025-11-18-reader3-readme]] §intro; [[x-2025-11-18-reading-with-llms]] #1).
- **Vibe coded, unsupported.** He says it was 90% vibe coded just to illustrate how easily one can read books together with LLMs; he will not support it in any way, provides it as is for other people's inspiration and does not intend to improve it ([[github-2025-11-18-reader3-readme]] §intro).
- **Change it with your LLM.** He says code is ephemeral now and libraries are over, so users should ask their LLM to change it however they like; see [[code-is-ephemeral-now-and-libraries-are-over]] ([[github-2025-11-18-reader3-readme]] §intro).
- **How it runs.** `uv run reader3.py dracula.epub` creates `dracula_data`, registering the book in the local library; `uv run server.py` serves the library at localhost:8123, and deleting a book's folder removes it ([[github-2025-11-18-reader3-readme]] §Usage). "It's not supposed to be complicated or complex." ([[github-2025-11-18-reader3-readme]] §Usage). The licence is MIT ([[github-2025-11-18-reader3-readme]] §License).
- **Note:** `status: active` because nothing marks it deprecated, despite his statement that he will not support or improve it, the same call as [[rendergit]]; `language: Python` is inferred from `uv run reader3.py` and `server.py`, since the README does not name the language ([[github-2025-11-18-reader3-readme]] §intro, §Usage).
- **Note:** the 2025-12-19 review lists reader3 among projects he vibe coded as quick app demos of something he wanted to exist; dates only ([[blog-2025-12-19-year-in-review-2025]] §5; [[github-2025-11-18-reader3-readme]] §intro).

## Related
- [[read-with-an-llm]] — the habit it serves
- [[vibe-coding]] — how he built it
- [[rendergit]] — another vibe-coded tool he shared without support
