---
type: claim
stated_on: 2023-11-23
confidence: stated
sources: ["[[youtube-2023-11-23-intro-to-llms]]", "[[talk-2024-03-26-sequoia-making-ai-accessible]]"]
topic: "[[llm-self-improvement]]"
context: ["[[youtube-2025-02-05-deep-dive-into-llms]]"]
extends: ["[[rl-lets-models-discover-their-own-thinking-strategies]]"]
---
# He thinks LLM self-improvement may be possible in narrow domains that have a reward function
> "in narrow domains it will be possible to self-improve language models" — [[youtube-2023-11-23-intro-to-llms]] @40:27

## Context
After describing AlphaGo's second stage of self-play against a simple reward, he says the main challenge for language models is the lack of a fast, easy-to-evaluate reward criterion in the general case, since language covers so many kinds of task ([[youtube-2023-11-23-intro-to-llms]] @39:52). In narrow domains, he says, such a reward function could be achievable, so he thinks self-improvement there is possible, while how to get it in the general case is an open question many people are thinking about ([[youtube-2023-11-23-intro-to-llms]] @40:27). His wording is hedged: "I think it is possible" ([[youtube-2023-11-23-intro-to-llms]] @40:27).

In the Sequoia interview he puts it as the field having done AlphaGo's imitation-learning step but not its RL step, the part that made AlphaGo superhuman ([[talk-2024-03-26-sequoia-making-ai-accessible]] @24:59, @25:32). The model, he says, needs to practise for itself and learn what works for it given its own capability, for example falling back to a calculator if it is bad at four-digit addition ([[talk-2024-03-26-sequoia-making-ai-accessible]] @26:04, @26:39). He does not speak of narrow domains or reward functions there; the interview supports the call for self-practice, not the narrow-domain hedge ([[talk-2024-03-26-sequoia-making-ai-accessible]] @26:39).

## Related claims
- Extended by [[rl-lets-models-discover-their-own-thinking-strategies]]: here self-improvement may be possible in narrow domains with a reward function ([[youtube-2023-11-23-intro-to-llms]] @40:27); on 2025-02-05 he describes RL on math and code problems with known answers producing the models' own reasoning strategies, still early and short of AlphaGo ([[youtube-2025-02-05-deep-dive-into-llms]] @2:32:04, @2:44:20). Dated on [[llm-self-improvement-over-time]].
- **Note:** his 2025-12-19 account of RLVR is on the [[rlvr]] topic, a connection rather than a link set here ([[youtube-2023-11-23-intro-to-llms]] @40:27).
