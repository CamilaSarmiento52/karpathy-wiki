---
type: artifact
repo_url: https://github.com/karpathy/makemore
language: Python
status: active
sources: ["[[youtube-2022-09-07-makemore-1-bigram]]", "[[youtube-2022-09-12-makemore-2-mlp]]", "[[youtube-2022-10-04-makemore-3-activations-batchnorm]]", "[[youtube-2022-10-11-makemore-4-backprop-ninja]]", "[[github-2022-11-20-makemore-readme]]", "[[youtube-2022-11-21-makemore-5-wavenet]]", "[[github-2024-02-20-nn-zero-to-hero-readme]]"]
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
- `status: active` comes from this 2022 source; the README snapshot of 2022-11-20 carries no deprecation notice, so it stands until a later snapshot says otherwise ([[youtube-2022-09-07-makemore-1-bigram]] @00:00; [[github-2022-11-20-makemore-readme]] §intro).

- Part 2 implements the MLP step of the plan on 228,000 three-character examples from the same 32,000 names, reaching a best validation loss of 2.17 ([[youtube-2022-09-12-makemore-2-mlp]] @01:40, @08:55, @41:35, @1:11:38).
- He shares a Google Colab so the notebook runs in the browser with no installation ([[youtube-2022-09-12-makemore-2-mlp]] @1:14:57, @1:15:30).

- Part 3 scrutinises the part-2 MLP's activations and gradients: about 32,000 names, a 27-token vocabulary with a special dot, split into train, dev and test; the starting net has about 11,000 parameters and reaches about 2.16 ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @00:00, @00:33, @01:06, @01:39, @02:12).
- Fixing the output scale and then tanh saturation moved validation loss from 2.17 to 2.13 to 2.10 ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @25:57).
- The bonus section rewrites the code into `Linear`, `BatchNorm1d` and `Tanh` modules with the `torch.nn` API, a six-layer MLP of about 46,000 parameters, and introduces his diagnostic plots ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:18:47, @1:25:25, @1:25:58, @1:52:07).
- He suspects performance is no longer bottlenecked by optimisation but by the three-character context, and that RNNs and Transformers are needed to push further ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:53:45, @1:54:17).

- Part 4 pauses the series to write the backward pass of the two-layer MLP with batchnorm by hand; the notebook is on GitHub and Google Colab, and he recommends attempting each gradient yourself before watching him ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @00:00, @07:13, @12:10, @12:41).
- Its starter code expands the forward pass into many intermediate tensors and retains their grads so each manual gradient can be checked ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @09:26, @09:58).
- Exercise four trains the MLP with only manual gradients, `torch.no_grad` and a zip of parameters and gradients for the update, reaching a similar loss and name-like samples with about 20 lines of backward code; the next lecture moves to RNNs and LSTMs ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:51:04, @1:52:13, @1:52:46, @1:53:18, @1:54:58).

- Part 5 starts from part 3's code (part 4 was the manual-backpropagation aside) with about 12,000 parameters, a validation loss of 2.10 and name-like samples not in the training set; with block size 3 there are 182,000 examples ([[youtube-2022-11-21-makemore-5-wavenet]] @01:36, @02:11, @05:33, @06:06, @06:40).
- It grows the MLP into a WaveNet-like hierarchical model: block size 8 alone gives 2.02, and the final 76,000-parameter model reaches 1.993; he invites viewers to beat it by reallocating channels, changing the embedding size, scaling the one-hidden-layer network, implementing WaveNet layers from the paper, or tuning initialisation and optimisation ([[youtube-2022-11-21-makemore-5-wavenet]] @20:29, @46:08, @55:06, @55:40, @56:12).
- Future lectures he names at the end of part 5: a convolutional version, residual and skip connections, an experimental harness, RNNs, LSTMs, GRUs and Transformers ([[youtube-2022-11-21-makemore-5-wavenet]] @53:57, @54:32, @55:06).

- The README describes makemore as taking a text file with one training example per line and generating more examples like it; under the hood it is an autoregressive character-level language model with models ranging from a bigram count table to a Transformer as in GPT ([[github-2022-11-20-makemore-readme]] §intro).
- He suggests feeding it names to get name-like baby names that do not already exist, company names, or valid Scrabble words for English-like babble ([[github-2022-11-20-makemore-readme]] §intro).
- It is one hackable file, mostly intended for education, and PyTorch is its only requirement ([[github-2022-11-20-makemore-readme]] §intro).
- The implementations follow specific papers: a lookup table of counts for the bigram, Bengio et al. 2003 for the MLP, WaveNet 2016 for the CNN (marked in progress in this snapshot), Mikolov et al. 2010 for the RNN, Graves et al. 2014 for the LSTM, Cho et al. 2014 for the GRU and Vaswani et al. 2017 for the Transformer ([[github-2022-11-20-makemore-readme]] §intro).
- The bundled `names.txt` is the 32K most common names from ssa.gov for 2018 ([[github-2022-11-20-makemore-readme]] §Usage).
- The default model is a roughly 200K-parameter Transformer; other configurations are reachable through argparse and reading the code ([[github-2022-11-20-makemore-readme]] §Usage).
- Training needs no special hardware and runs on his MacBook Air, faster with a GPU; a `--sample-only` flag samples from the best model so far ([[github-2022-11-20-makemore-readme]] §Usage).
- The default settings reach a test log-probability of about 1.92, and he says lower is achievable with hyperparameter tuning ([[github-2022-11-20-makemore-readme]] §Usage).
- Licensed MIT; the README also backs the `repo_url` above, which group A1 took from the merge map ([[github-2022-11-20-makemore-readme]] §License).

- In the Zero to Hero README it is the companion repo of Lectures 2 to 5, and Lecture 6's WaveNet notebook continues the same series ([[github-2024-02-20-nn-zero-to-hero-readme]] §intro, Lectures 2–6).

## Related
- [[character-level-language-modeling]] — the task
- [[bigram-language-model]] — the first model
- [[multilayer-perceptron]], [[embeddings]] — the second model
- [[learning-rate-sweep]], [[diagnose-under-or-overfitting]], [[training-diagnostics]]
- [[weight-initialization]], [[batch-normalization]] — the third lecture's fixes
- [[wavenet-hierarchical-model]] — the fifth lecture's deeper model
- [[prototype-in-jupyter-then-repo]] — how he says the code gets written
- [[micrograd]] — the predecessor repo and lecture
- [[nn-zero-to-hero]] — the course the makemore lectures belong to
- [[spelled-out-build-from-scratch]], [[check-shapes-and-broadcasting]], [[verify-gradients-against-pytorch]]
- [[backpropagation]] — the fourth lecture's hand-written tensor backward pass
- [[small-hackable-educational-code]] — the README's one-file, PyTorch-only framing
- **Note:** the series' endpoint is a GPT-2-grade transformer; [[nanogpt]] is his later repo for that, a connection the source does not make.
