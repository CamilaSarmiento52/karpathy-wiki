---
type: claim
stated_on: 2024-02-20
confidence: stated
sources: ["[[youtube-2024-02-20-gpt-tokenizer]]", "[[github-2024-02-20-nn-zero-to-hero-readme]]", "[[youtube-2025-02-05-deep-dive-into-llms]]"]
topic: "[[tokenization]]"
---
# A lot of LLM oddness traces back to tokenization
> "a lot of oddness with large language models typically traces back to tokenization" — [[youtube-2024-02-20-gpt-tokenizer]] @00:00

## Context
He opens the tokenizer lecture by advising viewers not to brush tokenization off: many issues that look like problems with the network architecture or the LLM itself are actually tokenization issues ([[youtube-2024-02-20-gpt-tokenizer]] @04:27). His list: spelling and simple string processing, non-English languages, simple arithmetic, GPT-2's trouble with Python, warnings about trailing whitespace, SolidGoldMagikarp, and being told to prefer YAML over JSON ([[youtube-2024-02-20-gpt-tokenizer]] @04:27, @05:00, @05:33). At the end of the lecture he returns to each item and explains it, adding the model halting at `<|endoftext|>` and partial and unstable tokens; the explanations, each cited, are on [[tokenization]] ([[youtube-2024-02-20-gpt-tokenizer]] @1:51:24, @1:57:09, @2:01:41, @2:03:20). He puts the root cause as LLMs working on text chunks rather than on characters as people think of them ([[youtube-2024-02-20-gpt-tokenizer]] @2:01:10). Several explanations carry his hedges: the `<|endoftext|>` failure is his suspicion about what OpenAI does, and the SolidGoldMagikarp mechanism is what is thought to have happened ([[youtube-2024-02-20-gpt-tokenizer]] @1:57:44, @2:07:16).

The Zero to Hero README's description of the same lecture says a lot of weird behaviours and problems of LLMs actually trace back to tokenization, and that the lecture discusses why tokenization is at fault ([[github-2024-02-20-nn-zero-to-hero-readme]] §intro, Lecture 8).

In the Deep Dive lecture, published 2025-02-05, he explains spelling failures the same way: models do not see characters, they see tokens, so a task such as printing every third letter of "ubiquitous", three tokens, often fails ([[youtube-2025-02-05-deep-dive-into-llms]] @2:01:07, @2:01:39, @2:02:12). Counting the r's in "strawberry" combines not seeing characters with not being good at counting ([[youtube-2025-02-05-deep-dive-into-llms]] @2:03:51), and the dots in a counting prompt are chunked into a few tokens ([[youtube-2025-02-05-deep-dive-into-llms]] @1:58:51, @1:59:25).

## Related claims
- **Note:** [[tokenization-free-modeling-would-be-amazing-but-is-unproven]] is the remedy he wishes for in the same lecture ([[youtube-2024-02-20-gpt-tokenizer]] @2:10:39). Not a claim relation: one diagnoses, the other hopes.
