# Digest: Verifiability
- raw: raw/blog/verifiability.md · published: 2025-11-17 · medium: blog · words: 382 (frontmatter); 402 by wc
- source slug: blog-2025-11-17-verifiability

Locations: the post has no headings, so every citation is `§intro`.

## Source page
```
---
type: source
raw_path: raw/blog/verifiability.md
published: 2025-11-17
medium: blog
summary: "Short essay arguing that verifiability is to AI what specifiability was to 1980s computing: the best predictor of which tasks get automated, and the driver of the jagged frontier."
url: https://karpathy.bearblog.dev/verifiability/
title: Verifiability
---
# Verifiability
Raw: [[raw/blog/verifiability]] · Original: https://karpathy.bearblog.dev/verifiability/

## Summary
He takes AI as a new computing paradigm, which he calls the strongest of the historical analogies because both are about automating digital information processing (§intro). In the 1980s, he argues, the most predictive feature of whether computing would automate a job was specifiability, whether it followed a rote, easy-to-specify algorithm; he calls such hand-written programs Software 1.0 (§intro). With AI, programs are found by specifying an objective and searching program space with gradient descent, his Software 2.0, and the most predictive feature becomes verifiability: a verifiable task can be optimised directly or with reinforcement learning (§intro). He requires the environment to be resettable, efficient and rewardable, so that an AI can "practice" (§intro). Unverifiable tasks must rely on generalisation or weaker means such as imitation, which he says drives the jagged frontier of LLM progress: math, code and puzzle-like tasks move fast, creative, strategic and common-sense tasks lag (§intro).

## Key points
- Verifiable tasks are optimisable with RL; resettable, efficient, rewardable environments → [[rlvr]]
- Software 1.0 automates what you can specify, Software 2.0 what you can verify → [[software-3-0]], [[software-2-0-automates-what-you-can-verify]]
- Verifiability drives the jagged frontier → [[jagged-intelligence]], [[verifiability-drives-the-jagged-frontier]]
- A job-market forecast from AI as a computing paradigm → [[ai-and-the-economy]]
- Unverifiable tasks fall back on generalisation or imitation → [[llm-self-improvement]]

## Fed pages
- [[rlvr]]
- [[software-3-0]]
- [[jagged-intelligence]]
- [[ai-and-the-economy]]
- [[llm-self-improvement]]
- [[software-2-0-automates-what-you-can-verify]]
- [[verifiability-drives-the-jagged-frontier]]
```

## Candidates

### topic: rlvr (existing)
- existing: yes. Suggest adding aliases `verifiability`, `resettable efficient rewardable`.
- statements:
  - He says a verifiable task is optimisable directly or with reinforcement learning, and a neural net can then be trained to work extremely well; the question is how far an AI can "practice" it (§intro).
  - He lists three requirements for the environment: resettable (a new attempt can start), efficient (many attempts can be made) and rewardable (an automated process rewards each attempt) (§intro).
  - He does not use the word RLVR in this post (§intro).
- year-in-review link: the 2025-12-19 review describes RLVR as training against automatically verifiable rewards (§1) and links this post under §2 ([[blog-2025-12-19-year-in-review-2025]] §1, §2). Dates only.

### topic: software-3-0 (existing; aliases include Software 2.0, Software 1.0)
- statements:
  - He calls hand-written programs, which automate rote, easy-to-specify work such as typing, bookkeeping and human calculation, Software 1.0 (§intro).
  - He describes Software 2.0, pointing to his Software 2.0 blog post "from a while ago", as writing programs by specifying objectives such as classification accuracy or reward functions and searching program space with gradient descent (§intro).
  - He closes with the pair: Software 1.0 easily automates what you can specify, Software 2.0 what you can verify (§intro).
  - The post does not mention Software 3.0 or prompts (§intro).
- caveat: his Software 2.0 blog post is linked, not in raw/; do not date it ("from a while ago" is his phrase).

### topic: jagged-intelligence (existing)
- statements:
  - He says what is not verifiable has to come from the "neural net magic of generalization fingers crossed", or from weaker means like imitation, and that this drives the jagged frontier of LLM progress (§intro).
  - Verifiable tasks progress rapidly, possibly beyond top experts, with examples math, code, amount of time spent watching videos and puzzle-like tasks with correct answers; creative, strategic and real-world-knowledge, state, context and common-sense tasks lag by comparison (§intro).
- year-in-review link: on 2025-12-19 he writes that LLMs "spike" in capability near verifiable domains because those allow RLVR, and lists this post as further reading for that section ([[blog-2025-12-19-year-in-review-2025]] §2). Dates only. The benchmark argument (benchmarks are verifiable environments) is in the review, not in this post.

### topic: ai-and-the-economy (existing)
- statements:
  - He calls AI as a new computing paradigm the strongest historical analogy, above electricity or the industrial revolution, since both are about automating digital information processing (§intro).
  - He frames the post as forecasting job impact: in the 1980s you would ask whether a job was specifiable; now you would ask whether it is verifiable, and the more verifiable a task or job, the more amenable it is to automation (§intro).
- relation: **Note** to [[ai-will-not-show-up-as-a-jump-in-gdp]], whose context also treats AI as an extension of computing (talk-2025-10-17 @1:07:55, per that page). Shared framing only; the GDP claim is about growth, this post about which tasks get automated. No link.

### topic: llm-self-improvement (existing) — context or one sentence
- statement: for tasks that are not verifiable he names imitation as a weaker means (§intro).
- relation: see claim below.

### claim: software-2-0-automates-what-you-can-verify
- existing: no
- aliases: verifiability, verifiability as the predictor of automation
- title: "Software 2.0 easily automates what you can verify" (his closing line); `stated_on: 2025-11-17`, `confidence: stated`, topic [[software-3-0]] or [[rlvr]] (merge picks).
- quote: "Software 2.0 easily automates what you can verify." (§intro)
- statements:
  - In the new programming paradigm, he says, verifiability is the most predictive feature of a task or job, as specifiability was for 1980s computing (§intro).
  - The more verifiable a task is, the more amenable to automation in the new paradigm (§intro).
- relations:
  - **supports [[self-improvement-may-be-possible-in-narrow-domains]]** (candidate, weakest link): on 2023-11-23 he thought self-improvement may be possible in narrow domains with a fast, easy-to-evaluate reward (youtube-2023-11-23-intro-to-llms @40:27, per that page); here a task with an automated reward ("rewardable") is optimisable with RL and a net can be trained to work extremely well (§intro). Caveat: this post speaks of automation and optimisation, not "self-improvement"; if merge reads that as too different, make it a **Note** instead.
  - Not `extends` of anything: no existing claim page states the specify/verify contrast.

### claim: verifiability-drives-the-jagged-frontier
- existing: no
- title: "Verifiability is what drives the jagged frontier of LLM progress"; `stated_on: 2025-11-17`, `confidence: stated`, topic [[jagged-intelligence]].
- quote: "This is what's driving the \"jagged\" frontier of progress in LLMs." (§intro)
- statements: as on jagged-intelligence above (§intro).
- relations:
  - **supports [[rl-is-terrible-but-better-than-imitation]]** (candidate, weak): there RL beats the imitation that came before it (talk-2025-10-17 @41:33, per that page); here imitation is one of the "weaker means" left for unverifiable tasks (§intro). Only the ranking of imitation below RL is shared; the Nov post does not call RL terrible. Merge may prefer a **Note**.
  - **Note** (no link) to [[llm-research-summons-ghosts-not-animals]]: the review joins jaggedness and ghosts in one section (2025-12-19 §2); this post does not mention ghosts.
- merge option: fold this into jagged-intelligence as sentences and keep only the first claim, if one claim per short post is preferred.

## Quotes
- "I think the strongest analogy is that of AI as a new computing paradigm" (§intro)
- "the new most predictive feature to look at is verifiability" (§intro)
- "It's about to what extent an AI can \"practice\" something." (§intro)
- "the more amenable it is to automation in the new programming paradigm" (§intro)
- "This is what's driving the \"jagged\" frontier of progress in LLMs." (§intro)
- "Software 1.0 easily automates what you can specify." (§intro)
- "Software 2.0 easily automates what you can verify." (§intro)

## Notes for merge
- Frontmatter `published` is the string '2025-11-17'; use 2025-11-17.
- The three requirements are a bullet list in the raw ("resettable", "efficient", "rewardable"); "a lot attempts" is his typo, do not quote it.
- "amount of time spent watching videos" is one of his examples of verifiable tasks; keep it as written, do not interpret.
- He links his Software 2.0 blog post (medium.com), not in raw/; cite only this post.
- Year-in-review: 2025-12-19 §2 links this post as further reading and repeats the spike-near-verifiable-domains idea; §1 is the RLVR stage. Write dates only, no order words.
