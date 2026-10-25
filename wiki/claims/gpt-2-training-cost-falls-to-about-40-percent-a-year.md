---
type: claim
stated_on: 2026-01-31
confidence: stated
sources: ["[[github-2026-01-31-nanochat-beating-gpt-2]]"]
context: ["[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]"]
topic: "[[compute-efficiency]]"
---
# He estimates the cost to train GPT-2 falls each year to about 40% of the year before
> "the cost to train GPT-2 is falling to approximately 40% of the previous year" — [[github-2026-01-31-nanochat-beating-gpt-2]] §intro

## Context
When OpenAI released GPT-2 in February 2019, he writes, the largest model, 1.5B parameters, took 32 TPU v3 chips for "a bit over a week", about 168 hours; at $8/hour per TPU v3 he computes 32 × 168 × $8 = $43,000, citing a 2019 Reddit thread and the Hugging Face model card (comparison, his arithmetic on reported figures) ([[github-2026-01-31-nanochat-beating-gpt-2]] §intro). Seven years later nanochat beats GPT-2's performance on one 8×H100 node in about 3 hours, $73 at about $24/hour (estimate from the measured 3.04 hours and the rental price), which he calls a ~600× cost reduction, i.e. each year's cost about 40% of the previous year's (estimates) ([[github-2026-01-31-nanochat-beating-gpt-2]] §intro, §Reproduce). He hedges it the other way: "I think this is an understimate and that further improvements are still quite possible" ([[github-2026-01-31-nanochat-beating-gpt-2]] §intro). The gains, he says, come from everywhere: hardware (H100 against TPU v3), software (Flash Attention 3, torch.compile), algorithms (Muon, architectural changes) and data (FineWeb-edu) ([[github-2026-01-31-nanochat-beating-gpt-2]] §intro).

## Related claims
- None set. **Note:** [[progress-comes-from-everything-improving-together]] (2025-10-17) expects data, hardware, kernels and algorithms all to improve with none winning ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @26:18, @1:05:39); this post names the same four sources for nanochat's cost drop ([[github-2026-01-31-nanochat-beating-gpt-2]] §intro). The 2026-01-31 post is added there as a source; the map sets no relation between the two claims.
