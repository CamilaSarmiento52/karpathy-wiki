---
type: claim
stated_on: 2026-03-09
confidence: stated
sources: ["[[x-2026-03-09-autoresearch-tuning-nanochat]]"]
context: ["[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]"]
topic: "[[autoresearch]]"
---
# His first autoresearch round found real, additive improvements to nanochat, though not novel research yet
> "So yes, these are real improvements and they make an actual difference." — [[x-2026-03-09-autoresearch-tuning-nanochat]] #1

## Context
He left autoresearch tuning nanochat's depth=12 model for about two days; as he reports the agent's run, it worked through about 700 changes and found about 20 that improved validation loss ([[x-2026-03-09-autoresearch-tuning-nanochat]] #1). He then tested them himself: all were additive and transferred to depth=24 models, and stacked they took the leaderboard's "Time to GPT-2" from 2.02 to 1.80 hours, about 11% in his figure, which will be the new leaderboard entry ([[x-2026-03-09-autoresearch-tuning-nanochat]] #1). He is "mildly surprised" that his very first naive attempt worked this well on a project he thought already fairly well tuned by hand ([[x-2026-03-09-autoresearch-tuning-nanochat]] #1). He keeps a hedge: it is not novel, ground-breaking "research" (yet), but the adjustments are "real", he had not found them manually, and they stack up ([[x-2026-03-09-autoresearch-tuning-nanochat]] #1). Seeing the agent do his whole workflow end to end and by itself, planning its next experiments from the sequence of earlier results, he calls "wild" ([[x-2026-03-09-autoresearch-tuning-nanochat]] #1).

## Related claims
- None set. **Note:** [[coding-models-are-weak-at-code-never-written-before]] (2025-10-17) says agents were not net useful for writing nanochat's novel code ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @35:43); here an agent runs and judges tuning experiments on existing code and finds changes he calls real but not novel research ([[x-2026-03-09-autoresearch-tuning-nanochat]] #1). Different tasks, so both can hold; the post does not speak about writing new code, so no relation is set.
- **Note:** [[all-frontier-labs-will-autoresearch]] is his prediction in the same post, made from this result ([[x-2026-03-09-autoresearch-tuning-nanochat]] #1).
