---
type: method
steps:
  - Write down both shapes
  - Align from the right and apply the rules
  - Keep keepdim=True when summing to normalise
  - Verify a row sums to one
  - Check the result against a known answer
  - Read off every layer's shapes
  - Read the backward structure off the forward shapes
  - Forward a scratch batch and print every layer's output shape
  - Break after the first training iteration
  - Avoid -1 in view; pass an explicit dimension to squeeze
sources: ["[[youtube-2022-09-07-makemore-1-bigram]]", "[[youtube-2022-09-12-makemore-2-mlp]]", "[[youtube-2022-10-11-makemore-4-backprop-ninja]]", "[[youtube-2022-11-21-makemore-5-wavenet]]"]
aliases: [check broadcasting carefully, respect broadcasting, inspect shapes layer by layer, layer inspector, shape debugging, break after first iteration]
---
# Check shapes and broadcasting
How he guards against silent broadcasting bugs: walk both shapes through the rules before an operation, then verify the result against something known ([[youtube-2022-09-07-makemore-1-bigram]] @42:32, @44:10).

## Steps
1. **Walk the shapes.** He takes 27×27 against 27×1 through the broadcasting rules before dividing ([[youtube-2022-09-07-makemore-1-bigram]] @42:32, @43:05).
2. **Keep the dimension.** The sum used for normalising needs `keepdim=True`, or the 27 becomes a row vector and the wrong axis is normalised ([[youtube-2022-09-07-makemore-1-bigram]] @47:29, @49:08).
3. **Verify a row.** He checks that `P[0].sum()` equals 1 and that the samples are identical to the earlier loop ([[youtube-2022-09-07-makemore-1-bigram]] @43:37, @44:10).
4. **Break it on purpose.** He deliberately removes `keepdim` to show the result is garbage even though broadcasting allows it, and suggests pausing to work out why ([[youtube-2022-09-07-makemore-1-bigram]] @45:15, @46:21, @46:57).

5. **Check every layer's shapes.** In the MLP he reads off the embedding output as 32×3×2, reshapes it to 32×6 with `.view`, and checks that the 100-vector bias broadcasts along the right axis of the 32×100 hidden pre-activation, saying to always check broadcasting ([[youtube-2022-09-12-makemore-2-mlp]] @18:16, @24:24, @28:16, @28:49).

6. **Shapes first in the backward pass too.** Writing the backward pass by hand, he says he likes to scrutinise the shapes first and writes out the shape of every tensor before each line; a gradient always has the shape of its variable, a reduction in the forward pass (32×64 to 1×64) signals a broadcast in the backward, and a forward broadcast signals a sum ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @13:13, @22:12, @1:08:38, @1:09:12, @1:09:47, @1:14:15).

7. **Scratch batch.** In the WaveNet lecture he creates a scratch space with a temporary batch of four random examples and passes it through the model to inspect tensor shapes along the forward pass ([[youtube-2022-11-21-makemore-5-wavenet]] @21:34, @22:06).
8. **Print every layer's output shape.** He iterates over the layers, printing each layer's class name and output shape ([[youtube-2022-11-21-makemore-5-wavenet]] @35:06, @36:10).
9. **Break after one iteration.** He inserts a break after the first training iteration to make sure one step runs before committing to a run ([[youtube-2022-11-21-makemore-5-wavenet]] @12:10, @19:56, @44:28).
10. **Running is not correct.** A layer that runs without errors can still do the wrong thing, since broadcasting can hide a wrong reduction, as his BatchNorm did on 3-D input ([[youtube-2022-11-21-makemore-5-wavenet]] @38:20, @39:26).
11. **Be explicit.** He avoids -1 in `view` and passes an explicit dimension to `squeeze`, so that wrong assumptions produce error messages; he says he likes to be as explicit as possible ([[youtube-2022-11-21-makemore-5-wavenet]] @32:49, @33:56).
12. **Re-run edited cells.** A forgotten cell left BatchNorm in the wrong mode ([[youtube-2022-11-21-makemore-5-wavenet]] @15:30).

## Seen in
- [[youtube-2022-11-21-makemore-5-wavenet]]
- [[youtube-2022-09-07-makemore-1-bigram]]
- [[youtube-2022-09-12-makemore-2-mlp]]
- [[youtube-2022-10-11-makemore-4-backprop-ninja]]
- [[makemore]]
- [[verify-gradients-against-pytorch]] — the same shape discipline used to derive gradients
- [[wavenet-hierarchical-model]] — the shapes printed layer by layer
- [[deep-learning-is-largely-shape-gymnastics]]
- [[how-he-explains]] — showing the shapes as one of his explaining moves
