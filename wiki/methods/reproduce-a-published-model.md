---
type: method
steps:
  - Pick a published model whose weights are released
  - Set the whole model series as the target
  - Take hyperparameters from the most detailed paper
  - Train from scratch on a modern open dataset
  - Compare held-out loss with the released checkpoint, and say why it is unfair
  - Confirm on a benchmark that is comparable across papers
  - Publish the launch command, the time and the cost
  - Scale to the next size and give it more tokens
sources: ["[[github-2024-05-03-llmc-state-of-the-union]]", "[[github-2024-05-28-llmc-gpt-2-124m]]"]
aliases: [Reproduce GPT-2, reproduce a paper, reproduction run]
---
# Reproduce a published model
How he tests a training stack: retrain a model someone has published, from scratch, and show that his run matches or beats the released checkpoint. In llm.c the model is GPT-2 (124M), reproduced in about 90 minutes for about $20 on one 8×A100 node ([[github-2024-05-28-llmc-gpt-2-124m]] §intro).

## Steps
1. **Pick a model with released weights.** He cares about GPT-2 because it was the first recognisably modern LLM stack and OpenAI released its parameters, and he picks the 124M, the smallest of the series, as accessible even for the "GPU poor" ([[github-2024-05-28-llmc-gpt-2-124m]] §intro, §intro (FAQ)).
2. **Aim at the whole series.** On 2024-05-03 the stated goal of llm.c is to reproduce the GPT-2 miniseries of all sizes, 124M to 1.6B, directly in C/CUDA ([[github-2024-05-03-llmc-state-of-the-union]] §intro (Goal)).
3. **Borrow the most detailed recipe.** Many hyperparameters follow the GPT-3 paper rather than GPT-2's, because it was a lot more detailed; the ~0.5M-token batch, for example, comes from the GPT-3 table for this size, since GPT-2's batch size is unknown ([[github-2024-05-28-llmc-gpt-2-124m]] §intro (Args guide)).
4. **Train from scratch on open data.** The run trains a 12-layer GPT-2 (124M) from scratch on 10B tokens of FineWeb with sequence length 1024 ([[github-2024-05-28-llmc-gpt-2-124m]] §intro (Args guide)).
5. **Compare with the checkpoint, and say why it is unfair.** His run beats OpenAI's checkpoint on held-out FineWeb validation loss, which he calls not a super fair comparison because GPT-2 trained on different data ([[github-2024-05-28-llmc-gpt-2-124m]] §intro).
6. **Confirm on a shared benchmark.** He evaluates HellaSwag because it can be compared across papers, and reports 29.9 for his run against 29.4 for GPT-2 (124M) and 33.7 for GPT-3 Small as cited in the GPT-3 paper ([[github-2024-05-28-llmc-gpt-2-124m]] §intro, §intro (Args guide)).
7. **Publish the recipe and the bill.** He gives the full install and launch commands, explains every flag, and states time and cost: about 90 minutes at about $14/hour, about $20 ([[github-2024-05-28-llmc-gpt-2-124m]] §intro, §intro (Args guide)).
8. **Scale up with more tokens.** Overnight he reproduced the 350M model, found 10B tokens was not enough, and trained about 30B tokens in 14 hours for about $200; next on his list is the 1558M "GPT-2" ([[github-2024-05-28-llmc-gpt-2-124m]] §intro (350M model), §intro (Coming up)).

## Seen in
- [[llm-c]]
- [[github-2024-05-28-llmc-gpt-2-124m]]
- [[llm-evaluation]] — the comparison steps
- [[verify-against-a-reference-implementation]] — the parity checks that came first
