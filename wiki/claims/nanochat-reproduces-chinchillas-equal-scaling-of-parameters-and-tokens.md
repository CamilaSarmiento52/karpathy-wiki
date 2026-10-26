---
type: claim
stated_on: 2026-01-07
confidence: stated
sources: ["[[github-2026-01-07-nanochat-miniseries-v1]]"]
topic: "[[scaling-laws]]"
---
# His nanochat sweeps reproduce Chinchilla's finding that compute-optimal parameters and tokens grow equally with compute
> "This is a remarkable result that we reproduce" — [[github-2026-01-07-nanochat-miniseries-v1]] §Details (Scaling laws)

## Context
From fixed-FLOP sweeps over depth he finds, "exactly like Chinchilla", that the optimal number of parameters and of tokens are each proportional to compute to the power of about 0.5; they sum to about 1 because C ≈ 6ND, and, more important to him, they are equal to each other ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (Scaling laws)). Parameters and tokens are therefore on an equal footing: doubling compute means about 1.41× more of each, and the optimal tokens-to-parameters ratio is a constant regardless of budget; he says "nature decided" compute-optimal Transformers fall on a straight line ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (Scaling laws)).

The reproduction is of the equal exponents, not of the constant: Chinchilla measures the ratio at 20 (comparison), and "In nanochat, when you do the fits you actually get something much lower: 8." (measured, fit) ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (Scaling laws)). He says this might come from nanochat specifics such as Muon or from the small model sizes ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (Scaling laws)). He reports that Kaplan et al. found a size-dependent ratio, incorrectly, because of a major learning-rate-decay bug that Chinchilla pointed out ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (Scaling laws)). The v1 models are trained at 8, unlike his earlier nanochat models at Chinchilla's 20, so they are less trained at each depth but compute optimal for their loss ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (Miniseries v1 CORE scores)). The post's extrapolation table is headed "12:1 D:N ratio", which the text does not reconcile with 8 ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (Miniseries v1 CORE scores)). The procedure is [[fit-your-own-scaling-law]] ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (Scaling laws)).

## Related claims
- None set. **Note:** [[scaling-offers-a-guaranteed-path-to-better-models]] is about how reliably scale improves models, not the ratio between parameters and data ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (Scaling laws)).
