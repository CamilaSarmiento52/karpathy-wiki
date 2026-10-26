---
type: claim
stated_on: 2024-09-05
confidence: stated
sources: ["[[talk-2024-09-05-no-priors-ep-80]]", "[[github-2025-10-24-nanochat-strawberry-guide]]"]
context: ["[[talk-2023-05-25-state-of-gpt]]"]
topic: "[[pretraining-and-finetuning]]"
---
# Synthetic data is the way forward, but models are silently collapsed, so its entropy must be kept
> "synthetic data absolutely the future" — [[talk-2024-09-05-no-priors-ep-80]] @20:13

## Context
Asked how far synthetic data gets us, he says it is the only way to make progress, so we have to make it work, but you have to be careful because the models are silently collapsed ([[talk-2024-09-05-no-priors-ep-80]] @18:38). His example: ask ChatGPT for a joke and it knows about three; any single output looks fine, but the distribution is not diverse ([[talk-2024-09-05-no-priors-ep-80]] @18:38, @19:10). In synthetic data generation you want that entropy, the diversity and richness of the dataset; otherwise the dataset collapses in a way you cannot see in any one example, and it silently gets worse ([[talk-2024-09-05-no-priors-ep-80]] @19:10). One technique he mentions is a Persona dataset someone released, a billion short fictional human backgrounds put into generation prompts so the model explores more of the space ([[talk-2024-09-05-no-priors-ep-80]] @19:10, @19:42). Injecting entropy and maintaining the distribution is the hard part, which he thinks people may not sufficiently appreciate; his impression is that we will not run out of data ([[talk-2024-09-05-no-priors-ep-80]] @20:13). The surrounding answer is that much current activity refactors datasets into inner-monologue formats, with a lot of synthetic data generation ([[talk-2024-09-05-no-priors-ep-80]] @18:05).

**Strawberry guide, 2025-10-24.** In his own synthetic task for nanochat, under a heading he calls "Entropy", he randomises the user prompts from many templates, including other languages, for diversity, and calls it important as a data augmentation so the skill is evoked however the user asks ([[github-2025-10-24-nanochat-strawberry-guide]] §Entropy). He lists more entropy in both user and assistant messages as a further improvement ([[github-2025-10-24-nanochat-strawberry-guide]] §Summary). The post does not mention collapse ([[github-2025-10-24-nanochat-strawberry-guide]] §Entropy).

## Related claims
- **Note:** no claim relation. A related observation from State of GPT is on [[pretraining-and-finetuning]]: RLHF models lose some entropy and give peakier samples ([[talk-2023-05-25-state-of-gpt]] @18:21). Here the loss of entropy is in generated datasets ([[talk-2024-09-05-no-priors-ep-80]] @19:10).
