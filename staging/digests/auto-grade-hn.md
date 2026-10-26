# Digest: Auto-grading decade-old Hacker News discussions with hindsight
- raw: raw/blog/auto-grade-hn.md · published: 2025-12-10 · medium: blog · words: 1026 (frontmatter); 1052 by wc
- source slug: blog-2025-12-10-auto-grade-hn

Locations: the post has no headings, so every citation is `§intro`. The quoted prompt (raw lines 30–55) is his own text inside the post; cite it `§intro (prompt)`.

## Source page
```
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

## Summary
Reading the Hacker News front page from December 2015 and mentally grading comments for prescience, he pasted one thread into ChatGPT 5.1 Thinking, found its analysis better and more detailed than his own, and decided the task was a good fit for LLMs (§intro). He gives two reasons the exercise matters: he believes training your forward future predictor is possible and desirable, and he recalls his line "Be good, future LLMs are watching": if intelligence becomes too cheap to meter, everything done today may be scrutinised for free, against an implicit security-by-obscurity assumption (§intro). He vibe coded the project in about 3 hours with Opus 4.5, relatively painlessly: fetch each day's 30 front-page articles and comment threads, package each into a markdown prompt asking for a six-section hindsight analysis with parseable grades, run it through GPT 5.1 Thinking, parse, render static HTML and host it with the data (§intro, §intro (prompt)). A Hall of Fame ranks December 2015 commenters by an IMDb-style grade average (§intro). The 930 queries cost about $58 and around an hour, and he expects future LLMs to make such work easier, faster and cheaper (§intro).

## Key points
- The pipeline and its prompt → [[hn-time-capsule]]
- Vibe coded in about 3 hours with Opus 4.5 → [[vibe-coding]], [[vibe-coding-over-time]]
- Future LLMs are watching → [[future-llms-are-watching]]
- An LLM's hindsight analysis beat his manual grading → [[hn-time-capsule]]

## Fed pages
- [[hn-time-capsule]]
- [[vibe-coding]]
- [[vibe-coding-over-time]]
- [[future-llms-are-watching]]
```

## Candidates

### artifact: hn-time-capsule
- existing: no (the README digest proposes it too; this post is a second source)
- aliases: [HN time capsule, HN Time Capsule, hncapsule]
- statements:
  - The idea came from an HN thread where Gemini 3 hallucinated the front page of 10 years ahead, and a comment linking the front page from exactly 10 years earlier, December 2015 (§intro).
  - He pasted one article and comment thread into ChatGPT 5.1 Thinking and got an analysis of what people thought and what happened, better and more detailed than his manual grading; he wanted an excuse to vibe code with the newly released Opus 4.5 (§intro).
  - Plan: all December 2015 front pages, 31 days of 30 articles, analysed by ChatGPT 5.1 Thinking and presented for historical reading (§intro).
  - Steps: given a date, download the front page's 30 articles; for each, download the article and full comment thread via the Algolia API; package everything into a markdown prompt; submit to GPT 5.1 Thinking via the OpenAI API; collect and parse; render static HTML; host the pages on his site and the intermediate data as data.zip under the same URL prefix (§intro).
  - His prompt asks for six sections: summary; what happened (research briefly); "Most prescient" and "Most wrong" awards; other notable aspects; grades for specific people; a final 0–10 interestingness score, with exact formats for sections 5 and 6 because he parses them programmatically to accumulate grades per account over time (§intro (prompt)).
  - The Hall of Fame sorts December 2015 commenters by IMDb-style score of their grade point average; he congratulates the top ten by handle and notes the noise at the bottom (§intro).
  - 31 × 30 = 930 LLM queries cost about $58 and took around an hour (§intro).
  - Example threads he picks: Swift going open source, Figma's launch, the original OpenAI announcement, geohot building Comma, a SpaceX Orbcomm-2 webcast, Theranos struggles (§intro).
- relation: none to claim pages.

### claim: future-llms-are-watching
- existing: no
- title: "Future LLMs are watching, so everything done today may be scrutinised"; better close to his words: "Everything we do today might be scrutinized in great detail in the future". `stated_on: 2025-12-10`, `confidence: stated` (hedged with "might" and a conditional, "if intelligence really does become too cheap to meter"; keep both in the page).
- quote: "Be good, future LLMs are watching" (§intro) — he quotes his own tweets; or "Everything we do today might be scrutinized in great detail in the future" (§intro)
- statements:
  - He was reminded of his tweets that said "Be good, future LLMs are watching" and focuses on the idea that future LLMs are watching (§intro).
  - Everything we do today might be scrutinised in great detail in the future because doing so will be "free" (§intro).
  - Much current behaviour, he thinks, makes an implicit "security by obscurity" assumption; if intelligence becomes too cheap to meter, a perfect reconstruction and synthesis of everything becomes possible (§intro).
  - LLMs are watching, or humans using them might be; best to be good (§intro).
- relations: none to an existing claim page. **Note** to [[llm-knowledge-bases]] (an LLM compiling your sources into a wiki, per the index): the README phrase about LLMs scouring past human artifacts is closer; connection only.
- caveat: his "tweets" are not dated in the post and are not in raw/ as far as the index shows; do not date them or write "earlier".

### claim candidate (weak; merge may fold into hn-time-capsule): training-a-forward-future-predictor-is-possible-and-desirable
- title: "He believes it is quite possible and desirable to train your forward future predictor"; `stated_on: 2025-12-10`, `confidence: stated`.
- quote: "quite possible and desirable to train your forward future predictor" (§intro)
- statement: he gives it as the first of two reasons the exercise is interesting, with "given training and effort" (§intro). He does not explain whose predictor (a person's or a model's); do not resolve it.
- relations: none. Recommend folding into the artifact page as one sentence.

### topic: vibe-coding (existing) and timeline: vibe-coding-over-time (existing)
- statements:
  - He says vibe coding the project was relatively painless and took about 3 hours with Opus 4.5, with a few hiccups but overall very impressive (§intro).
  - He calls the GitHub code "My code (wait, Opus' code?)" (§intro).
- timeline entry: **2025-12-10** — Vibe codes HN time capsule in about 3 hours with Opus 4.5, "relatively painless" ([[blog-2025-12-10-auto-grade-hn]] §intro; [[github-2025-12-10-hn-time-capsule-readme]] §Vibe code alert)
- relations:
  - **Note** to [[deploying-a-vibe-coded-app-is-harder-than-writing-it]]: MenuGen's deployment was the slog (2025-04-27, per that page); this project renders static HTML hosted on his own site, and he calls it relatively painless. Different kinds of app; no contradiction, no link.
  - **Note** to [[vibe-coding-will-terraform-software]]: the 2025-12-19 review lists HN time capsule among his vibe-coded quick app demos (§5). Dates only.

### method candidate considered: LLM batch-analysis pipeline
- Try the task by hand in a chat, then script fetch → prompt → model → parse → render, with a fixed output format for parsing (§intro, §intro (prompt)). One project only; recommend sentences on [[hn-time-capsule]] rather than a method page. If merge wants a method link, [[make-it-work-then-make-it-cheap]] is the nearest (a capable model first), but this post does not move to a cheaper model; the README's gpt-5-mini is for testing. No link.

## Quotes
- "an LLM might actually be a lot better at this task" (§intro)
- "I realized that this task is actually a really good fit for LLMs" (§intro)
- "quite possible and desirable to train your forward future predictor" (§intro)
- "Be good, future LLMs are watching" (§intro)
- "Everything we do today might be scrutinized in great detail in the future" (§intro)
- "make an implicit \"security by obscurity\" assumption" (§intro)
- "LLMs are watching (or humans using them might be)." (§intro)
- "Best to be good." (§intro)
- "relatively painless and took about 3 hours with Opus 4.5" (§intro)
- "(wait, Opus' code?)" (§intro)
- "Let's use our benefit of hindsight now in 6 sections:" (§intro (prompt))
- "cost about $58 and somewhere around ~1 hour" (§intro)

## Notes for merge
- "hickups" is his spelling (hiccups); do not quote that span.
- "Yesterday" in the first paragraph is relative to the post; do not turn it into a date beyond what the post links (the HN front page of 2015-12-09 is the linked page, and the thread is item 46205632).
- He names "ChatGPT 5.1 Thinking" and "GPT 5.1 Thinking" interchangeably; the model was used via the OpenAI API.
- The Hall of Fame names ten HN accounts; there is no need to list them in the wiki.
- data.zip is deliberately not linked; do not construct its URL.
- Intro says "31 days, 30 articles per day"; the cost line repeats 31 × 30 = 930. Consistent.
- He says "~1 hour" for the 930 queries and "about 3 hours" for the coding; keep them apart.
