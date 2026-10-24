---
type: claim
stated_on: 2025-10-17
confidence: stated
sources: ["[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]"]
context: ["[[talk-2024-03-26-sequoia-making-ai-accessible]]"]
topic: "[[llm-self-improvement]]"
---
# An LLM judge used as a reward gets gamed by adversarial examples within tens of steps
> "those LLMs are giant things with billions of parameters, and they're gameable" — [[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @46:34

## Context
Lots of labs, he says, try process supervision with LLM judges prompted to grade a student's partial solution ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @46:34). Any LLM used to assign a reward is gameable, and RL against it will almost certainly find adversarial examples, so it works for maybe 10 or 20 steps, not 100 or 1,000 ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @46:34, @47:11). His example, from training he describes with "we" and calls probably public: the reward against an LLM judge suddenly jumped to perfect, but the completions turned into "dhdhdhdh", nonsense the judge scored as perfect ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @47:11, @47:47). The wiki does not say where this happened. When Dwarkesh calls it training a prompt-injection model, he says prompt injection is too fancy: these are plain adversarial examples, out-of-sample inputs ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @48:27). Adding such examples to the judge's training set gives a new judge that still has adversarial examples, since there are infinitely many; it may get harder to find them over iterations, but he is not sure, and thinks other ideas are needed ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @49:05).

## Related claims
- **Note:** in the Sequoia interview he said a neural-net reward model is easy for the optimised model to overfit and hack; that is topic text on [[llm-self-improvement]] with no claim page, and this is the same idea with a concrete case ([[talk-2024-03-26-sequoia-making-ai-accessible]] @27:13; [[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @47:47).
- **Note:** this is why he does not see process supervision as a quick fix for [[rl-is-terrible-but-better-than-imitation]] ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @46:34).
