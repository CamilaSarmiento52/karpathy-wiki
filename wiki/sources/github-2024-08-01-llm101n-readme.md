---
type: source
raw_path: raw/github/karpathy__LLM101n.md
published: 2024-08-01
medium: github
summary: "The README of LLM101n, his planned course on building a storyteller LLM end to end from scratch, with a 17-chapter syllabus; a banner says the course does not yet exist, is being developed by Eureka Labs, and the repo is archived until it is ready."
url: https://github.com/karpathy/LLM101n
title: "LLM101n README"
---
# LLM101n README
Raw: [[raw/github/karpathy__LLM101n]] · Original: https://github.com/karpathy/LLM101n

Dated by its commit (c6de374). The only heading is the H1 title, so everything is cited as `§intro`, with the bold labels Syllabus and Appendix appended.

## Summary
The README opens with a banner saying the course does not yet exist, that it is being developed by Eureka Labs, and that he is archiving the repo until it is ready (§intro). It describes a course, "Let's build a Storyteller", in which you build a storyteller LLM that helps you create, refine and illustrate little stories, linking the TinyStories dataset (§intro). The plan is to build everything end to end, from basics to a working web app similar to ChatGPT, from scratch in Python, C and CUDA, with minimal computer science prerequisites, leaving the learner with a relatively deep understanding of AI, LLMs and deep learning (§intro). The syllabus lists 17 chapters, from a bigram language model and micrograd through attention, the Transformer, tokenization and optimization, three "Need for Speed" chapters on device, precision and distributed training, datasets, two inference chapters, two finetuning chapters, deployment and multimodal (§intro (Syllabus)). An appendix lists further topics still to be worked into the progression (§intro (Appendix)).

## Key points
- Planned course; not yet existing; developed by Eureka Labs; repo archived until ready → [[llm101n]], [[ai-for-education]]
- End to end, from scratch in Python, C and CUDA, minimal prerequisites, ChatGPT-like web app as endpoint → [[llm101n]], [[spelled-out-build-from-scratch]]
- Syllabus chapters on device, precision (fp16, bf16, fp8), distributed (DDP, ZeRO), kv-cache and quantization → [[llm101n]], [[compute-efficiency]]
- Syllabus starts from the bigram model, micrograd, attention, the Transformer and minBPE tokenization → [[llm101n]]
- Finetuning chapters: SFT (PEFT, LoRA, chat) and RL (RLHF, PPO, DPO) → [[llm101n]], [[pretraining-and-finetuning]]
- The Berkeley keynote's mention of LLM101n now links the artifact → [[build-and-publish-projects]]

## Fed pages
- [[llm101n]]
- [[ai-for-education]]
- [[spelled-out-build-from-scratch]]
- [[compute-efficiency]]
- [[pretraining-and-finetuning]]
- [[build-and-publish-projects]]
