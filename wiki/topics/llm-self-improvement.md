---
type: topic
aliases: [Self-improvement, LLM self-improvement, AlphaGo step two, beyond imitation, reward function, reinforcement learning beyond RLHF]
first_seen: 2023-11-23
last_updated: 2024-09-05
sources: ["[[youtube-2023-11-23-intro-to-llms]]", "[[talk-2024-03-26-sequoia-making-ai-accessible]]", "[[talk-2024-09-05-no-priors-ep-80]]"]
related: ["[[rlvr]]", "[[system-1-and-system-2-thinking]]"]
---
# LLM self-improvement
The open question, in his framing, of what an AlphaGo-style second stage would be for language models: going beyond imitating humans by improving against an automatic reward ([[youtube-2023-11-23-intro-to-llms]] @38:14, @39:52).

## What he says
AlphaGo, he recalls, had two stages: imitating expert human games, which can only reach the best human, and then self-improvement by playing millions of games against a simple automatic reward, winning, which took it past the top humans in 40 days ([[youtube-2023-11-23-intro-to-llms]] @38:14, @38:46, @39:20). LLMs today, he says, only do stage one, imitating human labelers, so it would be hard to go above human response accuracy ([[youtube-2023-11-23-intro-to-llms]] @39:20, @39:52). The main challenge for a step two in open language modelling is the lack of a fast, simple reward criterion in the general case ([[youtube-2023-11-23-intro-to-llms]] @39:52). In narrow domains such a reward function could be achievable, so he thinks self-improvement there may be possible; the general case remains open ([[youtube-2023-11-23-intro-to-llms]] @40:27).

**Step one of AlphaGo (Sequoia, 2024-03-26).** Asked whether next-word predictors can become a physicist, he says current models are not good enough and there are big rocks in capability still to turn: the field has done AlphaGo's imitation-learning step and not its RL step, which is what made AlphaGo work ([[talk-2024-03-26-sequoia-making-ai-accessible]] @24:59, @25:32). He calls data collection for ChatGPT-like models terrible, because human and model psychology differ: a human's ideal solution has steps trivial to the model and others that are leaps it does not understand ([[talk-2024-03-26-sequoia-making-ai-accessible]] @25:32, @26:04). The model needs to practise for itself and learn what works for it; he calls imitation a good initializer for something agent-like ([[talk-2024-03-26-sequoia-making-ai-accessible]] @26:04, @26:39).

**RLHF is a weak form of RL.** He says RLHF barely counts as reinforcement learning, since its reward model is a vibe check: an AlphaGo trained by RLHF would ask people which of two boards they prefer and train against those labels ([[talk-2024-03-26-sequoia-making-ai-accessible]] @26:39, @27:13). A neural-net reward model is easy for the optimised model to overfit and hack in spurious ways, whereas AlphaGo had a clear objective function; he calls imitation learning super silly and RLHF a nice improvement that is still silly, and wants training where the model is in the loop with its own psychology ([[talk-2024-03-26-sequoia-making-ai-accessible]] @27:13, @27:46). Learning from a textbook involves exercises, note-taking and rephrasing, and he says nothing equivalent exists in LLMs yet: super early days ([[talk-2024-03-26-sequoia-making-ai-accessible]] @28:19).

**A staircase (No Priors, 2024-09-05).** He says current models are helping create the next generation of models, a staircase of improvement ([[talk-2024-09-05-no-priors-ep-80]] @18:05). **Note:** this is models helping build their successors, for instance through synthetic data, not the AlphaGo-style self-play of the sections above; no claim relation is set ([[talk-2024-09-05-no-priors-ep-80]] @18:05; [[youtube-2023-11-23-intro-to-llms]] @38:46).

## Claims
- [[self-improvement-may-be-possible-in-narrow-domains]]

## Related
- [[rlvr]] — **Note:** his 2025 account of training against automatically checkable rewards in verifiable domains is close to the narrow-domain case he speculated about in 2023; a connection, not a link set between claims
- [[system-1-and-system-2-thinking]] — the other open direction in the same talk
- [[jagged-intelligence]] — in 2025, capability spikes near verifiable domains
