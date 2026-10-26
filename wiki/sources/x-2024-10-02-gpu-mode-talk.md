---
type: source
raw_path: raw/x/1841536804073439268.md
published: 2024-10-02
medium: x
summary: "A single post outlining his GPU MODE workshop talk on llm.c: why he left PyTorch, how he ported layers to C and then CUDA, the optimisations and multi-GPU work up to the $672 GPT-2 (1.6B) reproduction, the contributors, and a closing thought that LLMs may come to write custom binaries like llm.c directly."
url: https://x.com/karpathy/status/1841536804073439268
title: "I gave a talk at GPU MODE workshop last week on llm.c"
---
# I gave a talk at GPU MODE workshop last week on llm.c
Raw: [[raw/x/1841536804073439268]] · Original: https://x.com/karpathy/status/1841536804073439268

One post, so no locations are given. It says the talk was "last week"; it does not link or name a recording. **Note:** the CUDA MODE keynote video, [[talk-2024-10-03-cuda-mode-keynote]] (published 2024-10-03), has the same outline and the same closing thought, so this post very likely describes that talk; that is the wiki's inference, not something either source says.

## Summary
He announces a talk on llm.c that he says he gave at the GPU MODE workshop "last week", and lists what it covered. The list runs from the origin of llm.c and being without PyTorch, which meant re-inventing array, autograd, device, dtype, compile and distributed, through his four-step port of a PyTorch layer (explicit PyTorch, a hand-written backward, a C port, stringing the layers together) to one dependency-free C file that compiles and runs about instantly, pre-plans and allocates memory once and is fully deterministic. It then lists the CUDA work: fp32 on GPU, cuBLAS matmuls, cuDNN flash attention, bfloat16 mixed precision, kernel fusions, Packed128, stochastic rounding, multi-GPU with NCCL and a sharded optimizer, and multi-node, ending in the GPT-2 (1.6B) reproduction on one 8×H100 node in 24 hours for $672, which he says achieved, at the time, 29% less memory and 19% faster training than PyTorch nightly. It closes with contributors arriving through open source, an imminent Llama 3 port, many forks, and a last thought that software abstractions such as Python and PyTorch exist because humans are finite, and that more capable LLMs may export custom binaries like llm.c for any application directly.

## Key points
- Talk outline: origin, the PyTorch-free stack, porting, CUDA, multi-GPU, the 1.6B result, contributors, Llama 3, forks → [[llm-c]]
- The four-step layer port, from explicit PyTorch to C, strung together, then CUDA → [[port-a-pytorch-model-to-c-and-cuda]]
- One C file, no dependencies, memory allocated once, fully deterministic, portable → [[small-hackable-educational-code]]
- cuBLAS, cuDNN flash attention, bf16, kernel fusions, Packed128, stochastic rounding, NCCL, sharded optimizer, multi-node → [[compute-efficiency]]
- 29% less memory and 19% faster than PyTorch nightly "at the time" → [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]
- GPT-2 (1.6B) on one 8×H100 node, 24 hours, $672 → [[reproduce-a-published-model]]
- Open source attracts "Avengers from the internet" → [[build-and-publish-projects]]
- Abstractions exist because humans are finite; LLMs may export custom binaries like llm.c → [[llms-may-write-custom-low-level-code-for-any-application]]

## Fed pages
- [[llm-c]]
- [[port-a-pytorch-model-to-c-and-cuda]]
- [[small-hackable-educational-code]]
- [[compute-efficiency]]
- [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]]
- [[reproduce-a-published-model]]
- [[build-and-publish-projects]]
- [[llms-may-write-custom-low-level-code-for-any-application]]
