---
type: topic
aliases: [Scaling laws, scale, scaling, model size, compute, N and D, GPU gold rush]
first_seen: 2023-11-23
last_updated: 2023-11-23
sources: ["[[youtube-2023-11-23-intro-to-llms]]"]
context: ["[[talk-2023-05-25-state-of-gpt]]"]
related: ["[[pretraining-and-finetuning]]", "[[rlvr]]"]
---
# Scaling laws
In his framing, the accuracy of an LLM's next-word prediction is a remarkably smooth, predictable function of just two variables, N, the number of parameters, and D, the amount of text trained on ([[youtube-2023-11-23-intro-to-llms]] @25:28, @26:02).

## What he says
Given only those two numbers, he says, you can predict with remarkable confidence the accuracy you will reach, and the trends show no sign of topping out, so a bigger model trained on more text will improve next-word prediction with high confidence ([[youtube-2023-11-23-intro-to-llms]] @26:02). Next-word accuracy is not what you actually care about, but empirically it correlates with the evaluations you do care about; going from GPT-3.5 to GPT-4, all the tests he shows improve ([[youtube-2023-11-23-intro-to-llms]] @26:35, @27:10). This, he says, is what fundamentally drives the gold rush for bigger GPU clusters and more data; algorithmic progress is a nice bonus that organizations still invest in heavily ([[youtube-2023-11-23-intro-to-llms]] @27:10).

**Note:** six months earlier he made a related point about data: LLaMA 65B is more powerful than GPT-3 175B because it trained on 1.4 trillion tokens rather than 300 billion, so parameter count alone is no guide to a model's power ([[talk-2023-05-25-state-of-gpt]] @03:56; [[youtube-2023-11-23-intro-to-llms]] @25:28).

## Claims
- [[scaling-offers-a-guaranteed-path-to-better-models]]

## Related
- [[pretraining-and-finetuning]] — the stage whose loss these laws describe
- [[rlvr]] — **Note:** his 2025 account adds test-time compute as a different knob; not a link set between claims
