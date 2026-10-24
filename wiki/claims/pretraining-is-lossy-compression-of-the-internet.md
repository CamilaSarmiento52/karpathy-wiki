---
type: claim
stated_on: 2023-11-23
confidence: stated
sources: ["[[youtube-2023-11-23-intro-to-llms]]", "[[youtube-2025-02-05-deep-dive-into-llms]]", "[[github-2025-10-13-nanochat-discussion-introducing]]", "[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]"]
topic: "[[pretraining-and-finetuning]]"
---
# Pretraining is like a lossy compression of a chunk of the internet into the parameters
> "like a zip file of the internet" — [[youtube-2023-11-23-intro-to-llms]] @05:30

## Context
Training Llama 2 70B takes roughly 10 TB of crawled internet text and compresses it into 140 GB of parameters, about 100x, which he says are best thought of as a zip file of the internet ([[youtube-2023-11-23-intro-to-llms]] @04:25, @05:30). Unlike a zip file the compression is lossy: the parameters hold a kind of Gestalt of the text, not an identical copy ([[youtube-2023-11-23-intro-to-llms]] @05:30). He calls training a compression because there is a close mathematical relationship between prediction and compression ([[youtube-2023-11-23-intro-to-llms]] @07:10, @07:43).

The objective is simple but powerful: predicting the next word on, say, a Wikipedia page about Ruth Handler requires knowing who she was, when she lived and what she did, so the network learns a lot about the world and compresses that knowledge into its weights ([[youtube-2023-11-23-intro-to-llms]] @07:43, @08:16, @08:50). Because the compression is lossy, sampling from it "dreams" plausible documents, and you never know which parts are memorized and which hallucinated ([[youtube-2023-11-23-intro-to-llms]] @08:50, @10:30, @11:02).

In the Deep Dive lecture, published 2025-02-05, he says the same of Llama 3.1's 405 billion parameters: a kind of compression of the internet, like a zip file but lossy, from which you can still generate ([[youtube-2025-02-05-deep-dive-into-llms]] @49:59). His recap of pretraining calls the result kind of a lossy compression of the internet ([[youtube-2025-02-05-deep-dive-into-llms]] @2:07:45).

In the nanochat launch post, dated 2025-10-13, he describes pretraining as training the LLM to compress internet web text by predicting the next token, the stage "where the LLM gains a lot of knowledge about the world" ([[github-2025-10-13-nanochat-discussion-introducing]] §Pretraining).

In the Dwarkesh interview, published 2025-10-17, he says anything in the weights is only a hazy recollection of training, because the compression is dramatic, trillions of tokens into a few billion parameters, while what is in the context window is directly accessible, like working memory ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @18:39, @19:16). His example: asked about a book, a model gives roughly correct answers, and given the full chapter it does much better ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @19:16, @19:53). He says "I kind of agree" with Dwarkesh's comparison of information per token in the weights and in the KV cache; the figures are Dwarkesh's ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @17:24, @18:03).

## Related claims
- **Note:** [[pretraining-gives-a-document-completer]] is the same picture from the output side: a model that dreams internet documents is a document completer, not an assistant ([[youtube-2023-11-23-intro-to-llms]] @08:50, @20:30).
- **Note:** in the same interview he says most of that compression is memory work rather than cognitive work, because the internet is so bad, and wants to remove the memory and keep the cognition; see [[cognitive-core]]. No relation is set between the claims ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @1:01:26, @1:02:04).
