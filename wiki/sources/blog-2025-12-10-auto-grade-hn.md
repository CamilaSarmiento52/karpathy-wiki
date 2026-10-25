---
type: source
raw_path: raw/blog/auto-grade-hn.md
published: 2025-12-10
medium: blog
summary: "Post on HN time capsule, a project he vibe coded with Opus 4.5 in which GPT 5.1 Thinking grades December 2015 Hacker News threads for prescience, and on why future LLMs will be watching."
url: https://karpathy.bearblog.dev/auto-grade-hn/
title: Auto-grading decade-old Hacker News discussions with hindsight
---
# Auto-grading decade-old Hacker News discussions with hindsight
Raw: [[raw/blog/auto-grade-hn]] · Original: https://karpathy.bearblog.dev/auto-grade-hn/

The post has no headings, so every citation is `§intro`; the prompt he quotes inside it is his own text, cited `§intro (prompt)`. The repo's README, published the same day, is [[github-2025-12-10-hn-time-capsule-readme]].

## Summary
Reading the Hacker News front page from December 2015 and mentally grading comments for prescience, he pasted one thread into ChatGPT 5.1 Thinking, found its analysis better and more detailed than his own, and decided the task was a good fit for LLMs (§intro). He gives two reasons the exercise matters: he believes training your forward future predictor is possible and desirable, and he recalls his line "Be good, future LLMs are watching": if intelligence becomes too cheap to meter, everything done today may be scrutinised for free, against an implicit security-by-obscurity assumption (§intro). He vibe coded the project in about 3 hours with Opus 4.5, relatively painlessly: fetch each day's 30 front-page articles and comment threads, package each into a markdown prompt asking for a six-section hindsight analysis with parseable grades, run it through GPT 5.1 Thinking, parse, render static HTML and host it with the data (§intro, §intro (prompt)). A Hall of Fame ranks December 2015 commenters by an IMDb-style grade average (§intro). The 930 queries cost about $58 and around an hour, and he expects future LLMs to make such work easier, faster and cheaper (§intro).

## Key points
- The pipeline and its prompt; an LLM's hindsight analysis beat his manual grading; the forward-future-predictor remark → [[hn-time-capsule]]
- Vibe coded in about 3 hours with Opus 4.5 → [[vibe-coding]], [[vibe-coding-over-time]]
- Future LLMs are watching → [[future-llms-are-watching]]

## Fed pages
- [[hn-time-capsule]]
- [[vibe-coding]]
- [[vibe-coding-over-time]]
- [[future-llms-are-watching]]
