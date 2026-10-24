---
type: topic
aliases: [Self-improvement, LLM self-improvement, AlphaGo step two, beyond imitation, reward function, reinforcement learning beyond RLHF]
first_seen: 2023-11-23
last_updated: 2023-11-23
sources: ["[[youtube-2023-11-23-intro-to-llms]]"]
related: ["[[rlvr]]", "[[system-1-and-system-2-thinking]]"]
---
# LLM self-improvement
The open question, in his framing, of what an AlphaGo-style second stage would be for language models: going beyond imitating humans by improving against an automatic reward ([[youtube-2023-11-23-intro-to-llms]] @38:14, @39:52).

## What he says
AlphaGo, he recalls, had two stages: imitating expert human games, which can only reach the best human, and then self-improvement by playing millions of games against a simple automatic reward, winning, which took it past the top humans in 40 days ([[youtube-2023-11-23-intro-to-llms]] @38:14, @38:46, @39:20). LLMs today, he says, only do stage one, imitating human labelers, so it would be hard to go above human response accuracy ([[youtube-2023-11-23-intro-to-llms]] @39:20, @39:52). The main challenge for a step two in open language modelling is the lack of a fast, simple reward criterion in the general case ([[youtube-2023-11-23-intro-to-llms]] @39:52). In narrow domains such a reward function could be achievable, so he thinks self-improvement there may be possible; the general case remains open ([[youtube-2023-11-23-intro-to-llms]] @40:27).

## Claims
- [[self-improvement-may-be-possible-in-narrow-domains]]

## Related
- [[rlvr]] — **Note:** his 2025 account of training against automatically checkable rewards in verifiable domains is close to the narrow-domain case he speculated about in 2023; a connection, not a link set between claims
- [[system-1-and-system-2-thinking]] — the other open direction in the same talk
- [[jagged-intelligence]] — in 2025, capability spikes near verifiable domains
