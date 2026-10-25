---
type: artifact
repo_url: https://github.com/karpathy/rustbpe
language: Rust, Python
status: active
sources: ["[[github-2026-01-03-rustbpe-readme]]"]
context: ["[[github-2025-10-13-nanochat-discussion-introducing]]", "[[github-2024-04-22-minbpe-readme]]"]
aliases: [rustbpe, rust BPE tokenizer]
---
# rustbpe
His lightweight Rust library, with Python bindings, for training GPT-style BPE tokenizers, which he calls "the missing tiktoken training code" ([[github-2026-01-03-rustbpe-readme]] §intro).

## What it demonstrates
- **The gap it fills.** tiktoken is excellent for inference but does not support training; Hugging Face `tokenizers` trains but "carries significant complexity from years of accumulated tokenizer variants"; his own minbpe trains and infers, but "only in Python and not optimized for speed" ([[github-2026-01-03-rustbpe-readme]] §intro). rustbpe is meant to be a simple, efficient BPE trainer in Rust with Python bindings ([[github-2026-01-03-rustbpe-readme]] §intro).
- **Train here, infer in tiktoken.** "The main use case: train with rustbpe, inference with tiktoken."; the API exposes the regex pattern and the mergeable ranks for the export ([[github-2026-01-03-rustbpe-readme]] §Usage, §API Reference).
- **Features.** Parallel training with rayon, GPT-4-style regex pre-tokenization by default with a custom pattern allowed, direct tiktoken export, Python bindings via PyO3 and parallel batch encoding; it installs with `pip install rustbpe` ([[github-2026-01-03-rustbpe-readme]] §Features, §Installation, §Usage). The vocabulary size is 256 plus the number of merges; the examples use 4096 and 8192 (settings) ([[github-2026-01-03-rustbpe-readme]] §API Reference, §Usage).
- **How BPE works, in four steps.** Start from the 256 byte-level tokens, count all adjacent pairs, merge the most frequent pair into a new token, and repeat to the target vocabulary size; the README says the result represents common patterns efficiently and can still encode any input ([[github-2026-01-03-rustbpe-readme]] §How BPE works).
- **Tested against his own Python.** He wrote the Python reference code personally and from scratch and says he understands it fully, then wrote the Rust against it "with tests for equality"; Rust tests run with `cargo test` and the Python side with pytest, with the whole implementation, bindings and tests in one `src/lib.rs` ([[github-2026-01-03-rustbpe-readme]] §LLM Assistance note, §Development). "All the equality tests pass as far as I am aware" ([[github-2026-01-03-rustbpe-readme]] §LLM Assistance note). The README does not say whether that reference is minbpe ([[github-2026-01-03-rustbpe-readme]] §LLM Assistance note).
- **LLM help, disclosed.** "I am not a Rust developer by background", he writes, so he had significant help from ChatGPT and Claude Code Opus 4.5, apologises if some of the Rust is not properly arranged, and invites Issues and PRs ([[github-2026-01-03-rustbpe-readme]] §LLM Assistance note). The licence is MIT ([[github-2026-01-03-rustbpe-readme]] §License).
- **Note:** the README does not mention nanochat; the nanochat launch post (2025-10-13) describes nanochat's own Rust tokenizer, trained with OpenAI's algorithm and tested equal to the Python, with tiktoken for inference ([[github-2025-10-13-nanochat-discussion-introducing]] §Environment setup; [[github-2026-01-03-rustbpe-readme]] §intro). That they are the same code is likely but stated in neither source.
- **Note:** the minbpe README's 2024-04-22 todos list a C or Rust version ([[github-2024-04-22-minbpe-readme]] §todos); rustbpe fits that todo, but neither README says so ([[github-2026-01-03-rustbpe-readme]] §intro).
- **Note:** `language: Rust, Python` from the Rust library and its Python bindings ([[github-2026-01-03-rustbpe-readme]] §intro).

## Related
- [[tokenization]] — the algorithm it trains
- [[minbpe]] — his Python tokenizer, which it calls not optimized for speed
- [[nanochat]] — whose Rust tokenizer it likely is
- [[he-prefers-tiktoken-byte-level-bpe-to-sentencepiece]] — tiktoken with training code
- [[verify-against-a-reference-implementation]] — equality tests against his Python
