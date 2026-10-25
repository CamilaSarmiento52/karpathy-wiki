# Digest: [Jan 7 2026] nanochat miniseries v1
- raw: raw/github/karpathy__nanochat__discussion-420.md · published: 2026-01-07 · medium: github · words: 3176 (frontmatter)
- source slug: github-2026-01-07-nanochat-miniseries-v1

Number tags: **[measured]** his reported result from a run (including values read off his own
fits to his runs, marked "fit"); **[target]** a goal; **[comparison]** someone else's figure or a
baseline (GPT-2/GPT-3 scores, Chinchilla's constant, rental price); **[setting]** a configuration
value he chose; **[estimate]** extrapolation or arithmetic in place of a run.

Headings: the text before `## Details` is `§intro`, organised by bold run-in labels; cite as
`§intro (Why miniseries)`, `§intro (Miniseries v1)`, `§intro (Comparison to GPT-2/GPT-3 miniseries)`.
Under `## Details` the bold labels are `Scaling laws`, `Hyperparameter sweeps`,
`GPT-2 / GPT-3 CORE scores`, `Miniseries v1 CORE scores`; cite as `§Details (Scaling laws)` etc.
Two Python docstrings in §Details (Scaling laws) are his code comments. The raw file is his post only.

## Source page
```
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

Text before `## Details` is cited `§intro` with its bold label; text under Details as `§Details (<label>)`.

## Summary
He argues you optimise not one model but a family set by one compute dial, which lets you do the scaling-law science that makes a big run's extrapolation trustworthy; in nanochat the dial is depth, and he returns to pretraining after a first release that covered the whole pipeline (§intro (Why miniseries), §intro (Miniseries v1)). Miniseries v1 is eleven models, d10 to d20, trained back to back in about 4 hours for about $100 on one 8×H100 node, whose loss-against-FLOPs curves should not cross if the scaling is right (§intro (Miniseries v1)). He compares them with GPT-2 and GPT-3 on the DCLM CORE metric, which he reimplemented as one dependency-free file, not on validation loss, which he calls subtle and deceiving (§intro (Comparison to GPT-2/GPT-3 miniseries)). Fixed-FLOP sweeps over depth give U-shaped curves whose minima reproduce Chinchilla's finding that optimal parameters and tokens both grow as about the square root of compute, but with an optimal tokens-to-parameters ratio near 8 rather than 20 (§Details (Scaling laws)). He calculates GPT-2 CORE scores by running the released models, estimates GPT-3's from six overlapping tasks, and extrapolates a fit to the depth and cost each would take, with a warning not to read too much into it (§Details (GPT-2 / GPT-3 CORE scores), §Details (Miniseries v1 CORE scores)).

## Key points
- Optimise a family of models on one compute dial; depth as nanochat's dial; d10–d20 in ~4 h, ~$100 → [[nanochat]], [[scaling-laws]]
- Fixed-FLOP depth sweeps, U-shapes, fitted exponents, D:N ≈ 8 against Chinchilla's 20; Chinchilla over Kaplan → [[scaling-laws]], [[fit-your-own-scaling-law]]
- Equal exponents reproduced; constant optimal ratio → [[nanochat-reproduces-chinchillas-equal-scaling-of-parameters-and-tokens]]
- Validation loss is deceiving; only actual metrics are comparable; modded-nanogpt's B=1 → [[only-actual-metrics-are-real-and-comparable]], [[llm-evaluation]]
- CORE in one dependency-free file; GPT-2 CORE calculated, GPT-3 CORE estimated → [[llm-evaluation]], [[reproduce-a-published-model]]
- FLOPs per token 6N plus attention; parameters counted Chinchilla's way → [[compute-efficiency]]
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
```

## Candidates

### artifact: nanochat
- existing: yes
- statements:
  - For the first public release his focus was the end-to-end pipeline; he is now coming back to flesh out the parts he sped through, starting with pretraining, which he calls computationally heavy and critical as the foundation of intelligence and knowledge (§intro (Why miniseries)).
  - Depth is nanochat's single dial: it sets channels through a constant aspect ratio, hence parameters and FLOPs per token, the optimisation hyperparameters (the learning rate in particular), and through scaling laws the training horizon for a compute-optimal model (§intro (Miniseries v1)).
  - `miniseries.sh` sweeps d10 to d20; all fit on one 8×H100 node at a batch of 2^19 = 524,288 tokens without gradient accumulation, though nanochat supports it and he has trained larger models such as d34 (§intro (Miniseries v1)). [524,288: setting]
  - The 11 models took about 4 hours back to back on his 8×H100 node, about $100 in total (§intro (Miniseries v1)). [~4 h: measured; ~$100: estimate at $24/h]
  - To turn time into dollars, multiply hours by $24, i.e. $3 per GPU-hour × 8 GPUs (§intro (Comparison to GPT-2/GPT-3 miniseries)). [comparison, rental price]
  - The goal for miniseries v2 is to optimise the pretraining code further and lift, ideally tilt, the CORE-versus-cost line (§intro (Comparison to GPT-2/GPT-3 miniseries)). [target]
  - v1 models use a D:N ratio of 8 and are less trained at each depth than his earlier nanochat models, which used Chinchilla's 20, but compute optimal for their loss (§Details (Miniseries v1 CORE scores)). [settings]
- **Cost/time to GPT-2 for the series (estimate):** the extrapolation table puts GPT-2 XL's CORE 0.257 at d38, 2.2B params, 17.8B tokens, 2.9e20 FLOPs, 22.7 hours and $546 on 8×H100 (§Details (Miniseries v1 CORE scores)). [estimate, from a fit to d12–d20, assuming d20's utilisation and $3/GPU/h; table header says "12:1 D:N ratio"]. Record with its date; it is a projection under compute-optimal training, not a run.

### topic: scaling-laws
- existing: yes (last_updated 2024-09-05; this source would make it 2026-01-07)
- aliases to add: Chinchilla, compute-optimal, tokens-to-parameters ratio, D:N ratio, target_param_data_ratio, Kaplan
- statements:
  - The right way to think about LLMs, he says, is optimising a family of models controlled by one dial, the compute you spend, for monotonically better results; this enables careful scaling-law science and the confidence that the big run's extrapolation will pay off (§intro (Why miniseries)).
  - If code, architecture, optimisation and scaling laws are right, the curves of the miniseries should not intersect; each is the unique compute-optimal way to a target loss (§intro (Miniseries v1)).
  - At this small scale nanochat is in the infinite-data regime: no overfitting, train loss about equal to validation loss, and validation loss keeps falling as you train longer, so "how long to train a d12" is the wrong question; the real one is, for a FLOP budget, small model long or big model short (§Details (Scaling laws)).
  - With `--target_flops` fixed (e.g. 3e18) and several depths, iterations scale automatically; one depth in between (d16 at 3e18) reaches the lowest loss, and repeating for several budgets gives "surprisingly nice U shapes" (§Details (Scaling laws)). [3e18: setting; d16: measured]
  - Fit optima: 1e18 FLOPs → 137M params, 1.12B tokens, ratio 8.2, val bpb 0.9781; 3e18 → 240M, 1.88B, 8.1, 0.9202; 6e18 → 330M, 2.71B, 8.5, 0.8874 (§Details (Scaling laws)). [measured, fit]
  - Like Chinchilla, optimal parameters and tokens both scale as compute to about the 0.5, summing to about 1 because C ≈ 6ND; equal exponents mean the optimal D:N ratio is constant regardless of budget (§Details (Scaling laws)).
  - Chinchilla measures that constant at 20; nanochat's fits give much lower, 8, which he says might come from nanochat specifics such as Muon or from the small model sizes (§Details (Scaling laws)). [20: comparison; 8: measured, fit; reasons hedged]
  - He reports that Kaplan et al.'s scaling-law paper found a size-dependent ratio, incorrectly, because of a major bug in learning-rate decay, as Chinchilla pointed out (§Details (Scaling laws)). This is his report of the two papers.
  - His code comment says his own nanochat experiments confirm that counting all parameters, Chinchilla's way, gives the much cleaner scaling law than Kaplan's exclusion of embeddings (§Details (Scaling laws)).
  - Training length then follows: N × 8 = D tokens, divided by the ~0.5M batch, gives the iterations (§Details (Scaling laws)).
  - A fit over d12+ gives `CORE = 1.0000 - 3.7555 * FLOPs^(-0.0344)`, used to extrapolate to GPT-2 and GPT-3 (§Details (Miniseries v1 CORE scores)). [estimate, fit]
  - He warns not to read much into the extrapolation: many orders of magnitude from few points, and an optimistic assumption of d20's utilisation at scale; as a sanity check, it predicts 5.7e23 FLOPs for GPT-3 against about 3e23 for the real run (§Details (Miniseries v1 CORE scores)). [5.7e23: estimate; ~3e23: comparison]
- relation: topic-level. **Note:** the 2025-11-20 d34 post calls Chinchilla's 20 "compute optimal" ([[github-2025-11-20-nanochat-d34-model]] §intro), and the 2026-01-31 post measures about 10 ([[github-2026-01-31-nanochat-beating-gpt-2]] §What Worked). Record each with its date and code state.

### method: fit-your-own-scaling-law
- existing: no (no scaling or compute-optimal method in `wiki/index/methods.md`)
- aliases: compute-optimal sweep, IsoFLOP sweep (not his term; do not add unless merge wants it), scaling-law sweep
- proposed steps:
  1. Count FLOPs per token and parameters with explicit formulas (§Details (Scaling laws)).
  2. Fix a FLOP budget and train several depths to exactly that budget (§Details (Scaling laws)).
  3. Find the depth with the lowest loss at each budget (§Details (Scaling laws)).
  4. Repeat for a few budgets and fit the optima (§Details (Scaling laws)).
  5. Read the optimal tokens-to-parameters ratio off the fit and set training length from it (§Details (Scaling laws)).
  6. Check that the resulting family's curves do not cross (§intro (Miniseries v1)).
- statements: as on [[scaling-laws]] above. The 2026-01-31 post adds "It's important to do the actual experiment on your own network" ([[github-2026-01-31-nanochat-beating-gpt-2]] §What Worked).
- merge option: keep as a section of [[scaling-laws]] if a method page seems too fine-grained; the steps are his procedure, not a single idea, so a method fits the type.

### claim: nanochat-reproduces-chinchillas-equal-scaling-of-parameters-and-tokens
- existing: no
- title: His nanochat sweeps reproduce Chinchilla's finding that compute-optimal parameters and tokens grow equally with compute
- confidence: stated
- stated_on: 2026-01-07
- quote: "This is a remarkable result that we reproduce" (§Details (Scaling laws))
- statements:
  - Optimal N and D both scale as about C^0.5, equal to each other, so the optimal ratio is constant; he calls it remarkable and says "nature decided" compute-optimal Transformers fall on a straight line (§Details (Scaling laws)).
  - His constant is about 8, not Chinchilla's 20 (§Details (Scaling laws)). Keep both in the claim; the reproduction is of the exponents, not the constant.
- relation to existing claims: none. **Note:** [[scaling-offers-a-guaranteed-path-to-better-models]] (2023-11-23) is about scaling's reliability, not the ratio; a **Note:** at most.
- merge option: fold into [[scaling-laws]] as sentences if no claim page is wanted.

### claim: only-actual-metrics-are-real-and-comparable
- existing: no
- title: Validation loss can deceive when comparing models; he trusts benchmark metrics instead
- confidence: stated
- stated_on: 2026-01-07
- quote: "Only actual metrics are real and comparable." (§intro (Comparison to GPT-2/GPT-3 miniseries))
- statements:
  - He did not want to compare models by validation loss because, while simple, it can be subtle and deceiving (§intro (Comparison to GPT-2/GPT-3 miniseries)).
  - Example: modded-nanogpt, which he otherwise loves, merged changes he thought mildly gamed the metric; evaluating in one long row (B=1) gives more tokens more context than with B>>1, so the improvement is not real (§intro (Comparison to GPT-2/GPT-3 miniseries)).
  - Comparing FineWeb loss with GPT-2 and GPT-3 is not fair or informative because they trained on a very different, unknown data mix (§intro (Comparison to GPT-2/GPT-3 miniseries)).
- relation: **supports**-level link to an existing caveat, best written as a **Note:**: on [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]] he already called the FineWeb validation-loss comparison with GPT-2 unfair because GPT-2 trained on WebText ([[github-2024-05-28-llmc-gpt-2-124m]] §intro). Same reason, broader statement here. That claim's title is about HellaSwag results, not about metrics, so a `supports` link would be loose; recommend a **Note:** on both pages and a sentence on [[llm-evaluation]].

### topic: llm-evaluation
- existing: yes
- statements:
  - CORE, from the DCLM paper, is an ensemble over 22 high-quality datasets; DCLM's code for it was "complicated and bloated", so he stripped it to one simple, dependency-free file, `core_eval.py` (§intro (Comparison to GPT-2/GPT-3 miniseries)). [22: comparison]
  - GPT-2 CORE scores he calculated by running the released models: Small 0.114, Medium 0.185, Large 0.215, XL 0.257 (§Details (GPT-2 / GPT-3 CORE scores)). [measured by him, on OpenAI's models]
  - GPT-3 was never released, so he took six tasks present in both CORE and the GPT-3 paper's tables, calibrated a simple model on GPT-2 to map them to CORE with three approaches, and got estimates: Small 0.148, Medium 0.216, Large 0.266, XL 0.291, 2.7B 0.329, 6.7B 0.361, 13B 0.385, 175B 0.427 (§Details (GPT-2 / GPT-3 CORE scores)). [estimate] He says the solid evals and well-aligned points give him confidence these are not far off.
  - He attributes GPT-3's edge at equal size to data, architecture and optimisation improvements and to far more tokens, 300B against GPT-2's estimated ~100B (§Details (GPT-2 / GPT-3 CORE scores)). [300B: comparison; ~100B: estimate]
  - All are CORE v1, not v2 (§Details (GPT-2 / GPT-3 CORE scores)).
  - Miniseries v1 results (depth, params M, tokens B, val bpb, CORE, minutes): d10 91/0.73/1.0312/0.071/5; d12 135/1.08/0.9825/0.1059/7.8; d16 268/2.15/0.9101/0.1332/21.4; d20 477/3.82/0.8572/0.1708/59.5 (full table d10–d20 in the raw) (§Details (Miniseries v1 CORE scores)). [measured]
- relation: see claim above.

### method: reproduce-a-published-model
- existing: yes
- statements: estimating an unreleased model's score from its paper's tables, calibrated on the released sibling (GPT-2 for GPT-3) (§Details (GPT-2 / GPT-3 CORE scores)); targeting the whole GPT-2/GPT-3 miniseries on one CORE-vs-cost chart (§intro (Comparison to GPT-2/GPT-3 miniseries)).
- note: unlike llm.c, nanochat does not copy GPT-2's architecture or hyperparameters; it targets the score. Fits "Set the whole model series as the target" and "Confirm on a benchmark that is comparable across papers".

### topic: compute-efficiency
- existing: yes
- statements:
  - FLOPs per token: 6 × (non-embedding parameters) + 12·l·h·q·t for attention's key-query matmuls, about 1% off Chinchilla's exact formula, which counts the embedding lookup and softmax operations he ignores (§Details (Scaling laws)).
  - Batch 0.5M is a little large and FLOP-wise should be about half, but is good wall-clock-wise as is (§Details (Hyperparameter sweeps)). [setting]

### topic: gradient-descent
- existing: yes
- statements: learning rates were close to optimal after a small nudge to the embedding LR; the warmdown ratio was the biggest surprise, nudged 0.2 → 0.4; sequence length 2048 balances context and document diversity; tuning was basic and not exhaustive (§Details (Hyperparameter sweeps)). [settings]
- **Note:** the 2026-01-31 post tunes warmdown 0.4 → 0.5 ([[github-2026-01-31-nanochat-beating-gpt-2]] §intro).

### method: quick-experiment-loop
- existing: yes
- statement: d12 is his favourite model, GPT-1-sized, 12 layers, currently about 6 minutes to train (§intro (Miniseries v1)). [~6 min: measured, approximate; the table gives 7.8 min for d12 at ratio 8]
- **Note:** the README says about five minutes for d12 ([[github-2026-07-03-nanochat-readme]] §Research) and the 2026-01-31 post "only ~5 minutes". Different code states; give each with its date.

### method: small-hackable-educational-code
- existing: yes
- statement: he rewrote DCLM's "complicated and bloated" CORE code as one simple, dependency-free file (§intro (Comparison to GPT-2/GPT-3 miniseries)).

## Quotes
- "you are not optimizing for a single specific model but for a family models" (§intro (Why miniseries))
- "d12 is my favorite model (it's the size of GPT-1!)" (§intro (Miniseries v1))
- "and you did your scaling laws right these curves should not intersect" (§intro (Miniseries v1))
- "and the resulting "improvement" is not real" (§intro (Comparison to GPT-2/GPT-3 miniseries))
- "Only actual metrics are real and comparable." (§intro (Comparison to GPT-2/GPT-3 miniseries))
- "to get more bang for the buck" (§intro (Comparison to GPT-2/GPT-3 miniseries))
- "you don't really want to train a d12" (§Details (Scaling laws))
- "This is a remarkable result that we reproduce" (§Details (Scaling laws))
- "nature decided that compute optimal Transformers fall exactly on a straight line (what???)" (§Details (Scaling laws))
- "In nanochat, when you do the fits you actually get something much lower: 8." (§Details (Scaling laws))
- "We're now only training compute optimal models." (§Details (Scaling laws))
- "the Chinchilla approach gives the much cleaner scaling law" (§Details (Scaling laws), code comment)
- "The warmdown ratio was the biggest surprise" (§Details (Hyperparameter sweeps))
- "I wouldn't really read into this too much" (§Details (Miniseries v1 CORE scores))

All grep-checked (one match each, under 15 words). "a family models" is his typo (missing "of").

## Notes for merge
- **Ratio inconsistency in the raw:** the text says the fitted D:N is 8 and the v1 models use 8 (§Details (Scaling laws), §Details (Miniseries v1 CORE scores)), but the extrapolation table header says "12:1 D:N ratio" (§Details (Miniseries v1 CORE scores)). Not reconciled in the post; say so if the table is cited.
- **Fit description:** the text says a fit "predicting (total) parameters -> CORE", but the formula is in FLOPs. Cite the formula as given; do not reword it as a parameter law.
- **Cost figures:** ~$100 for the whole miniseries is ~4 h × $24; the extrapolated costs are $3/GPU/h × 8 × hours, assuming d20's utilisation. All are estimates, not bills.
- **d12 time:** "~6 minutes" (§intro) vs 7.8 min in the table; the table models use ratio 8; the prose may refer to another setting. Do not reconcile.
- **Kaplan's bug** is his report of Chinchilla's critique, attribute it as such ("he reports").
- **GPT-2 XL CORE:** 0.257 here; 0.256525 in the 2026-01-31 post and README; 0.25 in the d34 post; 0.26 for GPT-2 xl in the launch post. Rounding of one figure, likely.
- He says "Earlier in the year I stumbled by the DCLM paper": his own time reference; do not convert to a date.
- Images (wandb plots, CORE vs FLOPs chart, Chinchilla comparison) are not described beyond his text.
- modded-nanogpt is Keller Jordan's repo, not his; the B=1 critique is his opinion of their change.
