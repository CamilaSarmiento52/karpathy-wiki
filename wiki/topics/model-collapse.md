---
type: topic
aliases: [Model collapse, training on own samples, entropy loss, silently collapsed, collapsed data distribution, synthetic data collapse]
first_seen: 2025-10-17
last_updated: 2025-10-17
sources: ["[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]"]
context: ["[[talk-2024-09-05-no-priors-ep-80]]"]
related: ["[[cognitive-core]]", "[[pretraining-and-finetuning]]", "[[llm-self-improvement]]"]
---
# Model collapse
His account of why a model cannot simply be trained on its own outputs: its samples are "silently collapsed" onto a tiny manifold of the possible space of thoughts, so training on them makes it worse ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @52:12).

## What he says
**Why not train on synthetic reflections.** He would like a pretraining stage that thinks through material and reconciles it with what the model knows, but says it is not trivial ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @51:37). Every synthetic example of the model thinking about a book looks great, yet if you keep training on them the model gets much worse, because the samples are collapsed in a way that is not obvious from any single example ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @51:37, @52:12). His example: ask ChatGPT for a joke and it has about three jokes ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @52:12). Humans are noisier but not statistically biased that way and keep a lot of entropy; how to make synthetic data generation work while keeping the entropy is, he says, a research problem ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @52:52). Asked ten times to think about a chapter, the model gives the same thing: any sample looks okay, the distribution is terrible, and if you continue training on too much of your own stuff you collapse ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @53:28).

**"Possibly no fundamental solution", then a walk-back.** In the same breath he says he thinks there is possibly no fundamental solution to this ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @53:28). Later in the interview, when Dwarkesh recalls that he hinted it is a very fundamental problem, he says he does not know if it is super fundamental and does not know if he intended to say that ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @59:01). He adds that, without having done the experiments, he thinks you could probably regularise the entropy to be higher, though a model pushed that way risks drifting from the training data, using extremely rare words and making up its own language ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @59:01, @59:38). Both statements are his; the later one corrects the earlier.

**Humans collapse too.** He says humans also collapse over their lives: children have not overfit yet, while adults revisit the same thoughts, say more of the same and deteriorate ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @53:28, @54:06). Generating thoughts in your head and attending to them is training on your own samples, and doing it too long sends you off the rails, so you should always seek entropy, for example by talking to other people ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @54:44).

**Why labs have not fixed it.** Naive fixes such as a regularisation for entropy may not work as well empirically, he guesses, because most tasks labs want from models do not demand diversity ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @57:52). In RL, being super creative is actively penalised ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @58:26).

**Note:** in the No Priors interview, published 2024-09-05, he said synthetic data must keep its entropy, the claim [[synthetic-data-is-the-future-if-you-keep-its-entropy]]; this interview explains why that is hard, without naming the earlier statement ([[talk-2024-09-05-no-priors-ep-80]] @18:38; [[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @52:52).

## Claims
- [[training-on-own-samples-collapses-models]]
- [[synthetic-data-is-the-future-if-you-keep-its-entropy]] — the 2024 statement of the entropy requirement

## Related
- [[cognitive-core]] — memorisation is "almost a separate axis"
- [[pretraining-and-finetuning]] — RLHF models also lose entropy
- [[llm-self-improvement]] — why reflecting on its own outputs does not yet work
