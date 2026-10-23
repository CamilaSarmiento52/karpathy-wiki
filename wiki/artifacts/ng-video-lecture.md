---
type: artifact
repo_url: https://github.com/karpathy/ng-video-lecture
language: Python
status: active
sources: ["[[youtube-2023-01-17-gpt-from-scratch]]", "[[github-2023-01-31-ng-video-lecture-readme]]"]
aliases: [nanogpt-lecture, nanoGPT lecture code, bigram.py, gpt.py]
---
# ng-video-lecture
The code written during the GPT lecture: he develops it in a Google Colab notebook he shares in the video description, turns it into a roughly 120-line script he calls `bigram.py`, and ends with roughly 200 lines of training code that he releases with all the git-log commits made along the way, plus the notebook ([[youtube-2023-01-17-gpt-from-scratch]] @07:50, @41:36, @1:54:50). The repository's README describes it as the code created in the Neural Networks: Zero To Hero series, specifically the first lecture on nanoGPT, published as a GitHub repo so people can easily hack it and walk through its `git log` history; its H1 reads nanogpt-lecture ([[github-2023-01-31-ng-video-lecture-readme]] §intro). **Note:** the repository name is never spoken in the lecture; `repo_url` is backed by the README source ([[github-2023-01-31-ng-video-lecture-readme]] §intro).

## What it demonstrates
- The intermediate script packages the bigram model with hyperparameters at the top, GPU support and a loss estimator, as starter code to iterate on ([[youtube-2023-01-17-gpt-from-scratch]] @37:41, @38:15, @41:36).
- The final model is a decoder-only Transformer with the major pieces of the original paper in place, scaled to six layers, 384 embedding dimensions, six heads, block size 256, batch size 64 and dropout 0.2, reaching a validation loss of about 1.48 in what he says was about 15 minutes on his A100 ([[youtube-2023-01-17-gpt-from-scratch]] @1:37:35, @1:39:13, @1:39:46, @1:40:21).
- He advises against running the scaled configuration on a CPU or a MacBook ([[youtube-2023-01-17-gpt-from-scratch]] @1:40:54).
- Releasing the git log lets the build-up be followed step by step ([[youtube-2023-01-17-gpt-from-scratch]] @1:54:50).
- The README's caveat: he did not go much into model initialisation in the lecture, though he says it is quite important for good performance; the code trains and works fine but converges more slowly because it starts in a not-great spot in weight space ([[github-2023-01-31-ng-video-lecture-readme]] §intro).
- He points to the `# init all weights` comment and the `_init_weights` call in nanoGPT's `model.py` for the proper initialisation, but the lecture code names and stores modules differently, so it cannot be directly copy-pasted ([[github-2023-01-31-ng-video-lecture-readme]] §intro).
- His plan at the snapshot date: publish a supplementary lecture covering initialisation, then push the exact code changes; meanwhile the repo stays almost exactly as covered in the video ([[github-2023-01-31-ng-video-lecture-readme]] §intro). `status: active` rests on that stated intent ([[github-2023-01-31-ng-video-lecture-readme]] §intro).
- Licensed MIT ([[github-2023-01-31-ng-video-lecture-readme]] §License).

## Related
- [[weight-initialization]] — what the lecture skipped
- [[small-hackable-educational-code]] — published to be hacked, with its history- [[nanogpt]] — the repo the lecture writes toward; its `model.py` is almost identical to the lecture code
- [[spelled-out-build-from-scratch]] — the method the commits record
- [[transformer-architecture]], [[self-attention]], [[tokenization]]
