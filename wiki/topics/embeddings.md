---
type: topic
aliases: [Embeddings, embedding table, lookup table, positional embeddings]
first_seen: 2022-09-12
last_updated: 2023-01-17
sources: ["[[youtube-2022-09-12-makemore-2-mlp]]", "[[youtube-2023-01-17-gpt-from-scratch]]"]
related: ["[[multilayer-perceptron]]", "[[softmax]]", "[[pytorch]]", "[[makemore]]"]
---
# Embeddings
In the Bengio et al. 2003 model each word gets a roughly 30-dimensional feature vector, initialised randomly and tuned by backpropagation, stored as a lookup table C that is shared across all input positions; each index plucks out a row ([[youtube-2022-09-12-makemore-2-mlp]] @02:46, @03:21, @06:08, @06:42).

## What he says
Words are embedded as points in a small space, and similar words or synonyms may end up near each other after training ([[youtube-2022-09-12-makemore-2-mlp]] @03:21, @03:54). Embeddings let the model handle an out-of-distribution phrase by transferring knowledge from nearby embeddings, as between "a" and "the", or cats and dogs ([[youtube-2022-09-12-makemore-2-mlp]] @04:27, @05:01, @05:34).

A one-hot vector times C gives the same result as indexing the row, because the zeros mask out every other row ([[youtube-2022-09-12-makemore-2-mlp]] @13:19, @14:58). The embedding can therefore be read either as a lookup or as the first linear layer of the network with weight matrix C; he indexes because it is much faster and calls the two equivalent ways of doing the same thing ([[youtube-2022-09-12-makemore-2-mlp]] @15:30, @16:02). PyTorch can index C with a list, a tensor, or a multi-dimensional tensor of integers, so `C[X]` embeds all 32-by-3 integers at once ([[youtube-2022-09-12-makemore-2-mlp]] @16:34, @17:07, @18:16).

After training with 2D embeddings, the vowels a, e, i, o, u cluster together, q and the dot are outliers, and the structure is not random ([[youtube-2022-09-12-makemore-2-mlp]] @1:06:02, @1:06:35). He suspects two dimensions are the bottleneck and raises the embedding size to 10; the lower loss afterwards suggests the embedding size was holding the model back ([[youtube-2022-09-12-makemore-2-mlp]] @1:04:25, @1:07:08, @1:11:05).

In the GPT lecture he adds positional embeddings: beyond token identity, a second embedding table of block size by n_embd gives each position its own vector, and the input x becomes token embeddings plus positional embeddings, broadcast across the batch ([[youtube-2023-01-17-gpt-from-scratch]] @1:00:15, @1:00:47, @1:01:20). For a bigram model position is useless because the model is translation invariant; it starts to matter with self-attention, whose nodes have no notion of where they are ([[youtube-2023-01-17-gpt-from-scratch]] @1:01:20, @1:12:32). Because the table only covers block-size positions, generation must crop the context to the last block-size tokens ([[youtube-2023-01-17-gpt-from-scratch]] @1:20:55).

## Claims
- [[attention-is-a-communication-mechanism]] — attention acts over a set of vectors with no notion of space, which is why position is added
- [[gradient-based-models-scale-where-count-tables-do-not]] — embeddings are how the net takes more context than a table can

## Related
- [[multilayer-perceptron]] — the model the table feeds
- [[softmax]] — one-hot inputs, the other reading of the lookup
- [[pytorch]] — indexing and `.view`
- [[makemore]]
- [[self-attention]] — why positional embeddings are needed
- [[transformer-architecture]]
