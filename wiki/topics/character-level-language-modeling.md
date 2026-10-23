---
type: topic
aliases: [Character-level language model, language modeling, sampling, makemore task]
first_seen: 2022-09-07
last_updated: 2022-09-12
sources: ["[[youtube-2022-09-07-makemore-1-bigram]]", "[[youtube-2022-09-12-makemore-2-mlp]]"]
related: ["[[makemore]]", "[[bigram-language-model]]", "[[softmax]]", "[[loss-functions]]"]
---
# Character-level language modeling
A character-level language model treats each line of a dataset as an example and each example as a sequence of characters, and predicts the next character given the ones before it ([[youtube-2022-09-07-makemore-1-bigram]] @01:06, @01:39, @04:24).

## What he says
One word like Isabella contains many examples: which character comes first, which follows each prefix, and that the word is likely to end after the last letter ([[youtube-2022-09-07-makemore-1-bigram]] @04:24, @04:58). With about 32,000 words there is a lot of statistical structure to model; the dataset's shortest word has 2 characters and the longest 15 ([[youtube-2022-09-07-makemore-1-bigram]] @03:52, @05:31).

To sample from the bigram model, he starts at the `.` token, takes that row of counts, converts to float and normalises to a probability vector, then draws an index ([[youtube-2022-09-07-makemore-1-bigram]] @24:17, @25:21, @25:52). `torch.multinomial` takes probabilities and returns integers sampled according to them; `replacement=True` must be set because it defaults to false ([[youtube-2022-09-07-makemore-1-bigram]] @26:26, @28:05, @28:37). He uses a seeded `torch.Generator` so viewers get exactly the same results as he does ([[youtube-2022-09-07-makemore-1-bigram]] @26:59, @27:32). The loop feeds each sampled character back in as the row for the next draw and stops when index 0, the end token, is sampled ([[youtube-2022-09-07-makemore-1-bigram]] @31:26, @32:02, @32:35). Comparing against a uniform distribution over 27 characters shows the trained bigram model is more name-like than an untrained one, though still bad ([[youtube-2022-09-07-makemore-1-bigram]] @35:24, @35:58). Re-normalising a row on every step is wasteful, so he precomputes a probability matrix P once, also as practice for tensor manipulation ([[youtube-2022-09-07-makemore-1-bigram]] @36:30, @37:03). The same sampling loop works for the neural net by replacing the row lookup with one-hot, W, exp and normalise ([[youtube-2022-09-07-makemore-1-bigram]] @1:54:33, @1:55:05).

The 32,000 names give 228,000 three-character examples for the MLP ([[youtube-2022-09-12-makemore-2-mlp]] @08:55, @41:35). Sampling from the MLP works the same way: start from dots, embed the context, get logits, apply `F.softmax`, draw with `torch.multinomial`, and shift the window ([[youtube-2022-09-12-makemore-2-mlp]] @1:13:16, @1:13:50).

## Claims
- [[the-logits-softmax-nll-machinery-stays-fixed-up-to-transformers]]
- [[counting-and-gradient-bigram-models-are-the-same-model]]

## Related
- [[makemore]] — the repo built around this task
- [[bigram-language-model]] — the first model
- [[softmax]] — turning logits into the distribution sampled from
- [[loss-functions]] — negative log likelihood as the quality measure
- [[multilayer-perceptron]] — the second model
