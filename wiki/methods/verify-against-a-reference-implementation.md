---
type: method
steps:
  - Pick a known-good reference implementation
  - Run the same input through the reference and yours
  - Compare your code with the reference code
  - Show the matching outputs side by side
  - Repeat the comparison on edge cases such as special tokens
  - Round-trip to check nothing is lost
sources: ["[[youtube-2024-02-20-gpt-tokenizer]]", "[[github-2024-04-22-minbpe-readme]]"]
aliases: [parity check, reproduce the reference output, match tiktoken, benchmark against PyTorch, cross-check against a reference]
---
# Verify against a reference implementation
When he reimplements something that already exists, he treats matching the existing implementation's output as the test that his version is right: for the tokenizer lecture the reference is tiktoken's GPT-4 encoding ([[youtube-2024-02-20-gpt-tokenizer]] @1:26:20).

## Steps
1. **Pick the reference.** For the GPT-4 tokenizer he takes OpenAI's tiktoken, the official inference library, as the known-good implementation ([[youtube-2024-02-20-gpt-tokenizer]] @1:11:42, @1:26:20).
2. **Same input, both implementations.** Once you have written your tokenizer, encoding a string should give the same tokens tiktoken gives ([[youtube-2024-02-20-gpt-tokenizer]] @1:26:20).
3. **Compare the code too.** He reads OpenAI's GPT-2 `encoder.py` against his own and finds that, apart from a byte-encoder layer, it is algorithmically identical to what he built ([[youtube-2024-02-20-gpt-tokenizer]] @1:15:36, @1:16:44, @1:17:50).
4. **Show the parity in the docs.** The minbpe README verifies feature parity by encoding the same text, mixing ASCII, punctuation, Korean and an emoji, with tiktoken's `cl100k_base` and with `GPT4Tokenizer`, and printing identical token lists ([[github-2024-04-22-minbpe-readme]] §inference: GPT-4 comparison).
5. **Edge cases too.** It repeats the check with `<|endoftext|>` and special tokens allowed, getting the same ids ([[github-2024-04-22-minbpe-readme]] §inference: GPT-4 comparison).
6. **Round-trip.** Encoding and decoding the same string should recover it ([[youtube-2024-02-20-gpt-tokenizer]] @55:56, @1:26:20).

## Seen in
- [[minbpe]]
- [[github-2024-04-22-minbpe-readme]]
- [[youtube-2024-02-20-gpt-tokenizer]]
- [[verify-gradients-against-pytorch]] — the gradient-specific version of the same habit
