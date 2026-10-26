# Digest: Train a GPT-4 tokenizer using huggingface Tokenizers
- raw: raw/github/karpathy__minbpe__discussion-98.md · published: 2025-08-08 · medium: github · words: 275 (frontmatter); 301 by wc
- source slug: github-2025-08-08-minbpe-gpt-4-tokenizer-discussion

Location scheme: no headings, so prose and code are both `§intro`. Comment lines inside the
code are his words too; cite them as `§intro (code)`.

## Source page
```
---
type: source
raw_path: raw/github/karpathy__minbpe__discussion-98.md
published: 2025-08-08
medium: github
summary: "A minbpe Discussion where he posts his best-guess configuration for training a GPT-4-style BPE tokenizer with the Hugging Face Tokenizers library, unsure it is correct."
url: https://github.com/karpathy/minbpe/discussions/98
title: Train a GPT-4 tokenizer using huggingface Tokenizers
---
# Train a GPT-4 tokenizer using huggingface Tokenizers
Raw: [[raw/github/karpathy__minbpe__discussion-98]] · Original: https://github.com/karpathy/minbpe/discussions/98

## Summary
In a Discussion on the [[minbpe]] repo he posts how he believes one could train a GPT-4 tokenizer on one's own documents with the Hugging Face Tokenizers library, after about an hour with its documentation and code, for future reference and comparison (§intro). The example trains a 32,768-token vocabulary with one special document-delimiter token on 1 billion characters of FineWeb-edu (§intro). He says he is not fully confident the configuration is correct (§intro). The code sets a BPE model with byte fallback, no normalizer, a pre-tokenizer that splits on the GPT-4 regex and then maps to bytes, a matching byte-level decoder, no post-processor, and a BPE trainer with no minimum frequency seeded with the byte-level alphabet (§intro (code)).

## Key points
- His HF Tokenizers recipe for a GPT-4-style tokenizer, posted on minbpe → [[minbpe]]
- The pieces of a GPT-4-style tokenizer as a library configures them: GPT-4 split regex, byte-level mapping, BPE training → [[tokenization]]

## Fed pages
- [[minbpe]]
- [[tokenization]]
```

## Candidates

### artifact: minbpe (existing)
- statement: the repo's Discussions hold his post (2025-08-08) on training a GPT-4 tokenizer with the Hugging Face Tokenizers library instead, kept for future reference and comparison (§intro).
- **Note:** the post does not compare the result with minbpe or mention minbpe's code; it is filed on the repo only. Write nothing beyond "posted on the minbpe Discussions".

### topic: tokenization (existing)
- statements:
  - He describes the example as training 32,768 tokens with only one special token, for the document delimiter, on 1B characters from FineWeb-edu-10B (§intro).
  - The pre-tokenizer splits text with the GPT-4 split pattern, isolating each match, then applies a byte-level mapping; the decoder is byte-level to pair with it (§intro (code)).
  - He marks `byte_fallback=True` on the BPE model as "needed!" and sets no unknown token (§intro (code)).
  - The trainer has no minimum frequency and starts from the byte-level alphabet; the only special token is `<|endoftext|>` (§intro (code)).
  - A code comment estimates the FineWeb-edu sample-10BT set at ~10B GPT-2 tokens, ~30B characters, at ~3 characters per token (§intro (code)).
  - He says he is not 100% confident it is configured correctly, and calls it his best shot (§intro).
- relation: none to claims. [[he-prefers-tiktoken-byte-level-bpe-to-sentencepiece]] concerns SentencePiece's byte fallback over code points; this config uses HF's `byte_fallback` flag alongside byte-level pre-tokenization. He does not comment on that, so no link; at most a reviewer's curiosity.

No claim (no position taken; he reports uncertainty). No method page: "post a recipe for future reference" is too thin. Not linked to [[nanochat]]: the post does not mention it.

## Quotes
- "Putting it here for future reference and comparison." (§intro)
- "after ~1 hour of staring at their documentation and the code" (§intro)
- "I am not 100% confident that this is correctly configured" (§intro)
- "huggingface demands that you wrap it in Regex!!" (§intro (code))

## Notes for merge
- The snippet as posted uses `Regex(...)` but the imports shown do not import `Regex` (only `Tokenizer, pre_tokenizers, decoders`, `BPE`, `BpeTrainer`, `load_dataset`). That is an observation about the raw text; do not claim the code fails, and do not fix or reproduce the code in the wiki.
- Do not copy the regex or code into the wiki (short-quote rule); paraphrase the configuration.
- "1B characters" is a subset cap in the iterator (stops after > 1,000,000,000 characters), not the full dataset.
- Published date is the Discussion's date; the repo README snapshot is a separate source ([[github-2024-04-22-minbpe-readme]]).
- Medium is github; this is a Discussion he opened, filed under the minbpe repo per CLAUDE.md §3 naming.
