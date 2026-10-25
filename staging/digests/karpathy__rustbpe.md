# Digest: rustbpe README
- raw: raw/github/karpathy__rustbpe.md · published: 2026-01-03 · medium: github · words: 670 (frontmatter) · commit: ddf848f6961a0655dc8693742fc338e5682c0d3b
- source slug: github-2026-01-03-rustbpe-readme

Number tags: **[setting]** values in his usage examples; **[comparison]** another library's
property. The README reports no runs, so nothing here is **[measured]**, **[target]** or
**[estimate]**.

Headings (exact): `§intro` (text under `# rustbpe`, before `## Features`, as for the minbpe
README), `§Features`, `§Installation`, `§Usage` (`### Training`, `### Export to tiktoken`,
`### Custom regex pattern`), `§API Reference`, `§Development`, `§How BPE works`,
`§LLM Assistance note`, `§License`.

## Source page
```
---
type: source
raw_path: raw/github/karpathy__rustbpe.md
published: 2026-01-03
medium: github
summary: "README of rustbpe, his Rust BPE tokenizer trainer with Python bindings, billed as the missing tiktoken training code: train with rustbpe, export to tiktoken for inference; the Rust was written against his own Python reference with equality tests and significant help from ChatGPT and Claude Code."
url: https://github.com/karpathy/rustbpe
title: rustbpe README
---
# rustbpe README
Raw: [[raw/github/karpathy__rustbpe]] · Original: https://github.com/karpathy/rustbpe

Dated by the README's commit ddf848f. Text under the `# rustbpe` title, before the first `##` heading, is cited `§intro`.

## Summary
rustbpe is a lightweight Rust library with Python bindings for training GPT-style BPE tokenizers, which he calls "the missing tiktoken training code" (§intro). He places it against three alternatives: tiktoken is excellent for inference but cannot train, Hugging Face `tokenizers` trains but carries years of accumulated complexity, and his own minbpe does both but only in unoptimised Python (§intro). The intended use is to train with rustbpe and export to tiktoken for fast inference, with GPT-4-style regex pre-tokenization by default, parallel training and batch encoding (§Features, §Usage). The README explains BPE as starting from 256 byte tokens and repeatedly merging the most frequent adjacent pair (§How BPE works). In an LLM-assistance note he says he wrote the Python reference himself, then the Rust against it with equality tests, with significant help from ChatGPT and Claude Code Opus 4.5 because he is not a Rust developer (§LLM Assistance note).

## Key points
- The repo, its API and its gap between tiktoken, HF tokenizers and minbpe → [[rustbpe]]
- Byte-level BPE in four steps; GPT-4 regex pattern by default; tiktoken export → [[tokenization]]
- minbpe trains and infers, but only in Python and slowly → [[minbpe]]
- tiktoken for inference plus training code is the combination it provides → [[he-prefers-tiktoken-byte-level-bpe-to-sentencepiece]]
- The tokenizer nanochat uses, now its own repo → [[nanochat]]
- Python reference first, Rust tested for equality against it → [[verify-against-a-reference-implementation]]
- LLM help in a language he does not know; disclosed in the README → [[coding-models-are-weak-at-code-never-written-before]], [[vibe-coding]]

## Fed pages
- [[rustbpe]]
- [[tokenization]]
- [[minbpe]]
- [[nanochat]]
- [[he-prefers-tiktoken-byte-level-bpe-to-sentencepiece]]
- [[verify-against-a-reference-implementation]]
- [[coding-models-are-weak-at-code-never-written-before]]
- [[vibe-coding]]
```

## Candidates

### artifact: rustbpe
- existing: no. Not in `wiki/index/artifacts.md` and not an alias anywhere (grep for "rustbpe" finds only the nanochat artifact and the launch source page, as a tokenizer name). The prompt points rustbpe at [[tokenization]]; that page should get the sentences below, but a separate repo with its own README fits the artifact type (as [[minbpe]] has its page). Merge decides; if folded, put `rustbpe` in [[tokenization]]'s and [[nanochat]]'s aliases instead.
- repo_url: https://github.com/karpathy/rustbpe · language: Rust (with Python bindings) · status: active (no deprecation note)
- aliases: rustbpe, rust BPE tokenizer, nanochat tokenizer trainer
- statements:
  - A lightweight Rust library for training GPT-style BPE tokenizers, with Python bindings via PyO3, installable with `pip install rustbpe` (§intro, §Features, §Installation).
  - He calls it "the missing tiktoken training code" (§intro).
  - The gap it fills: tiktoken is excellent for inference but does not train; Hugging Face `tokenizers` trains but carries significant complexity from years of tokenizer variants; minbpe trains and infers, but only in Python and not optimised for speed (§intro). [comparison]
  - Main use case: train with rustbpe, then export to tiktoken for inference, via the pattern and mergeable ranks the API exposes (§Usage, §API Reference).
  - Features: parallel training (rayon), GPT-4-style regex pre-tokenization by default with a custom pattern allowed, direct tiktoken export, parallel batch encoding (§Features, §Usage).
  - Vocabulary size is 256 plus the number of merges (§API Reference). Example vocab sizes 4096 and 8192 (§Usage). [setting, examples only]
  - Tests: `cargo test` for the core algorithm in Rust, pytest for the Python side; the whole implementation, bindings and tests are in one `src/lib.rs` (§Development).
  - MIT licence (§License).
  - LLM assistance: he wrote the Python reference personally and from scratch and understands it fully, then wrote the Rust against it with equality tests; not a Rust developer, he had significant help from ChatGPT and Claude Code Opus 4.5, and apologises if some Rust is not properly arranged, inviting Issues and PRs (§LLM Assistance note).
- **Note:** the README does not mention nanochat. The link to nanochat comes from the 2025-10-13 launch post, which describes nanochat's own Rust tokenizer trained with OpenAI's algorithm and tested equal to the Python ([[github-2025-10-13-nanochat-discussion-introducing]] §Environment setup). That they are the same code is likely but not stated in either source; write it as a **Note:**.

### topic: tokenization
- existing: yes
- statements:
  - BPE builds a vocabulary iteratively: start with the 256 byte-level tokens, count adjacent pairs in the corpus, merge the most frequent pair into a new token, repeat to the target vocabulary size; the result represents common patterns efficiently and can encode any input (§How BPE works).
  - rustbpe uses the GPT-4 tokenization pattern for regex pre-tokenization by default (§Features, §Usage (Custom regex pattern)).

### artifact: minbpe
- existing: yes
- statement: his minbpe handles both training and inference, but only in Python and not optimised for speed (§intro).
- **Note:** minbpe's todos list a faster version in Rust among others ([[github-2024-04-22-minbpe-readme]] §todos); rustbpe fits that todo, but neither README says so. Connection only.

### claim (existing): he-prefers-tiktoken-byte-level-bpe-to-sentencepiece
- existing: yes (2024-02-20; the launch post was already added as support for the tiktoken half)
- statement: rustbpe exists to supply the training code tiktoken lacks, so you train byte-level BPE in rustbpe and infer in tiktoken (§intro, §Usage (Export to tiktoken)).
- relation: **supports.** In 2024 he said the ideal, tiktoken with training code, did not exist ([[youtube-2024-02-20-gpt-tokenizer]] @2:11:45, @2:12:18); here he ships that pairing and names it "the missing tiktoken training code" (§intro). Like the launch post, it says nothing about SentencePiece: evidence for the tiktoken half only.

### claim (existing): coding-models-are-weak-at-code-never-written-before
- existing: yes (2025-10-17)
- statement: §LLM Assistance note, as above.
- relation: **supports** the claim's scoped part: on 2025-10-17 he said agents helped him in an unfamiliar language, Rust ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @34:26); here, with the date of this README, he says he had significant help from ChatGPT and Claude Code Opus 4.5 because he is not a Rust developer, while the reference he understands fully was his own (§LLM Assistance note). Not evidence on the "never written before" half; BPE has been written before, by him.

### topic: vibe-coding
- existing: yes
- statement: the README's own account of how the Rust was written (§LLM Assistance note).
- **Note:** the 2025-12-19 review says he vibe-coded nanochat's Rust BPE tokenizer instead of learning Rust to that level ([[blog-2025-12-19-year-in-review-2025]] §5). This README adds that the Rust was checked by equality tests against a Python reference he wrote and understands (§LLM Assistance note). Both can be true; the README does not use the word "vibe". Merge: a dated sentence on [[vibe-coding]] and possibly a line on [[vibe-coding-over-time]]; not a change of mind.

### method: verify-against-a-reference-implementation
- existing: yes
- statement: he wrote the Python reference from scratch, then wrote the Rust against it "with tests for equality"; all equality tests pass as far as he is aware (§LLM Assistance note).
- fits the method's core step (run the same input through a known-good implementation and match its output); here the known-good one is his own Python.

### artifact: nanochat
- existing: yes
- statement: none from this README directly (it does not name nanochat). Add only the **Note:** linking [[rustbpe]] from nanochat's tokenizer bullet, citing the launch post for nanochat's side.

## Quotes
- "The missing tiktoken training code" (§intro)
- "carries significant complexity from years of accumulated tokenizer variants" (§intro)
- "only in Python and not optimized for speed" (§intro)
- "Train your tokenizer with rustbpe, then export to tiktoken for fast inference." (§intro)
- "The main use case: train with rustbpe, inference with tiktoken." (§Usage)
- "I wrote the Python reference code personally and from scratch" (§LLM Assistance note)
- "I am not a Rust developer by background" (§LLM Assistance note)
- "All the equality tests pass as far as I am aware" (§LLM Assistance note)

All grep-checked (one match each, under 15 words). "The missing tiktoken training code" is a blockquote tagline in the raw (`> `).

## Notes for merge
- **Date:** dated by commit ddf848f (2026-01-03). The repo may predate that; the launch post (2025-10-13) already had a Rust tokenizer inside nanochat. Do not write "split out of nanochat" or "later released"; neither source says so.
- **Python reference:** the README says he wrote "the Python reference code", but does not say whether that is minbpe or other code. Do not equate them.
- "Claude Code Opus 4.5" is his wording for the tool and model.
- The README is mostly installation and API; code blocks are usage, not statements. Do not quote API docs as his views.
- No numbers from runs; vocab sizes are example arguments.
- **AI-written text (CLAUDE.md §3):** the LLM Assistance note says the Rust code had significant LLM help; it does not say the README text was AI-written. Treat the README prose as his. Do not cite the Rust code itself as his wording.
