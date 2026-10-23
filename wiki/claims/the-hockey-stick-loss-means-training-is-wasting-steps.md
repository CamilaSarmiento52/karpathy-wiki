---
type: claim
stated_on: 2022-10-04
confidence: stated
sources: ["[[youtube-2022-10-04-makemore-3-activations-batchnorm]]"]
topic: "[[weight-initialization]]"
---
# A hockey-stick loss curve means the first iterations are wasted squashing overconfident weights
> "the plot of the loss uh now doesn't have this hockey shape appearance" — [[youtube-2022-10-04-makemore-3-activations-batchnorm]] @11:11

## Context
His makemore MLP started at a loss of 27 when roughly 3.29 was expected, because extreme logits made the output layer confidently wrong ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @05:38, @07:51). After shrinking the output weights the loss curve no longer has the hockey-stick shape, because the easy early gains from squashing the logits are gone ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @11:11, @11:44). He says this is true for any neural net you might train and is something to look out for ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @12:19). The final loss improved slightly, about 2.2 to 2.16 in that run, because more cycles went to real training instead of shrinking weights ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @12:19, @12:52). In the closing summary he ties hockey-stick losses to confident mispredictions from messed-up activations at the last layer ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:14:18).

## Related claims
- **Note:** this is the first check in [[training-diagnostics]]; the fix is the output-layer scaling described on [[weight-initialization]] ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @04:28, @09:33).
