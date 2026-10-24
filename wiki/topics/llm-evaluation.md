---
type: topic
aliases: [Evaluation, LLM evaluation, evals, eval, HellaSwag, benchmarks, validation loss comparison, Eleuther evaluation harness, early signal]
first_seen: 2024-05-03
last_updated: 2024-07-11
sources: ["[[github-2024-05-03-llmc-state-of-the-union]]", "[[github-2024-05-24-llmc-pytorch-cross-checks]]", "[[github-2024-05-28-llmc-gpt-2-124m]]", "[[youtube-2024-06-09-reproduce-gpt-2]]", "[[github-2024-06-12-llmc-gpt-2-774m]]", "[[github-2024-07-11-llmc-gpt-2-1-6b]]"]
related: ["[[llm-c]]", "[[loss-functions]]", "[[reproduce-a-published-model]]"]
---
# LLM evaluation
How he judges a model he has trained against someone else's: in the llm.c GPT-2 (124M) reproduction he plots validation loss on held-out FineWeb and accuracy on HellaSwag, a benchmark he says is commonly used to assess LLM capability, and compares both with OpenAI's released checkpoint ([[github-2024-05-28-llmc-gpt-2-124m]] §intro).

## What he says
Evaluation enters llm.c as a missing piece: on 2024-05-03 he lists "evaluation (WikiText 103?)" among the components still needed for a proper GPT-2 reproduction ([[github-2024-05-03-llmc-state-of-the-union]] §intro (Functional)). On 2024-05-24 the checklist for a serious "production" pretraining run includes evaluating on a standard dataset, then HellaSwag ([[github-2024-05-24-llmc-pytorch-cross-checks]] §intro).

**Validation loss is not a fair comparison.** His run beats OpenAI's checkpoint on the withheld FineWeb validation set, but he says this is not the ideal metric: GPT-2 was trained on the never-released WebText, and the internet's statistics may have been different five years earlier ([[github-2024-05-28-llmc-gpt-2-124m]] §intro).

**HellaSwag as the main number.** So he also plots HellaSwag accuracy, which he calls nice, smooth and well-behaved; he would mostly look at HellaSwag and treat FineWeb validation as a confirmation ([[github-2024-05-28-llmc-gpt-2-124m]] §intro). He adds a caveat himself: HellaSwag has no math or code, so it slightly favours his common-crawl-like training data ([[github-2024-05-28-llmc-gpt-2-124m]] §intro). The `-h 1` flag runs it, and he chose it as something comparable across papers ([[github-2024-05-28-llmc-gpt-2-124m]] §intro (Args guide)).

**Reference points.** His run reaches 29.9 (his result) against 29.4 for OpenAI's GPT-2 (124M) checkpoint and 33.7 for GPT-3 Small (124M) as cited in the GPT-3 paper's Appendix H (comparison numbers); he reminds the reader that his model trained on 10B tokens while the GPT-3 models all trained on 300B ([[github-2024-05-28-llmc-gpt-2-124m]] §intro).

**HellaSwag in the GPT-2 lecture (2024-06-09).** HellaSwag (2019) is a sentence-completion multiple-choice set: one natural continuation and wrong options drawn from ActivityNet and WikiHow contexts ([[youtube-2024-06-09-reproduce-gpt-2]] @3:28:13, @3:28:47, @3:29:22, @3:29:55). Per the paper, the wrong options were generated adversarially by language models to be hard for models but easy for humans, who scored 95% against 48% for the best models of the time ([[youtube-2024-06-09-reproduce-gpt-2]] @3:30:32). Today models score about 96%, so he considers it crushed, the last points likely dataset errors ([[youtube-2024-06-09-reproduce-gpt-2]] @3:31:05). People like it, he says, because it is smooth and gives early signal: small models start at the 25% chance level and improve slowly; it appears in the GPT-3 paper, not GPT-2's ([[youtube-2024-06-09-reproduce-gpt-2]] @3:31:05, @3:31:39, @3:32:15).

Small models cannot do multiple choice with labels, so he scores each option as a token completion and picks the one with the lowest average loss, which he believes is how GPT-3 did it; seeing all options at once is an easier format ([[youtube-2024-06-09-reproduce-gpt-2]] @3:32:47, @3:33:55, @3:34:29, @3:35:02). His script scores GPT-2 124M at 29.55% and GPT-2 XL at about 49%; the Eleuther harness gets slightly different numbers, possibly because it uses the multiple-choice format ([[youtube-2024-06-09-reproduce-gpt-2]] @3:37:16, @3:37:48). HellaSwag might have leaked into FineWeb's training data; he hopes Hugging Face deduplicated against it but cannot be sure, so it is not a perfect eval ([[youtube-2024-06-09-reproduce-gpt-2]] @3:45:57, @3:46:29). Saving checkpoints lets you evaluate more carefully later, for example with the Eleuther harness on math, code or other languages ([[youtube-2024-06-09-reproduce-gpt-2]] @3:54:47, @3:55:21).

**Wider evals, and a suspected overlap (2024-06-12).** After the 774M run beat expectations he plans to convert the checkpoint to Hugging Face format and run a wider, bigger suite of evals before the next big run ([[github-2024-06-12-llmc-gpt-2-774m]] §intro (Reflections)). A downward kink in validation loss exactly at the one-epoch boundary makes him nervous that FineWeb's validation and training sets overlap more than expected ([[github-2024-06-12-llmc-gpt-2-774m]] §intro (Reflections)).

**Reading the 1.6B evals (2024-07-11).** OpenAI's GPT-2 scores 2.83 on FineWeb-Edu validation loss by his measurement, and his run passes it by about step 5,000; he calls that unfair because GPT-2 trained on the never-released WebText, and shows that finetuning OpenAI's model for 1,000 steps at LR 1e-4 drops its loss to 2.61 as it adapts to the new data ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (Evals)). He looks at validation loss as a sanity check and wants fixed third-party evals for the real comparison; HellaSwag, simple common-sense scenarios where the model picks the right continuation, is well-behaved, smooth, common, often cited and gives early signal ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (Evals)). Even HellaSwag is not an ideal single comparison, he says: it tests simple English and common sense, not multilingual, math or code, which WebText may have weighted more, and good evals are harder at GPT-2's capability because such models do not understand multiple choice and their samples cannot dent math or code evals ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (Evals)). Exporting to Hugging Face format enables the Eleuther harness and Hugging Face sampling, and `dev/eval` has instructions for the Eleuther harness and the Open LLM Leaderboard evals ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (Model export)).

## Claims
- [[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]]

## Related
- [[llm-c]] — the codebase whose runs are evaluated
- [[reproduce-a-published-model]] — evaluation as the last steps of a reproduction
- [[loss-functions]] — the validation loss read as perplexity
- [[overfitting-and-generalization]] — train and validation splits in the earlier lectures
