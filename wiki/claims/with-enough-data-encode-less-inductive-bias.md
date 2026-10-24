---
type: claim
stated_on: 2023-05-19
confidence: stated
sources: ["[[talk-2023-05-19-stanford-cs25-transformers]]"]
topic: "[[transformer-architecture]]"
---
# With enough data, he says, hand-coded inductive biases tend to hurt
> "if you have Infinity data then you actually want to encode less and less" — [[talk-2023-05-19-stanford-cs25-transformers]] @1:06:28

## Context
Answering a question about inductive biases in the CS25 Q&A, he says that with enough data, trying to put knowledge in is usually not productive; it depends on scale, and with very little data you do want some biases, so convolutions may then be a good idea ([[talk-2023-05-19-stanford-cs25-transformers]] @1:06:28). In the Transformer, he says, the biases are factored out of the core into the connectivity between nodes and the positional encodings, which is where people add structure, for instance fixed sinusoidal encodings or masking attention to a patch neighbourhood ([[talk-2023-05-19-stanford-cs25-transformers]] @1:06:28, @1:07:00). He says there are perhaps 200 or more papers on such tricks ([[talk-2023-05-19-stanford-cs25-transformers]] @1:07:35).

## Related claims
- **Note:** he gives the same reason for preferring trainable positional vectors, which he says carry very little inductive bias; that sentence is on [[embeddings]] ([[talk-2023-05-19-stanford-cs25-transformers]] @1:05:57).
