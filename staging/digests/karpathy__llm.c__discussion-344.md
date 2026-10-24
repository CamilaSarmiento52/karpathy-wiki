# Digest: State of the Union [May 3, 2024]
- raw: raw/github/karpathy__llm.c__discussion-344.md · published: 2024-05-03 · medium: github · words: 1339
- source slug: github-2024-05-03-llmc-state-of-the-union

## Source page
```
---
type: source
raw_path: raw/github/karpathy__llm.c__discussion-344.md
published: 2024-05-03
medium: github
summary: "His day-24 llm.c progress report: single-GPU GPT-2 (124M) training about 7% faster than PyTorch nightly after mixed precision, kernel fusion, flash attention and memory savings, a first multi-GPU version, the goal of reproducing the GPT-2 miniseries in C/CUDA, and the costs in lines of code and compile time."
url: https://github.com/karpathy/llm.c/discussions/344
title: State of the Union [May 3, 2024]
---
# State of the Union [May 3, 2024]
Raw: [[raw/github/karpathy__llm.c__discussion-344]] · Original: https://github.com/karpathy/llm.c/discussions/344

## Summary
On day 24 of the project he reports that llm.c trains GPT-2 (124M) on one GPU about 7% faster than PyTorch nightly with mixed precision, torch compile and flash attention, about 46% faster than PyTorch 2.3.0, and about 3X faster than ten days earlier (§intro). The gains come from bfloat16 mixed precision with an fp32 master copy, kernel optimisations including a fused classifier, cuDNN flash attention, a 128-bit load/store data structure, and memory savings; a first multi-GPU version uses MPI and NCCL (§intro). He states the goal: a reliable, clean, tested, minimal and sufficiently optimised stack that reproduces the GPT-2 miniseries from 124M to 1.6B in C/CUDA, which needs gradient accumulation, clipping, random init in C, a learning-rate schedule, evals and a modern dataset (§intro). He also reports the downsides: the main file grew to about 3,000 lines and compile time to 4.3 s, or about 1m24s with cuDNN, which he wants to remove as a dependency (§intro). The fine print gives the hardware and a tokens-per-second comparison, and explains why padding GPT-2's vocabulary is a non-trivial trick in PyTorch (§intro).

## Key points
- Day-24 status, goal of reproducing the GPT-2 miniseries 124M–1.6B, LOC, forks, plan for a pure-CUDA fp32 file as a course endpoint → [[llm-c]]
- ~7% faster than PyTorch nightly, ~46% faster than 2.3.0, measured with fine print → [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]
- How he compares: same batch and sequence, named PyTorch features, invocations, hardware fine print, a flagged suspicious number → [[benchmark-against-pytorch]]
- Mixed precision, fused classifier, flash attention, Packed128, memory savings, multi-GPU with MPI+NCCL, ZeRO-1 → [[gpu-training-efficiency]]
- Components still needed for a real reproduction: gradient accumulation, clipping, warmup and schedule → [[gradient-descent]]
- LOC and compile latency reported as costs; pure-CUDA file as the end of a course from gpt2.c → [[small-hackable-educational-code]]
- Vocabulary padding to 50304 and the tied embedding/classifier weights → [[pytorch]]

## Fed pages
- [[llm-c]]
- [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]
- [[benchmark-against-pytorch]]
- [[gpu-training-efficiency]]
- [[gradient-descent]]
- [[small-hackable-educational-code]]
- [[pytorch]]
```

## Candidates
### artifact: llm-c
- existing: no
- statements:
  - Day 24 of the project on 2024-05-03: multi-GPU training, in bfloat16, with flash attention (§intro).
  - Goal: a reliable, stable, clean, tested, minimal, hardened and sufficiently optimised LLM stack that reproduces the GPT-2 miniseries of all sizes, 124M to 1.6B, directly in C/CUDA; at the current pace he guessed about two weeks out (§intro). [target, not a result]
  - Still needed for that: gradient accumulation, gradient clipping, random init directly in C, learning-rate warmup and schedule, an evaluation (he floats WikiText 103) and a modern pretraining dataset (he floats FineWeb) (§intro).
  - `train_gpt2.cu` is about 3,000 lines, plus `common.h` (300) and `tokenizer.h` (100), up from about 2,000 on April 22 (§intro). [his count]
  - The fp32 CUDA code was split into `train_gpt2fp32.cu`, to become pure CUDA kernels with no cuBLAS or cuDNN, which they think would be a nice endpoint of a CUDA course that starts from the pure-CPU `gpt2.c` (§intro).
  - He singles out @ngc92 and @ademeure as major contributors; Lambda labs sponsors GPUs; more forks appear (C++ with CCCL, Zig, Go) (§intro).
  - Community: #llmc on the nn zero to hero Discord and #llmdotc on CUDA MODE Discord (§intro).

### claim: llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements
- existing: no
- title: In his measurements llm.c trained GPT-2 faster than PyTorch
- confidence: stated
- statements:
  - GPT-2 (124M) single-GPU training ~7% faster than PyTorch nightly "with no asterisks", against what he calls the fastest PyTorch configuration he knows on Ampere: mixed precision, torch compile and flash attention (§intro). [his measurement]
  - ~46% faster than PyTorch stable 2.3.0; he credits the PyTorch team with recent changes that greatly sped up the GPT-2 setting (§intro). [his measurement]
  - ~3X faster than his own April 22 report (§intro). [his measurement]
  - Fine print: A100 40GB PCIe on Lambda; llm.c ~167K tok/s on a PR about to merge, ~160K on master; PyTorch ~150K tok/s, i.e. ~11%; padding PyTorch's vocab to 50304 lifts it to ~156K, leaving ~7% (§intro).
  - Peak memory at batch 32, sequence 1024: llm.c 16.6 GiB, PyTorch 37.2 GiB; he says the PyTorch number feels suspiciously high and is to be investigated (§intro).
- relation to existing claims: none.

### method: benchmark-against-pytorch
- existing: no
- statements:
  - He compares against the strongest PyTorch setup he knows of (nightly, mixed precision, compile, flash attention), and separately against the stable release (§intro).
  - He gives the invocations for both sides, the hardware and driver/CUDA versions, and tokens per second, and shows how one trick (vocab padding) shifts the comparison from ~11% to ~7% (§intro).
  - He flags a number he does not trust (PyTorch's 37.2 GiB) rather than leaving it unqualified (§intro).
  - He reports losses as well as wins: thumbs-down sections for LOC growth and compile latency (§intro).

### topic: gpu-training-efficiency
- existing: no
- statements:
  - Mixed precision: bfloat16 training with a master copy of parameters in fp32 (§intro).
  - A fused classifier that, he says, improves algorithmically on what the PyTorch compiler does: it does not materialise normalised logits and evaluates the loss only at the label's index (§intro).
  - Flash attention, currently cuDNN's (§intro).
  - Packed128, a structure like float4 but supporting mixed precision, which forces 128-bit load and store instructions to maximise memory bandwidth (§intro).
  - Memory savings by deleting unnecessary memory for backward-pass gradients, and by being careful with allocation, especially in the fused classifier (§intro).
  - Multi-GPU v1 with MPI+NCCL; a ZeRO stage 1 (optimizer state sharding) PR about to merge (§intro).
  - Profile at batch 24: a step takes 302.5 ms, about 61% in backward blocks; bf16 matmul kernels take about 55% and cuDNN attention about 9% (§intro). [his measurement]
  - cuDNN flash attention gives large speedups and memory savings but raises compile time to ~1m24s, which they want to remove (§intro).

### topic: gradient-descent
- existing: yes
- statements:
  - For a proper GPT-2 reproduction llm.c still needed gradient accumulation, gradient clipping, and learning-rate warmup and schedule (§intro).
- note: thin here; the substantive optimisation settings are in the 481 and 677 digests.

### method: small-hackable-educational-code
- existing: yes
- statements:
  - He reports added lines of code as a cost of features and optimisations (§intro).
  - He calls the nvcc compile time of 4.3 s, up from 2.4 s, about as bad as `import torch`, and wants to lower it (§intro).
  - The pure-CUDA fp32 file is meant as the endpoint of a CUDA course: start from the CPU-only `gpt2.c` and see how fast you can make it with kernels only and no dependencies (§intro).
- relation: extends the existing "teeth when it needs them" step: here simplicity is kept in a separate dependency-free file while the main file takes the optimisations.

### topic: pytorch
- existing: yes
- statements:
  - Padding the vocab is not trivial for GPT-2 in PyTorch: you must know 50257 is bad and 50304 (divisible by 64) is better, mask the padded dimensions to -inf because the token embedding is shared with the classifier, never sample them, and do model surgery when loading OpenAI weights; OpenAI's original code did not pad (§intro).
  - He thanks the PyTorch team for recent nightly changes that sped up GPT-2 training, and credits @Chillee for discussions and PyTorch support (§intro).

## Quotes
- "It is day 24 of the llm.c project." (§intro)
- "this is now about as bad as `import torch`" (§intro)
- "Note that padding the vocab is not a trivial matter for GPT-2 in PyTorch." (§intro)
- "The original OpenAI GPT-2 code also did not pad the vocab in this way." (§intro)
- "the PyTorch number feels a bit suspiciously high in this comparison" (§intro)
- "which we think would make a really nice endpoint of a CUDA course" (§intro)
- "At current pace this feels like somewhere around ~2 weeks out." (§intro)

## Notes for merge
- No markdown headings; one `---` rule splits it. Bold labels: Single GPU training, Multi-GPU training, Functional, Goal, Lines of code, Latency, Peak memory, Runtime/DRAM traffic/instructions, Contributors, Notable forks, Featured discussions, fp32 CUDA version plans, Fine print, Acknowledgements. All cite as `§intro`; append the label if merge wants precision.
- Two different "faster" numbers: ~7% (vs nightly, headline, and also the tok/s result after padding the vocab) and ~11% (vs PyTorch master without padding). The ~46% is against stable 2.3.0. Keep each with its baseline.
- The "~2 weeks out" is a forecast; the 124M reproduction did come on 2024-05-28 (digest 481) — merge may note this with **Note:**, not as his statement.
- One garbled sentence: "With more features and optimizations can more lines of code." Paraphrased, not quoted.
- "Featured discussions" links a profiling Discussion by @ademeure; that is someone else's analysis, not his.
- No replies by other people in the raw file.
