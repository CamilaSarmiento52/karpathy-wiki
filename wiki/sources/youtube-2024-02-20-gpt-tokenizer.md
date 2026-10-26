---
type: source
raw_path: raw/youtube/zduSFxRajkE.md
published: 2024-02-20
medium: youtube
summary: Two-hour lecture that builds a byte-level BPE tokenizer from scratch, walks through the GPT-2 and GPT-4 tokenizers, special tokens, SentencePiece and vocabulary size, and traces a list of LLM failures back to tokenization.
url: https://www.youtube.com/watch?v=zduSFxRajkE
title: "Let's build the GPT Tokenizer"
---
# Let's build the GPT Tokenizer
Raw: [[raw/youtube/zduSFxRajkE]] · Original: https://www.youtube.com/watch?v=zduSFxRajkE

Lecture 8 of Zero to Hero. The two caption blocks after his goodbye (@2:12:56, @2:13:33) are leftover outtakes and are not cited.

## Summary
A 2h13m lecture on tokenization, which he calls his least favourite part of working with LLMs and the root of a lot of their oddness (@00:00, @04:27). He opens with a list of LLM failures he traces to tokenization and demonstrates several in a live tokenizer web app, then explains why Python strings are Unicode code points, why UTF-8 bytes are the starting vocabulary, and why raw bytes alone make sequences too long (@05:00, @15:41, @21:20). He builds byte-pair encoding from scratch in a notebook: count pairs, merge the most frequent, repeat to a chosen vocabulary size, then write decode and encode and test the round trip (@23:32, @28:32, @35:45, @42:59, @48:38, @55:56). He then walks through what real tokenizers add: the GPT-2 and GPT-4 regex pre-split, OpenAI's `encoder.py` and tiktoken, special tokens and the model surgery they need, and SentencePiece as used by Llama 2 (@57:37, @1:12:17, @1:18:23, @1:28:35). After a section on vocabulary size and multimodal tokens he returns to each failure on his list and explains it, ending with his recommendations and his wish that tokenization could be removed (@1:43:09, @1:51:24, @2:10:39). He publishes the code as minbpe with an exercise progression (@1:25:09, @1:25:45).

## Key points
- Tokenization converts text to and from integer tokens, the atom of an LLM; byte-level BPE starts from 256 UTF-8 byte tokens and iteratively merges the most frequent pair → [[tokenization]]
- A lot of LLM oddness traces back to tokenization: spelling, non-English text, arithmetic, GPT-2's Python, `<|endoftext|>`, trailing spaces, partial tokens, SolidGoldMagikarp, JSON vs YAML → [[a-lot-of-llm-oddness-traces-back-to-tokenization]], [[tokenization]]
- The tokenizer is a separate pre-processing stage with its own training set; vocabulary size is an empirical hyperparameter; he prefers not to normalise raw text → [[tokenization]]
- GPT-2 and GPT-4 split text with a regex before BPE so some merges never happen → [[tokenization]]
- Special tokens such as `<|endoftext|>` and chat delimiters sit outside BPE and need embedding and output-layer surgery → [[tokenization]], [[embeddings]], [[pretraining-and-finetuning]]
- He prefers tiktoken's byte-level BPE to SentencePiece's code-point BPE with byte fallback → [[he-prefers-tiktoken-byte-level-bpe-to-sentencepiece]]
- Tokenization-free byte-level modelling would be amazing but is not yet proven at scale → [[tokenization-free-modeling-would-be-amazing-but-is-unproven]]
- An untrained embedding row behaves like unallocated memory → [[embeddings]]
- minbpe: his clean Python BPE tokenizer with training code, plus an exercise progression → [[minbpe]], [[small-hackable-educational-code]]
- Once built, it should reproduce tiktoken's GPT-4 tokens exactly → [[verify-against-a-reference-implementation]]
- He builds the tokenizer up from scratch with a failure list first, toy examples, pause-and-implement prompts and round-trip tests → [[spelled-out-build-from-scratch]]

## Fed pages
- [[tokenization]]
- [[embeddings]]
- [[pretraining-and-finetuning]]
- [[a-lot-of-llm-oddness-traces-back-to-tokenization]]
- [[tokenization-free-modeling-would-be-amazing-but-is-unproven]]
- [[he-prefers-tiktoken-byte-level-bpe-to-sentencepiece]]
- [[minbpe]]
- [[verify-against-a-reference-implementation]]
- [[spelled-out-build-from-scratch]]
- [[small-hackable-educational-code]]
- [[how-he-explains]]
