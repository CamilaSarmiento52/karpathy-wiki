---
type: claim
stated_on: 2024-03-26
confidence: stated
sources: ["[[talk-2024-03-26-sequoia-making-ai-accessible]]", "[[youtube-2025-02-05-deep-dive-into-llms]]"]
context: ["[[talk-2023-05-25-state-of-gpt]]"]
topic: "[[llm-self-improvement]]"
---
# RLHF is not reinforcement learning in the full sense, because its learned reward model can be gamed
> "super weak form of reinforcement learning doesn't even count as reinforcement learning" — [[talk-2024-03-26-sequoia-making-ai-accessible]] @26:39

## Context
**Sequoia, 2024-03-26.** He calls RLHF a super weak form of RL that, he thinks, does not even count as RL, because its reward model is a vibe check: an AlphaGo trained this way would ask people which of two boards they prefer and train against those labels ([[talk-2024-03-26-sequoia-making-ai-accessible]] @26:39, @27:13). A neural-net reward model is very easy for the optimised model to overfit and hack in spurious ways ([[talk-2024-03-26-sequoia-making-ai-accessible]] @27:13).

**Deep Dive, 2025-02-05.** RLHF handles unverifiable domains such as jokes, poems and summaries by training a reward model to match human orderings of rollouts and then running RL against that simulator of human preferences ([[youtube-2025-02-05-deep-dive-into-llms]] @2:51:02, @2:52:08, @2:52:41, @2:54:19, @2:57:04). He names two downsides: the simulation is lossy and may mislead, and RL finds adversarial inputs that game the reward model, his example being pelican jokes that collapse after a few hundred updates into nonsense the reward model scores top ([[youtube-2025-02-05-deep-dive-into-llms]] @3:00:55, @3:01:31, @3:02:05, @3:02:38, @3:03:10). Patching adversarial examples never wins, so you run RLHF for a few hundred steps, crop it and ship ([[youtube-2025-02-05-deep-dive-into-llms]] @3:03:43, @3:04:15). Verifiable answers and Go's win or loss are hard to game, so RL there can run for very many steps; RLHF, by contrast, is in his words a little fine-tune that slightly improves the model, and not RL in the sense that it lacks magic ([[youtube-2025-02-05-deep-dive-into-llms]] @3:05:21, @3:05:54, @3:06:27). GPT-4o has been through RLHF, but he says it is basically not an RL model ([[youtube-2025-02-05-deep-dive-into-llms]] @3:06:27, @3:27:03).

## Related claims
- **Note:** compatible with [[rlhf-works-better-because-comparing-is-easier-than-generating]], not a contradiction: in State of GPT (published 2023-05-25) he reports that RLHF models are preferred ([[talk-2023-05-25-state-of-gpt]] @17:16), and in the 2025-02-05 lecture he says RLHF done correctly gives slightly better models while denying it is RL in the full sense ([[youtube-2025-02-05-deep-dive-into-llms]] @2:58:09, @3:06:27).
- **Note:** the dated sequence is on [[llm-self-improvement-over-time]] ([[talk-2024-03-26-sequoia-making-ai-accessible]] @26:39; [[youtube-2025-02-05-deep-dive-into-llms]] @3:05:54).
