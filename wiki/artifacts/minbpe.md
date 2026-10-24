---
type: artifact
repo_url: https://github.com/karpathy/minbpe
language: Python
status: active
sources: ["[[youtube-2024-02-20-gpt-tokenizer]]", "[[github-2024-02-20-nn-zero-to-hero-readme]]", "[[github-2024-04-22-minbpe-readme]]", "[[github-2025-08-08-minbpe-gpt-4-tokenizer-discussion]]"]
aliases: [minBPE, min bpe]
---
# minbpe
The tokenizer code he wrote while developing the GPT tokenizer lecture and published as its own repository; he said at recording time that it would probably change quite a bit because he intended to keep working on it ([[youtube-2024-02-20-gpt-tokenizer]] @1:25:09, @1:25:45). The Zero to Hero README links it as Lecture 8's code ([[github-2024-02-20-nn-zero-to-hero-readme]] §intro, Lecture 8).

## What it demonstrates
- An `exercise.md` breaks building your own tokenizer into four steps that build up to a GPT-4 tokenizer, with the repo's tests and code as reference when stuck; he says he tried to keep the code fairly clean and understandable ([[youtube-2024-02-20-gpt-tokenizer]] @1:25:45, @1:26:20).
- Once written, it should reproduce tiktoken's GPT-4 encoding and decoding exactly, and it adds a train function, which tiktoken, being inference-only, does not provide ([[youtube-2024-02-20-gpt-tokenizer]] @1:26:20, @1:26:52).
- Trained on the Taylor Swift Wikipedia page, its merges look like GPT-4's, which he attributes to the same algorithm on a different training set; from GPT-4's many whitespace merges he suspects, unsure, a lot of Python in its tokenizer training data ([[youtube-2024-02-20-gpt-tokenizer]] @1:26:52, @1:27:27, @1:28:04).
- It is in Python; he hopes to make it efficient enough to be the tiktoken-with-training-code he says does not yet exist ([[youtube-2024-02-20-gpt-tokenizer]] @2:11:45, @2:12:18).

- The README snapshot of 2024-04-22 describes it as minimal, clean code for byte-level BPE, "byte-level" because it runs on UTF-8 encoded strings ([[github-2024-04-22-minbpe-readme]] §intro).
- Files: `base.py` holds the `Tokenizer` base class with train, encode and decode stubs and save/load; `basic.py` the `BasicTokenizer`, which runs BPE directly on text; `regex.py` the `RegexTokenizer`, which splits text by a regex first and handles special tokens; and `gpt4.py` the `GPT4Tokenizer`, a light wrapper that exactly reproduces GPT-4's tiktoken tokenization, including recovering the exact merges and some 1-byte token permutations he calls unfortunate and likely historical ([[github-2024-04-22-minbpe-readme]] §intro).
- `train.py` trains both tokenizers on the Wikipedia entry for Taylor Swift in about 25 seconds on his M1 MacBook and saves the vocab for visualisation; every file is very short, thoroughly commented and ends with a usage example ([[github-2024-04-22-minbpe-readme]] §intro).
- `save` writes a `.model` file for loading and a `.vocab` file for viewing ([[github-2024-04-22-minbpe-readme]] §quick start, §training).
- Tests run with pytest from `tests/`, and a Rust port, minbpe-rs, is listed as a community extension ([[github-2024-04-22-minbpe-readme]] §tests, §community extensions).
- `exercise.md` gives the advised progression for building your own minbpe step by step, and `lecture.md` holds the lecture in text form ([[github-2024-04-22-minbpe-readme]] §exercise, §lecture).
- Todos at the snapshot: a faster Python version for large files and vocabularies, a C or Rust version, generalising the GPT-4 wrapper to GPT-2, GPT-3 and GPT-3.5, and a LlamaTokenizer attempting a SentencePiece equivalent ([[github-2024-04-22-minbpe-readme]] §todos).
- `status: active` rests on the lecture's stated plan to keep working on it and on the open todo list in this snapshot ([[youtube-2024-02-20-gpt-tokenizer]] @1:25:45; [[github-2024-04-22-minbpe-readme]] §todos).

- The repo's Discussions hold his post of 2025-08-08 on training a GPT-4-style tokenizer with the Hugging Face Tokenizers library instead, which he puts there for future reference and comparison; the post does not mention minbpe's own code or compare against it ([[github-2025-08-08-minbpe-gpt-4-tokenizer-discussion]] §intro). The configuration is described on [[tokenization]] ([[github-2025-08-08-minbpe-gpt-4-tokenizer-discussion]] §intro (code)).

## Related
- [[tokenization]] — what it implements
- [[nn-zero-to-hero]] — the course whose eighth lecture builds it
- [[small-hackable-educational-code]], [[spelled-out-build-from-scratch]]
- [[verify-against-a-reference-implementation]] — tiktoken as the reference
