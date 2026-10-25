# Digest: Beating GPT-2 for <<$100: the nanochat journey
- raw: raw/github/karpathy__nanochat__discussion-481.md · published: 2026-01-31 · medium: github · words: 2674 (frontmatter)
- source slug: github-2026-01-31-nanochat-beating-gpt-2

Number tags: **[measured]** his reported result from a run; **[target]** a goal; **[comparison]**
someone else's figure or a baseline (GPT-2 in 2019, GPT-2's CORE); **[setting]** a configuration
value he chose; **[estimate]** arithmetic or approximation in place of measurement.

Headings (exact): `§intro`, `§The Goal`, `§The Jan 29 Model: Architecture Deep Dive` with
`### Model Architecture (\`nanochat/gpt.py\`)`, `### Optimizer (\`nanochat/optim.py\`)`,
`### Training Script (\`scripts/base_train.py\`)`; `§The Optimization Journey` with
`### What Worked`, `### What Didn't Work`; `§Reproduce`, `§Discord`, `§Acknowledgements`,
`§Samples fun`. Short forms below: §Model Architecture, §Optimizer, §Training Script,
§What Worked, §What Didn't Work. The raw file is his post only.

## Source page
```
---
type: source
raw_path: raw/github/karpathy__nanochat__discussion-481.md
published: 2026-01-31
medium: github
summary: "His account of nanochat beating GPT-2's CORE score with a d24 trained in 3.04 hours for about $73 on one 8×H100 node, against about $43,000 for GPT-2 in 2019, with a time-to-GPT-2 leaderboard, the record model's architecture and optimizer, and lists of what worked and what did not."
url: https://github.com/karpathy/nanochat/discussions/481
title: "Beating GPT-2 for <<$100: the nanochat journey"
---
# Beating GPT-2 for <<$100: the nanochat journey
Raw: [[raw/github/karpathy__nanochat__discussion-481]] · Original: https://github.com/karpathy/nanochat/discussions/481

The text before the first heading is cited `§intro`.

## Summary
He sets GPT-2's 2019 training, 32 TPU v3 chips for about a week at an estimated $43,000, against nanochat beating its CORE score in about 3 hours on one 8×H100 node, about $73, a ~600× reduction he reads as cost falling to about 40% of the previous year each year, gains he credits to hardware, software, algorithms and data together (§intro). A new leaderboard tracks wall-clock time to beat GPT-2's CORE of 0.256525, with a first record of 3.04 hours by a d24 on 2026-01-29 (§The Goal). He details the record model's departures from a vanilla Transformer, its split Muon/AdamW optimizer with no DDP, and a training script driven by one `--depth` knob, most ideas adapted from modded-nanogpt (§The Jan 29 Model: Architecture Deep Dive). He lists what worked, including value embeddings, residual scalars, a BOS-aligned loader that let him delete midtraining and a measured optimal ratio near 10, and what did not, warning that an idea is very hard to rule out and that small-scale tuning does not always transfer (§What Worked, §What Didn't Work, §Reproduce). He gives the reproduction command and run summary, and base-model samples (§Reproduce, §Samples fun).

## Key points
- GPT-2 capability in 3.04 h, ~$73; leaderboard; ~1000 lines; three files to edit → [[nanochat]]
- $43,000 in 2019 vs $73; ~600×; cost to ~40% each year; gains from everywhere → [[gpt-2-training-cost-falls-to-about-40-percent-a-year]], [[progress-comes-from-everything-improving-together]], [[compute-efficiency]]
- CORE as the target, GPT-2 0.256525, beat at 0.25851 → [[llm-evaluation]], [[reproduce-a-published-model]], [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]
- RoPE, parameter-free RMSNorm, QK norm, untied embeddings, ReLU², softcap, sliding windows, value embeddings, residual scalars, FA3 → [[transformer-architecture]]
- Muon for matrices, AdamW for embeddings and scalars; Polar Express, cautious weight decay; warmdown to 0 → [[gradient-descent]], [[do-not-decay-the-learning-rate-to-zero]]
- Optimal tokens:params ~10, measure it on your own network → [[scaling-laws]], [[fit-your-own-scaling-law]]
- BOS-aligned loader made midtraining unnecessary → [[pretraining-and-finetuning]]
- 320-experiment sweep: small-scale tuning doesn't transfer; d12 in ~5 min, many but not all ideas transfer → [[small-scale-tuning-does-not-always-transfer]], [[quick-experiment-loop]]
- An uneventful loss curve → [[training-diagnostics]]

## Fed pages
- [[nanochat]]
- [[gpt-2-training-cost-falls-to-about-40-percent-a-year]]
- [[progress-comes-from-everything-improving-together]]
- [[compute-efficiency]]
- [[llm-evaluation]]
- [[reproduce-a-published-model]]
- [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]
- [[transformer-architecture]]
- [[gradient-descent]]
- [[do-not-decay-the-learning-rate-to-zero]]
- [[scaling-laws]]
- [[fit-your-own-scaling-law]]
- [[pretraining-and-finetuning]]
- [[small-scale-tuning-does-not-always-transfer]]
- [[quick-experiment-loop]]
- [[training-diagnostics]]
```

## Candidates

### artifact: nanochat
- existing: yes
- statements:
  - Beating GPT-2 for under $100 from scratch has been, he says, "a bit of an odd obsession" (§intro).
  - nanochat beats GPT-2's performance with about 1000 lines of code on one 8×H100 node in about 3 hours, $73 at about $24/hour (§intro). [~3 h: measured (3.04 h); $73: estimate, time × rental; $24/h: comparison; ~1000 lines: his figure, see Notes]
  - New "time to GPT-2" leaderboard: wall-clock training time, excluding eval and logging, to beat GPT-2's CORE on 8×H100; record #1 is 3.04 hours, "d24 baseline, slightly overtrained", 2026-01-29, commit 348fbb3, by him (§The Goal). [measured]
  - Inspired by modded-nanogpt's leaderboard, but the target is CORE rather than validation loss and GPT-2 specifically; contributions welcome, mostly in `base_train.py`, `gpt.py` and `optim.py`, possibly also the dataset or tokenizer (§The Goal).
  - The record model: 24 layers, 1536 channels (depth × 64), 12 heads of dim 128; 1,384,124,976 parameters in total, of which value embeddings 603,979,776 and transformer matrices 679,481,856 (§Model Architecture). [setting; counts printed]
  - `--depth` is the single knob: model_dim = depth × 64, heads = model_dim / 128, token budget scales with depth, weight decay with 1/depth² (§Training Script).
  - Reproduction on commit 348fbb3: run the setup from `runs/speedrun.sh`, then `base_train` with `--depth=24 --target-param-data-ratio=12 --device-batch-size=16`; after about 3 hours, CORE 0.25851 against GPT-2's 0.256525, 3.04 hours (10,949 s), ~$73 (§Reproduce). [CORE, time: measured; $73: estimate]
  - The majority of the optimisations were cherry-picked and adapted from modded-nanogpt; not all of them worked for nanochat (§Training Script, last paragraph; §Acknowledgements).
  - Base-model samples show "pretty decent knowledge" on prompts like the capital of France, gold's symbol, the planets; "If 5*x + 3 = 13, then x is" gets "a factor of 5" (§Samples fun). [model output, not statements]
- **Cost/time series (for a timeline):** 2026-01-31: GPT-2 CORE beaten in 3.04 h (measured), ~$73 (estimate), d24 at ratio 12. GPT-2 in 2019: ~168 h on 32 TPU v3, $43,000 (comparison, his arithmetic). Do not write "down from" relative to other sources.

### claim: gpt-2-training-cost-falls-to-about-40-percent-a-year
- existing: no
- title: He estimates the cost to train GPT-2 falls each year to about 40% of the year before
- confidence: stated (the figure is his estimate, hedged as probably an underestimate of progress)
- stated_on: 2026-01-31
- quote: "the cost to train GPT-2 is falling to approximately 40% of the previous year" (§intro)
- statements:
  - GPT-2 1.5B in February 2019: 32 TPU v3 chips, "a bit over a week" (~168 hours), at $8/hour per TPU v3, 32 × 168 × $8 = $43,000, citing a 2019 Reddit thread and the Hugging Face model card (§intro). [comparison; his arithmetic on reported figures]
  - Seven years later nanochat beats it for $73, about a 600× cost reduction, i.e. cost falling to about 40% of the previous year each year (§intro). [600×, 40%: estimate]
  - He thinks this is an underestimate and further improvements are quite possible (§intro).
- relation: **supports** [[progress-comes-from-everything-improving-together]] (2025-10-17), see below. None otherwise.
- **Note:** "~600×" is $43,000 / $73 ≈ 589; "40%" is 600^(-1/7) ≈ 0.40. Both his rounding; fine to cite.

### claim (existing): progress-comes-from-everything-improving-together
- existing: yes (2025-10-17)
- statement: the gains come from everywhere: better hardware (H100 vs TPU v3), software (Flash Attention 3, torch.compile), algorithms (Muon, architecture) and data (FineWeb-edu) (§intro).
- relation: **supports.** In the Dwarkesh interview he says progress came from data, hardware, software and algorithms all improving, none winning ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @1:05:39); here he gives the same four sources for nanochat's cost drop (§intro). Add as a source.

### topic: llm-evaluation
- existing: yes
- statements:
  - The target is the DCLM CORE metric over 22 benchmarks; GPT-2's CORE is 0.256525 (§The Goal). [comparison]
  - The leaderboard target is CORE, not validation loss as in modded-nanogpt (§The Goal).

### claim (existing): his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag
- existing: yes (2024-05-28, llm.c runs)
- statement: the d24 beats GPT-2 (1.6B)'s CORE, 0.25851 vs 0.256525 (§Reproduce).
- relation: **none as a claim link; a Note.** The claim is about llm.c reproductions of the same size, on HellaSwag ([[github-2024-05-28-llmc-gpt-2-124m]] §intro). nanochat's d24 (1.38B parameters) is not a GPT-2 reproduction and the metric is CORE. Both are true; `extends` would need the claim title broadened. Recommend a **Note:** on the claim pointing to [[nanochat]], and leave the title alone.

### topic: compute-efficiency
- existing: yes
- statements:
  - Flash Attention 3 gave about 9% more tokens/sec, with native (B, T, H, D) layout and one API for training and inference; falls back to PyTorch SDPA off Hopper (§What Worked, §Model Architecture). [measured]
  - Sliding window attention, `SSSL` (three 1024-token windows, one 2048), saves compute without quality loss; he first saw the idea in the GPT-3 paper (§What Worked, §Model Architecture).
  - Value embeddings add a lot of parameters at near-zero FLOPs (§Model Architecture).
  - Distributed optimizer: ZeRO-2-style sharded state, three-phase async (reduce, compute, gather), no DDP, gradient sync in the optimizer step (§Optimizer).
  - Batch 524,288 tokens (32 × 2048 × 8 GPUs) (§Training Script). [setting]
  - BestFit-Crop packing: 100% utilisation, about 35% token waste from cropping (§Training Script). [measured/setting, unclear]
  - Did not work: multi-token prediction (+13GB, no gain), FP8 for lm_head (+2GB, 1% speedup), skip connections (+2GB, no gain) (§What Didn't Work). [measured]

### topic: transformer-architecture
- existing: yes
- statements: departures from a vanilla Transformer in the record model: RoPE (base theta 10,000); RMSNorm with no learnable parameters after the embedding, before each block and before lm_head; QK normalisation after RoPE instead of softcapping attention; untied wte and lm_head; ReLU² instead of GELU; logit softcap 15·tanh(x/15) in float32; sliding window attention `SSSL` with the final layer full; gated value embeddings at alternating layers; per-layer residual scalars mixing x and the initial embedding x0; Flash Attention 3 (§Model Architecture). [settings]
  - Started from learned positional embeddings, LayerNorm, GELU, AdamW, FA2 (§The Optimization Journey).
  - Residual scalars gave a consistent 0.003–0.01 bpb improvement at all sizes; models "love" value-embedding capacity and every attempt to reduce it hurt; alternating placement beat U-shaped and every-layer (§What Worked). [measured]
  - No gain or not worth it: half-truncated RoPE, asymmetric softcap (slightly worse), smear and attention gates, varlen attention, bigram embeddings (Engram-lite, works a little but bloats), Hyperball/MuonH (§What Didn't Work).
- relation: **Note:** [[the-architecture-is-no-longer-the-bottleneck]] (2024-09-05) says only RoPE has changed since Llama; here a list of architecture changes each gave measured gains in nanochat. Different scale and question (frontier bottleneck vs a speedrun); not a contradiction. A **Note:** at most, and only if merge wants it; do not set `contradicts`.

### topic: gradient-descent
- existing: yes; aliases to add: Muon, warmdown, weight decay
- statements:
  - Split optimizer: AdamW for embeddings and scalars, Muon for weight matrices (attention projections and MLP), grouped by shape and stacked for batched updates (§Optimizer).
  - AdamW groups: lm_head lr 0.004, wte and value embeddings 0.3, both scaled by 1/√(dim/768); resid_lambdas 0.005; x0_lambdas 0.5 with beta1 0.96 (§Optimizer). [settings]
  - Muon internals: Nesterov momentum warmed 0.85 → 0.95 over 300 steps; Polar Express orthogonalisation (5 iterations) instead of Newton-Schulz; Adafactor-style factored variance reduction; cautious weight decay, only where grad·param ≥ 0, on a linear schedule to zero (§Optimizer). [settings]
  - The Muon overhaul worked; cautious weight decay was a clear win; "I tried to delete Muon and couldn't." (§What Worked).
  - Warmdown is 50% of training, linear LR decay to 0; weight decay 0.2 at d12 scaled by (12/depth)² (§Training Script). [settings]
  - The run in the intro chart was a little better after tuning warmdown 0.4 → 0.5 (§intro). [setting; "a little bit better": measured, no number]

### claim (existing): do-not-decay-the-learning-rate-to-zero
- existing: yes (2024-06-12, scoped to llm.c)
- statement: nanochat's record run decays the LR linearly to 0 over a 50% warmdown (§Training Script).
- relation: **none; a Note**, as for the launch post: different project and optimiser, and he gives no opinion on the floor here. Not a contradiction or change of mind.

### topic: scaling-laws
- existing: yes
- statements:
  - Tokens:params is 10.5 for compute-optimal, or 12 for the speedrun, a slight overtrain (§Training Script). [settings]
  - He empirically measured the optimal ratio at about 10, and says it is important to do the actual experiment on your own network (§What Worked). [measured]
  - About 8.8B FineWeb-edu tokens are needed in total (§Training Script). [setting]
- **Note:** the 2026-01-07 post's fits gave about 8 ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (Scaling laws)). Different code states; give each with its date, do not write "revised".

### method: fit-your-own-scaling-law
- existing: no (proposed by the 2026-01-07 digest)
- statement: "It's important to do the actual experiment on your own network." (§What Worked) — supports the method's premise.

### topic: pretraining-and-finetuning
- existing: yes
- statement: the BOS-aligned dataloader, every row starting with `<|bos|>`, made midtraining unnecessary, so he deleted it (§What Worked, §Training Script).
- **Note:** the launch post (2025-10-13) describes midtraining as a stage ([[github-2025-10-13-nanochat-discussion-introducing]] §Midtraining); write both with dates. This post deletes it from base training's pipeline in his words; it does not discuss SFT.

### claim: small-scale-tuning-does-not-always-transfer
- existing: no
- title: In his nanochat sweeps, small-scale hyperparameter tuning did not transfer, so he validates at target scale
- confidence: stated
- stated_on: 2026-01-31
- quote: "Key lesson: small-scale tuning doesn't transfer." (§What Worked)
- statements:
  - A 320-experiment sweep found `x0_beta1=0.96` optimal at d20; the lesson, he says, is that small-scale tuning doesn't transfer, so validate at target scale (§What Worked). [320, 0.96, d20: measured/setting]
  - Yet he does much of his iteration at small scale, d12 in about 5 minutes or d16, and says many but not all ideas that work there transfer (§Reproduce).
  - It is very difficult, perhaps impossible, to rule out an idea; sometimes you must try several times, and his lists reflect at most medium effort (§What Didn't Work).
- keep the title scoped to his sweep: the two statements together say hyperparameter values may not transfer while many ideas do.
- relation to existing pages: no claim. **Note:** on [[quick-experiment-loop]], whose last step is "Keep a change only if it works at every scale" ([[github-2026-07-03-nanochat-readme]] §Research); this source qualifies the loop's reach. merge option: fold into [[quick-experiment-loop]] as sentences instead of a claim page.

### method: quick-experiment-loop
- existing: yes
- statement: as above: d12 trains in about 5 minutes; many (not all) ideas transfer (§Reproduce). [~5 min: measured, approximate]

### method: reproduce-a-published-model
- existing: yes
- statements: he publishes the command, commit, run summary, time and cost so anyone can reproduce the record on a rented node (§Reproduce); the 2019 cost estimate cites its sources (§intro).

### method: training-diagnostics
- existing: yes
- statement: he calls the record run's loss curve "nicely uneventful"; the wandb x-axis looks longer because it includes inline evaluation (§intro).

## Quotes
- "a bit of an odd obsession for me" (§intro)
- "the cost to train GPT-2 is falling to approximately 40% of the previous year" (§intro)
- "I think this is an understimate and that further improvements are still quite possible" (§intro)
- "The gains come from everywhere" (§intro)
- "a nicely uneventful run of training a GPT-2 capability model" (§intro)
- "I tried to delete Muon and couldn't." (§What Worked)
- "Models love the value embeddings capacity." (§What Worked)
- "Made midtraining unnecessary (deleted it)." (§What Worked)
- "Key lesson: small-scale tuning doesn't transfer." (§What Worked)
- "Validate at target scale." (§What Worked)
- "It's important to do the actual experiment on your own network." (§What Worked)
- "it is very difficult (/impossible) to rule out an idea" (§What Didn't Work)
- "many (but not all!) ideas that work there transfer to the bigger models" (§Reproduce)
- "So the model has pretty decent knowledge!" (§Samples fun)

All grep-checked (one match each, under 15 words). "understimate" is his typo; keep it in the quote.

## Notes for merge
- **Date:** published 2026-01-31 per the raw; the 2026-07-03 README links it as "Feb 1 2026". Use 2026-01-31 (raw `published`); the README's date is its own wording.
- **Leaderboard overlap:** the README's leaderboard (2026-07-03) includes this record (#1, 3.04 h, Jan 29 2026) and later ones, down to 1.65 h; cite each row to the README, this record to this post.
- **Value embeddings count:** §Model Architecture says VE adds "~150M for d24", but the printed count is 603,979,776. Unreconciled in the raw (perhaps per layer or per group); do not pick one.
- **~1000 lines** (§intro) vs the launch report's 8,304 lines in 44 files (2025-10-13). Different counts, perhaps different scopes; neither source reconciles. Do not write "shrunk".
- **Ratio:** 10.5 compute-optimal and 12 for speedrun (§Training Script); "~10" measured (§What Worked); 8 in the 2026-01-07 fits. Give all with dates.
- **Midtraining:** "deleted it" is about the base pipeline as of this post; do not say nanochat has no midtraining in other sources' dates.
- The title has "<<$100", the intro "<$100".
- Most architecture and optimizer ideas are credited to modded-nanogpt (Keller Jordan and contributors); attribute them as adopted by nanochat, not invented by him.
- Samples are model output; do not quote them as his words.
- The 2019 GPT-2 compute and cost figures come from a Reddit thread and the Hugging Face card he cites; they are his comparison, not his measurement.
- **AI-written text (CLAUDE.md §3):** nothing in this post says any part was written by a model, so all of it is treated as his. Its heavily structured style (numbered departures, bold lists) is not evidence either way; do not label it AI-written without a statement from him.
