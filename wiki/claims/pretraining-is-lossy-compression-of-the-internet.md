---
type: claim
stated_on: 2023-11-23
confidence: stated
sources: ["[[youtube-2023-11-23-intro-to-llms]]", "[[youtube-2025-02-05-deep-dive-into-llms]]"]
topic: "[[pretraining-and-finetuning]]"
---
# Pretraining is like a lossy compression of a chunk of the internet into the parameters
> "like a zip file of the internet" — [[youtube-2023-11-23-intro-to-llms]] @05:30

## Context
Training Llama 2 70B takes roughly 10 TB of crawled internet text and compresses it into 140 GB of parameters, about 100x, which he says are best thought of as a zip file of the internet ([[youtube-2023-11-23-intro-to-llms]] @04:25, @05:30). Unlike a zip file the compression is lossy: the parameters hold a kind of Gestalt of the text, not an identical copy ([[youtube-2023-11-23-intro-to-llms]] @05:30). He calls training a compression because there is a close mathematical relationship between prediction and compression ([[youtube-2023-11-23-intro-to-llms]] @07:10, @07:43).

The objective is simple but powerful: predicting the next word on, say, a Wikipedia page about Ruth Handler requires knowing who she was, when she lived and what she did, so the network learns a lot about the world and compresses that knowledge into its weights ([[youtube-2023-11-23-intro-to-llms]] @07:43, @08:16, @08:50). Because the compression is lossy, sampling from it "dreams" plausible documents, and you never know which parts are memorized and which hallucinated ([[youtube-2023-11-23-intro-to-llms]] @08:50, @10:30, @11:02).

In the Deep Dive lecture, published 2025-02-05, he says the same of Llama 3.1's 405 billion parameters: a kind of compression of the internet, like a zip file but lossy, from which you can still generate ([[youtube-2025-02-05-deep-dive-into-llms]] @49:59). His recap of pretraining calls the result kind of a lossy compression of the internet ([[youtube-2025-02-05-deep-dive-into-llms]] @2:07:45).

## Related claims
- **Note:** [[pretraining-gives-a-document-completer]] is the same picture from the output side: a model that dreams internet documents is a document completer, not an assistant ([[youtube-2023-11-23-intro-to-llms]] @08:50, @20:30).
