---
type: claim
stated_on: 2025-02-05
confidence: stated
sources: ["[[youtube-2025-02-05-deep-dive-into-llms]]"]
context: ["[[youtube-2023-11-23-intro-to-llms]]"]
topic: "[[rlvr]]"
supports: ["[[self-improvement-may-be-possible-in-narrow-domains]]"]
---
# Through RL on problems with known answers, models discover their own ways of thinking that humans could not write down for them
> "the model is discovering ways to think" — [[youtube-2025-02-05-deep-dive-into-llms]] @2:32:04

## Context
Humans, he argues, are not in a good position to write the best token sequences for a model, because what is easy or hard for a labeler differs from what is easy or hard for the LLM: some of a person's steps are too much of a leap for it, others are wasted tokens ([[youtube-2025-02-05-deep-dive-into-llms]] @2:17:44, @2:18:16, @2:18:49, @2:19:21). So imitation is useful to initialise the system, but the LLM needs to discover what reliably works for it through trial and error in reinforcement learning ([[youtube-2025-02-05-deep-dive-into-llms]] @2:19:55).

In the DeepSeek-R1 paper, as he reads it, the model learns to re-evaluate steps, backtrack and try other perspectives, which no human could hardcode into an ideal assistant response ([[youtube-2025-02-05-deep-dive-into-llms]] @2:30:56, @2:31:30). He calls these chains of thought an emergent property of the optimisation, given only correct answers, and says the model is learning what he calls cognitive strategies ([[youtube-2025-02-05-deep-dive-into-llms]] @2:32:04, @2:32:37). He compares it to AlphaGo, where RL went past imitation of experts, and says LLMs show only hints of that so far ([[youtube-2025-02-05-deep-dive-into-llms]] @2:44:20, @2:44:52). He calls this RL primordial and early, and says it is unknown in the field whether the thinking learned in verifiable domains transfers to unverifiable ones ([[youtube-2025-02-05-deep-dive-into-llms]] @3:28:45, @3:29:18).

## Related claims
- Supports [[self-improvement-may-be-possible-in-narrow-domains]]: on 2023-11-23 he thought self-improvement may be possible in narrow domains with a reward function ([[youtube-2023-11-23-intro-to-llms]] @40:27); on 2025-02-05 he describes RL on math and code problems with known answers producing reasoning strategies, while saying it is still early ([[youtube-2025-02-05-deep-dive-into-llms]] @2:32:04, @2:44:20). Evidence for the 2023 hedge in what the lecture calls verifiable domains, not a statement that self-improvement has arrived; the 2025 lecture never uses the word "self-improvement". Dated on [[llm-self-improvement-over-time]].
- **Note:** [[llms-currently-only-have-a-system-1]] describes a limitation of models at the time: on 2023-11-23 LLMs "currently" could not convert time into accuracy ([[youtube-2023-11-23-intro-to-llms]] @36:31, @37:06). The 2025-02-05 lecture describes thinking models whose longer responses raise accuracy, without the System 1 / System 2 words ([[youtube-2025-02-05-deep-dive-into-llms]] @2:30:24, @2:32:04). A connection between two dated descriptions, not a claim link; no relation is set.
