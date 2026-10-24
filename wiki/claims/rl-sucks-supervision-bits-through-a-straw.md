---
type: claim
stated_on: 2025-10-13
confidence: stated
sources: ["[[github-2025-10-13-nanochat-discussion-introducing]]", "[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]"]
context: ["[[blog-2025-10-01-animals-vs-ghosts]]"]
topic: "[[llm-self-improvement]]"
supports: ["[[rl-is-terrible-but-better-than-imitation]]"]
---
# Reinforcement learning is sucking supervision bits through a straw
> "reinforcement learning is sucking supervision bits through a straw" — [[github-2025-10-13-nanochat-discussion-introducing]] §Reinforcement Learning (RL)

## Context
In the nanochat launch post he gives the phrase as the reason the optional RL stage runs for quite a while, about 1.5 hours with the default settings (measured) ([[github-2025-10-13-nanochat-discussion-introducing]] §Reinforcement Learning (RL)). It is said in passing, about run time, in a stage that interleaves sampling and training to hill-climb GSM8K, the one dataset with a clear, objective reward ([[github-2025-10-13-nanochat-discussion-introducing]] §Reinforcement Learning (RL)). The stage is commented out by default because it is not well tuned and produces "a GSM-specific model, not a general chat model" ([[github-2025-10-13-nanochat-discussion-introducing]] §Reinforcement Learning (RL)).

In the Dwarkesh interview, published 2025-10-17, he explains the phrase: in RL on a math problem the model makes hundreds of attempts, and for each one that reaches the right answer every step is upweighted, so you are "sucking supervision through a straw.", broadcasting a single final reward across a whole trajectory ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @42:08, @42:46, @43:22). Dwarkesh repeats the phrase back later ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @45:19).

## Related claims
- **Note:** the post dated 2025-10-01 says billions of parameters need a "rich, high information density supervision signal", which is why pretraining comes before RL ([[blog-2025-10-01-animals-vs-ghosts]] §intro); the two fit together, RL's signal being thin, but neither text links them, so no relation is set here ([[github-2025-10-13-nanochat-discussion-introducing]] §Reinforcement Learning (RL)).
- **Note:** the dated sequence is on [[llm-self-improvement-over-time]] ([[github-2025-10-13-nanochat-discussion-introducing]] §Reinforcement Learning (RL)).
- Supported by [[rl-is-terrible-but-better-than-imitation]]: the Dwarkesh interview gives the mechanism, one final reward broadcast across a trajectory, which the nanochat post only names ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @42:46, @43:22; [[github-2025-10-13-nanochat-discussion-introducing]] §Reinforcement Learning (RL)).
