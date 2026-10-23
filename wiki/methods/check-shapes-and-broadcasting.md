---
type: method
steps:
  - Write down both shapes
  - Align from the right and apply the rules
  - Keep keepdim=True when summing to normalise
  - Verify a row sums to one
  - Check the result against a known answer
  - Read off every layer's shapes
sources: ["[[youtube-2022-09-07-makemore-1-bigram]]", "[[youtube-2022-09-12-makemore-2-mlp]]"]
aliases: [check broadcasting carefully, respect broadcasting, inspect shapes layer by layer]
---
# Check shapes and broadcasting
How he guards against silent broadcasting bugs: walk both shapes through the rules before an operation, then verify the result against something known ([[youtube-2022-09-07-makemore-1-bigram]] @42:32, @44:10).

## Steps
1. **Walk the shapes.** He takes 27×27 against 27×1 through the broadcasting rules before dividing ([[youtube-2022-09-07-makemore-1-bigram]] @42:32, @43:05).
2. **Keep the dimension.** The sum used for normalising needs `keepdim=True`, or the 27 becomes a row vector and the wrong axis is normalised ([[youtube-2022-09-07-makemore-1-bigram]] @47:29, @49:08).
3. **Verify a row.** He checks that `P[0].sum()` equals 1 and that the samples are identical to the earlier loop ([[youtube-2022-09-07-makemore-1-bigram]] @43:37, @44:10).
4. **Break it on purpose.** He deliberately removes `keepdim` to show the result is garbage even though broadcasting allows it, and suggests pausing to work out why ([[youtube-2022-09-07-makemore-1-bigram]] @45:15, @46:21, @46:57).

5. **Check every layer's shapes.** In the MLP he reads off the embedding output as 32×3×2, reshapes it to 32×6 with `.view`, and checks that the 100-vector bias broadcasts along the right axis of the 32×100 hidden pre-activation, saying to always check broadcasting ([[youtube-2022-09-12-makemore-2-mlp]] @18:16, @24:24, @28:16, @28:49).

## Seen in
- [[youtube-2022-09-07-makemore-1-bigram]]
- [[youtube-2022-09-12-makemore-2-mlp]]
- [[makemore]]
