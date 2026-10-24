---
type: source
raw_path: raw/talks/aR6CzM0x-g0.md
published: 2024-10-03
medium: talk
summary: "His CUDA MODE keynote on llm.c: how frustration with torch.compile led him to drop PyTorch, how he ported GPT-2 layer by layer to one C file and then to CUDA with a team of contributors, what it took to beat PyTorch on GPT-2 training, and why he thinks LLMs may one day write code like llm.c for any custom application."
url: https://www.youtube.com/watch?v=aR6CzM0x-g0
title: "CUDA Mode Keynote | Andrej Karpathy | Eureka Labs"
---
# CUDA Mode Keynote | Andrej Karpathy | Eureka Labs
Raw: [[raw/talks/aR6CzM0x-g0]] · Original: https://www.youtube.com/watch?v=aR6CzM0x-g0

An unnamed host introduces him in the [00:00] and [00:39] blocks and at the start of [01:11]; nothing in the introduction is his. From partway into [01:11] to the end he is the only speaker. The recording date is not stated; this page uses the published date. **Note:** his post of 2024-10-02, [[x-2024-10-02-gpu-mode-talk]], outlines a GPU MODE workshop talk he gave "last week" with the same sequence and the same closing thought, so it very likely describes this talk; neither source says so.

## Summary
After a host's introduction, he tells the story of llm.c: while preparing a YouTube video on GPT training he hit torch.compile errors in eval and inference he could not solve, and decided to write the whole computation himself (@01:45, @02:19, @03:22). He lists what PyTorch gives you that he had to replace, ports each layer from PyTorch to explicit PyTorch, a hand-derived backward and plain C on float arrays checked against the PyTorch reference, then strings the layers into one dependency-free C file with all memory allocated once (@03:55, @05:00, @05:32, @06:37, @07:09, @08:48). Moving to CUDA, he develops kernels that match the C version exactly, finds CUDA harder to learn than he expected, and credits contributors who arrived from the internet with much of the optimisation, from cuBLAS and cuDNN flash attention to mixed precision, Packed128, determinism and a sharded optimizer, while he rejected complexity that did not pay for itself (@10:27, @11:33, @13:11, @14:17, @15:58, @17:05). The result reproduces GPT-2 (1.6B) on one H100 node in about 24 hours and, at the time of the 1.6B post, used about 30% less memory and trained about 20% faster than PyTorch, specifically for GPT-2 (@17:38, @18:10, @19:17). He closes with a further motivation: if llm.c is like writing assembly by hand, LLMs that become better at coding may act as a compiler that writes such code for any custom application, with llm.c as example code in their context (@20:59, @21:32, @22:05, @22:37).

## Key points
- Origin: torch.compile errors, stages of grief, writing it himself; Maldives jetlag; contributors; CUDA harder to learn than expected; Llama 3 and fp8 coming; forks → [[llm-c]]
- What PyTorch provides (array, autograd, device, dtype, compile, distributed) and what dropping it costs → [[pytorch]]
- Layer by layer: explicit PyTorch, hand-derived backward, C on float arrays, string together, CUDA kernels v1…v6 → [[port-a-pytorch-model-to-c-and-cuda]]
- PyTorch becomes only the reference to check correctness; kernels match the specification exactly → [[verify-against-a-reference-implementation]]
- No tensor abstraction, just float arrays; why should it be more complicated → [[neural-net-training-should-not-be-complicated]]
- Too much complexity for not enough gain: CUDA streams nuked, PRs rejected, ZeRO-2 not merged → [[small-hackable-educational-code]]
- cuBLAS, cuDNN flash attention, bf16, fusions, recompute, Packed128 and SASS, determinism without atomics, NCCL, ZeRO-1, multi-node, ~50% MFU → [[compute-efficiency]]
- ~30% less memory, ~20% faster than PyTorch for GPT-2 training at the time; anything else is a lot of trouble → [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]
- GPT-2 (1.6B), one H100 node, ~24 hours, roughly $600; beats GPT-2 on HellaSwag → [[reproduce-a-published-model]], [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]
- People came from the internet to help; one of his favourite things about an open-source MIT repo → [[build-and-publish-projects]]
- torch.compile as GCC for Software 2.0, llm.c as assembly → [[software-3-0]]
- LLMs as a compiler for custom applications; Python and PyTorch as a crutch for finite humans; llm.c as few-shot example code → [[llms-may-write-custom-low-level-code-for-any-application]], [[prompting-llms]]

## Fed pages
- [[llm-c]]
- [[pytorch]]
- [[port-a-pytorch-model-to-c-and-cuda]]
- [[verify-against-a-reference-implementation]]
- [[neural-net-training-should-not-be-complicated]]
- [[small-hackable-educational-code]]
- [[compute-efficiency]]
- [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]
- [[reproduce-a-published-model]]
- [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]
- [[build-and-publish-projects]]
- [[software-3-0]]
- [[llms-may-write-custom-low-level-code-for-any-application]]
- [[prompting-llms]]
