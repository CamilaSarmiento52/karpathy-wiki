---
type: topic
aliases: [Cognitive core, memory vs cognition, knowledge vs intelligence, small reasoning core, less memory]
first_seen: 2024-09-05
last_updated: 2025-10-17
sources: ["[[talk-2024-09-05-no-priors-ep-80]]", "[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]"]
related: ["[[pretraining-and-finetuning]]", "[[model-collapse]]", "[[scaling-laws]]"]
---
# Cognitive core
What he calls the cognitive core: an intelligent entity stripped of knowledge that still contains the algorithms, the magic of intelligence and problem-solving and its strategies, which he wants research to find ways to keep while removing much of the memorised knowledge ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @13:43, @14:23).

## What he says
**A thing that thinks and uses tools (No Priors, 2024-09-05).** Asked how small a performant model can get, he says current models waste capacity remembering things that do not matter, and that what is needed is a cognitive core, a thing that thinks and, when it needs information, knows how to use tools; he thinks a billion parameters could suffice; see [[a-cognitive-core-could-be-a-billion-parameters-or-less]] ([[talk-2024-09-05-no-priors-ep-80]] @26:53, @27:27). He describes the internet as about 0.001% cognition and the rest information ([[talk-2024-09-05-no-priors-ep-80]] @28:00, @28:36).

**Knowledge and intelligence (Dwarkesh, 2025-10-17).** Pretraining on next-token prediction, he says, does two unrelated things: it picks up knowledge, and it becomes intelligent, booting up circuits such as in-context learning from the algorithmic patterns of the internet ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @13:05, @13:43). He thinks the knowledge is probably holding networks back, making them rely on it too much; agents, for example, are not very good at going off the data manifold of the internet, and might be better with less knowledge or memory ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @13:43).

**Memorisation as a distraction.** Humans, he says, are not that good at memorisation, which is a feature, because it forces them to find general patterns; LLMs memorise extremely well, can regurgitate a hashed random sequence after a single iteration or two of training on it, and are distracted by their memory of pretraining documents ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @55:55, @56:33). So he would like models to have less memory and have to look things up, keeping only the algorithms for thought, the idea of an experiment and the "cognitive glue" of acting ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @57:10). Asked whether this bears on model collapse, he says he is not sure; it is almost a separate axis ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @57:10).

**Garbage data, small cores.** A random pretraining document at a frontier lab, he says, is total garbage, stock tickers and slop; because the internet is so terrible, models must be big to compress it, and most of that compression is memory work rather than cognitive work ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @1:01:26). He expects intelligent models to help refine the pretraining set down to its cognitive components, and the small model to be distilled from a much better one, since distillation works extremely well ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @1:02:04). He repeats his earlier prediction that cognitive cores can be very good at a billion parameters; in 20 years, he thinks, you could have a very productive conversation with one that knows it does not know a fact and looks it up ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @1:00:14). Dwarkesh restates the horizon as 10 years; that is Dwarkesh's figure, not his ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @1:00:47). Practically, the model should keep some basic curriculum of knowledge so it is not looking up everything and can think in its head, but not esoteric knowledge ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @1:03:14).

**Model sizes.** On frontier model size he has no super strong prediction: labs have a FLOPs and cost budget, pretraining turned out not to be where most of it should go, so models got smaller and make it up with RL, mid-training and later stages ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @1:03:51).

**Note:** the hazy-recollection framing of the weights on [[pretraining-is-lossy-compression-of-the-internet]] is the other side of this: what pretraining compresses is mostly memory ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @18:39, @1:01:26).

## Claims
- [[a-cognitive-core-could-be-a-billion-parameters-or-less]]

## Related
- [[pretraining-and-finetuning]] — the stage that mixes knowledge and intelligence
- [[pretraining-is-lossy-compression-of-the-internet]] — weights as a hazy recollection
- [[model-collapse]] — "almost a separate axis"
- [[scaling-laws]] — model size
