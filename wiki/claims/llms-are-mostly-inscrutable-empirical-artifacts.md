---
type: claim
stated_on: 2023-11-23
confidence: stated
sources: ["[[youtube-2023-11-23-intro-to-llms]]"]
topic: "[[pretraining-and-finetuning]]"
---
# LLMs are mostly inscrutable artifacts, to be studied empirically with sophisticated evaluations
> "they're not like a car where we sort of understand all the parts" — [[youtube-2023-11-23-intro-to-llms]] @13:15

## Context
He says we know every mathematical operation in the Transformer, but not what the roughly 100 billion parameters are doing; we only know how to adjust them iteratively to make the network better at next-word prediction ([[youtube-2023-11-23-intro-to-llms]] @11:36, @12:10). The networks seem to build a knowledge database that is strange and imperfect: in the viral reversal-curse example, GPT-4 knows who Tom Cruise's mother is but not, asked the other way, who her son is, so its knowledge is one-dimensional and accessible from one direction ([[youtube-2023-11-23-intro-to-llms]] @12:43). The field of mechanistic interpretability tries to explain parts of them, but for now, he says, we treat them as empirical artifacts and measure their behaviour, which needs correspondingly sophisticated evaluations ([[youtube-2023-11-23-intro-to-llms]] @13:15, @13:49).

## Related claims
- **Note:** the 2025 [[jagged-intelligence]] page describes the same unevenness under a later name; he does not use "jagged" in 2023, so this is a connection, not support ([[youtube-2023-11-23-intro-to-llms]] @12:43).
