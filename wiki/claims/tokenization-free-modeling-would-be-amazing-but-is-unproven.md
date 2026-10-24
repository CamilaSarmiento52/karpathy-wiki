---
type: claim
stated_on: 2024-02-20
confidence: stated
sources: ["[[youtube-2024-02-20-gpt-tokenizer]]", "[[github-2024-02-20-nn-zero-to-hero-readme]]"]
topic: "[[tokenization]]"
---
# Feeding raw bytes without tokenization would be amazing, but he does not know that it is proven at scale
> "tokenization free would indeed be amazing" — [[youtube-2024-02-20-gpt-tokenizer]] @22:59

## Context
After showing that raw UTF-8 bytes give sequences too long for a finite attention context, he says he would love to feed raw byte sequences into language models, and cites a paper from the previous summer that proposes a hierarchical Transformer to do it ([[youtube-2024-02-20-gpt-tokenizer]] @22:26, @22:59). That requires modifying the architecture, since attention becomes extremely expensive on such long sequences ([[youtube-2024-02-20-gpt-tokenizer]] @22:59). The paper's authors conclude it is viable at scale; he says he does not know that it has been proven out by enough groups at sufficient scale, hopes someone comes up with it, and for now compresses with BPE ([[youtube-2024-02-20-gpt-tokenizer]] @22:59, @23:32). Closing the lecture he says he personally really dislikes the stage and that eternal glory goes to anyone who can get rid of it, hoping more work follows ([[youtube-2024-02-20-gpt-tokenizer]] @2:10:06, @2:10:39).

The Zero to Hero README's description of the lecture says it discusses why someone ideally finds a way to delete the tokenization stage entirely ([[github-2024-02-20-nn-zero-to-hero-readme]] §intro, Lecture 8).

## Related claims
- **Note:** the wish answers [[a-lot-of-llm-oddness-traces-back-to-tokenization]], the diagnosis in the same lecture ([[youtube-2024-02-20-gpt-tokenizer]] @00:00, @2:10:39).
