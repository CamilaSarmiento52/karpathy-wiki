---
type: source
raw_path: raw/github/karpathy__hn-time-capsule.md
published: 2025-12-10
medium: github
summary: "README of hn-time-capsule, a vibe-coded five-stage pipeline that has an LLM grade decade-old Hacker News threads with hindsight and track commenters' prediction records."
url: https://github.com/karpathy/hn-time-capsule
title: hn-time-capsule README
---
# hn-time-capsule README
Raw: [[raw/github/karpathy__hn-time-capsule]] · Original: https://github.com/karpathy/hn-time-capsule

Dated by the README's commit (ca02ebb). Text under `# HN Time Capsule` is cited `§intro`. The README links his blog post of the same published date, [[blog-2025-12-10-auto-grade-hn]]; no order between them is stated.

## Summary
HN Time Capsule pulls the Hacker News front page from exactly 10 years ago, has an LLM analyse each article and discussion for prescience with hindsight, and generates an HTML report; it points to his blog post for context (§intro). Its five steps fetch the front page, fetch each article and its comments, generate prompts, parse the responses for each commenter's grade, and render an HTML summary (§What it does). The goal is to find which commenters were most prescient or most wrong over time; the more general idea, he says, is LLMs scouring past human artifacts and synthesising them into knowledge and insights (§What it does). He says 99% of it was vibe coded in a few hours with Opus 4.5 and that he does not intend to support it (§Vibe code alert). `pipeline.py` runs the stages together or one by one, with a date option and a cheaper model for testing; grades from A+ to F are aggregated into a Hall of Fame of prediction track records (§Usage, §Example Output).

## Key points
- Five-stage pipeline, per-article data directory, Hall of Fame → [[hn-time-capsule]]
- LLMs scouring past human artifacts into knowledge → [[hn-time-capsule]], [[llm-knowledge-bases]], [[future-llms-are-watching]]
- 99% vibe coded with Opus 4.5 → [[vibe-coding]], [[vibe-coding-over-time]]

## Fed pages
- [[hn-time-capsule]]
- [[llm-knowledge-bases]]
- [[future-llms-are-watching]]
- [[vibe-coding]]
- [[vibe-coding-over-time]]
