---
type: source
raw_path: raw/github/karpathy__llm.c__discussion-224.md
published: 2024-04-22
medium: github
summary: "His first llm.c progress report: a profile of the mainline CUDA training step, speed and peak memory against PyTorch, lines of code, compile and run latency, the next big pieces of work, and the first ports to other languages."
url: https://github.com/karpathy/llm.c/discussions/224
title: State of the Union [April 22, 2024]
---
# State of the Union [April 22, 2024]
Raw: [[raw/github/karpathy__llm.c__discussion-224]] · Original: https://github.com/karpathy/llm.c/discussions/224

No markdown headings: the body is bold-labelled paragraphs, cited as `§intro` with the label where useful, e.g. `§intro (peak memory)`.

## Summary
He says he will post periodic reports on where llm.c stands, focusing on the mainline CUDA code, and gives the profiler output of one GPT-2 training step on an A10: 76% of the time is in NVIDIA cutlass kernels, which he calls encouraging (§intro). On his A100 he measures about 73 ms per iteration against 78.2 ms for a PyTorch run in fp32 without flash attention, about 6.4% faster in that constrained setting, and peak memory of 8753 MiB against PyTorch's 12879 MiB, 32% lower (§intro). He also reports the main file at 2097 lines of clean code, a 2.4 s compile and 2.2 s from launch to first step (§intro). The open "big stones" are faster attention kernels, fp16/bf16 done cleanly, multi-GPU training with allreduce, and an experiment harness for bigger runs; he credits contributors for kernels and tooling and lists the first ports to Mojo, C#, Rust and Metal by other people (§intro).

## Key points
- First State of the Union: profile, speed, memory, LOC, latency, roadmap, forks → [[llm-c]]
- Speed and memory measured against a PyTorch reference run, with the setting spelled out → [[verify-against-a-reference-implementation]]
- Kernel time breakdown, cutlass share, memory footprint → [[compute-efficiency]]
- Lines of code and compile/run latency tracked as first-class metrics → [[small-hackable-educational-code]]
- llm.c at ~6.4% faster than PyTorch in a constrained fp32 setting → [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]

## Fed pages
- [[llm-c]]
- [[verify-against-a-reference-implementation]]
- [[compute-efficiency]]
- [[small-hackable-educational-code]]
- [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]
