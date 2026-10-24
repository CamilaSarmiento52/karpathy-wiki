---
type: source
raw_path: raw/github/karpathy__build-nanogpt.md
published: 2024-06-17
medium: github
summary: "README of build-nanogpt, a from-scratch reproduction of nanoGPT up to GPT-2 (124M) with step-by-step commits and an accompanying video; it notes that such base models only dream internet documents and lists errata."
url: https://github.com/karpathy/build-nanogpt
title: build-nanogpt README
---
# build-nanogpt README
Raw: [[raw/github/karpathy__build-nanogpt]] · Original: https://github.com/karpathy/build-nanogpt

Dated by the README's last commit (f6d194b). Text under the `# build nanoGPT` heading is cited as `§intro`; then `§Video`, `§Errata`, `§Prod`, `§FAQ` (empty).

## Summary
The repo is a from-scratch reproduction of nanoGPT, its git commits kept step by step and clean so the history can be walked, with a YouTube lecture in which he introduces each commit (§intro). It starts from an empty file and reaches a reproduction of GPT-2 (124M), and with more patience or money GPT-3 models; he says reproducing the 124M model is now a matter of about an hour and $10 (§intro). He notes that GPT-2 and GPT-3 are simple language models trained on internet documents that only "dream" such documents, so the repo does not cover chat finetuning; SFT, conceptually simple, comes later (§intro). Sample completions after 10B and 40B tokens illustrate the base model (§intro). The README lists errata, mostly PyTorch details, and points to litGPT and TinyLlama for production-grade runs (§Errata, §Prod).

## Key points
- The repo, its video, its cost, errata and production pointers → [[build-nanogpt]]
- A from-scratch rebuild of nanoGPT to GPT-2 (124M) → [[nanogpt]]
- Empty file to GPT-2, commits kept step by step, a video per commit → [[spelled-out-build-from-scratch]]
- Clean commit history as the teaching artefact; production work belongs in other repos → [[small-hackable-educational-code]]
- Base models only dream internet documents; you cannot talk to them like ChatGPT → [[pretraining-gives-a-document-completer]]
- SFT is conceptually just swapping the dataset and continuing training → [[pretraining-and-finetuning]]
- PyTorch errata: `torch.autocast`'s device_type, uint16 conversion, `require_backward_grad_sync` → [[pytorch]]

## Fed pages
- [[build-nanogpt]]
- [[nanogpt]]
- [[spelled-out-build-from-scratch]]
- [[small-hackable-educational-code]]
- [[pretraining-gives-a-document-completer]]
- [[pretraining-and-finetuning]]
- [[pytorch]]
