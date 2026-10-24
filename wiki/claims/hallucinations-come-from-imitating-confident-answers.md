---
type: claim
stated_on: 2025-02-05
confidence: stated
sources: ["[[youtube-2025-02-05-deep-dive-into-llms]]"]
context: ["[[youtube-2025-06-19-software-is-changing]]"]
topic: "[[llm-hallucinations]]"
---
# Models hallucinate because they imitate the confident style of training answers, even where part of the network may know it doesn't know
> "these are statistical token tumblers as I call them" — [[youtube-2025-02-05-deep-dive-into-llms]] @1:22:42

## Context
In training data, questions of the form "who is X" are answered confidently, so the model takes on the style of the answer and gives its statistically most likely guess; it has no internet access and is not doing research, so it makes stuff up ([[youtube-2025-02-05-deep-dive-into-llms]] @1:21:36, @1:22:09, @1:22:42). His wording is hedged: the model might know, in some neuron he says we presume exists, that it does not know, but that uncertainty is not wired to saying so ([[youtube-2025-02-05-deep-dive-into-llms]] @1:26:33, @1:27:06, @1:31:37). Adding training examples whose correct answer is "I don't know" lets the model make that connection, which he calls a large mitigation ([[youtube-2025-02-05-deep-dive-into-llms]] @1:31:37). The procedure, which he takes from Meta's Llama 3 paper, is on [[llm-hallucinations]] ([[youtube-2025-02-05-deep-dive-into-llms]] @1:26:02).

## Related claims
- **Note:** [[jagged-intelligence]] lists hallucination as a deficit in the 2025-06-19 YC talk ([[youtube-2025-06-19-software-is-changing]] @16:04); this claim gives his explanation of its cause ([[youtube-2025-02-05-deep-dive-into-llms]] @1:22:42). A connection, not a claim link.
- **Note:** [[chatgpt-answers-simulate-a-human-data-labeler]] is the same mechanism in general: the assistant imitates what labelers wrote ([[youtube-2025-02-05-deep-dive-into-llms]] @1:18:17).
