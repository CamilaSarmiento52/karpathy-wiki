---
type: claim
stated_on: 2023-01-08
confidence: stated
sources: ["[[github-2023-01-08-mingpt-readme]]"]
context: ["[[github-2025-11-12-nanogpt-readme]]", "[[youtube-2024-06-09-reproduce-gpt-2]]", "[[github-2024-07-11-llmc-gpt-2-1-6b]]"]
supports: ["[[neural-net-training-should-not-be-complicated]]"]
topic: "[[transformer-architecture]]"
---
# GPT is not a complicated model
> "GPT is not a complicated model" — [[github-2023-01-08-mingpt-readme]] §intro

## Context
He backs it with the implementation: minGPT's model is appropriately about 300 lines of code, because all that goes on is that a sequence of indices feeds into a Transformer and a probability distribution over the next index comes out ([[github-2023-01-08-mingpt-readme]] §intro). The majority of the complexity, he says, is being clever with batching, across examples and over sequence length, for efficiency ([[github-2023-01-08-mingpt-readme]] §intro). **Note:** the README is dated by its January 2023 snapshot; the repo itself is older ([[github-2023-01-08-mingpt-readme]] §intro).

## Related claims
- **Note:** the [[nanogpt]] README makes the same point in code size, a roughly 300-line model file, without stating the claim; a later claim page could carry it ([[github-2023-01-08-mingpt-readme]] §intro; [[github-2025-11-12-nanogpt-readme]] §intro).
- **Note:** in the GPT-2 lecture his complete GPT-2 is under 100 lines against roughly 2,000 in Hugging Face's `modeling_gpt2.py`; he does not repeat the phrase, so this is evidence beside the claim, not a restatement ([[youtube-2024-06-09-reproduce-gpt-2]] @27:27).
- Supported by [[neural-net-training-should-not-be-complicated]]: in the 2024-07-11 llm.c post he says neural net training is one while loop of simple arithmetic on a float array and should not be that complicated ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (Code)), which carries this page's point about the model ([[github-2023-01-08-mingpt-readme]] §intro) to the whole training loop.
