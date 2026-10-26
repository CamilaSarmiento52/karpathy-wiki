---
type: claim
stated_on: 2022-10-11
confidence: stated
sources: ["[[youtube-2022-10-11-makemore-4-backprop-ninja]]", "[[youtube-2022-10-04-makemore-3-activations-batchnorm]]"]
topic: "[[batch-normalization]]"
supports: ["[[avoid-batch-normalization-where-possible]]"]
---
# He considers batchnorm's biased-in-training, unbiased-at-test variance a bug
> "I basically consider this to be a bug" — [[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:08:05

## Context
In his hand-written batchnorm he normalises the variance by 1/(n-1), Bessel's correction, rather than the paper's 1/m, and does so deliberately ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:00:11, @1:00:43, @1:05:16). The paper, he says, uses the biased 1/n estimate during training but the unbiased n-1 estimate when calibrating running statistics for inference, which he finds extremely confusing ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:05:49, @1:06:22). He says 1/n almost always underestimates the variance, that this matters when samples are small, as with mini-batches, and that the unbiased version is advised ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:06:22, @1:06:57). `torch.var` takes an `unbiased` flag whose default he believes is true but is not sure, and the docs do not state; the `BatchNorm1d` docs say biased but the implementation uses the unbiased version for the running std, which others have flagged in issues ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:06:57, @1:07:31). He is not a fan of train/test discrepancies, sees no good reason given in the paper, and prefers Bessel's correction consistently in his own work ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:07:31, @1:08:05). Because BatchNorm takes no keyword to choose the estimator consistently, in his view anyone using it has a bit of a bug in their code, which matters less with larger batch sizes; he hedges that maybe someone can explain why this is okay ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:08:05, @1:08:38).

## Related claims
- supports [[avoid-batch-normalization-where-possible]]: in the activations lecture (2022-10-04) he said the layer causes a huge amount of bugs and told viewers to avoid it; this variance mismatch is one concrete bug he points to; he does not connect it to the coupling he blamed in the earlier lecture ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:17:07; [[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:08:05).
