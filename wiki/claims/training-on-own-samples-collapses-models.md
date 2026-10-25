---
type: claim
stated_on: 2025-10-17
confidence: stated
sources: ["[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]"]
context: ["[[talk-2024-09-05-no-priors-ep-80]]"]
topic: "[[model-collapse]]"
---
# Training a model on too much of its own output collapses it, because its samples are silently collapsed
> "They're silently collapsed." — [[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @52:12

## Context
Explaining why a model cannot simply train on its own reflections, he says every synthetic sample looks great but the model gets much worse if you keep training on them, because samples from models occupy a very tiny manifold of the possible space of thoughts, in a way not obvious from any one example ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @51:37, @52:12). Asked ten times to think about a chapter, the model gives the same thing; each sample looks okay, the distribution is terrible, and if you continue training on too much of your own stuff you collapse ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @53:28). Humans are noisier but keep a lot of entropy, and how to keep it in synthetic data is a research problem ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @52:52).

His view of how deep the problem goes is stated twice. He first says he thinks there is possibly no fundamental solution ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @53:28). Later in the interview he says he does not know if it is super fundamental, does not know if he intended to say that, and thinks entropy could probably be regularised higher, though he has not done the experiments ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @59:01). The later statement is his own correction of the earlier.

## Related claims
- **Note:** [[synthetic-data-is-the-future-if-you-keep-its-entropy]] (No Priors, published 2024-09-05) says synthetic data must keep its entropy ([[talk-2024-09-05-no-priors-ep-80]] @18:38); this claim says what happens when it does not ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @52:12). Both hold; no relation is set.
