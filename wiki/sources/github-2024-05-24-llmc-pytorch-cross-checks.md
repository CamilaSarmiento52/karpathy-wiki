---
type: source
raw_path: raw/github/karpathy__llm.c__discussion-454.md
published: 2024-05-24
medium: github
summary: "A thread checking that llm.c and the PyTorch reference produce the same GPT-2 (124M) training run: on one A100 the two match to about 1e-3 in loss and gradient norm after 50 steps, while the 4-GPU PyTorch run does not yet match."
url: https://github.com/karpathy/llm.c/discussions/454
title: PyTorch vs. llm.c cross-checks
---
# PyTorch vs. llm.c cross-checks
Raw: [[raw/github/karpathy__llm.c__discussion-454]] · Original: https://github.com/karpathy/llm.c/discussions/454

Text before `### 1 GPU training in FP32` is cited as `§intro`; the other headings are `§1 GPU training in FP32`, `§1 GPU training in BF16` and `§multiGPU`. Only his opening post is in the raw file.

## Summary
He says llm.c is nearing serious "production" pretraining: from random init, on FineWeb, evaluated on HellaSwag, in bfloat16, multi-GPU, with gradient clipping, accumulation and a learning-rate schedule (§intro). He opens a thread comparing llm.c and PyTorch training for correctness only, meaning the two runs should match, and setting speed aside (§intro). On one A100 40GB he trains GPT-2 (124M) from scratch for 50 steps with warmup, decay and weight decay switched off, and the two agree within about 1e-3 in loss and gradient norm, which he says gives confidence in correctness (§1 GPU training in FP32). He gives the flags for a bfloat16 variant and a 4-GPU llm.c run with ZeRO-1 that should reproduce the same results, because the total batch stays fixed and only the gradient-accumulation steps fall (§1 GPU training in BF16, §multiGPU). The matching 4-GPU PyTorch run does not yet produce the same results, and he says he is tracking it down (§multiGPU).

## Key points
- Run-level parity check of llm.c against the PyTorch reference: same model, data, batch, LR, with schedule and decay off; compare loss and grad norm → [[verify-against-a-reference-implementation]]
- The list of what a "production" pretraining run needs; status of the parity work → [[llm-c]]
- Total batch size fixed, gradient accumulation computed from it; multi-GPU only lowers the accumulation steps → [[gradient-descent]]
- ZeRO-1 optimizer sharding to save GPU memory → [[compute-efficiency]]
- PyTorch's `train_gpt2.py` as the reference implementation; its multi-GPU run not yet matching → [[pytorch]]
- A standard eval, HellaSwag, on the production-run checklist → [[llm-evaluation]]

## Fed pages
- [[verify-against-a-reference-implementation]]
- [[llm-c]]
- [[gradient-descent]]
- [[compute-efficiency]]
- [[pytorch]]
- [[llm-evaluation]]
