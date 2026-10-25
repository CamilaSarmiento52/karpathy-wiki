# Digest: hn-time-capsule README
- raw: raw/github/karpathy__hn-time-capsule.md · published: 2025-12-10 · medium: github · words: 515 (frontmatter); 538 by wc
- source slug: github-2025-12-10-hn-time-capsule-readme
- commit: ca02ebb4de5e953bf1629689abd1f82b454b6905

Locations: `§intro` (text under `# HN Time Capsule`), `§What it does`, `§Vibe code alert`, `§Setup`, `§Usage`, `§Data Directory Structure`, `§Files`, `§Example Output`, `§License`.

## Source page
```
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

Dated by the README's commit (ca02ebb).

## Summary
HN Time Capsule pulls the Hacker News front page from exactly 10 years ago, has an LLM analyse each article and discussion for prescience with hindsight, and generates an HTML report; it points to his blog post for context (§intro). Its five steps fetch the front page, fetch each article and its comments, generate prompts, parse the responses for each commenter's grade, and render an HTML summary (§What it does). The goal is to find which commenters were most prescient or most wrong over time; the more general idea, he says, is LLMs scouring past human artifacts and synthesising them into knowledge and insights (§What it does). He says 99% of it was vibe coded in a few hours with Opus 4.5 and that he does not intend to support it (§Vibe code alert). `pipeline.py` runs the stages together or one by one, with a date option and a cheaper model for testing; grades from A+ to F are aggregated into a Hall of Fame of prediction track records (§Usage, §Example Output).

## Key points
- Five-stage pipeline, per-article data directory, Hall of Fame → [[hn-time-capsule]]
- LLMs scouring past human artifacts into knowledge → [[hn-time-capsule]], [[llm-knowledge-bases]]
- 99% vibe coded with Opus 4.5 → [[vibe-coding]], [[vibe-coding-over-time]]

## Fed pages
- [[hn-time-capsule]]
- [[llm-knowledge-bases]]
- [[vibe-coding]]
- [[vibe-coding-over-time]]
```

## Candidates

### artifact: hn-time-capsule
- existing: no
- aliases: [HN Time Capsule, HN time capsule, hncapsule]
- frontmatter: repo_url https://github.com/karpathy/hn-time-capsule · language: Python (`uv run python pipeline.py`) · status: as with rendergit and reader3, not deprecated but unsupported.
- statements:
  - It pulls the HN front page from exactly 10 years ago, analyses articles and discussions with an LLM to evaluate prescience with hindsight, and generates an HTML report (§intro).
  - Steps: fetch the front page from 10 years ago; fetch each article's content and all its HN comments; generate prompts asking an LLM what happened with hindsight; parse responses for each commenter's grade; render an HTML summary (§What it does).
  - The goal is to find the most prescient and most wrong commenters over time and surface interesting decade-old predictions (§What it does).
  - `pipeline.py` has the stages fetch, prompt, analyze (which "costs money!"), parse and render, runnable all at once, individually, with `--limit` for testing or `--date` for a given day; `--model gpt-5-mini` uses a cheaper model for testing (§Usage). §Files also lists a `clean` stage (§Files).
  - Setup: `uv sync` and an OpenAI API key in `.env` (§Setup).
  - Per day it stores the front page, aggregated grades and the HTML report; per article, metadata, article text or fetch error, the comment tree, the full prompt, the LLM response and parsed grades (§Data Directory Structure).
  - The LLM summarises what happened over 10 years, awards "Most prescient" and "Most wrong", notes fun aspects and grades each commenter A+ to F on how their comments aged; grades aggregate into the Hall of Fame (§Example Output).
  - Licence MIT (§License).

### topic: llm-knowledge-bases (existing) — context, not evidence
- statement: he says the more general and interesting idea behind the repo is LLMs combing through past human artifacts on their own and turning them into knowledge and insight (§What it does).
- caveat: the topic is about an LLM compiling a markdown wiki of your sources (per the index). This README describes a grading pipeline, not a wiki. Recommend `context` with a **Note:**, not `sources`. No claim link.

### topic: vibe-coding (existing) and timeline: vibe-coding-over-time (existing)
- statement: 99% of the repo was vibe coded in a few hours with Opus 4.5; code is provided as is and unsupported (§Vibe code alert).
- timeline: same 2025-12-10 entry as the blog digest; cite both source pages.
- year-in-review link: the 2025-12-19 review names HN time capsule among projects he vibe coded as quick app demos (§5). Dates only.

## Quotes
- "evaluate prescience with the benefit of hindsight" (§intro)
- "find which HN commenters were most prescient or most wrong over time" (§What it does)
- "LLMs automatically scouring human artifacts from the past" (§What it does)
- "99% of this repo was vibe coded in a few hours with Opus 4.5." (§Vibe code alert)
- "Code is provided as is and I don't intend to support it." (§Vibe code alert)
- "track which HN accounts have the best prediction track records over time" (§Example Output)

## Notes for merge
- The README says "a few hours"; the blog says "about 3 hours". Not a conflict; cite each for its own wording.
- §What it does lists five steps (no "analyze" step by name; step 3 generates prompts, then parse), while §Usage has five stages including analyze, and §Files lists six (adds clean). Report each list as written.
- The README does not name GPT 5.1 Thinking; the blog does. The README's example cheaper model is gpt-5-mini.
- `your-key-here` is a placeholder; nothing to redact.
- The intro links the blog post (blog-2025-12-10-auto-grade-hn), same published date; link the two source pages, no order.
