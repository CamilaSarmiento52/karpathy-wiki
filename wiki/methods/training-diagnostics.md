---
type: method
steps:
  - Compare the first loss with the expected loss at initialisation
  - Check the loss curve for a hockey stick
  - Histogram activations per layer and report saturation
  - Image the saturated units and look for dead neurons
  - Histogram gradients per layer across depth
  - Plot gradient-to-data ratios per weight tensor
  - Track the update-to-data ratio over time against -3
  - Retune the learning rate from the update-ratio plot
  - Average the loss over many batches before reading it
  - Switch eval and train mode deliberately
sources: ["[[youtube-2022-10-04-makemore-3-activations-batchnorm]]", "[[youtube-2023-01-17-gpt-from-scratch]]"]
aliases: [training diagnostics plots, activation and gradient statistics, update-to-data ratio, check the loss at initialization, evaluate with a single loss number]
---
# Training diagnostics
How he tells whether a training run is healthy: sanity-check the loss at initialisation, then read a fixed set of per-layer plots of activations, gradients and the ratio of update size to parameter size; he says understanding these statistics becomes increasingly important as networks get bigger and deeper ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @04:28, @1:14:18, @1:42:06). The single-number loss that these plots complement is described on [[loss-functions]] ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @05:38).

## Steps
1. **Expected loss at init.** Compute the loss a uniform prediction would give (about 3.29 for 27 characters) and compare it with the first recorded loss; 27 means the net is confidently wrong ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @04:28, @05:38).
2. **Hockey stick.** Plot the loss curve; a hockey-stick shape means the early iterations are spent squashing down overconfident weights ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @11:11, @12:19).
3. **Activation histograms.** Histogram the tanh activations per layer and report mean, std and percent saturation (|t| > 0.97); roughly 5% saturation and std about 0.65 was a good range for his tanh sandwich with gain 5/3 ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @13:26, @14:00, @1:27:05, @1:27:38, @1:28:12).
4. **Dead neurons.** Visualise |h| > 0.99 as a boolean image over the batch and look for all-white columns, neurons no example activates ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @18:36, @19:44).
5. **Gradient histograms.** Histogram the gradients at each tanh layer and check they look similar across layers, neither shrinking nor exploding with depth ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:30:30, @1:31:03).
6. **Weight gradients.** For each weight tensor plot the gradient mean, std, histogram and gradient-to-data ratio; the output layer was an outlier because its weights were shrunk by 0.1, giving 10× larger gradients that stabilise after about 1,000 steps ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:36:35, @1:37:07, @1:37:41, @1:38:15, @1:38:47, @1:39:20).
7. **Update-to-data ratio.** Track, per weight tensor and per iteration, log10 of std(learning rate × gradient) divided by std(parameter), and plot it over time against -3; he calls the gradient-to-data ratio less informative because the update is what actually changes the data ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:39:52, @1:40:26, @1:41:00, @1:41:33, @1:42:06).
8. **Read the learning rate off it.** He gives -3 (updates about a thousandth of the tensor's magnitude) as a rough guide and rough heuristic, not a rule: well below -3 usually means the parameters train too slowly, as with learning rate 0.001 where updates were 10,000× too small; his run sat around -2.5, a little high but stabilising, which he called decent ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:42:06, @1:43:12, @1:43:45, @1:44:17, @1:53:12).

The plots are read over time rather than as one snapshot ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:52:40, @1:53:12). To gather the statistics he adds a `.out` attribute to his modules, which PyTorch's do not have ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:23:48). He demonstrates that forgetting fan-in normalisation shows up at once in the saturation, gradient and update-ratio plots, and that with batchnorm and no fan-in scaling the update ratio fell well below -3, so he raised the learning rate 10× to 1.0 ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:44:49, @1:45:22, @1:50:24, @1:51:00). He also mentions the learning-rate finding mechanism from an earlier lecture ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:53:45). **Note:** that mechanism is [[learning-rate-sweep]]; and [[quick-experiment-loop]] is a later, higher-level habit of judging runs by fixed plots ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:53:45).

The GPT lecture repeats the first step on a new problem: with 65 vocabulary elements he expects an initial loss of about -ln(1/65), roughly 4.17, and the measured 4.87 tells him the initial predictions are not diffuse and the model is guessing wrong at init ([[youtube-2023-01-17-gpt-from-scratch]] @28:03, @28:37). Hygiene he adds in the same script: average the loss over many batches with an `estimate_loss` function because a single batch is a noisy measurement ([[youtube-2023-01-17-gpt-from-scratch]] @39:23, @39:56); switch the model between eval and train mode as good practice even when no layer yet depends on it ([[youtube-2023-01-17-gpt-from-scratch]] @40:31); wrap evaluation in `torch.no_grad` so PyTorch can save memory ([[youtube-2023-01-17-gpt-from-scratch]] @41:04).

## Seen in
- [[youtube-2023-01-17-gpt-from-scratch]]
- [[bigram-language-model]], [[ng-video-lecture]]
- [[youtube-2022-10-04-makemore-3-activations-batchnorm]]
- [[makemore]]
- [[weight-initialization]], [[batch-normalization]], [[activation-functions]], [[gradient-descent]]
- [[the-hockey-stick-loss-means-training-is-wasting-steps]]
