---
type: method
steps:
  - Start from a blank notebook
  - Build intuition numerically first
  - Work at the scalar level before tensors
  - Backprop by hand, then codify it
  - Pick inputs so the numbers come out nice
  - Leave instructive errors in
  - Walk the real repo at the end
  - Seed randomness so viewers reproduce the numbers
  - Build the explicit baseline, then the neural net
  - Package the baseline as a script with a stable loss estimate
  - Add one component at a time and read validation loss
  - Release the code with its git log
sources: ["[[youtube-2022-08-16-micrograd]]", "[[youtube-2022-09-07-makemore-1-bigram]]", "[[youtube-2023-01-17-gpt-from-scratch]]"]
aliases: [spelled-out lecture, spell it out step by step, explicit baseline then neural net, build from a blank notebook, build up from a bigram baseline, incremental model build-up]
---
# Spelled-out build from scratch
How he teaches: he starts with a blank Jupyter notebook and builds the whole thing step by step, commenting on every piece ([[youtube-2022-08-16-micrograd]] @00:00, @00:32).

## Steps
1. **Blank notebook.** Start with nothing and build up live ([[youtube-2022-08-16-micrograd]] @00:00, @00:32).
2. **Intuition first.** Build intuition for what a derivative measures before writing the data structure ([[youtube-2022-08-16-micrograd]] @08:07, @10:18).
3. **Scalars before tensors.** Work at the level of individual scalars so the math is visible, deferring tensors as pure efficiency ([[youtube-2022-08-16-micrograd]] @05:24, @05:56, @06:30).
4. **By hand, then code.** Do the backward pass fully by hand on a small expression and on a neuron, then codify what you saw ([[youtube-2022-08-16-micrograd]] @31:45, @1:08:59).
5. **Nice numbers.** Choose inputs so intermediate numbers come out clean, such as a bias of 6.88 so tanh's local derivative is exactly 0.5 ([[youtube-2022-08-16-micrograd]] @1:01:09, @1:03:56).
6. **Skip the plumbing.** Copy-paste the slightly scary plumbing, like the graphviz drawing, and explain it briefly rather than typing it live ([[youtube-2022-08-16-micrograd]] @24:40, @25:13).
7. **Pause-the-video exercises.** Ask the viewer to derive a local gradient before showing it ([[youtube-2022-08-16-micrograd]] @1:30:38, @1:33:56).
8. **Leave errors in.** Keep his own mistakes in the recording when they are instructive, including a bug he says he has made for the 20th time ([[youtube-2022-08-16-micrograd]] @1:15:05, @2:10:28).
9. **Connect to the real thing.** Finish by walking the real repo and the production library ([[youtube-2022-08-16-micrograd]] @2:16:34, @2:20:56).

10. **Seed the randomness.** He uses a seeded generator so viewers get exactly the same results on their computer ([[youtube-2022-09-07-makemore-1-bigram]] @26:59, @1:26:13).
11. **Explicit baseline, then the net.** He first arrives at the bigram model by counting and normalising, then takes the neural-net route, which should land in a very similar spot ([[youtube-2022-09-07-makemore-1-bigram]] @1:03:22, @1:03:55). The counting loss, about 2.45 to 2.47, becomes the target that confirms the net is right, and he checks the equivalence by comparing samples and showing `W.exp()` equals the counts ([[youtube-2022-09-07-makemore-1-bigram]] @1:44:36, @1:45:08, @1:49:31, @1:55:39).
12. **Show a bug on purpose.** He invites viewers to pause and think about why the `keepdim` bug happens before explaining it ([[youtube-2022-09-07-makemore-1-bigram]] @46:57).
13. **Warn about the framework.** He cautions viewers about framework APIs and tells them to get used to reading docs and threads ([[youtube-2022-09-07-makemore-1-bigram]] @1:07:47, @1:09:28).

14. **Start from the bigram again.** In the GPT lecture he begins with an empty file and defines the Transformer piece by piece on tiny Shakespeare, starting from the bigram model he calls the simplest possible neural network for language modelling ([[youtube-2023-01-17-gpt-from-scratch]] @06:45, @21:57).
15. **Package the baseline as a script.** He converts the notebook into a roughly 120-line script, `bigram.py`, as starter code to iterate on, with hyperparameters at the top, GPU support and a loss estimator ([[youtube-2023-01-17-gpt-from-scratch]] @37:41, @38:15, @41:36).
16. **One addition, one number.** He reads validation loss after each addition: bigram about 2.5, one self-attention head about 2.4, four heads about 2.28, feed-forward about 2.24, residuals with the 4x inner layer about 2.08, LayerNorm about 2.06, the scaled-up model about 1.48 ([[youtube-2023-01-17-gpt-from-scratch]] @41:36, @1:21:27, @1:23:41, @1:25:52, @1:31:57, @1:36:59, @1:40:21).
17. **Adjust the learning rate as the model grows.** He lowers the learning rate when adding self-attention because attention cannot tolerate very high learning rates, and again when the network gets much bigger ([[youtube-2023-01-17-gpt-from-scratch]] @1:21:27, @1:39:46).
18. **Borrow the paper's fixes, not tuning.** When stacking blocks fails to train well he recognises deep-network optimisation issues and borrows residual connections and LayerNorm from the paper ([[youtube-2023-01-17-gpt-from-scratch]] @1:28:02).
19. **Regularise, then scale up last.** He adds dropout before scaling up because he is concerned about overfitting ([[youtube-2023-01-17-gpt-from-scratch]] @1:39:13).
20. **Release the git log.** He releases the code with the commits made along the way so the build-up can be followed step by step ([[youtube-2023-01-17-gpt-from-scratch]] @1:54:50).

## Seen in
- [[youtube-2023-01-17-gpt-from-scratch]]
- [[ng-video-lecture]], [[nanogpt]]
- [[youtube-2022-08-16-micrograd]]
- [[youtube-2022-09-07-makemore-1-bigram]]
- [[makemore]]
- [[micrograd]]
