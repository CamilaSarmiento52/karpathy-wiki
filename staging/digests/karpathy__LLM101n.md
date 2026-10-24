# Digest: LLM101n README
- raw: raw/github/karpathy__LLM101n.md · published: 2024-08-01 · medium: github · words: 338 (frontmatter; 361 by `wc -w` with markup)
- source slug: github-2024-08-01-llm101n-readme
- commit: c6de374acd4b57b6fea3b1a1b6e945d58f19cd30

## Source page
```
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

## Summary
The README opens with a banner saying the course does not yet exist, that it is being developed by Eureka Labs, and that he is archiving the repo until it is ready (§intro). It describes a course, "Let's build a Storyteller", in which you build a storyteller LLM that helps you create, refine and illustrate little stories, linking the TinyStories dataset (§intro). The plan is to build everything end to end, from basics to a working web app similar to ChatGPT, from scratch in Python, C and CUDA, with minimal computer science prerequisites, leaving the learner with a relatively deep understanding of AI, LLMs and deep learning (§intro). The syllabus lists 17 chapters, from a bigram language model and micrograd through attention, the Transformer, tokenization and optimization, three "Need for Speed" chapters on device, precision and distributed training, datasets, two inference chapters, two finetuning chapters, deployment and multimodal (§intro (Syllabus)). An appendix lists further topics still to be worked into the progression (§intro (Appendix)).

## Key points
- Planned course; not yet existing; developed by Eureka Labs; repo archived until ready → [[llm101n]]
- End to end, from scratch in Python, C and CUDA, minimal prerequisites, ChatGPT-like web app as endpoint → [[llm101n]], [[spelled-out-build-from-scratch]]
- Syllabus chapters on device, precision (fp16, bf16, fp8), distributed (DDP, ZeRO), kv-cache and quantization → [[llm101n]], [[compute-efficiency]]
- Syllabus starts from the bigram model, micrograd, attention, the Transformer and minBPE tokenization → [[llm101n]]
- Finetuning chapters: SFT (PEFT, LoRA, chat) and RL (RLHF, PPO, DPO) → [[llm101n]], [[pretraining-and-finetuning]]

## Fed pages
- [[llm101n]]
- [[spelled-out-build-from-scratch]]
- [[compute-efficiency]]
- [[pretraining-and-finetuning]]
- [[build-and-publish-projects]]
```

## Candidates
### artifact: llm101n
- existing: no (mentioned only on [[build-and-publish-projects]] and [[small-projects-can-snowball]], citing the Berkeley keynote @13:01, which says the wiki has no artifact page yet)
- repo_url: https://github.com/karpathy/LLM101n
- language: none yet (the README plans Python, C and CUDA; the snapshot has no code, only a README and a header image). Suggest `language: "Python / C / CUDA (planned)"` or similar; merge decides.
- status: **archived** — the banner says "Until it is ready I am archiving this repo" (§intro). Not `superseded`: the README does not name a replacement repo, only says the course is being developed by Eureka Labs.
- aliases: LLM101n, "LLM101n: Let's build a Storyteller", Storyteller course
- statements:
  - The banner says the course does not yet exist, is currently being developed by Eureka Labs, and that until it is ready he is archiving the repo (§intro).
  - The course would build a Storyteller AI LLM with which you create, refine and illustrate little stories; "stories" links the TinyStories dataset on Hugging Face (§intro).
  - Everything is to be built end to end, from basics to a functioning web app similar to ChatGPT, from scratch in Python, C and CUDA, with minimal computer science prerequisites (§intro).
  - By the end the learner should have a relatively deep understanding of AI, LLMs and deep learning more generally (§intro).
  - Syllabus, 17 chapters (§intro (Syllabus)): 01 Bigram Language Model; 02 Micrograd (machine learning, backpropagation); 03 N-gram model (MLP, matmul, gelu); 04 Attention (attention, softmax, positional encoder); 05 Transformer (residual, layernorm, GPT-2); 06 Tokenization (minBPE, BPE); 07 Optimization (initialization, AdamW); 08–10 Need for Speed I–III: Device (CPU, GPU), Precision (mixed precision, fp16, bf16, fp8), Distributed (DDP, ZeRO); 11 Datasets (data loading, synthetic data generation); 12 Inference I: kv-cache; 13 Inference II: Quantization; 14 Finetuning I: SFT (PEFT, LoRA, chat); 15 Finetuning II: RL (RLHF, PPO, DPO); 16 Deployment (API, web app); 17 Multimodal (VQVAE, diffusion transformer).
  - Appendix of further topics to work into the progression: programming languages (Assembly, C, Python); data types including ASCII, Unicode, UTF-8; tensor shapes, views, strides, contiguity; frameworks PyTorch and JAX; architectures GPT 1–4, Llama (RoPE, RMSNorm, GQA), MoE; multimodal images, audio, video, VQVAE, VQGAN, diffusion (§intro (Appendix)).
- Related (for merge): [[build-and-publish-projects]] (Berkeley keynote's mention; replace "The wiki has no artifact page for it yet" with a link), [[small-projects-can-snowball]], [[micrograd]], [[minbpe]], [[nn-zero-to-hero]], [[llm-c]] (C/CUDA). **Note:** candidates only — the README itself names minBPE and micrograd as chapter subjects but does not link those repos or mention Zero to Hero or llm.c.

### method: build-and-publish-projects
- existing: yes
- statements:
  - The Berkeley keynote's LLM101n mention can now link [[llm101n]]; the README snapshot dated 2024-08-01 says the course does not yet exist and the repo is archived until it is ready (§intro). **Note:** state the dates only; do not write that the project stalled or moved, since the README says only that Eureka Labs is developing it.

### method: spelled-out-build-from-scratch
- existing: yes
- statements:
  - The planned course builds everything end to end from basics, from scratch in Python, C and CUDA, with minimal prerequisites (§intro); the README opens with Feynman's "What I cannot create, I do not understand" as an epigraph (§intro). [the epigraph is Feynman's words, not his; do not quote it as him]
- relation: a plan, not a performed build; cite as stated intent only. Merge may prefer `context` here.

### topic: compute-efficiency
- existing: yes
- statements:
  - The syllabus gives three chapters to speed: device (CPU, GPU), precision (mixed precision, fp16, bf16, fp8) and distributed (distributed optimization, DDP, ZeRO), plus inference chapters on kv-cache and quantization (§intro (Syllabus)).
- note: chapter titles only, no explanation; merge may put this source in `context` rather than `sources`.

### topic: pretraining-and-finetuning
- existing: yes
- statements:
  - The syllabus splits finetuning into SFT (PEFT, LoRA, chat) and RL (RLHF, PPO, DPO) (§intro (Syllabus)).
- note: list of chapter headings only; `context` is probably the right field.

### claims
- none. The README states a plan and a status, not a position.

## Quotes
- "this course does not yet exist." (§intro)
- "Until it is ready I am archiving this repo" (§intro)
- "In this course we will build a Storyteller AI Large Language Model (LLM)." (§intro)
- "from scratch in Python, C and CUDA, and with minimal computer science prerequisites" (§intro)
- "you should have a relatively deep understanding of AI, LLMs, and deep learning" (§intro)

## Notes for merge
- **Status.** The banner is the basis for `status: archived`: "this course does not yet exist", "current being developed by Eureka Labs" (typo "current" in the raw), "Until it is ready I am archiving this repo". It is the only source in the wiki that mentions Eureka Labs (grep finds nothing in `wiki/`); the README links eurekalabs.ai but says nothing else about it. Do not add facts about Eureka Labs.
- The Berkeley keynote (published 2024-07-03) says he put LLM101n on GitHub two or three days earlier and that it was still raw (@13:01, as cited on [[build-and-publish-projects]]). This README snapshot is dated 2024-08-01 by its commit. Write both dates; do not write an interval or say it was archived "a month later".
- The only heading is the H1 title; everything is under it, so cite `§intro`, with the bold labels Syllabus and Appendix appended as in batch 2.
- The Feynman line is an epigraph quoting Richard Feynman, not his own words.
- No code in the snapshot; `language` is the planned stack.
- "N-gram model" chapter covers MLP, matmul and gelu; "Need for Speed" is his chapter naming. Chapter subtopic lists are terse; they are not explanations, so do not cite them as him explaining DDP, ZeRO, LoRA, etc.
