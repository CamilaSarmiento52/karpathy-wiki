---
type: claim
stated_on: 2024-07-11
confidence: stated
sources: ["[[github-2024-07-11-llmc-gpt-2-1-6b]]"]
context: ["[[github-2023-01-08-mingpt-readme]]", "[[youtube-2022-08-16-micrograd]]"]
supports: ["[[gpt-is-not-a-complicated-model]]"]
topic: "[[small-hackable-educational-code]]"
---
# Neural net training is one loop of simple arithmetic and should not be that complicated
> "Neural net training is just one while loop of the same, simple arithmetic operations" — [[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (Code)

## Context
In the 1.6B post he says, admitting he feels biased, that llm.c is quite beautiful, and lists why: it needs only basic CUDA dependencies; it is a direct, minimal, readable C/CUDA implementation of about 5,000 lines, mostly C rather than C++ to keep it simple; and neural net training is one while loop of the same simple arithmetic, +, -, *, /, on a single float array, which "really shouldn't be that complicated" ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (Code)). The rest of his list is practical: it compiles and runs in seconds, allocates all GPU memory once for a constant footprint, is bitwise deterministic and runs at just below ~50% MFU ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (Code)). He contrasts llm.c with the typical stack of a Python interpreter and a much more complex library such as PyTorch, JAX or huggingface/transformers ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro).

## Related claims
- Supports [[gpt-is-not-a-complicated-model]]: the minGPT README says GPT is not complicated and most of the complexity is batching for efficiency ([[github-2023-01-08-mingpt-readme]] §intro); here he says training as a whole, the loop around the model, should not be complicated either ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (Code)). Both hold; this one broadens from the model to the training loop.
- **Note:** [[micrograd-is-all-you-need-everything-else-is-efficiency]] is the 2022 version of the same reduction, with a scalar autograd engine as all you need and the rest efficiency ([[youtube-2022-08-16-micrograd]] @06:30); llm.c's simple arithmetic on one float array keeps that view at GPT-2 scale, but no relation is set ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (Code)).
