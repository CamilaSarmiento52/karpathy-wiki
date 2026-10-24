---
type: claim
stated_on: 2025-10-17
confidence: stated
sources: ["[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]"]
context: ["[[youtube-2023-11-23-intro-to-llms]]", "[[talk-2024-03-26-sequoia-making-ai-accessible]]", "[[blog-2025-12-19-year-in-review-2025]]", "[[github-2025-10-13-nanochat-discussion-introducing]]"]
topic: "[[llm-self-improvement]]"
supports: ["[[self-improvement-may-be-possible-in-narrow-domains]]", "[[rl-sucks-supervision-bits-through-a-straw]]"]
---
# Reinforcement learning is terrible, but what came before it was much worse
> "Reinforcement learning is terrible." — [[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @41:33

## Context
He says humans do not use reinforcement learning as such, that RL is a lot worse than the average person thinks, and that it just happens that everything before it, imitating people, is much worse ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @41:33). In RL on a math problem the model tries hundreds of attempts, checks the answer and upweights every step of the attempts that got it right, including the wrong alleys taken along the way; he calls that noise ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @42:08, @42:46). His phrase is that you are "sucking supervision through a straw": a single final reward is broadcast across a trajectory that could be a minute of rollout, which he calls stupid and crazy, something a human would never do ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @42:46, @43:22). A person would not do hundreds of rollouts and, on finding a solution, would review which parts went well; he says nothing in current LLMs does that, though papers are appearing ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @43:22, @44:00).

He credits RL with letting a model hill-climb on problems that have correct answers without expert trajectories to imitate, and discover solutions a human might never find, and then calls it still stupid ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @44:36). He expects a major update to LLM algorithms in the reflect-and-review direction and thinks "three or four or five more" such ideas are needed ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @45:19). Process supervision, rewarding each step, is tricky because there is no obvious automatable partial credit, while an outcome reward is a simple equality match to the answer ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @46:01, @46:34); why LLM judges do not solve this is [[llm-judges-are-gameable-rewards]] ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @46:34).

## Related claims
- Supports [[self-improvement-may-be-possible-in-narrow-domains]]: in 2023 he said a reward function could be achievable in narrow domains, so self-improvement there may be possible ([[youtube-2023-11-23-intro-to-llms]] @40:27); here RL hill-climbs on problems that "just have correct answers" without expert trajectories ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @44:36). It is evidence for the 2023 hedge, given beside his verdict that the method is noisy and still stupid ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @42:46, @44:36); it does not say self-improvement has arrived.
- Supports [[rl-sucks-supervision-bits-through-a-straw]]: the nanochat post gives the straw phrase in passing, as the reason RL runs long ([[github-2025-10-13-nanochat-discussion-introducing]] §Reinforcement Learning (RL)); here he explains it, one final reward broadcast across a whole trajectory ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @42:46, @43:22).
- **Note:** the Sequoia interview called imitation learning super silly and RLHF a weak form of RL ([[talk-2024-03-26-sequoia-making-ai-accessible]] @26:39, @27:13); the ranking here, imitation below RL and something better still needed, is the same, with the straw diagnosis added. It is topic text on [[llm-self-improvement]], not a claim page, so no relation is set ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @41:33).
- **Note:** the 2025-12-19 review calls RLVR the major new stage of 2025 ([[blog-2025-12-19-year-in-review-2025]] §1); this interview stresses the method's crude credit assignment. Both can hold: effective enough to be a major stage, still noisy ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @42:46).
- **Note:** the dated sequence is on [[llm-self-improvement-over-time]] ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @41:33).
