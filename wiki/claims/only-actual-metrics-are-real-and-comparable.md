---
type: claim
stated_on: 2026-01-07
confidence: stated
sources: ["[[github-2026-01-07-nanochat-miniseries-v1]]"]
context: ["[[github-2024-05-28-llmc-gpt-2-124m]]"]
topic: "[[llm-evaluation]]"
---
# Validation loss can deceive when comparing models; he trusts benchmark metrics instead
> "Only actual metrics are real and comparable." — [[github-2026-01-07-nanochat-miniseries-v1]] §intro (Comparison to GPT-2/GPT-3 miniseries)

## Context
Comparing the nanochat miniseries with GPT-2 and GPT-3, he did not want to use validation loss because, while simple, it can be subtle and deceiving ([[github-2026-01-07-nanochat-miniseries-v1]] §intro (Comparison to GPT-2/GPT-3 miniseries)). His example is modded-nanogpt, Keller Jordan's repo, which he says he otherwise loves: it merged changes he thought mildly gamed the metric, such as very long sequences and batch size 1, because evaluating in one long row leaves fewer tokens with cropped contexts than a batch with B much greater than 1, so the "improvement" is not real ([[github-2026-01-07-nanochat-miniseries-v1]] §intro (Comparison to GPT-2/GPT-3 miniseries)). Comparing FineWeb validation loss with GPT-2 and GPT-3 would also be neither fair nor informative, he says, because they trained on a very different, unknown data mix ([[github-2026-01-07-nanochat-miniseries-v1]] §intro (Comparison to GPT-2/GPT-3 miniseries)). So he compares on the DCLM CORE metric instead; see [[llm-evaluation]] ([[github-2026-01-07-nanochat-miniseries-v1]] §intro (Comparison to GPT-2/GPT-3 miniseries)).

## Related claims
- None set. **Note:** on [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]] (2024-05-28) he already called the FineWeb validation-loss comparison with GPT-2 unfair because GPT-2 trained on WebText ([[github-2024-05-28-llmc-gpt-2-124m]] §intro); here the same reason is part of a broader statement about validation loss ([[github-2026-01-07-nanochat-miniseries-v1]] §intro (Comparison to GPT-2/GPT-3 miniseries)). That claim is about HellaSwag results, so no relation is set.
