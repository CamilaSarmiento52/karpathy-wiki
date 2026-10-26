---
type: topic
aliases: [Broadcasting, broadcasting semantics]
first_seen: 2022-09-07
last_updated: 2022-10-11
sources: ["[[youtube-2022-09-07-makemore-1-bigram]]", "[[youtube-2022-09-12-makemore-2-mlp]]", "[[youtube-2022-10-11-makemore-4-backprop-ninja]]"]
related: ["[[pytorch]]", "[[check-shapes-and-broadcasting]]", "[[makemore]]", "[[backpropagation]]"]
---
# Broadcasting
PyTorch's broadcasting rules, as he states them: each tensor has at least one dimension; shapes are aligned from the trailing dimension; and each pair of dimensions must be equal, one of them must be 1, or one must be missing ([[youtube-2022-09-07-makemore-1-bigram]] @42:01, @42:32).

## What he says
`torch.sum` with `dim` sums along one dimension; `keepdim=True` keeps that dimension as size 1, while `keepdim=False` squeezes it out ([[youtube-2022-09-07-makemore-1-bigram]] @38:43, @39:16, @39:50). For the bigram counts, row sums and column sums happen to be identical, which hides which axis you summed ([[youtube-2022-09-07-makemore-1-bigram]] @40:55). Dividing 27×27 by 27×1 stretches the column vector across 27 columns and divides element-wise, normalising rows ([[youtube-2022-09-07-makemore-1-bigram]] @43:05, @43:37). Dividing 27×27 by a bare 27 also broadcasts: the 27 becomes 1×27, a row vector, which is replicated vertically, so columns get normalised instead of rows and `P[0].sum()` is 7, not 1 ([[youtube-2022-09-07-makemore-1-bigram]] @45:47, @46:21, @47:29, @48:02). The issue comes from the silent adding of a dimension on the left ([[youtube-2022-09-07-makemore-1-bigram]] @48:02, @48:36).

He encourages viewers to read the broadcasting semantics, treat them with respect, practise, and check which direction things broadcast, because the bugs are subtle and hard to find ([[youtube-2022-09-07-makemore-1-bigram]] @44:10, @49:08, @49:40). In-place operations such as `/=` avoid allocating a new tensor and can be faster ([[youtube-2022-09-07-makemore-1-bigram]] @49:40).

In the MLP he broadcasts a 100-vector bias onto a 32-by-100 matrix: the shapes align on the right, a fake dimension is added, and the row is copied; he says to always check broadcasting ([[youtube-2022-09-12-makemore-2-mlp]] @28:16, @28:49).

The backprop lecture shows what broadcasting means for the backward pass. A broadcasted multiply like `counts * counts_sum_inv` is really two operations: replication of the column across 27 columns, then the element-wise multiply ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @23:19, @23:54). Replication means one variable is reused many times, so, as in micrograd, the gradients from all the uses sum; the backward pass is a `sum(1, keepdim=True)` so the gradient keeps the variable's shape ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @25:02, @25:34, @26:07). A forward `sum` over rows becomes a backward replication, which he implements as `torch.ones_like(counts) * dcounts_sum` to let broadcasting do the replication ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @31:11, @31:45). A bias vector of 27 is padded to a row vector and replicated vertically 32 times in the forward pass, so its gradient is a sum over dimension 0; batchnorm's gain and bias are 1×64 against 32×64 activations, so their gradients need a sum over the examples with `keepdim=True` ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @42:18, @52:17, @55:43, @56:49, @57:21). He states the duality explicitly: a sum in the forward pass turns into replication or broadcasting in the backward pass along the same dimension, and a broadcast in the forward pass indicates variable reuse and turns into a sum over that dimension ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:09:12, @1:09:47). Shapes alone hint at the backward structure: seeing a 32×64 reduced to 1×64 tells him there will be a broadcast in the backward pass ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:09:12, @1:14:15).

## Claims
- [[treat-broadcasting-with-respect]]

## Related
- [[pytorch]]
- [[check-shapes-and-broadcasting]] — how he guards against it
- [[backpropagation]] — the sum/broadcast duality in the backward pass
- [[makemore]]
