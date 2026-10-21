---
type: topic
aliases: [RLVR, Reinforcement Learning from Verifiable Rewards]
first_seen: 2025-12-19
last_updated: 2025-12-19
sources: ["[[blog-2025-12-19-year-in-review-2025]]"]
related: ["[[jagged-intelligence]]"]
---
# RLVR
Reinforcement Learning from Verifiable Rewards: training LLMs against automatically checkable rewards such as math and code puzzles, which he calls the major new stage of 2025 ([[blog-2025-12-19-year-in-review-2025]] §1).

## What he says
Before 2025 the production recipe was pretraining, supervised finetuning and RLHF ([[blog-2025-12-19-year-in-review-2025]] §1). Under RLVR, models develop strategies that look like reasoning, because they must find what works for them through optimisation rather than imitate traces ([[blog-2025-12-19-year-in-review-2025]] §1).

Unlike the short SFT and RLHF stages, RLVR allows long optimisation against non-gameable rewards, and it took compute that labs had meant for pretraining ([[blog-2025-12-19-year-in-review-2025]] §1). It also added a new knob, test-time compute, scaled by letting models think longer ([[blog-2025-12-19-year-in-review-2025]] §1). He names o1 as the first RLVR model and o3 as the point where the difference became obvious ([[blog-2025-12-19-year-in-review-2025]] §1).

## Related
- [[jagged-intelligence]] — RLVR makes capability spike near verifiable domains
