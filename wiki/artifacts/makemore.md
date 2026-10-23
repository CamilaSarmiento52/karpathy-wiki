---
type: artifact
repo_url: https://github.com/karpathy/makemore
language: Python
status: active
sources: ["[[youtube-2022-09-07-makemore-1-bigram]]", "[[youtube-2022-09-12-makemore-2-mlp]]"]
aliases: [make more]
---
# makemore
makemore is a repository on his GitHub that, like micrograd before it, he builds out step by step in a video series; it makes more of the things you give it, and under the hood it is a character-level language model ([[youtube-2022-09-07-makemore-1-bigram]] @00:00, @01:06).

## What it demonstrates
- The example dataset `names.txt` holds about 32,000 names he found on a government website ([[youtube-2022-09-07-makemore-1-bigram]] @00:00, @00:34).
- Trained on names it generates unique name-like strings such as Dontal, Irot and Zendy ([[youtube-2022-09-07-makemore-1-bigram]] @01:06).
- The announced series implements bigram and bag-of-words models, MLPs, RNNs and a transformer he says is basically equivalent to GPT-2 ([[youtube-2022-09-07-makemore-1-bigram]] @02:13).
- Possible later extensions: word level, then images and image-text networks such as DALL-E and Stable Diffusion ([[youtube-2022-09-07-makemore-1-bigram]] @02:13, @02:45).
- Part 1 builds the bigram model twice, by counting and as a one-layer net, and shows they are the same model ([[youtube-2022-09-07-makemore-1-bigram]] @1:49:31, @1:55:39).
- `status: active` comes from this 2022 source; a later GitHub README snapshot should decide the real status ([[youtube-2022-09-07-makemore-1-bigram]] @00:00).

- Part 2 implements the MLP step of the plan on 228,000 three-character examples from the same 32,000 names, reaching a best validation loss of 2.17 ([[youtube-2022-09-12-makemore-2-mlp]] @01:40, @08:55, @41:35, @1:11:38).
- He shares a Google Colab so the notebook runs in the browser with no installation ([[youtube-2022-09-12-makemore-2-mlp]] @1:14:57, @1:15:30).

## Related
- [[character-level-language-modeling]] — the task
- [[bigram-language-model]] — the first model
- [[multilayer-perceptron]], [[embeddings]] — the second model
- [[learning-rate-sweep]], [[diagnose-under-or-overfitting]]
- [[micrograd]] — the predecessor repo and lecture
- [[spelled-out-build-from-scratch]], [[check-shapes-and-broadcasting]]
- **Note:** the series' endpoint is a GPT-2-grade transformer; [[nanogpt]] is his later repo for that, a connection the source does not make.
