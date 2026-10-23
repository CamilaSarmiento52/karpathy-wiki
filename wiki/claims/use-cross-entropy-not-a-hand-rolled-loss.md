---
type: claim
stated_on: 2022-09-12
confidence: stated
sources: ["[[youtube-2022-09-12-makemore-2-mlp]]"]
topic: "[[loss-functions]]"
---
# Call F.cross_entropy rather than rolling your own softmax and log-likelihood
> "I did this for educational reasons, but you'd never use this in practice." — [[youtube-2022-09-12-makemore-2-mlp]] @33:16

## Context
Having written the softmax and negative log likelihood by hand, he gives three reasons to call `F.cross_entropy` instead: the forward pass is more efficient via fused kernels, the backward pass is simpler analytically, and the result is numerically well-behaved ([[youtube-2022-09-12-makemore-2-mlp]] @33:16, @34:56, @37:41). Large positive logits overflow `exp` to infinity and produce nan; PyTorch subtracts the maximum logit internally, which leaves the probabilities unchanged ([[youtube-2022-09-12-makemore-2-mlp]] @36:02, @37:08).
