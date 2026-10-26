---
type: claim
stated_on: 2026-03-20
confidence: stated
sources: ["[[talk-2026-03-20-skill-issue]]"]
context: ["[[blog-2025-11-17-verifiability]]"]
topic: "[[autoresearch]]"
supports: ["[[software-2-0-automates-what-you-can-verify]]"]
---
# Autoresearch suits tasks with objective metrics that are easy to evaluate, and not tasks without them
> "if you can't evaluate then you can't auto research it" — [[talk-2026-03-20-skill-issue]] @24:02

## Context
Asked what the implication is for other areas, his first caveat is that this is extremely well suited to anything with objective metrics that are easy to evaluate ([[talk-2026-03-20-skill-issue]] @23:29). Writing more efficient CUDA kernels is a perfect fit, because you want code with exactly the same behaviour that is much faster ([[talk-2026-03-20-skill-issue]] @23:29, @24:02). Many things will not fit, he says ([[talk-2026-03-20-skill-issue]] @24:02). [[autoresearch]] itself is "here's an objective, here's a metric, here's your boundaries" and go ([[talk-2026-03-20-skill-issue]] @17:32). Later he says LLM training fits the paradigm very well, with code to optimise and metrics to optimise against; an autonomous loop over those metrics would overfit to them, but the system could be used to devise more metrics ([[talk-2026-03-20-skill-issue]] @1:00:35, @1:01:07).

## Related claims
- Supports [[software-2-0-automates-what-you-can-verify]]: on 2025-11-17 he wrote that a task is optimisable when it is verifiable, resettable, efficient and rewardable, and that the more verifiable a task, the more amenable it is to automation ([[blog-2025-11-17-verifiability]] §intro); here autoresearch, automated research against a metric, is limited to what can be evaluated ([[talk-2026-03-20-skill-issue]] @24:02). **Note:** autoresearch is an agent editing training code against a metric, not RL on a model, so this is support for the verifiability condition, not for the RL mechanism ([[talk-2026-03-20-skill-issue]] @17:32).
