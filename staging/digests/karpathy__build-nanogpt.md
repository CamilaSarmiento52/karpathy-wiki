# Digest: build-nanogpt README
- raw: raw/github/karpathy__build-nanogpt.md · published: 2024-06-17 · medium: github · words: 686
- source slug: github-2024-06-17-build-nanogpt-readme

## Source page
```
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

Dated by the README's last commit (f6d194b).

## Summary
The repo is a from-scratch reproduction of nanoGPT, its git commits kept step by step and clean so the history can be walked, with a YouTube lecture in which he introduces each commit (§intro). It starts from an empty file and reaches a reproduction of GPT-2 (124M), and with more patience or money GPT-3 models; he says reproducing the 124M model is now a matter of about an hour and $10 (§intro). He notes that GPT-2 and GPT-3 are simple language models trained on internet documents that only "dream" such documents, so the repo does not cover chat finetuning; SFT, conceptually simple, comes later (§intro). Sample completions after 10B and 40B tokens illustrate the base model (§intro). The README lists errata, mostly PyTorch details, and points to litGPT and TinyLlama for production-grade runs (§Errata, §Prod).

## Key points
- The repo, its video, errata and production pointers → [[build-nanogpt]]
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
```

## Candidates
### artifact: build-nanogpt
- existing: no
- aliases: [build nanoGPT, Let's reproduce GPT-2 (124M)]
- frontmatter: repo_url https://github.com/karpathy/build-nanogpt · language Python · status active
- statements:
  - Holds the from-scratch reproduction of nanoGPT; commits kept step by step and clean so one can walk the history and see it built slowly; an accompanying YouTube lecture introduces each commit (§intro)
  - Starts from an empty file and works up to reproducing GPT-2 (124M); with more patience or money it can reproduce GPT-3 models (§intro)
  - GPT-2 (124M) probably trained for quite some time in 2019; today reproducing it takes about 1 hour and $10, on a cloud GPU box if needed (he recommends Lambda) (§intro)
  - Does not cover chat finetuning; that comes later (§intro)
  - Sample outputs for the prompt "Hello, I'm a language model," after 10B and 40B tokens of training (§intro)
  - The README is also meant as the place for FAQ and errata, of which he is sure there will be a number; discussion on GitHub Discussions and the Zero To Hero Discord #nanoGPT channel (§intro)
  - Errata: a leftover `register_buffer` of the attention bias after switching to flash attention; older PyTorch converting uint16 to long; `torch.autocast` wanting a device type rather than a device; `require_backward_grad_sync` affecting the forward pass too (§Errata)
  - For production-grade runs very similar to nanoGPT he recommends litGPT and TinyLlama (§Prod)
  - The FAQ section is empty at snapshot time (§FAQ)
- relation: links to [[nanogpt]] (what it reproduces); video "Let's reproduce GPT-2 (124M)" (l8pRSuU81PU) has no source page.

### artifact: nanogpt
- existing: yes
- statements:
  - build-nanogpt is a from-scratch reproduction of nanoGPT, built up commit by commit (§intro)

### method: spelled-out-build-from-scratch
- existing: yes
- statements:
  - Start from an empty file and work up to reproducing GPT-2 (124M) (§intro)
  - Keep the commits step by step and clean so the history shows the build, and introduce each commit in the video (§intro)
- relation: same pattern as step 20 "Release the git log" ([[youtube-2023-01-17-gpt-from-scratch]] @1:54:50); this repo makes the commit-per-step structure explicit.

### method: small-hackable-educational-code
- existing: yes
- statements:
  - For production-grade runs he points elsewhere (litGPT, TinyLlama) rather than growing this repo (§Prod)
  - Commit history kept clean for walkthrough (§intro); matches the existing step "Publish with the history" ([[github-2023-01-31-ng-video-lecture-readme]] §intro)

### claim: pretraining-gives-a-document-completer
- existing: yes
- relation: supports. Here he says GPT-2 and GPT-3 are simple language models trained on internet documents that only "dream" internet documents, and that you cannot talk to them as with ChatGPT (§intro); the claim page has pretraining giving a document completer that babbles internet until finetuned ([[youtube-2023-01-17-gpt-from-scratch]] @1:51:29). Same view about 17 months later; `supports`, not `extends`.

### topic: pretraining-and-finetuning
- existing: yes
- aliases to add: SFT, supervised finetuning
- statements:
  - The finetuning process comes after pretraining and is quite simple conceptually: SFT is just swapping out the dataset and continuing the training (§intro)
  - build-nanogpt covers only the pretraining part; chat finetuning will be covered later (§intro)
- relation: compatible with the GPT lecture's statement that the finetuning stage is much harder to replicate because the data is internal to OpenAI ([[youtube-2023-01-17-gpt-from-scratch]] @1:54:16): one is about conceptual simplicity, the other about replication. Not a contradiction. Also matches nanoGPT's finetuning-is-training-from-a-checkpoint ([[github-2025-11-12-nanogpt-readme]] §finetuning).

### topic: pytorch
- existing: yes
- statements:
  - `torch.autocast`'s `device_type` wants only the type (e.g. `cuda`, not `cuda:3`) and errors in some PyTorch versions if given a device; he is not sure mapping `mps` to CPU is the intended way (§Errata)
  - Earlier PyTorch versions may struggle converting uint16 to long; the fix converts via numpy int32 first (§Errata)
  - Confusingly, `model.require_backward_grad_sync` is used by both forward and backward passes (§Errata)
- relation: small supporting detail for [[pytorch-documentation-is-unreliable]]'s spirit, but he does not criticise the docs here; no link proposed.

## Quotes
- "The git commits were specifically kept step by step and clean" (§intro)
- "We basically start from an empty file" (§intro)
- "today, reproducing it is a matter of ~1hr and ~$10" (§intro)
- "all they do is "dream" internet documents" (§intro)
- "SFT is just about swapping out the dataset and continuing the training" (§intro)
- "of which I am sure there will be a number" (§intro)
- "I tried to stubbornly just pass `device` hoping it works ok" (§Errata)

## Notes for merge
- Locations: text under the `# build nanoGPT` H1 is `§intro`; then `§Video`, `§Errata`, `§Prod`, `§FAQ` (empty), `§License`.
- "~1hr and ~$10" is for GPT-2 (124M) on rented GPUs; nanochat's ~$48 / ~2 hours is for beating GPT-2's CORE score with a larger model ([[github-2026-07-03-nanochat-readme]] §Leaderboard). Different targets; do not set them side by side as one trend without a **Note:** that says so.
- Raw grammar: "GPT-2 and GPT-3 and both simple language models", "this repo/video this does not cover"; avoid quoting those.
- "Lol." after the samples, and the sample completions themselves are model output, not his words; do not quote the samples as him.
- The video (l8pRSuU81PU) is not ingested; nothing here says what the video covers beyond introducing each commit.
- Errata reflect a later edit than the "once the video comes out" text; the README mixes pre- and post-release text.
