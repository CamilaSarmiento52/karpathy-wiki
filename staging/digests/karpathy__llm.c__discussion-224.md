# Digest: State of the Union [April 22, 2024]
- raw: raw/github/karpathy__llm.c__discussion-224.md · published: 2024-04-22 · medium: github · words: 394
- source slug: github-2024-04-22-llmc-state-of-the-union

## Source page
```
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

## Summary
He says he will post periodic reports on where llm.c stands, focusing on the mainline CUDA code, and gives the profiler output of one GPT-2 training step on an A10: 76% of the time is in NVIDIA cutlass kernels, which he calls encouraging (§intro). On his A100 he measures about 73 ms per iteration against 78.2 ms for a PyTorch run in fp32 without flash attention, about 6.4% faster in that constrained setting, and peak memory of 8753 MiB against PyTorch's 12879 MiB, 32% lower (§intro). He also reports the main file at 2097 lines of clean code, a 2.4 s compile and 2.2 s from launch to first step (§intro). The open "big stones" are faster attention kernels, fp16/bf16 done cleanly, multi-GPU training with allreduce, and an experiment harness for bigger runs; he credits contributors for kernels and tooling and lists the first ports to Mojo, C#, Rust and Metal (§intro).

## Key points
- First State of the Union: profile, speed, memory, LOC, latency, roadmap, forks → [[llm-c]]
- Speed and memory measured against a PyTorch reference run, with the setting spelled out → [[benchmark-against-pytorch]]
- Kernel time breakdown, cutlass share, DRAM/L2 traffic, memory footprint → [[gpu-training-efficiency]]
- Lines of code and compile/run latency tracked as first-class metrics → [[small-hackable-educational-code]]
- llm.c at ~6.4% faster than PyTorch in a constrained fp32 setting → [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]

## Fed pages
- [[llm-c]]
- [[benchmark-against-pytorch]]
- [[gpu-training-efficiency]]
- [[small-hackable-educational-code]]
- [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]
```

## Candidates
### artifact: llm-c
- existing: no
- aliases: [llm.c, train_gpt2.cu]
- frontmatter: repo_url https://github.com/karpathy/llm.c · language C/CUDA · status active
- statements:
  - He plans to post occasional reports on where the code is, focusing on the mainline CUDA code; the numbers come from running `profile_gpt2cu.py` (§intro).
  - `train_gpt2.cu` was at 2097 lines of clean code on 2024-04-22 (§intro). [his measurement]
  - Ongoing "big stones": attention kernel improvement or fusion (e.g. only lower-triangular matmuls), fp16/bf16 in the cleanest way, multi-GPU training with allreduce over MPI/NCCL, and an experimentation harness (argparse, logging, sweeps) for bigger runs (§intro).
  - He credits named contributors for kernels and tooling, and peak-memory work to @ngc92 (§intro).
  - First notable forks: ports to Mojo, C#, Rust and C/Metal by other people (§intro).

### method: benchmark-against-pytorch
- existing: no (distinct from [[verify-gradients-against-pytorch]], which is about correctness; this is speed and memory)
- aliases: [PyTorch comparison, State of the Union metrics, speed and memory vs PyTorch]
- proposed steps: Profile the training step by kernel · Time the iteration on a named GPU · Run an equivalent PyTorch script and say which features it uses · Compare peak memory from nvidia-smi · Publish the reproduce command · Track LOC and latency alongside speed · State the caveats of the comparison
- statements:
  - He reports a per-kernel time breakdown from `profile_gpt2cu.py`, then the step time split into encoder, forward blocks, classifier, backward blocks and optimizer, then DRAM and L2 traffic (§intro).
  - He names the hardware (the profile on an A10, timings on his A100) and the PyTorch configuration compared against (fp32, no flash attention, slightly stale PyTorch), and calls the setting constrained (§intro).
  - He compares peak memory as read from `nvidia-smi` and gives the exact PyTorch command to reproduce it (§intro).
  - Alongside speed and memory he reports lines of code, nvcc compile latency and launch-to-first-step latency (§intro).

### topic: gpu-training-efficiency
- existing: no (no topic on GPU kernels, mixed precision, MFU or memory; checked aliases in `wiki/index/topics.md`)
- aliases: [training efficiency, CUDA kernels, kernel fusion, mixed precision, bfloat16, flash attention, MFU, model flops utilization, ZeRO-1, recompute, multi-GPU training]
- statements:
  - In his April profile 76% of step time is in NVIDIA cutlass kernels (the matmuls), which he calls encouraging; softmax, AdamW, classifier, layernorm and GELU kernels take a few percent each (§intro). [his measurement, A10]
  - A training step took 212.4 ms on the A10, with about 48% in backward blocks, 26% in forward blocks, 23% in the classifier and 3% in the optimizer (§intro). [his measurement]
  - Memory was a constant 8753 MiB in `nvidia-smi`, heavily optimised by @ngc92 (§intro). [his measurement]
  - Planned efficiency work: attention via kernel improvement or fusion, such as computing only lower-triangular matmuls (§intro).

### method: small-hackable-educational-code
- existing: yes
- statements:
  - He tracks the main file's size as a headline metric ("2097 of clean LOC") together with compile latency (2.4 s) and run latency (2.2 s) (§intro).
- relation: extends the method's few-hundred-line PyTorch repos to a C/CUDA codebase where size and latency are reported as numbers. Merge may prefer a single sentence here rather than a step.

### claim: llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements
- existing: no
- title: In his measurements llm.c trained GPT-2 faster than PyTorch
- confidence: stated
- stated_on: 2024-04-22 (first instance; 344 and 677 add later measurements)
- quote: none from this file is a clean one-sentence statement of the speed result (the sentence has bold markup); use the 344 or 677 quote on the claim page.
- statements: on his A100, llm.c at about 73 ms/iteration vs PyTorch at 78.2 ms (fp32, no flash attention, slightly stale PyTorch) is ~6.4% faster "in this constrained setting"; peak memory 8753 MiB vs 12879 MiB, 32% lower (§intro). [his measurements; he scopes them himself]
- relation to existing claims: none.

## Quotes
- "Spending 76% in NVIDIA cutlass kernels, which is encouraging." (§intro)
- "I will post here once in a while on where the code is" (§intro)
- "fp16/bf16 in the cleanest way: how" (§intro)

## Notes for merge
- No markdown headings: the body is bold-labelled paragraphs (**runtime, DRAM traffic, instructions:**, **peak memory**, **lines of code**, **latency**, **"big stones" ongoing work:**, **major merged improvements last few days:**, **first notable forks appearing**). Everything is `§intro`. If merge wants finer location, append the bold label, e.g. `§intro (peak memory)`.
- Numbers: all speed/memory/LOC/latency figures are his measurements. The profile ran on an A10; the 73 ms vs 78.2 ms comparison is on his A100. The PyTorch side is fp32, no flash attention, "slightly stale" PyTorch; do not drop that qualifier.
- Profile numbers: the kernel table and DRAM/L2 lines sit in a code block; paraphrase only.
- No replies by other people are in the raw file. Contributor handles are credits, not authors of text.
- The forks are other people's projects; mention them only as "ports by others".
