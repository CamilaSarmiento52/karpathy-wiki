---
type: topic
aliases: [Scaling laws, scale, scaling, model size, compute, N and D, GPU gold rush]
first_seen: 2023-11-23
last_updated: 2025-11-20
sources: ["[[youtube-2023-11-23-intro-to-llms]]", "[[talk-2024-03-26-sequoia-making-ai-accessible]]", "[[talk-2024-09-05-no-priors-ep-80]]", "[[github-2025-11-20-nanochat-d34-model]]"]
context: ["[[talk-2023-05-25-state-of-gpt]]", "[[youtube-2025-02-05-deep-dive-into-llms]]", "[[blog-2025-10-01-animals-vs-ghosts]]"]
related: ["[[pretraining-and-finetuning]]", "[[rlvr]]"]
---
# Scaling laws
In his framing, the accuracy of an LLM's next-word prediction is a remarkably smooth, predictable function of just two variables, N, the number of parameters, and D, the amount of text trained on ([[youtube-2023-11-23-intro-to-llms]] @25:28, @26:02).

## What he says
Given only those two numbers, he says, you can predict with remarkable confidence the accuracy you will reach, and the trends show no sign of topping out, so a bigger model trained on more text will improve next-word prediction with high confidence ([[youtube-2023-11-23-intro-to-llms]] @26:02). Next-word accuracy is not what you actually care about, but empirically it correlates with the evaluations you do care about; going from GPT-3.5 to GPT-4, all the tests he shows improve ([[youtube-2023-11-23-intro-to-llms]] @26:35, @27:10). This, he says, is what fundamentally drives the gold rush for bigger GPU clusters and more data; algorithmic progress is a nice bonus that organizations still invest in heavily ([[youtube-2023-11-23-intro-to-llms]] @27:10).

**Note:** in State of GPT (published 2023-05-25) he made a related point about data: LLaMA 65B is more powerful than GPT-3 175B because it trained on 1.4 trillion tokens rather than 300 billion, so parameter count alone is no guide to a model's power ([[talk-2023-05-25-state-of-gpt]] @03:56; [[youtube-2023-11-23-intro-to-llms]] @25:28).

**Scale first, but not enough (Sequoia, 2024-03-26).** Asked by the host whether scale is all that matters, he says scale is definitely number one, the first principal component, though there are details to get right; dataset preparation and algorithms are compute-efficiency gains that matter a lot ([[talk-2024-03-26-sequoia-making-ai-accessible]] @09:38, @10:10). Scale sets something like a speed limit: without it you cannot train the massive models, though finetuning may need less ([[talk-2024-03-26-sequoia-making-ai-accessible]] @10:10). Even with money and scale, training is a very complicated distributed-optimisation problem on tens of thousands of GPUs failing at random, the infrastructure is creaking and the talent is scarce ([[talk-2024-03-26-sequoia-making-ai-accessible]] @10:43, @11:15). It is not obvious to him that someone given a ton of money or GPUs could produce one of these models; it takes expertise in infrastructure, algorithms and data ([[talk-2024-03-26-sequoia-making-ai-accessible]] @11:15).

**A property of the Transformer (No Priors, 2024-09-05).** He says scaling laws are to a large extent a property of the Transformer: stacked LSTMs did not give clean scaling laws, and the Transformer was the first thing that just scales ([[talk-2024-09-05-no-priors-ep-80]] @14:49). On the data wall and the cost of another generation of scale, he says the architecture no longer holds us back fundamentally; the dataset and the loss function have become the bottlenecks ([[talk-2024-09-05-no-priors-ep-80]] @15:56, @16:29). On model size he expects a small cognitive core may suffice ([[talk-2024-09-05-no-priors-ep-80]] @27:27).

**The GPU gold rush (Deep Dive, 2025-02-05, background).** He says big tech's demand for GPUs to train language models is what drove Nvidia to $3.4 trillion (as of 2025-02-05), and calls getting enough GPUs the gold rush; more GPUs let you process the data and iterate faster and train a bigger network ([[youtube-2025-02-05-deep-dive-into-llms]] @41:23, @41:56). **Note:** he states no scaling law there, so the lecture is background on this page ([[youtube-2025-02-05-deep-dive-into-llms]] @41:56).

**Note:** in a post dated 2025-10-01 he reports that frontier researchers assume LLMs are highly bitter-lesson pilled because scaling laws go up and to the right with compute, and Richard Sutton's counterpoint that the data is human and finite; he expects more powerful paradigms but does not say scaling stops working, so the post is background here; see [[bitter-lesson]] ([[blog-2025-10-01-animals-vs-ghosts]] §intro).

**Training past Chinchilla (nanochat d34, 2025-11-20).** His d34 run is "2X longtrained" compared to Chinchilla: the parameter-to-token ratio is overridden from 20 (comparison, Chinchilla) to 40 (setting), so the model is trained longer than compute optimal, "just to squeeze a bit more capability into a bit smaller package" ([[github-2025-11-20-nanochat-d34-model]] §intro). The script derives 88,683,315,200 training tokens and 169,150 iterations at 524,288 tokens per batch and sequence length 2048 (settings) ([[github-2025-11-20-nanochat-d34-model]] §intro). Here "compute optimal" means Chinchilla's ratio of 20 ([[github-2025-11-20-nanochat-d34-model]] §intro).

## Claims
- [[scaling-offers-a-guaranteed-path-to-better-models]]
- [[small-llms-can-be-strong-in-narrow-domains]] — small models, narrow domains
- [[the-architecture-is-no-longer-the-bottleneck]]
- [[a-cognitive-core-could-be-a-billion-parameters-or-less]]
- [[progress-comes-from-everything-improving-together]] — data, hardware, kernels and algorithms, none winning

## Related
- [[pretraining-and-finetuning]] — the stage whose loss these laws describe
- [[bitter-lesson]] — why researchers read scaling laws as bitter-lesson pilled
- [[compute-efficiency]] — the efficiency gains he lists beside scale
- [[rlvr]] — **Note:** his 2025 account adds test-time compute as a different knob; not a link set between claims
