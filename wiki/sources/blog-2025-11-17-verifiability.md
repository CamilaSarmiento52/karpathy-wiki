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

The post has no headings; every citation is `§intro`.

## Summary
He takes AI as a new computing paradigm, which he calls the strongest of the historical analogies because both are about automating digital information processing (§intro). In the 1980s, he argues, the most predictive feature of whether computing would automate a job was specifiability, whether it followed a rote, easy-to-specify algorithm; he calls such hand-written programs Software 1.0 (§intro). With AI, programs are found by specifying an objective and searching program space with gradient descent, his Software 2.0, and the most predictive feature becomes verifiability: a verifiable task can be optimised directly or with reinforcement learning (§intro). He requires the environment to be resettable, efficient and rewardable, so that an AI can "practice" (§intro). Unverifiable tasks must rely on generalisation or weaker means such as imitation, which he says drives the jagged frontier of LLM progress: math, code and puzzle-like tasks move fast, creative, strategic and common-sense tasks lag (§intro). The 2025-12-19 year in review links this post as further reading for its jagged-intelligence section; see [[blog-2025-12-19-year-in-review-2025]].

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
