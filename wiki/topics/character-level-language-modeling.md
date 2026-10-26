---
type: topic
aliases: [Character-level language model, language modeling, makemore task, tiny Shakespeare]
first_seen: 2022-09-07
last_updated: 2026-02-12
sources: ["[[youtube-2022-09-07-makemore-1-bigram]]", "[[youtube-2022-09-12-makemore-2-mlp]]", "[[github-2022-11-20-makemore-readme]]", "[[talk-2023-05-19-stanford-cs25-transformers]]", "[[blog-2026-02-12-microgpt]]"]
related: ["[[makemore]]", "[[bigram-language-model]]", "[[softmax]]", "[[loss-functions]]"]
---
# Character-level language modeling
A character-level language model treats each line of a dataset as an example and each example as a sequence of characters, and predicts the next character given the ones before it ([[youtube-2022-09-07-makemore-1-bigram]] @01:06, @01:39, @04:24).

## What he says
One word like Isabella contains many examples: which character comes first, which follows each prefix, and that the word is likely to end after the last letter ([[youtube-2022-09-07-makemore-1-bigram]] @04:24, @04:58). With about 32,000 words there is a lot of statistical structure to model; the dataset's shortest word has 2 characters and the longest 15 ([[youtube-2022-09-07-makemore-1-bigram]] @03:52, @05:31).

To sample from the bigram model, he starts at the `.` token, takes that row of counts, converts to float and normalises to a probability vector, then draws an index ([[youtube-2022-09-07-makemore-1-bigram]] @24:17, @25:21, @25:52). `torch.multinomial` takes probabilities and returns integers sampled according to them; `replacement=True` must be set because it defaults to false ([[youtube-2022-09-07-makemore-1-bigram]] @26:26, @28:05, @28:37). He uses a seeded `torch.Generator` so viewers get exactly the same results as he does ([[youtube-2022-09-07-makemore-1-bigram]] @26:59, @27:32). The loop feeds each sampled character back in as the row for the next draw and stops when index 0, the end token, is sampled ([[youtube-2022-09-07-makemore-1-bigram]] @31:26, @32:02, @32:35). Comparing against a uniform distribution over 27 characters shows the trained bigram model is more name-like than an untrained one, though still bad ([[youtube-2022-09-07-makemore-1-bigram]] @35:24, @35:58). Re-normalising a row on every step is wasteful, so he precomputes a probability matrix P once, also as practice for tensor manipulation ([[youtube-2022-09-07-makemore-1-bigram]] @36:30, @37:03). The same sampling loop works for the neural net by replacing the row lookup with one-hot, W, exp and normalise ([[youtube-2022-09-07-makemore-1-bigram]] @1:54:33, @1:55:05).

The 32,000 names give 228,000 three-character examples for the MLP ([[youtube-2022-09-12-makemore-2-mlp]] @08:55, @41:35). Sampling from the MLP works the same way: start from dots, embed the context, get logits, apply `F.softmax`, draw with `torch.multinomial`, and shift the window ([[youtube-2022-09-12-makemore-2-mlp]] @1:13:16, @1:13:50).

The makemore README frames the task the same way: each line of a text file is one training example, and the model learns to generate more lines like it, one character at a time, as an autoregressive character-level language model ([[github-2022-11-20-makemore-readme]] §intro). The simplest version is a bigram model, where one character predicts the next from a lookup table of counts; the README lists an MLP, RNN, LSTM, GRU, CNN and Transformer as other models for the same task ([[github-2022-11-20-makemore-readme]] §intro). His example inputs are names, company names and Scrabble words ([[github-2022-11-20-makemore-readme]] §intro).

In the CS25 lecture his character-level example is tiny Shakespeare, one of his favourite toy datasets: all of Shakespeare concatenated into a file of about 1 MB ([[talk-2023-05-19-stanford-cs25-transformers]] @31:35). Batches are B×T chunks of the one-dimensional sequence; block size is the maximum context, and a 4×8 batch holds many examples because every prefix predicts its next element ([[talk-2023-05-19-stanford-cs25-transformers]] @32:40, @33:15, @33:48, @34:19). His generation loop for it is on [[sampling-from-language-models]] ([[talk-2023-05-19-stanford-cs25-transformers]] @41:34).

**microgpt (2026-02-12).** The goal is to learn the statistical patterns of about 32,000 names and generate new, plausible-sounding ones ([[blog-2026-02-12-microgpt]] §Dataset). The model learns a distribution that reflects rules such as names often starting with consonants, "qu" appearing together and three consonants in a row being rare, not the rules themselves ([[blog-2026-02-12-microgpt]] §FAQ). Swap in city names, Pokemon names, English words or short poems and it learns those instead, with no other code change; see [[microgpt]] ([[blog-2026-02-12-microgpt]] §FAQ).

## Claims
- [[the-logits-softmax-nll-machinery-stays-fixed-up-to-transformers]]
- [[counting-and-gradient-bigram-models-are-the-same-model]]

## Related
- [[makemore]] — the repo built around this task
- [[bigram-language-model]] — the first model
- [[softmax]] — turning logits into the distribution sampled from
- [[loss-functions]] — negative log likelihood as the quality measure
- [[multilayer-perceptron]] — the second model
- [[tokenization]] — the character-level choice against sub-word tokenizers
- [[sampling-from-language-models]] — sampling in general; this page keeps the bigram and MLP sampling loops
