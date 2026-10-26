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

No markdown headings: bold-labelled paragraphs (Single GPU training, Multi-GPU training, Functional, Goal, Lines of code, Latency, Peak memory, Fine print, and others), cited as `§intro` with the label where useful.

## Summary
On day 24 of the project he reports that llm.c trains GPT-2 (124M) on one GPU about 7% faster than PyTorch nightly with mixed precision, torch compile and flash attention, about 46% faster than PyTorch 2.3.0, and about 3X faster than at his April 22 report (§intro). The gains come from bfloat16 mixed precision with an fp32 master copy, kernel optimisations including a fused classifier, cuDNN flash attention, a 128-bit load/store data structure, and memory savings; a first multi-GPU version uses MPI and NCCL (§intro). He states the goal: a reliable, clean, tested, minimal and sufficiently optimised stack that reproduces the GPT-2 miniseries from 124M to 1.6B in C/CUDA, which needs gradient accumulation, clipping, random init in C, a learning-rate schedule, evals and a modern dataset (§intro (Functional), §intro (Goal)). He also reports the downsides: the main file grew to about 3,000 lines and compile time to 4.3 s, or about 1m24s with cuDNN, which he wants to remove as a dependency (§intro (Lines of code), §intro (Latency)). The fine print gives the hardware and a tokens-per-second comparison, and explains why padding GPT-2's vocabulary is a non-trivial trick in PyTorch (§intro (Fine print)).

## Key points
- Day-24 status, goal of reproducing the GPT-2 miniseries 124M–1.6B, LOC, forks, plan for a pure-CUDA fp32 file as a course endpoint → [[llm-c]]
- ~7% faster than PyTorch nightly, ~46% faster than 2.3.0, measured with fine print → [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]
- How he compares: strongest PyTorch setup he knows, named features, invocations, hardware fine print, a flagged suspicious number → [[verify-against-a-reference-implementation]]
- Mixed precision, fused classifier, flash attention, Packed128, memory savings, multi-GPU with MPI+NCCL, ZeRO-1 → [[compute-efficiency]]
- Components still needed for a real reproduction: gradient accumulation, clipping, warmup and schedule → [[gradient-descent]]
- LOC and compile latency reported as costs; pure-CUDA file as the end of a course from gpt2.c → [[small-hackable-educational-code]]
- Vocabulary padding to 50304 and the tied embedding/classifier weights → [[pytorch]]
- An evaluation still to be added (WikiText 103?) → [[llm-evaluation]]
- The goal of reproducing the GPT-2 miniseries → [[reproduce-a-published-model]]

## Fed pages
- [[llm-c]]
- [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]
- [[verify-against-a-reference-implementation]]
- [[compute-efficiency]]
- [[gradient-descent]]
- [[small-hackable-educational-code]]
- [[pytorch]]
- [[llm-evaluation]]
- [[reproduce-a-published-model]]
- [[memory-access-not-flops-limits-training-speed]]
