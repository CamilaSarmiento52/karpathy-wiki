---
type: claim
stated_on: 2025-02-05
confidence: stated
sources: ["[[youtube-2025-02-05-deep-dive-into-llms]]"]
context: ["[[youtube-2023-11-23-intro-to-llms]]"]
topic: "[[llm-hallucinations]]"
---
# Knowledge in the parameters is a vague recollection; the context window is working memory
> "knowledge in the parameters of the neural network is a vague recollection" — [[youtube-2025-02-05-deep-dive-into-llms]] @1:39:25

## Context
He builds the point from the base model: things that appear frequently in the training data are more likely to be remembered correctly, and its knowledge is vague, probabilistic and statistical ([[youtube-2025-02-05-deep-dive-into-llms]] @51:07, @51:40). Highly weighted sources such as Wikipedia may be seen around ten times and can be recited verbatim, which he calls regurgitation and usually undesirable ([[youtube-2025-02-05-deep-dive-into-llms]] @52:13, @53:18, @53:50).

Knowledge in the weights, he says, is like something you read a month ago; looking a thing up refreshes your working memory ([[youtube-2025-02-05-deep-dive-into-llms]] @1:32:43, @1:33:17). Text that a search pastes into the context window is directly accessible to the network rather than recollected ([[youtube-2025-02-05-deep-dive-into-llms]] @1:34:58, @1:35:31). He stresses this as an important point of LLM psychology: the parameters are a vague recollection and the tokens in the context window are the working memory ([[youtube-2025-02-05-deep-dive-into-llms]] @1:39:25). The practical consequence he draws is to paste the material into the prompt, his example being the first chapter of Pride and Prejudice, rather than rely on the model's memory of it ([[youtube-2025-02-05-deep-dive-into-llms]] @1:40:32, @1:41:04).

## Related claims
- **Note:** [[pretraining-is-lossy-compression-of-the-internet]] is the same picture of the parameters; he repeats in this lecture that they are a lossy compression of the internet, like a zip file ([[youtube-2025-02-05-deep-dive-into-llms]] @49:59). No claim link is set.
- **Note:** [[llms-are-the-kernel-of-an-emerging-operating-system]] calls the context window RAM, a finite, precious working memory, in the 2023-11-23 talk ([[youtube-2023-11-23-intro-to-llms]] @43:45); here it is working memory without the operating-system analogy ([[youtube-2025-02-05-deep-dive-into-llms]] @1:39:25).
