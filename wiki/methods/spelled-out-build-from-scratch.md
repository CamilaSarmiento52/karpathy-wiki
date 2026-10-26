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
  - Ship exercises and have viewers work them alongside
  - Motivate with the failures before the code
  - Round-trip test on unseen text
  - Write your own class rather than read the library's
  - Debug on a toy before fixing the real code
  - Keep one clean commit per step and narrate each
sources: ["[[youtube-2022-08-16-micrograd]]", "[[youtube-2022-09-07-makemore-1-bigram]]", "[[youtube-2023-01-17-gpt-from-scratch]]", "[[github-2024-02-20-nn-zero-to-hero-readme]]", "[[youtube-2024-02-20-gpt-tokenizer]]", "[[x-2024-02-21-technical-accessibility]]", "[[github-2024-04-22-minbpe-readme]]", "[[youtube-2024-06-09-reproduce-gpt-2]]", "[[github-2024-06-17-build-nanogpt-readme]]", "[[github-2024-08-01-llm101n-readme]]", "[[blog-2026-02-12-microgpt]]"]
aliases: [spelled-out lecture, spell it out step by step, explicit baseline then neural net, build from a blank notebook, build up from a bigram baseline, incremental model build-up]
---
# Spelled-out build from scratch
How he teaches: he starts with a blank Jupyter notebook and builds the whole thing step by step, commenting on every piece ([[youtube-2022-08-16-micrograd]] @00:00, @00:32). He credits the video that built micrograd and walked through it, not the code, with making that code accessible: he calls such a walkthrough the ramp to build after the thing ([[x-2024-02-21-technical-accessibility]]).

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

21. **Ship exercises; work them alongside the video.** Every Zero to Hero lecture has exercises in its video description; for the backprop lecture he recommends working the exercise yourself in tandem with the video, unpausing to see him give the answer when stuck, and says the video is not meant to be simply watched ([[github-2024-02-20-nn-zero-to-hero-readme]] §intro, Lecture 5). He asks viewers of the GPT lecture to watch the earlier makemore videos first, since it takes the language-modelling framework and tensor basics for granted ([[github-2024-02-20-nn-zero-to-hero-readme]] §intro, Lecture 7).

22. **Failures first.** The tokenizer lecture opens with the list of LLM weirdness that tokenization causes, demonstrated in a tokenizer web app, and promises to loop back; it does, at the end ([[youtube-2024-02-20-gpt-tokenizer]] @04:27, @05:33, @1:51:24). He explains BPE on Wikipedia's four-letter toy example before applying it to bytes ([[youtube-2024-02-20-gpt-tokenizer]] @23:32, @24:06), and invites viewers to write `get_stats`, the merge, decode and encode themselves before showing his ([[youtube-2024-02-20-gpt-tokenizer]] @28:01, @30:47, @42:59, @48:38). He shows decode failing on token 128 and asks viewers to work out why before fixing it ([[youtube-2024-02-20-gpt-tokenizer]] @45:16, @45:51).
23. **Round-trip tests.** He checks that encoding then decoding returns the original string, on the training text and on validation text the tokenizer never saw ([[youtube-2024-02-20-gpt-tokenizer]] @55:56, @56:30). He then shows OpenAI's `encoder.py` is algorithmically identical to what he built, and publishes minbpe with an `exercise.md` breaking the build into four steps toward a GPT-4 tokenizer ([[youtube-2024-02-20-gpt-tokenizer]] @1:15:36, @1:17:50, @1:25:45). The repo's README points to that advised progression and to the lecture, also kept in text form as `lecture.md` ([[github-2024-04-22-minbpe-readme]] §exercise, §lecture).

24. **Write your own class.** In the GPT-2 lecture he writes the GPT-2 class from scratch instead of using Hugging Face's `modeling_gpt2.py`, which he finds too complicated, to have full understanding ([[youtube-2024-06-09-reproduce-gpt-2]] @12:18, @12:50).
25. **Toy first.** He debugs the gradient-accumulation bug on a toy MSE network in a notebook before fixing the real code ([[youtube-2024-06-09-reproduce-gpt-2]] @2:39:41, @2:40:15).

26. **One clean commit per step.** The build-nanogpt README says they start from an empty file and work up to GPT-2 (124M), with the git commits kept step by step and clean so the history can be walked, and the video introducing each commit ([[github-2024-06-17-build-nanogpt-readme]] §intro). **Note:** this makes explicit the git log released after the GPT lecture (step 20) ([[youtube-2023-01-17-gpt-from-scratch]] @1:54:50; [[github-2024-06-17-build-nanogpt-readme]] §intro).

The same approach appears as a plan in the [[llm101n]] README: build everything end to end from basics, from scratch in Python, C and CUDA, with minimal computer science prerequisites; the course does not yet exist, so this is stated intent, not a performed build ([[github-2024-08-01-llm101n-readme]] §intro).

**Layers of the onion (microgpt, 2026-02-12).** To see the code built up piece by piece he advises six files: a bigram count table with no net and no gradients; an MLP with manual numerical and analytic gradients and SGD; autograd replacing the manual gradients; position embeddings, single-head attention, RMSNorm and residuals; multi-head attention and the layer loop; and Adam ([[blog-2026-02-12-microgpt]] §Progression). Each is a revision of the build_microgpt.py gist, so the diffs show one component added at a time ([[blog-2026-02-12-microgpt]] §Progression). In the post he explains each piece with plain intuitions: lego blocks for operations, a car, a bicycle and a walking man for the chain rule, and the "emma" example for attention ([[blog-2026-02-12-microgpt]] §Autograd, §Architecture).

## Seen in
- [[youtube-2023-01-17-gpt-from-scratch]]
- [[ng-video-lecture]], [[nanogpt]]
- [[youtube-2022-08-16-micrograd]]
- [[youtube-2022-09-07-makemore-1-bigram]]
- [[makemore]]
- [[micrograd]]
- [[nn-zero-to-hero]]
- [[build-the-ramp-not-just-the-thing]]
- [[minbpe]], [[youtube-2024-02-20-gpt-tokenizer]]
- [[youtube-2024-06-09-reproduce-gpt-2]]
- [[build-nanogpt]]
- [[llm101n]] — planned, not yet built
- [[microgpt]] — six gist revisions, one component each
- [[how-he-explains]] — the explaining moves across his lectures, compiled
