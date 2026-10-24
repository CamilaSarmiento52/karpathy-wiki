---
type: topic
aliases: [Embeddings, embedding table, lookup table, positional embeddings, positional encodings, weight tying, tied embeddings, learned position embeddings]
first_seen: 2022-09-12
last_updated: 2024-06-09
sources: ["[[youtube-2022-09-12-makemore-2-mlp]]", "[[youtube-2023-01-17-gpt-from-scratch]]", "[[talk-2023-05-19-stanford-cs25-transformers]]", "[[youtube-2024-02-20-gpt-tokenizer]]", "[[youtube-2024-06-09-reproduce-gpt-2]]"]
related: ["[[multilayer-perceptron]]", "[[softmax]]", "[[pytorch]]", "[[makemore]]"]
---
# Embeddings
In the Bengio et al. 2003 model each word gets a roughly 30-dimensional feature vector, initialised randomly and tuned by backpropagation, stored as a lookup table C that is shared across all input positions; each index plucks out a row ([[youtube-2022-09-12-makemore-2-mlp]] @02:46, @03:21, @06:08, @06:42).

## What he says
Words are embedded as points in a small space, and similar words or synonyms may end up near each other after training ([[youtube-2022-09-12-makemore-2-mlp]] @03:21, @03:54). Embeddings let the model handle an out-of-distribution phrase by transferring knowledge from nearby embeddings, as between "a" and "the", or cats and dogs ([[youtube-2022-09-12-makemore-2-mlp]] @04:27, @05:01, @05:34).

A one-hot vector times C gives the same result as indexing the row, because the zeros mask out every other row ([[youtube-2022-09-12-makemore-2-mlp]] @13:19, @14:58). The embedding can therefore be read either as a lookup or as the first linear layer of the network with weight matrix C; he indexes because it is much faster and calls the two equivalent ways of doing the same thing ([[youtube-2022-09-12-makemore-2-mlp]] @15:30, @16:02). PyTorch can index C with a list, a tensor, or a multi-dimensional tensor of integers, so `C[X]` embeds all 32-by-3 integers at once ([[youtube-2022-09-12-makemore-2-mlp]] @16:34, @17:07, @18:16).

After training with 2D embeddings, the vowels a, e, i, o, u cluster together, q and the dot are outliers, and the structure is not random ([[youtube-2022-09-12-makemore-2-mlp]] @1:06:02, @1:06:35). He suspects two dimensions are the bottleneck and raises the embedding size to 10; the lower loss afterwards suggests the embedding size was holding the model back ([[youtube-2022-09-12-makemore-2-mlp]] @1:04:25, @1:07:08, @1:11:05).

In the GPT lecture he adds positional embeddings: beyond token identity, a second embedding table of block size by n_embd gives each position its own vector, and the input x becomes token embeddings plus positional embeddings, broadcast across the batch ([[youtube-2023-01-17-gpt-from-scratch]] @1:00:15, @1:00:47, @1:01:20). For a bigram model position is useless because the model is translation invariant; it starts to matter with self-attention, whose nodes have no notion of where they are ([[youtube-2023-01-17-gpt-from-scratch]] @1:01:20, @1:12:32). Because the table only covers block-size positions, generation must crop the context to the last block-size tokens ([[youtube-2023-01-17-gpt-from-scratch]] @1:20:55).

In the CS25 lecture he explains that because the Transformer processes sets, token-identity embeddings and positional embeddings are added together to give what and where ([[talk-2023-05-19-stanford-cs25-transformers]] @35:29, @36:01). Extra inputs such as radar or vehicle information get a learnable special embedding token so the Transformer knows their source ([[talk-2023-05-19-stanford-cs25-transformers]] @1:04:42). Positional encodings can be hard-wired with sines and cosines, but he prefers a trainable vector that always sits at a location, and says they carry very little inductive bias ([[talk-2023-05-19-stanford-cs25-transformers]] @1:05:18, @1:05:57). Rotary and relative positional encodings are now more common than the original ([[talk-2023-05-19-stanford-cs25-transformers]] @22:11).

In the tokenizer lecture each token's integer looks up a row of trainable parameters in the embedding table, and that vector is how the Transformer perceives the token ([[youtube-2024-02-20-gpt-tokenizer]] @01:40, @02:12). A larger vocabulary means more rows, and rare tokens get few examples, so their vectors may be undertrained ([[youtube-2024-02-20-gpt-tokenizer]] @1:44:13, @1:45:18, @1:45:51). Adding a token means adding a row initialised with small random numbers ([[youtube-2024-02-20-gpt-tokenizer]] @1:24:37, @1:47:32). A token that never appears in the LLM's training data keeps a random row that is never updated; he likens it to unallocated memory in a C program, so invoking it gives undefined behaviour, his reading of SolidGoldMagikarp ([[youtube-2024-02-20-gpt-tokenizer]] @2:08:24, @2:08:57).

**GPT-2's embeddings (2024-06-09).** In the released GPT-2 weights the token embedding is 50,257 × 768 and the position embedding covers 1,024 positions, each a learned 768-dimensional vector ([[youtube-2024-06-09-reproduce-gpt-2]] @06:06, @07:13). Plotted, the learned position embeddings show sinusoid-like structure; their jaggedness suggests to him the model was somewhat undertrained, and since they start as random noise he finds the smooth structure falling out of optimisation impressive ([[youtube-2024-06-09-reproduce-gpt-2]] @08:19, @09:30, @10:03). In the original Transformer paper the positional encodings were, if he remembers correctly, fixed sinusoids; in GPT-2 they are trained, which seems to work about as well ([[youtube-2024-06-09-reproduce-gpt-2]] @10:03, @10:37).

**Weight tying.** In GPT-2 the token embedding at the bottom and the language-model head at the top are one tensor: same shape, same values, same data pointer ([[youtube-2024-06-09-reproduce-gpt-2]] @1:06:53, @1:07:27, @1:07:58). The scheme comes from "Attention is all you need" and a 2017 paper it cites; the intuition is that semantically similar tokens should be close in embedding space and also get similar output probabilities ([[youtube-2024-06-09-reproduce-gpt-2]] @1:07:58, @1:08:34, @1:09:07). In his summary, that paper found output embeddings behave like word embeddings and that tying improved performance a lot ([[youtube-2024-06-09-reproduce-gpt-2]] @1:09:41). He could not find the tying in Hugging Face's implementation but found it in OpenAI's TensorFlow GPT-2 code, where the embedding is reused to compute the logits and gets gradient from both ends ([[youtube-2024-06-09-reproduce-gpt-2]] @1:10:14, @1:10:46, @1:11:19). It saves about 40M of the 124M parameters, roughly 30%, which may be one reason it helps when training is short ([[youtube-2024-06-09-reproduce-gpt-2]] @1:13:03).

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
- [[tokenization]] — what the integers come from
