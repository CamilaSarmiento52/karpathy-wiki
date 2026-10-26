---
type: claim
stated_on: 2026-01-31
confidence: stated
sources: ["[[github-2026-01-31-nanochat-beating-gpt-2]]"]
context: ["[[github-2026-07-03-nanochat-readme]]"]
topic: "[[gradient-descent]]"
---
# In his nanochat sweeps, small-scale hyperparameter tuning did not transfer, so he validates at target scale
> "Key lesson: small-scale tuning doesn't transfer." — [[github-2026-01-31-nanochat-beating-gpt-2]] §What Worked

## Context
Among what worked he lists a hyperparameter sweep at scale: 320 experiments to find that `x0_beta1=0.96` is optimal at d20 (measured; setting), from which he draws the lesson that small-scale tuning does not transfer, and the instruction "Validate at target scale." ([[github-2026-01-31-nanochat-beating-gpt-2]] §What Worked). The same post says much of his iteration is at small scale, a d12 that trains in about 5 minutes or a d16, and that "many (but not all!) ideas that work there transfer to the bigger models" ([[github-2026-01-31-nanochat-beating-gpt-2]] §Reproduce). Read together, a tuned hyperparameter value may not carry over while many ideas do; the title is kept to his sweep ([[github-2026-01-31-nanochat-beating-gpt-2]] §What Worked, §Reproduce). He also says it is very difficult, perhaps impossible, to rule out an idea, that sometimes you must try several times, and that his lists reflect at most a medium amount of effort ([[github-2026-01-31-nanochat-beating-gpt-2]] §What Didn't Work).

## Related claims
- None set. **Note:** the wiki's method page [[quick-experiment-loop]] ends with a step, in its own words, of keeping a change only if it holds at every scale, which it draws from the nanochat README ([[github-2026-07-03-nanochat-readme]] §Research); this post qualifies how far small-scale results reach ([[github-2026-01-31-nanochat-beating-gpt-2]] §What Worked, §Reproduce).
