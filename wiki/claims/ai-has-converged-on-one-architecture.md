---
type: claim
stated_on: 2023-05-19
confidence: stated
sources: ["[[talk-2023-05-19-stanford-cs25-transformers]]"]
topic: "[[transformer-architecture]]"
---
# Since 2017, AI fields have converged on one architecture, the Transformer
> "literally the architecture is converged to like one architecture" — [[talk-2023-05-19-stanford-cs25-transformers]] @13:56

## Context
Opening his CS25 lecture, he recalls computer-vision papers around 2011 spending pages on a zoo of feature descriptors with an SVM on top, collecting code from everywhere, and it not working well ([[talk-2023-05-19-stanford-cs25-transformers]] @11:12, @11:43, @12:16). Each area of AI had its own vocabulary, so you could not read papers across areas ([[talk-2023-05-19-stanford-cs25-transformers]] @12:16, @12:50). From 2012, Krizhevsky and colleagues showed that a large neural net on a large dataset performs strongly; the focus moved from algorithms to compute and data, and the recipe was copy-pasted across vision, NLP, speech, translation and RL, lowering the barrier to entry ([[talk-2023-05-19-stanford-cs25-transformers]] @12:50, @13:23).

Since 2017, he says, the Transformer is copy-pasted everywhere and what changes is the data and how it is chunked and fed; he calls this a caricature but a correct first-order statement ([[talk-2023-05-19-stanford-cs25-transformers]] @13:56, @14:28). He offers, hedged with "maybe", that this hints we are converging to something like what the brain does, since the cortex is homogeneous across areas ([[talk-2023-05-19-stanford-cs25-transformers]] @14:28, @15:00). His examples include ViT image patches, speech spectrogram slices including Whisper, the Decision Transformer, and a Transformer at the computational heart of AlphaFold ([[talk-2023-05-19-stanford-cs25-transformers]] @52:43, @53:17, @53:50).

## Related claims
- **Note:** [[the-logits-softmax-nll-machinery-stays-fixed-up-to-transformers]] is about one lecture series' pipeline staying fixed, not about fields converging; the pages are adjacent, not linked as support ([[talk-2023-05-19-stanford-cs25-transformers]] @13:56).
