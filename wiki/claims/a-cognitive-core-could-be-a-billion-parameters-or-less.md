---
type: claim
stated_on: 2024-09-05
confidence: stated
sources: ["[[talk-2024-09-05-no-priors-ep-80]]", "[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]"]
context: ["[[github-2024-05-29-llama2c-readme]]"]
topic: "[[cognitive-core]]"
supports: ["[[small-llms-can-be-strong-in-narrow-domains]]"]
---
# A "cognitive core" that thinks and uses tools could be about a billion parameters, maybe fewer
> "I think the cognitive core can be extremely small" — [[talk-2024-09-05-no-priors-ep-80]] @27:27

## Context
Asked by a host how small a performant model can get, he says surprisingly small, and that current models waste a ton of capacity remembering things that do not matter, such as SHA hashes, because the dataset is not curated well ([[talk-2024-09-05-no-priors-ep-80]] @26:53, @27:27). He expects that to go away: what is needed is a cognitive core, a thing that thinks and, when it needs information, knows how to use tools; he thinks even a billion parameters suffices ([[talk-2024-09-05-no-priors-ep-80]] @27:27). His reason is that distillation, a big model supervising a small one, works surprisingly well ([[talk-2024-09-05-no-priors-ep-80]] @27:27, @28:00). He describes the internet as about 0.001% cognition and the rest information, most of it not useful to the thinking part ([[talk-2024-09-05-no-priors-ep-80]] @28:00, @28:36). After a line suggesting a billion parameters may give a good cognitive core, which the unlabelled captions make likely a host's, he says even a billion may be too much, hedging "I don't know, we'll see" ([[talk-2024-09-05-no-priors-ep-80]] @28:36).

**Restated with a horizon (Dwarkesh, published 2025-10-17).** He says model sizes went up and have come down, and state-of-the-art models are smaller but still memorise way too much ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @1:00:14). He recalls predicting that we can get "cognitive cores that are very good at even a billion parameters", and says that in 20 years you could have a very productive conversation with one, which would know that it does not know a fact and look it up ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @1:00:14). Dwarkesh restates the horizon as 10 years and he does not take that up; 20 years is his figure ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @1:00:47). Pressed to go smaller, he says at some point it should take at least a billion knobs to do something interesting, that he already feels contrarian, and "maybe we could get a little bit smaller" ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @1:02:39, @1:03:14). Small models, he says, are almost certainly distilled, and distillation works extremely well ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @1:02:04). The topic is [[cognitive-core]] ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @14:23).

## Related claims
- Supports [[small-llms-can-be-strong-in-narrow-domains]]: the llama2.c README says very small LLMs can be strong in a narrow domain and expects custom micro-LLMs of about 100M to 1B parameters ([[github-2024-05-29-llama2c-readme]] §intro, §contributing); here a general cognitive core of about a billion or fewer, with tools for knowledge ([[talk-2024-09-05-no-priors-ep-80]] @27:27, @28:36). Different ideas, narrow domain versus tool-using core, so the link is support, not extension.
