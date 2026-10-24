---
type: topic
aliases: [Evaluation, LLM evaluation, evals, eval, HellaSwag, benchmarks, validation loss comparison]
first_seen: 2024-05-03
last_updated: 2024-05-28
sources: ["[[github-2024-05-03-llmc-state-of-the-union]]", "[[github-2024-05-24-llmc-pytorch-cross-checks]]", "[[github-2024-05-28-llmc-gpt-2-124m]]"]
related: ["[[llm-c]]", "[[loss-functions]]", "[[reproduce-a-published-model]]"]
---
# LLM evaluation
How he judges a model he has trained against someone else's: in the llm.c GPT-2 (124M) reproduction he plots validation loss on held-out FineWeb and accuracy on HellaSwag, a benchmark he says is commonly used to assess LLM capability, and compares both with OpenAI's released checkpoint ([[github-2024-05-28-llmc-gpt-2-124m]] §intro).

## What he says
Evaluation enters llm.c as a missing piece: on 2024-05-03 he lists "evaluation (WikiText 103?)" among the components still needed for a proper GPT-2 reproduction ([[github-2024-05-03-llmc-state-of-the-union]] §intro (Functional)). On 2024-05-24 the checklist for a serious "production" pretraining run includes evaluating on a standard dataset, then HellaSwag ([[github-2024-05-24-llmc-pytorch-cross-checks]] §intro).

**Validation loss is not a fair comparison.** His run beats OpenAI's checkpoint on the withheld FineWeb validation set, but he says this is not the ideal metric: GPT-2 was trained on the never-released WebText, and the internet's statistics may have been different five years earlier ([[github-2024-05-28-llmc-gpt-2-124m]] §intro).

**HellaSwag as the main number.** So he also plots HellaSwag accuracy, which he calls nice, smooth and well-behaved; he would mostly look at HellaSwag and treat FineWeb validation as a confirmation ([[github-2024-05-28-llmc-gpt-2-124m]] §intro). He adds a caveat himself: HellaSwag has no math or code, so it slightly favours his common-crawl-like training data ([[github-2024-05-28-llmc-gpt-2-124m]] §intro). The `-h 1` flag runs it, and he chose it as something comparable across papers ([[github-2024-05-28-llmc-gpt-2-124m]] §intro (Args guide)).

**Reference points.** His run reaches 29.9 (his result) against 29.4 for OpenAI's GPT-2 (124M) checkpoint and 33.7 for GPT-3 Small (124M) as cited in the GPT-3 paper's Appendix H (comparison numbers); he reminds the reader that his model trained on 10B tokens while the GPT-3 models all trained on 300B ([[github-2024-05-28-llmc-gpt-2-124m]] §intro).

## Claims
- [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]

## Related
- [[llm-c]] — the codebase whose runs are evaluated
- [[reproduce-a-published-model]] — evaluation as the last steps of a reproduction
- [[loss-functions]] — the validation loss read as perplexity
- [[overfitting-and-generalization]] — train and validation splits in the earlier lectures
