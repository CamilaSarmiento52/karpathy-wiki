---
type: claim
stated_on: 2023-01-08
confidence: stated
sources: ["[[github-2023-01-08-mingpt-readme]]"]
topic: "[[transformer-architecture]]"
---
# GPT is not a complicated model
> "GPT is not a complicated model" — [[github-2023-01-08-mingpt-readme]] §intro

## Context
He backs it with the implementation: minGPT's model is appropriately about 300 lines of code, because all that goes on is that a sequence of indices feeds into a Transformer and a probability distribution over the next index comes out ([[github-2023-01-08-mingpt-readme]] §intro). The majority of the complexity, he says, is being clever with batching, across examples and over sequence length, for efficiency ([[github-2023-01-08-mingpt-readme]] §intro). The README is dated by its January 2023 snapshot; the repo itself is older ([[github-2023-01-08-mingpt-readme]] §intro).

## Related claims
- **Note:** the [[nanogpt]] README makes the same point in code size, a roughly 300-line model file, without stating the claim; a later claim page could carry it ([[github-2023-01-08-mingpt-readme]] §intro).
