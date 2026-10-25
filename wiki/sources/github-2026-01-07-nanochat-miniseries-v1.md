---
type: source
raw_path: raw/github/karpathy__nanochat__discussion-420.md
published: 2026-01-07
medium: github
summary: "His nanochat miniseries v1: eleven compute-optimal models, d10 to d20, trained in about 4 hours for about $100, with his own scaling-law sweeps reproducing Chinchilla's equal exponents but an optimal tokens-to-parameters ratio near 8, compared with GPT-2 and estimated GPT-3 scores on the CORE metric rather than validation loss."
url: https://github.com/karpathy/nanochat/discussions/420
title: "[Jan 7 2026] nanochat miniseries v1"
---
# [Jan 7 2026] nanochat miniseries v1
Raw: [[raw/github/karpathy__nanochat__discussion-420]] · Original: https://github.com/karpathy/nanochat/discussions/420

Text before `## Details` is cited `§intro` with its bold label, e.g. `§intro (Why miniseries)`; text under Details as `§Details (<label>)`. The raw file is his post only. Number tags: measured (his run, including values read off his own fits, marked "fit"), target, comparison (someone else's figure or a baseline), setting, estimate (extrapolation or arithmetic). **Inconsistency kept:** the text gives the fitted and used tokens-to-parameters ratio as 8, while the header of the extrapolation table says "12:1 D:N ratio" (§Details (Scaling laws), §Details (Miniseries v1 CORE scores)); the post does not reconcile them and the wiki does not either.

## Summary
He argues you optimise not one model but a family set by one compute dial, which lets you do the scaling-law science that makes a big run's extrapolation trustworthy; in nanochat the dial is depth, and he returns to pretraining after a first release that covered the whole pipeline (§intro (Why miniseries), §intro (Miniseries v1)). Miniseries v1 is eleven models, d10 to d20, trained back to back in about 4 hours for about $100 on one 8×H100 node, whose loss-against-FLOPs curves should not cross if the scaling is right (§intro (Miniseries v1)). He compares them with GPT-2 and GPT-3 on the DCLM CORE metric, which he reimplemented as one dependency-free file, not on validation loss, which he calls subtle and deceiving (§intro (Comparison to GPT-2/GPT-3 miniseries)). Fixed-FLOP sweeps over depth give U-shaped curves whose minima reproduce Chinchilla's finding that optimal parameters and tokens both grow as about the square root of compute, but with an optimal tokens-to-parameters ratio near 8 rather than 20 (§Details (Scaling laws)). He calculates GPT-2 CORE scores by running the released models, estimates GPT-3's from six overlapping tasks, and extrapolates a fit to the depth and cost each would take, with a warning not to read too much into it (§Details (GPT-2 / GPT-3 CORE scores), §Details (Miniseries v1 CORE scores)).

## Key points
- Optimise a family of models on one compute dial; depth as nanochat's dial; d10–d20 in ~4 h, ~$100 → [[nanochat]], [[scaling-laws]]
- Fixed-FLOP depth sweeps, U-shapes, fitted exponents, D:N ≈ 8 against Chinchilla's 20; Chinchilla over Kaplan → [[scaling-laws]], [[fit-your-own-scaling-law]]
- Equal exponents reproduced; constant optimal ratio → [[nanochat-reproduces-chinchillas-equal-scaling-of-parameters-and-tokens]]
- Validation loss is deceiving; only actual metrics are comparable; modded-nanogpt's B=1 → [[only-actual-metrics-are-real-and-comparable]], [[llm-evaluation]]
- CORE in one dependency-free file; GPT-2 CORE calculated, GPT-3 CORE estimated → [[llm-evaluation]], [[reproduce-a-published-model]]
- FLOPs per token 6N plus attention; batch a little large FLOP-wise → [[compute-efficiency]]
- Warmdown 0.2 → 0.4, embedding LR nudge, sequence 2048, batch 0.5M → [[gradient-descent]]
- d12 favourite, GPT-1 size, ~6 minutes → [[quick-experiment-loop]]
- Simplified DCLM's bloated CORE code → [[small-hackable-educational-code]]

## Fed pages
- [[nanochat]]
- [[scaling-laws]]
- [[fit-your-own-scaling-law]]
- [[nanochat-reproduces-chinchillas-equal-scaling-of-parameters-and-tokens]]
- [[only-actual-metrics-are-real-and-comparable]]
- [[llm-evaluation]]
- [[reproduce-a-published-model]]
- [[compute-efficiency]]
- [[gradient-descent]]
- [[quick-experiment-loop]]
- [[small-hackable-educational-code]]
