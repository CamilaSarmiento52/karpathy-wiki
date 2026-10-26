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
  - Read loss, gradient norm, MFU and tokens per second off every log line
  - Plot the gradient norm and read spikes as instability
  - Evaluate validation loss, samples and an eval on a fixed schedule
  - Read the tail and the epoch boundary of the loss curve
  - Keep long runs alive: watch the log and restart a hung run
  - Make runs resumable, deterministic and constant in memory
  - Skip updates on instantaneous instability, and watch for drift
sources: ["[[youtube-2022-10-04-makemore-3-activations-batchnorm]]", "[[youtube-2023-01-17-gpt-from-scratch]]", "[[github-2024-05-28-llmc-gpt-2-124m]]", "[[youtube-2024-06-09-reproduce-gpt-2]]", "[[github-2024-06-12-llmc-gpt-2-774m]]", "[[github-2024-07-11-llmc-gpt-2-1-6b]]", "[[github-2025-11-20-nanochat-d34-model]]", "[[github-2026-01-31-nanochat-beating-gpt-2]]"]
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
6. **Weight gradients.** For each weight tensor plot the gradient mean, std, histogram and gradient-to-data ratio; the output layer was an outlier because its weights were shrunk by 0.1, giving 10× larger gradients that stabilise after about 1,000 steps ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:36:35, @1:37:07, @1:37:41, @1:38:15, @1:38:47, @1:39:20, @1:42:39).
7. **Update-to-data ratio.** Track, per weight tensor and per iteration, log10 of std(learning rate × gradient) divided by std(parameter), and plot it over time against -3; he calls the gradient-to-data ratio less informative because the update is what actually changes the data ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:39:52, @1:40:26, @1:41:00, @1:41:33, @1:42:06).
8. **Read the learning rate off it.** He gives -3 (updates about a thousandth of the tensor's magnitude) as a rough guide and rough heuristic, not a rule: well below -3 usually means the parameters train too slowly, as with learning rate 0.001 where updates were 10,000× too small; his run sat around -2.5, a little high but stabilising, which he called decent ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:42:06, @1:43:12, @1:43:45, @1:44:17, @1:53:12).

The plots are read over time rather than as one snapshot ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:52:40, @1:53:12). To gather the statistics he adds a `.out` attribute to his modules, which PyTorch's do not have ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:23:48). He demonstrates that forgetting fan-in normalisation shows up at once in the saturation, gradient and update-ratio plots, and that with batchnorm and no fan-in scaling the update ratio fell well below -3, so he raised the learning rate 10× to 1.0 ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:44:49, @1:45:22, @1:50:24, @1:51:00). He also mentions the learning-rate finding mechanism from an earlier lecture ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:53:45). **Note:** that mechanism is [[learning-rate-sweep]]; and [[quick-experiment-loop]] is a later, higher-level habit of judging runs by fixed plots ([[youtube-2022-10-04-makemore-3-activations-batchnorm]] @1:53:45).

The GPT lecture repeats the first step on a new problem: with 65 vocabulary elements he expects an initial loss of about -ln(1/65), roughly 4.17, and the measured 4.87 tells him the initial predictions are not diffuse and the model is guessing wrong at init ([[youtube-2023-01-17-gpt-from-scratch]] @28:03, @28:37). Hygiene he adds in the same script: average the loss over many batches with an `estimate_loss` function because a single batch is a noisy measurement ([[youtube-2023-01-17-gpt-from-scratch]] @39:23, @39:56); switch the model between eval and train mode as good practice even when no layer yet depends on it ([[youtube-2023-01-17-gpt-from-scratch]] @40:31); wrap evaluation in `torch.no_grad` so PyTorch can save memory ([[youtube-2023-01-17-gpt-from-scratch]] @41:04).

11. **Read every log line.** In the llm.c GPT-2 (124M) walkthrough he reads one printed line field by field: step time, MFU, tokens per second, loss and gradient norm ([[github-2024-05-28-llmc-gpt-2-124m]] §intro (Training)). A loss of 7.577 at step 80 means the model is as confused as if guessing at random among exp(7.577), about 2,000 of the 50,257 tokens, and by the end about 3.29 means about 27 ([[github-2024-05-28-llmc-gpt-2-124m]] §intro (Training)). When the gradient norm spikes the gradient is exploding, which he calls very bad; clipping at 1.0 scales it back, and later in training the norm usually calms down ([[github-2024-05-28-llmc-gpt-2-124m]] §intro (Training)). The log file `main.log` is visualised with the `dev/vislog.ipynb` notebook ([[github-2024-05-28-llmc-gpt-2-124m]] §intro (Visualization)).

The GPT-2 lecture repeats step 1 at a larger vocabulary: with 50,257 tokens he expects an initial loss of -ln(1/50257), about 10.82, sees about 11, and concludes the initial distribution is roughly diffuse ([[youtube-2024-06-09-reproduce-gpt-2]] @55:37, @56:11). Early drops in the loss come cheaply, from pushing down tokens that never occur in the data ([[youtube-2024-06-09-reproduce-gpt-2]] @1:04:39, @1:05:12).

12. **Plot the gradient norm.** He always visualises the norm that clipping computes: well-behaved is good, climbing or spiking signals instability ([[youtube-2024-06-09-reproduce-gpt-2]] @2:18:49). In his run it started around 30 and settled below 1; a sequence of 28, 6, 2, then 10 struck him as a little funky but not insane ([[youtube-2024-06-09-reproduce-gpt-2]] @2:20:30).
13. **Evaluate on a schedule.** He evaluates validation loss every 100 (later 250) steps over about 20 batches, samples text periodically, and logs train loss, validation loss and HellaSwag to a text file he plots ([[youtube-2024-06-09-reproduce-gpt-2]] @3:23:11, @3:23:47, @3:39:28, @3:43:03). He reads sample quality over training: still garbled at step 1,000, more coherent by step 10,000 ([[youtube-2024-06-09-reproduce-gpt-2]] @3:26:00, @3:41:45).

14. **Read the curve's shape.** After the llm.c 774M run he reads the tail of the loss curve to judge the schedule: going way too slow at the end means the learning rate decayed too low ([[github-2024-06-12-llmc-gpt-2-774m]] §intro (Reflections)). A downward kink in validation loss exactly at the epoch boundary he reads as a warning that train and validation data may overlap ([[github-2024-06-12-llmc-gpt-2-774m]] §intro (Reflections)).
15. **Keep long runs alive.** Because a run sometimes stalls on a weird MPI error, he ran `watcher.sh` in a second screen session beside training: if `main.log` has not been written for about two minutes it sends CTRL+C to the `train` session, it checks every two minutes so the training script has time to restart, and it exits once the run's final DONE file exists ([[github-2024-06-12-llmc-gpt-2-774m]] §intro).

16. **Make the run resumable.** In the 1.6B post `-y 1` turns on resume: if training crashes or hangs, CTRL+C and re-run the same command and it resumes, and because llm.c is bitwise-deterministic the result is identical to an uninterrupted run ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (Args guide)). Checkpoints are written every 2,000 steps (`-n 2000`), and llm.c allocates all GPU memory once at the start with a constant footprint, so once stepping starts it will not run out of memory ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (Args guide), §intro (Code)). In the same log he expects the gradient norm to stabilise around 0.1–1, with the learning rate warming up over the first few steps, and uses validation loss as a sanity check rather than the comparison ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (Training), §intro (Evals)).
17. **Skip spikes, and watch for drift.** Loss spikes and bad activation ranges are his signs of instability; the code detects simple instantaneous instability and skips the update (`-sl 5.0 -sg 5.0`), which mitigates and defers problems, but his 420B-token run still exploded after about step 330,000 ([[github-2024-07-11-llmc-gpt-2-1-6b]] §intro, §intro (400B token run)).

In the nanochat d34 post he reads the wandb curves against d32's: d34 trained fairly stably except for a tiny bump near the beginning that recovered quickly ([[github-2025-11-20-nanochat-d34-model]] §intro). When training crashed in the last 5% with a cryptic NCCL error, he used nanochat's new optimisation-resumption logic to resume from that point, which he says "worked perfect" ([[github-2025-11-20-nanochat-d34-model]] §intro).

He calls the GPT-2 record run of 2026-01-31 "a nicely uneventful run of training a GPT-2 capability model", and notes that its wandb x-axis looks longer because it includes inline evaluation ([[github-2026-01-31-nanochat-beating-gpt-2]] §intro).

## Seen in
- [[youtube-2023-01-17-gpt-from-scratch]]
- [[bigram-language-model]], [[ng-video-lecture]]
- [[youtube-2022-10-04-makemore-3-activations-batchnorm]]
- [[makemore]]
- [[weight-initialization]], [[batch-normalization]], [[activation-functions]], [[gradient-descent]]
- [[the-hockey-stick-loss-means-training-is-wasting-steps]]
- [[llm-c]]
- [[youtube-2024-06-09-reproduce-gpt-2]]
- [[github-2024-06-12-llmc-gpt-2-774m]]
- [[llm-c-was-not-yet-careful-enough-about-training-stability]]
- [[nanochat]] — the d34 run's curves and resumed crash
- [[how-he-explains]] — predicting the loss at init as one of his explaining moves
- [[predict-the-number-before-you-run]] — the rule: say the expected number before the run
