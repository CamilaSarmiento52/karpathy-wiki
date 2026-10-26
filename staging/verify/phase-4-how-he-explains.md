# Verification: phase 4, method page (how-he-explains)
Verified 2026-10-26 by a fresh reader. Sources: [[youtube-2022-08-16-micrograd]], [[youtube-2022-09-07-makemore-1-bigram]], [[youtube-2022-09-12-makemore-2-mlp]], [[youtube-2022-10-04-makemore-3-activations-batchnorm]], [[youtube-2022-10-11-makemore-4-backprop-ninja]], [[youtube-2022-11-21-makemore-5-wavenet]], [[youtube-2023-01-17-gpt-from-scratch]], [[github-2023-01-31-ng-video-lecture-readme]], [[github-2024-02-20-nn-zero-to-hero-readme]], [[youtube-2024-02-20-gpt-tokenizer]], [[x-2024-02-21-technical-accessibility]], [[youtube-2024-06-09-reproduce-gpt-2]], [[talk-2025-10-17-dwarkesh-ghosts-not-animals]], [[blog-2026-02-12-microgpt]]

## Coverage
- pages checked: 1 ([[how-he-explains]]), every sentence (not one in five), as the prompt asked.
- citations checked: 63 location citations across the definition paragraph and 11 steps; every `[mm:ss]` block read with its neighbours; every text §heading found.
- quotes checked: 3 of 3. All verbatim, his, under 15 words:
  - "I always like to work with simpler examples" (makemore-4 @14:26, 8 words)
  - "I figured I should just leave the error in here because it's pretty funny" (micrograd @1:15:05, 14 words)
  - "I'm not going to present the solution before you guess." (Dwarkesh @2:19:57, 10 words). The transcript has no speaker labels, and the lines just before it ("You're presenting the pain before you present a solution...") are Dwarkesh's. "You want to take the student through that progression..." onward, quote included, is Karpathy's from context (it carries on into @2:20:34, "before I give you a shot").
- frontmatter: all 14 `sources` are cited in the body, and every cited source is listed.
- AI-written parts: none of these sources has one (microgpt is his own text).
- practice vs advice: the body describes what he does. Step headings are imperatives, which `steps` requires. No sentence turns his practice into advice to the reader.

## Findings

### F1: overstated, [[how-he-explains]] step 7 (Ask the learner to try first)
- sentence: "He states the rule in the Dwarkesh interview: "I'm not going to present the solution before you guess."" (closing the step, after the lecture examples)
- cited: [[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @2:19:57, with micrograd @1:30:38, makemore-1 @46:57, tokenizer @28:01, reproduce-gpt-2 @2:39:41, nn-zero-to-hero README §Lecture 5
- raw says: in all four videos he invites the viewer to pause or think. micrograd @1:30:38: "you can potentially pause the video and think". makemore-1 @46:57: "encourage you to potentially like pause this video". tokenizer @28:01 is conditional, for viewers "working along on a notebook". reproduce-gpt-2 @2:39:41: "I invite you to think about why", then straight away "let me fix it then", with no pause. Only the README asks for real work before the answer ("whenever you are stuck unpause the video", Lecture 5). In the interview he gives the rule as something "a lot of good educators will do", in the context of tutoring and Eureka. So what the six sources show is an optional, occasional invitation to pause. They do not show him withholding a solution until the learner has guessed. Put right after the lecture examples, "states the rule" reads as a description of his lectures, and an agent copying it would hold back answers. The sources show nothing like that.
- fix: change the heading to "Invite the learner to pause and try first". Replace the last sentence with: "In the Dwarkesh interview he describes this as something good educators do, not presenting a solution before the student has had a shot: "I'm not going to present the solution before you guess." ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @2:19:57, @2:20:34). In the lectures the invitation is brief, and he goes straight on to the answer ([[youtube-2024-06-09-reproduce-gpt-2]] @2:39:41)." Also update `steps[6]`.

### F2: overstated, [[how-he-explains]] step 3 (Add one piece at a time to a baseline)
- sentence: "In the first makemore lecture he builds the bigram model by counting, then takes the neural-net route and expects it to land near the counting loss of about 2.45 to 2.47"
- cited: [[youtube-2022-09-07-makemore-1-bigram]] @1:03:22, @1:44:36
- raw says: the neural-net version is "an alternative approach" that ends up "in a very, very similar position" (@1:03:22, @1:03:55). It is the same model trained a second way, with no extra information (@1:45:08), not a piece added to a baseline. The loss expectation at @1:44:36 is the predict-and-check move, already used as step 4's example.
- fix: delete this sentence from step 3 (step 4 already covers @1:44:36). If an example is needed, the GPT lecture's 2.5 to 2.4 is enough.

### F3: overstated, [[how-he-explains]] step 6 (Leave the bug in, show it fail, then fix it)
- sentence: the heading, and "When a call fails in micrograd he says ... and he keeps a forgotten zero-grad in rather than reshoot"
- cited: [[youtube-2022-08-16-micrograd]] @1:15:05, @2:10:28; [[youtube-2022-11-21-makemore-5-wavenet]] @38:20, @45:01
- raw says: both micrograd bugs were accidents he chose to keep on camera ("i thought about redoing it", "i could have reshot the whole thing but i think it's pretty funny"). He did not set them up. The WaveNet bug never "fails": the code "runs but does it do the right thing" (@38:20). It is a silent bug he finds by checking the shapes. Only makemore-1 (`keepdim`) and the tokenizer (token 128) are deliberate demonstrations. The heading reads as "plant a bug", which only two of the five instances support.
- fix: change the heading to "Show a bug on purpose, and keep real ones in". Change the first sentence to: "When he makes real mistakes on camera in micrograd he keeps them rather than reshoot ..." Change the WaveNet clause to: "after a flat WaveNet result he suspects a silent BatchNorm bug, ...". Update `steps[5]`.

### F4: overstated, [[how-he-explains]] step 10 (Use a physical or everyday analogy)
- sentence: "For the chain rule he reads out Wikipedia's car, bicycle and walking man ..., and repeats it in the microgpt post, where each operation is also a little lego block ..."
- cited: [[youtube-2022-08-16-micrograd]] @42:53; [[blog-2026-02-12-microgpt]] §Autograd; [[youtube-2022-10-11-makemore-4-backprop-ninja]] @1:33:50, @1:34:57
- raw says: every location is correct. But the car analogy is Wikipedia's ("pulled up a chain rule here from wikipedia"), and the blog repeats it inside quotation marks. That leaves two analogies of his own: the lego block (microgpt, and the Dwarkesh interview @2:18:10, which the page does not cite) and forces/pulley (makemore-4 only). That is thin evidence for a step presented as one of his habits.
- fix: add "borrowed" before "Wikipedia's car". Cite the lego blocks in the interview too ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @2:18:10). Or soften the step's lead-in to "Sometimes he reaches for a physical analogy".

### F5: mis-cited, [[how-he-explains]] definition paragraph
- sentence: "The longer lists of lecture steps are on [[spelled-out-build-from-scratch]] and [[learn-by-building-and-explaining]] ([[youtube-2022-08-16-micrograd]] @00:32; [[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @2:17:33)."
- raw says: neither passage says anything about lists of steps. This is a pointer between wiki pages.
- fix: make it "**Note:** the longer lists of lecture steps are on [[spelled-out-build-from-scratch]] and [[learn-by-building-and-explaining]]." and drop the citations.

### F6: minor, step 1
- sentence: "the GPT lecture with an empty file and the bigram model, which he calls the simplest possible neural network for language modelling"
- cited: [[youtube-2023-01-17-gpt-from-scratch]] @21:57
- raw says: "the simplest possible neural network which in the case of language modeling in my opinion is the Byram language model". The bigram comes about 15 minutes after the empty file (@06:45), once the data has been prepared.
- fix: "... the GPT lecture with an empty file, and its first model is the bigram, which he calls, in his opinion, the simplest possible neural network for language modelling".

### F7: minor, step 2
- sentence: "He develops the MLP on only the first five words for efficiency"
- cited: [[youtube-2022-09-12-makemore-2-mlp]] @10:02
- raw says: "first five just for efficiency while we are developing all the code", and he later erases it to use the whole training set. It is a development shortcut, not an input chosen to explain something.
- fix: "He develops the MLP code on only the first five words, for efficiency while developing, then uses the full set".

### F8: minor, step 3
- sentence: "adding one self-attention head brings it to about 2.4"
- cited: [[youtube-2023-01-17-gpt-from-scratch]] @1:21:27
- raw says: positional embeddings were added and the learning rate was lowered with more iterations, alongside the head (@1:20:55, @1:21:27).
- fix: "adding a self-attention head (with position embeddings and a lower learning rate) brings it to about 2.4".

### F9: minor, step 3
- sentence: "For microgpt he suggests six files that each add one component"
- cited: [[blog-2026-02-12-microgpt]] §Progression
- raw says: the table's files add several components each (train3 adds position embeddings, single-head attention, rmsnorm and residuals). His own wording is stepping through "where you add one component at a time".
- fix: "For microgpt he suggests six files, train0 to train5, each adding the next layer of the build".

### F10: minor, step 11
- sentence: "The microgpt post ends with what changes between it and a production LLM"
- cited: [[blog-2026-02-12-microgpt]] §Real stuff
- raw says: §Real stuff is followed by §FAQ, so it is not the end of the post.
- fix: "The microgpt post has a closing section on what changes between it and a production LLM".

## Checked and correct
- Definition paragraph: the micrograd blank notebook, step-by-step build, "comment on all the pieces" (@00:00, @00:32); the ramp (Dwarkesh @2:18:43); the video, not the unchanged code, driving interest (X post). All supported.
- Step 1: micrograd @00:00; the interview's first-order terms and ~100 lines (@2:17:33 to @2:18:43). Supported.
- Step 2: the 6.88 bias (@1:01:09), quote and 2x2 matmul (@14:26, @43:55 to @45:02), BPE toy from Wikipedia (@23:32), toy MSE network of four examples (@2:39:41, @2:40:15). Supported.
- Step 4: all four citations supported, including "almost always", 27, 4.17 vs 4.87, and 1/50,257.
- Step 5: all five citations supported.
- Step 8: all three supported.
- Step 9: all five supported ("exact same result", "exactly equivalent").
- Step 11: micrograd scalars and "none of the math changes" (@05:24, @05:56); copy-pasted drawing code (@24:40); ng-video-lecture README NOTE. Supported.
- Generalisation from one instance: every step has at least two instances in at least two sources. Step 10 is the thinnest (F4); step 7's habit is real but weaker than written (F1).

## Resolution
Applied 2026-10-26 by the fix step.
- F1: fixed (heading "Invite the learner to pause and try first"; lecture invitations described as brief and optional; README's real-work-first request kept; interview quote now a separate sentence about good educators in general, citing @2:19:57, @2:20:34; `steps[6]` updated)
- F2: fixed (makemore-1 sentence deleted from step 3; makemore-1 still cited elsewhere, so `sources` and its Fed pages unchanged)
- F3: fixed (heading "Show a bug on purpose, and keep real ones in"; micrograd and WaveNet clauses reworded; `steps[5]` updated)
- F4: fixed (car analogy marked borrowed and quoted in the post; Dwarkesh @2:18:10 lego blocks cited; heading softened to "Sometimes use a physical analogy"; `steps[9]` updated)
- F5: fixed (now a **Note:** with no citations; both sources still cited elsewhere)
- F6: fixed
- F7: fixed
- F8: fixed (also cites @1:20:55)
- F9: fixed
- F10: fixed
