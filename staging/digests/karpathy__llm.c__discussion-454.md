# Digest: PyTorch vs. llm.c cross-checks
- raw: raw/github/karpathy__llm.c__discussion-454.md · published: 2024-05-24 · medium: github · words: 620
- source slug: github-2024-05-24-llmc-pytorch-cross-checks

## Source page
```
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

## Summary
He says llm.c is nearing serious "production" pretraining: from random init, on FineWeb, evaluated on HellaSwag, in bfloat16, multi-GPU, with gradient clipping, accumulation and a learning-rate schedule (§intro). He opens a thread comparing llm.c and PyTorch training for correctness only, meaning the two runs should match, and setting speed aside (§intro). On one A100 40GB he trains GPT-2 (124M) from scratch for 50 steps with warmup, decay and weight decay switched off, and the two agree within about 1e-3 in loss and gradient norm, which he says gives confidence in correctness (§1 GPU training in FP32). He gives the flags for a bfloat16 variant and a 4-GPU llm.c run with ZeRO-1 that should reproduce the same results, because the total batch stays fixed and only the gradient-accumulation steps fall (§1 GPU training in BF16, §multiGPU). The matching 4-GPU PyTorch run does not yet produce the same results, and he says he is tracking it down (§multiGPU).

## Key points
- Run-level parity check of llm.c against the PyTorch reference: same model, data, batch, LR, with schedule and decay off; compare loss and grad norm → [[verify-gradients-against-pytorch]]
- The list of what a "production" pretraining run needs; status of the parity work → [[llm-c]]
- Total batch size fixed, gradient accumulation computed from it; multi-GPU only lowers the accumulation steps → [[gradient-descent]]
- ZeRO-1 optimizer sharding to save GPU memory → [[gpu-training-efficiency]]
- PyTorch's `train_gpt2.py` as the reference implementation; its multi-GPU run not yet matching → [[pytorch]]

## Fed pages
- [[verify-gradients-against-pytorch]]
- [[llm-c]]
- [[gradient-descent]]
- [[gpu-training-efficiency]]
- [[pytorch]]
```

## Candidates
### method: verify-gradients-against-pytorch
- existing: yes (aliases include "PyTorch parity check")
- new steps proposed (append after step 15, under a "whole training runs" heading): Fix every hyperparameter identically on both sides · Switch off schedule, warmup and weight decay · Train a few dozen steps from scratch · Compare loss and gradient norm per step · Check multi-GPU against single-GPU at the same total batch
- statements:
  - Once llm.c could do serious pretraining runs, he started a thread comparing llm.c and PyTorch training with the focus on correctness, the two runs matching, ignoring speed (§intro).
  - The comparison run: GPT-2 (124M) from scratch on FineWeb, micro-batch 16, sequence 1024, total batch 131072 (so 8 accumulation steps), LR 1e-4, warmup and LR decay off, weight decay off, 50 iterations, validation and generation effectively off (§1 GPU training in FP32).
  - He gives the equivalent PyTorch command and suggests TinyStories for anyone who does not want to preprocess FineWeb: the numbers differ but the two should still match (§1 GPU training in FP32).
  - He pins the repo commit and the GPU (A100 40GB) (§1 GPU training in FP32).
  - Result: after 50 iterations the two are within about 1e-3 or less in loss and gradient-norm difference, shown side by side (§1 GPU training in FP32). [his measurement]
  - Multi-GPU: with the total batch unchanged, llm.c on 4 GPUs should give exactly the same results, just faster, because only the number of accumulation steps falls (§multiGPU).
  - The 4-GPU PyTorch run produced different results; he was tracking it down and posted the log of where things stood (§multiGPU).
- relation: extends the method from per-tensor gradient checks (micrograd, makemore 4) to whole-run parity between two implementations. **Note:** the existing page already has PyTorch parity as its second check ([[youtube-2022-08-16-micrograd]] @1:39:28); this is the same habit at the scale of a training run.

### artifact: llm-c
- existing: no
- statements:
  - By 2024-05-24 he says llm.c is getting to the point of nice, serious "production" pretraining runs: random init, a large diverse dataset (FineWeb), a standard eval (HellaSwag), bfloat16, multi-GPU, gradient clipping, gradient accumulation and learning-rate scheduling (§intro).
  - bfloat16 runs compile with `USE_CUDNN=1`; the PyTorch side uses `--dtype bfloat16 --flash 1` (§1 GPU training in BF16).

### topic: gradient-descent
- existing: yes
- statements:
  - llm.c takes a desired total batch size and computes the gradient-accumulation steps internally: micro-batch 16 × 1024 tokens against 131072 gives 8 (§1 GPU training in FP32).
  - On 4 GPUs the total batch stays identical, so llm.c lowers the accumulation steps and everything else stays the same (§multiGPU).

### topic: gpu-training-efficiency
- existing: no
- statements:
  - `-z 1` turns on ZeRO-1, optimizer sharding, which saves GPU memory; optional for the comparison (§multiGPU).

### topic: pytorch
- existing: yes
- statements:
  - PyTorch's `train_gpt2.py` serves as the reference for llm.c's correctness checks; in May 2024 the two matched on one GPU but not yet on four (§1 GPU training in FP32, §multiGPU).

## Quotes
- "with a focus on CORRECTNESS (i.e. the two training runs matching)" (§intro)
- "ignore speed considerations in this thread" (§intro)
- "This gives nice confidence for correctness and match to PyTorch!" (§1 GPU training in FP32)
- "I am tracking this down now." (§multiGPU)

## Notes for merge
- Headings: text before `### 1 GPU training in FP32` is §intro; then `### 1 GPU training in FP32`, `### 1 GPU training in BF16`, `### multiGPU`.
- Inconsistency in the raw: under the FP32 heading the llm.c side compiles with `PRECISION=FP32`, but the PyTorch command shown passes `--dtype bfloat16 --flash 1`; in the multiGPU section the PyTorch command uses `--dtype float32 --flash 0`. Do not state that both sides were fp32 in the single-GPU run; say "the commands he gives".
- The ~1e-3 match is his measurement from a screenshot (an image link); the per-step numbers are not in the text.
- The thread title is cross-checks, but the body as fetched is only his opening post; no replies are in the raw file, and no later resolution of the multi-GPU mismatch is in this file.
- This is the source the prompt flagged for [[verify-gradients-against-pytorch]]: the existing page's steps are gradient-level; merge should add a short run-level block rather than a new method.
