---
type: artifact
repo_url: https://github.com/karpathy/makemore
language: Python
status: active
sources: ["[[youtube-2022-09-07-makemore-1-bigram]]", "[[youtube-2022-09-12-makemore-2-mlp]]", "[[youtube-2022-10-04-makemore-3-activations-batchnorm]]", "[[youtube-2022-10-11-makemore-4-backprop-ninja]]"]
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

- Part 3 scrutinises the part-2 MLP's activations and gradients: about 32,000 names, a 27-token vocabulary with a special dot, split into train, dev and test; the starting net has about 11,000 parameters and reaches about 2.16 ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @00:00, @00:33, @01:06, @01:39, @02:12).
- Fixing the output scale and then tanh saturation moved validation loss from 2.17 to 2.13 to 2.10 ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @25:57).
- The bonus section rewrites the code into `Linear`, `BatchNorm1d` and `Tanh` modules with the `torch.nn` API, a six-layer MLP of about 46,000 parameters, and introduces his diagnostic plots ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:18:47, @1:25:25, @1:25:58, @1:52:07).
- He suspects performance is no longer bottlenecked by optimisation but by the three-character context, and that RNNs and Transformers are needed to push further ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:53:45, @1:54:17).

- Part 4 pauses the series to write the backward pass of the two-layer MLP with batchnorm by hand; the notebook is on GitHub and Google Colab, and he recommends attempting each gradient yourself before watching him ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @00:00, @07:13, @12:10, @12:41).
- Its starter code expands the forward pass into many intermediate tensors and retains their grads so each manual gradient can be checked ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @09:26, @09:58).
- Exercise four trains the MLP with only manual gradients, `torch.no_grad` and a zip of parameters and gradients for the update, reaching a similar loss and name-like samples with about 20 lines of backward code; the next lecture moves to RNNs and LSTMs ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:51:04, @1:52:13, @1:52:46, @1:53:18, @1:54:58).

## Related
- [[character-level-language-modeling]] — the task
- [[bigram-language-model]] — the first model
- [[multilayer-perceptron]], [[embeddings]] — the second model
- [[learning-rate-sweep]], [[diagnose-under-or-overfitting]], [[training-diagnostics]]
- [[weight-initialization]], [[batch-normalization]] — the third lecture's fixes
- [[micrograd]] — the predecessor repo and lecture
- [[spelled-out-build-from-scratch]], [[check-shapes-and-broadcasting]], [[verify-gradients-against-pytorch]]
- [[backpropagation]] — the fourth lecture's hand-written tensor backward pass
- **Note:** the series' endpoint is a GPT-2-grade transformer; [[nanogpt]] is his later repo for that, a connection the source does not make.
