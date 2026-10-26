# Digest: minGPT README
- raw: raw/github/karpathy__minGPT.md · published: 2023-01-08 · medium: github · words: 1545
- source slug: github-2023-01-08-mingpt-readme

## Source page
```
---
type: source
raw_path: raw/github/karpathy__minGPT.md
published: 2023-01-08
medium: github
summary: README of minGPT, his roughly 300-line PyTorch re-implementation of GPT training and inference, built to be small, clean and educational, and marked semi-archived in January 2023 in favour of its rewrite nanoGPT.
url: https://github.com/karpathy/minGPT
title: minGPT README
---
# minGPT README
Raw: [[raw/github/karpathy__minGPT]] · Original: https://github.com/karpathy/minGPT

Dated by the README's last commit (37baab7); the repo itself is older.

## Summary
minGPT is a PyTorch re-implementation of GPT covering both training and inference, written to be small, clean, interpretable and educational because he found existing implementations sprawling (§intro). He states that GPT is not a complicated model: a sequence of indices goes into a Transformer and a probability distribution over the next index comes out, with most of the complexity in batching for efficiency, and the model fits in about 300 lines (§intro). A January 2023 note declares the repo semi-archived and points to his rewrite nanoGPT; being referenced widely in notebooks, blogs, courses and books made him less willing to make large changes, and he also wanted to move from a sole focus on education to code that stays simple and hackable but has "teeth" (§intro). The library is three files, model, BPE tokenizer and a GPT-independent trainer, plus demo projects such as an adder trained from scratch and a character-level model (§intro). The README shows how to instantiate and train a GPT-2 (124M) configuration (§Usage), lists open todos (§todos), and ends with reference code and his own condensed implementation notes from the GPT-1, GPT-2, GPT-3 and Image GPT papers (§References).

## Key points
- What minGPT is, its three-file layout, demos and semi-archived status → [[mingpt]]
- minGPT superseded by his rewrite nanoGPT, and why → [[nanogpt]]
- GPT as indices in, next-index distribution out; paper-by-paper architecture and training notes → [[gpt-architecture]]
- "GPT is not a complicated model" → [[gpt-is-not-a-complicated-model]]
- Small, clean, interpretable, educational as the design goal → [[small-hackable-educational-code]]

## Fed pages
- [[mingpt]]
- [[nanogpt]]
- [[gpt-architecture]]
- [[gpt-is-not-a-complicated-model]]
- [[small-hackable-educational-code]]
```

## Candidates
### artifact: mingpt
- existing: no (the [[nanogpt]] page mentions minGPT in prose but there is no page or alias)
- aliases: [minGPT]
- frontmatter: repo_url https://github.com/karpathy/minGPT · language Python · status superseded (semi-archived by his own note, rewrite is nanoGPT)
- statements:
  - A PyTorch re-implementation of GPT, both training and inference (§intro)
  - Design goal: small, clean, interpretable and educational, because he found most available GPT implementations somewhat sprawling (§intro)
  - The model is about 300 lines of code in `mingpt/model.py` (§intro)
  - As of January 2023 he describes it as semi-archived and may still accept and change some details (§intro)
  - It became referenced across notebooks, blogs, courses and books, which made him less willing to make the bigger changes he wanted (§intro)
  - He wanted to change direction from a sole focus on education to something still simple and hackable but with teeth: reproducing medium-sized industry benchmarks and accepting some tradeoffs for runtime efficiency; that became nanoGPT (§intro)
  - Three files: `model.py` (Transformer definition), `bpe.py` (a mildly refactored Byte Pair Encoder matching OpenAI's GPT), `trainer.py` (GPT-independent PyTorch training boilerplate) (§intro)
  - Demos: `projects/adder` trains a GPT from scratch to add numbers, inspired by the GPT-3 paper's addition section; `projects/chargpt` trains a character-level model on a text file; `demo.ipynb` is a sorting example; `generate.ipynb` loads pretrained GPT-2 and generates from a prompt (§intro)
  - Installable with `pip install -e .`; the README shows a GPT-2 124M configuration (vocab 50257, block size 1024) and a Trainer with learning rate, max iterations and batch size (§Library Installation, §Usage)
  - Unit test coverage described by him as not great yet (§Unit tests)
  - Open todos include finetuning and dialog demos, mixed precision, distributed training, reproducing benchmarks, proper logging, a requirements file, and loading weights beyond gpt2-* (§todos)
  - Reference code he points to: openai/gpt-2 (model but no training code), openai/image-gpt, huggingface/transformers' language-modeling example, which he calls full-featured but hard to trace (§References)
  - Licence MIT (§License)
- relation to existing pages: **superseded by** [[nanogpt]]. The nanoGPT page already says nanoGPT is "a rewrite of minGPT" and prioritises "teeth over education" ([[github-2025-11-12-nanogpt-readme]] §intro); this source gives the minGPT-side account of the same handover, dated January 2023. Add this source to [[nanogpt]] `sources` with a sentence on why minGPT was frozen. Also link [[makemore]] (sibling educational repo, see makemore digest) and the future lecture source `youtube-2023-01-17-gpt-from-scratch` (not in index yet).

### topic: gpt-architecture
- existing: no (no GPT topic or alias in index)
- aliases: [GPT, GPT-1, GPT-2, GPT-3, Image GPT, decoder-only Transformer]
- statements:
  - All that happens in GPT is that a sequence of indices feeds into a Transformer and a probability distribution over the next index comes out (§intro)
  - Most of the implementation complexity is being clever with batching, across examples and over sequence length, for efficiency (§intro)
  - GPT-1 (per his notes on the paper): 12-layer decoder-only Transformer with masked self-attention, 768-dimensional states, 12 heads, 3072-dimensional feed-forward, learned position embeddings, GELU, BPE with 40,000 merges, dropout 0.1, about 117M parameters (§References (GPT-1))
  - GPT-2 (per his notes): LayerNorm moved to the input of each sub-block plus one after the final block, residual weights scaled by 1/√N at init, vocabulary 50,257, context 1024, batch 512, 48 layers and d_model 1600 for about 1.542B parameters (§References (GPT-2))
  - He flags that he could not find the 1/√N residual initialisation in OpenAI's released GPT-2 code, only partly in image-gpt (§References (GPT-2))
  - GPT-3 (per his notes): same architecture as GPT-2 with alternating dense and locally banded sparse attention, dff = 4·d_model, context 2048, Adam β2 = 0.95, weight decay 0.1, gradient clipping at 1.0, linear warmup then cosine decay to 10%, batch size ramped up during training; largest model 96 layers, 96 heads, d_model 12,288, 175B parameters (§References (GPT-3))
  - Image GPT (per his notes): pixels in raster order with a 512-colour k-means palette, GPT-2 model code with Sparse-Transformer-style layer-dependent init and zero-initialised logit projections, no dropout, no weight decay (§References (Image GPT))
- caution: the §References bullets are his condensed reading notes of OpenAI's papers, interspersed with his own asides. Attribute the numbers to "his notes on the paper", not to him as claims about his own models.

### claim: gpt-is-not-a-complicated-model
- existing: no
- title as a sentence: GPT is not a complicated model
- confidence: stated
- quote: "GPT is not a complicated model" (§intro)
- stated_on: 2023-01-08 (the README is older; this is the snapshot date)
- topic: [[gpt-architecture]]
- context: he backs it with the roughly 300-line implementation and the indices-in, distribution-out description; complexity comes from batching, not the model (§intro)
- relation to existing pages: none in index. Candidate future `supports` link with nanoGPT's ~300-line model statement already on [[nanogpt]] ([[github-2025-11-12-nanogpt-readme]] §intro), if merge considers that a claim.

### method: small-hackable-educational-code
- existing: no (shared candidate with the makemore and ng-video-lecture digests; create once, feed from all three)
- statements from this source:
  - minGPT tries to be small, clean, interpretable and educational, in contrast to sprawling implementations (§intro)
  - The whole model is about 300 lines; the library is three files (§intro)
  - He criticises the Hugging Face language-modeling example as full-featured but hard to trace, with large functions mostly unused in the default setting (§References)
  - The limit of the approach, in his telling: once a repo is widely referenced, large changes become harder, and education-only code lacks the "teeth" to reproduce benchmarks, which is why he started nanoGPT (§intro)

### timeline (optional): gpt-training-repos-over-time
- existing: no
- topic: [[small-hackable-educational-code]] or [[gpt-architecture]], merge to decide
- entries available so far: minGPT semi-archived Jan 2023 → nanoGPT ([[github-2023-01-08-mingpt-readme]] §intro); nanoGPT deprecated Nov 2025 → nanochat ([[github-2025-11-12-nanogpt-readme]] §intro); nanochat ([[github-2026-07-03-nanochat-readme]]). Only create if merge wants a lineage page; §7.7 requires timelines only for extends/contradicts claims.

## Quotes
- "GPT is not a complicated model" (§intro) — 6 words
- "minGPT tries to be small, clean, interpretable and educational" (§intro) — 9 words
- "minGPT is in a semi-archived state." (§intro) — 6 words
- "The majority of the complexity is just being clever with batching" (§intro) — 11 words

## Notes for merge
- Read at commit 37baab71b9abea1b76ab957409a1cc2fbfba8a26 (2023-01-08). The repo is from 2020; the published date is the snapshot date. The in-text "note (Jan 2023)" matches the snapshot date, so this snapshot is the one that announced the semi-archive.
- Heading map: text before `### Library Installation` is §intro; H3 headings are Library Installation, Usage, Unit tests, todos, References, License. The four H4 headings under References are full paper titles; I cite them abbreviated as §References (GPT-1), (GPT-2), (GPT-3), (Image GPT). Expand to the full titles if lint requires exact headings.
- The README's intro grammar is loose ("can a bit sprawling"); paraphrased, not quoted.
- Several §References bullets are near-verbatim from OpenAI's papers, not his own prose. Do not quote them as his words; the only quotes above are from §intro.
- Existing [[nanogpt]] page: `status: superseded` and its intro sentence about "teeth over education" already align with this source. Suggested update there: add `[[github-2023-01-08-mingpt-readme]]` to `sources` and one sentence that minGPT's wide adoption and education-only focus are the reasons he gave for the rewrite (§intro). Set [[mingpt]] `status: superseded` and link both ways.
- The `image-gpt` asides contain his unresolved questions ("huh", "how many heads?"); report them as open questions he raised, not findings.
