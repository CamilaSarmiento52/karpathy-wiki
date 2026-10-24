---
type: claim
stated_on: 2024-03-26
confidence: stated
sources: ["[[talk-2024-03-26-sequoia-making-ai-accessible]]"]
context: ["[[talk-2023-05-19-stanford-cs25-transformers]]"]
topic: "[[transformer-architecture]]"
---
# The Transformer has been remarkably resilient but is probably not the final neural network
> "I don't know that it's like the final neural network" — [[talk-2024-03-26-sequoia-making-ai-accessible]] @33:51

## Context
Asked whether the next leap needs modifications to the Transformer or a new building block, he calls the Transformer amazing and says he would not have seen it coming: before it he expected an insane diversification of neural networks, and the opposite happened ([[talk-2024-03-26-sequoia-making-ai-accessible]] @33:51). Given the field's history, he says, it is really hard to say this is the end of it, "absolutely it's not", and he is optimistic someone will find a pretty big change ([[talk-2024-03-26-sequoia-making-ai-accessible]] @33:51, @34:24). He sees possible fruit in the autoregressive-versus-diffusion modelling setup and in precision, sparsity and co-design with hardware ([[talk-2024-03-26-sequoia-making-ai-accessible]] @34:24, @34:57). The Transformer, he says, was designed for the GPU: its leap was an extremely parallelisable architecture that broke the RNN's sequential dependencies through attention ([[talk-2024-03-26-sequoia-making-ai-accessible]] @34:57, @35:30). He thinks changes are very likely, though it has proven remarkably resilient: the original and today's are not super different ([[talk-2024-03-26-sequoia-making-ai-accessible]] @35:30).

## Related claims
- **Note:** [[the-transformer-is-a-general-purpose-efficient-optimizable-computer]] records, from the CS25 lecture, that nothing but the pre-norm change has stuck since 2017 and that the design was deliberately made for GPUs ([[talk-2023-05-19-stanford-cs25-transformers]] @21:39, @58:44). Both can hold: resilience so far, change expected later. No claim relation is set ([[talk-2024-03-26-sequoia-making-ai-accessible]] @35:30).
