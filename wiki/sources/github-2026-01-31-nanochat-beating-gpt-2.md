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

The text before the first heading is cited `§intro`; short forms §Model Architecture, §Optimizer and §Training Script stand for the three subsections of `§The Jan 29 Model: Architecture Deep Dive`, and §What Worked and §What Didn't Work for those of `§The Optimization Journey`. The raw file is his post only. Number tags: measured, target, comparison (someone else's figure or a baseline), setting, estimate.

**Inconsistencies kept, each with its own source and location.**
- *Date.* The raw's `published` is 2026-01-31, the date used here; the nanochat README links the post as "Feb 1 2026" ([[github-2026-07-03-nanochat-readme]] §Guides).
- *Parameter count.* §Model Architecture says value embeddings add "~150M for d24", while its printed counts give value_embeds 603,979,776 of 1,384,124,976 in total; the post does not reconcile them.
- *Lines of code.* §intro says nanochat beats GPT-2 in "~1000 lines of code"; the launch post's report card gives 8,304 lines in 44 files ([[github-2025-10-13-nanochat-discussion-introducing]] §Report card). Neither reconciles them; perhaps different scopes.
- *GPT-2's size.* §intro gives the largest 2019 GPT-2 as 1.5B parameters; the README's leaderboard calls the target GPT-2 (1.6B) ([[github-2026-07-03-nanochat-readme]] §Time-to-GPT-2 Leaderboard); the 2026-01-07 post's CORE table also lists GPT-2 XL as 1.6B ([[github-2026-01-07-nanochat-miniseries-v1]] §Details (GPT-2 / GPT-3 CORE scores)).

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
