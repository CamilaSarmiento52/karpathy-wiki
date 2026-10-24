---
type: artifact
repo_url: https://github.com/karpathy/LLM101n
language: "Python / C / CUDA (planned; the repo holds only a README)"
status: archived
sources: ["[[github-2024-08-01-llm101n-readme]]", "[[talk-2024-07-03-berkeley-hackathon-keynote]]"]
aliases: [LLM101n, "LLM101n: Let's build a Storyteller", Storyteller course]
---
# LLM101n
His planned course "LLM101n: Let's build a Storyteller", in which learners would build a storyteller LLM with which you create, refine and illustrate little stories; the README's banner says the course does not yet exist, is being developed by Eureka Labs, and that he is archiving the repo until it is ready ([[github-2024-08-01-llm101n-readme]] §intro).

## What it demonstrates
- The plan: build everything end to end, from basics to a functioning web app similar to ChatGPT, from scratch in Python, C and CUDA, with minimal computer science prerequisites, so that by the end the learner has a relatively deep understanding of AI, LLMs and deep learning ([[github-2024-08-01-llm101n-readme]] §intro). The word "stories" links the TinyStories dataset ([[github-2024-08-01-llm101n-readme]] §intro).
- The syllabus, 17 chapters: bigram language model; micrograd; an N-gram model (MLP, matmul, GELU); attention; the Transformer (residual, layernorm, GPT-2); tokenization (minBPE, BPE); optimization (initialization, AdamW); three "Need for Speed" chapters on device (CPU, GPU), precision (mixed precision, fp16, bf16, fp8) and distributed (DDP, ZeRO); datasets (data loading, synthetic data generation); inference with a kv-cache and with quantization; finetuning with SFT (PEFT, LoRA, chat) and with RL (RLHF, PPO, DPO); deployment (API, web app); and multimodal (VQVAE, diffusion transformer) ([[github-2024-08-01-llm101n-readme]] §intro (Syllabus)).
- An appendix of topics still to be worked into the progression: programming languages (Assembly, C, Python), data types (ASCII, Unicode, UTF-8), tensor shapes, views, strides and contiguity, PyTorch and JAX, GPT 1–4, Llama (RoPE, RMSNorm, GQA) and MoE, and multimodal images, audio and video ([[github-2024-08-01-llm101n-readme]] §intro (Appendix)).
- The README opens with an epigraph from Richard Feynman, not his own words ([[github-2024-08-01-llm101n-readme]] §intro).
- In the Berkeley keynote, published 2024-07-03, he calls LLM101n his next class, says he had put it on GitHub two or three days earlier, and that it was still raw ([[talk-2024-07-03-berkeley-hackathon-keynote]] @13:01). The README snapshot here is dated 2024-08-01 by its commit ([[github-2024-08-01-llm101n-readme]] §intro).

## Related
- [[ai-for-education]] — his education plans
- [[build-and-publish-projects]], [[small-projects-can-snowball]] — the Berkeley keynote's mention
- [[spelled-out-build-from-scratch]] — how he has taught the same material
- **Note:** the syllabus names micrograd and minBPE as chapter subjects; the README does not link [[micrograd]], [[minbpe]] or [[nn-zero-to-hero]]
