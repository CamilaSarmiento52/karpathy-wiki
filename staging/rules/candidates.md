# Rule candidates (phase 4, extract step)

_Drafted 2026-10-26 by the extract agent. Read-only pass over `wiki/methods/` (all 26),
`wiki/index/claims.md`, 45 claim pages on how he builds, teaches, debugs, reviews,
simplifies and evaluates, and the raw files behind them. Every quote below was copied from
the raw file and checked verbatim with a script (case, whitespace, curly quotes and
`[mm:ss]` markers ignored; no quote crosses a caption marker). Every quote is under 15
words. No AI-written part of any source is used (the autoresearch session report and the
Sequoia Ascent blog summary are not cited). This file is input for the verify agent, not a
wiki page._

**Independence used here** (plan §1): different source pages, not the same text, not
AI-written, not a summary of each other. Separate Zero to Hero lectures count separately.
Separate llm.c GitHub discussions (#224, #454, #481, #677) are separate posts and count
separately; the llm.c README and the CUDA MODE keynote are different texts and count
separately.

**Summary**

| # | slug | proposed status | hypothesis |
|---|---|---|---|
| 1 | build-it-yourself-to-understand-it | promoted | H1, confirmed (reworded) |
| 2 | start-from-the-simplest-thing-that-shows-it | promoted | H2, reworded; absorbs "build the ramp" |
| 3 | predict-the-number-before-you-run | promoted | H3, confirmed (reworded) |
| 4 | check-every-shape-and-be-explicit | promoted | new |
| 5 | check-against-a-known-good-reference | promoted | H5, reworded |
| 6 | report-every-result-with-its-baseline-and-caveats | promoted | new; takes the reporting half of H5 |
| 7 | keep-model-written-changes-small-and-check-them | promoted | new; takes the AI-code half of H5 |
| 8 | cut-complexity-that-does-not-pay-for-itself | promoted | H7, reworded |
| 9 | let-the-learner-try-before-you-show-the-answer | promoted | new |
| 10 | show-the-instructive-bug-failing-then-explain-it | promoted | H4, reworded (drops "first") |
| 11 | surface-assumptions-and-ask-when-unclear | inferred | H6, reworded |

---

## 1. build-it-yourself-to-understand-it

**Title:** Build it yourself, without copy-paste, to understand it.

**Quotes**
- "Build the stuff yourself, but don't allow yourself copy-paste." — [[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @29:27
- "write our own gpt2 class so that we have full understanding" — [[youtube-2024-06-09-reproduce-gpt-2]] @12:18
- "you will need to understand how it works under the hood" — [[youtube-2022-10-11-makemore-4-backprop-ninja]] @01:05

**Independent sources:** 3 (Dwarkesh interview; GPT-2 lecture; makemore 4 lecture). All
independent: different recordings, none AI-written. Note: the Dwarkesh @30:04 line "If I
can't build it, I don't understand it" is a Feynman quote he endorses, so it is not used as
his wording; his own "Build the code, arrange it, get it to work." (@30:04) is available as
an alternate.

**Proposed status:** promoted.

**Rests on:** [[learn-by-building-and-explaining]], [[spelled-out-build-from-scratch]],
[[if-you-cannot-build-it-you-do-not-understand-it]], [[understand-backprop-even-with-autograd]],
[[understanding-cannot-be-outsourced]] (context only: an endorsed line, not his own),
[[backpropagation]], [[ai-for-education]].

**In practice**
- Teaching: the walkthrough writes the thing from an empty file (the learner types it), with
  the finished repo allowed only as a reference, never pasted in.
- Teaching: when a library call hides the idea being taught (autograd, a scheduler, a
  framework model class), write the few explicit lines first, then show the library call is
  equivalent.
- Reviewing: flag code the author cannot explain line by line, especially framework
  calls used to paper over a behaviour they have not traced.

**Hypothesis:** confirms H1 ("Build it or you don't understand it"), reworded to the
narrower thing the quotes say: build it yourself, without copy-paste.

---

## 2. start-from-the-simplest-thing-that-shows-it

**Title:** Start from the simplest thing that shows the idea working, then add one piece at
a time, and show the steps.

**Quotes**
- "I always try to find the first-order terms" — [[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @2:17:33
- "we're going to start off with the simplest possible neural network" — [[youtube-2023-01-17-gpt-from-scratch]] @21:57
- "where you add one component at a time" — [[blog-2026-02-12-microgpt]] §Progression
- "Step 2 build the ramp." — [[x-2024-02-21-technical-accessibility]] #1

**Independent sources:** 4 (Dwarkesh interview; GPT lecture; microgpt blog; X post).
All independent. The microgpt post is his own text (no AI-written part noted on its source
page).

**Proposed status:** promoted.

**Rests on:** [[learn-by-building-and-explaining]] (steps 2–3), [[spelled-out-build-from-scratch]]
(steps 3, 11, 14–16, 26, microgpt progression), [[small-hackable-educational-code]] (step 9),
[[micrograd-is-all-you-need-everything-else-is-efficiency]],
[[microgpt-is-the-full-algorithm-everything-else-is-efficiency]],
[[build-the-ramp-not-just-the-thing]], [[education-is-building-ramps-to-knowledge]],
[[verify-gradients-against-pytorch]] (step 8, tiny 2×2 examples).

**In practice**
- Teaching: open with the smallest working version (a count table, a scalar engine, a
  bigram), on a tiny input, then add exactly one component per step and say what problem
  each addition solves.
- Teaching: deliver the build-up, not only the end state: a sequence of small diffs or
  commits the learner can walk.
- Reviewing: ask what the first-order version of the change is; if a PR mixes the core idea
  with efficiency work, suggest landing the simple version first.

**Hypothesis:** rewords H2 ("First-order term first"); merges his "build the ramp" idea,
which was not a separate DESIGN.md rule.

---

## 3. predict-the-number-before-you-run

**Title:** Before you run it, say what number you expect; then compare.

**Quotes**
- "you will have a rough idea for what loss to expect at initialization" — [[youtube-2022-10-04-makemore-3-activations-batchnorm]] @04:28
- "we can actually guess at what the loss should be" — [[youtube-2023-01-17-gpt-from-scratch]] @28:03
- "what do we expect to see before this actually happens" — [[youtube-2024-06-09-reproduce-gpt-2]] @1:04:39
- "your network might actually work" — [[youtube-2022-08-16-micrograd]] @2:13:16 (the reason: buggy code can still train)

**Independent sources:** 4 lectures (makemore 3, GPT, GPT-2, micrograd). All independent
(separate lectures of the series). The micrograd quote supports the reason, not the
procedure.

**Proposed status:** promoted.

**Rests on:** [[training-diagnostics]] (step 1, the GPT and GPT-2 repeats, steps 11–13),
[[diagnose-under-or-overfitting]] (steps 2, 6, 13), [[the-hockey-stick-loss-means-training-is-wasting-steps]],
[[a-buggy-neural-net-can-still-train-on-a-simple-problem]], [[forgetting-to-zero-grad-is-a-common-neural-net-bug]],
[[loss-functions]], [[weight-initialization]].

**In practice**
- Teaching: before each run, write the expected value and why (e.g. -ln(1/vocab) at init,
  "loss should drop but not to zero"), then run and read the gap aloud.
- Reviewing: for any training or numeric code, state the expected first loss, shape or
  output, run it, and treat a mismatch as a bug to explain, even if the run "works".
- Never accept "it trains" as evidence of correctness on its own.

**Hypothesis:** confirms H3 ("Predict, then run, then compare"). The DESIGN.md wording
"silently work a bit worse" was not found in any raw file; it is replaced by the micrograd
quote.

---

## 4. check-every-shape-and-be-explicit

**Title:** Check every shape and broadcast, and write code explicit enough that a wrong
assumption raises an error.

**Quotes**
- "And I encourage you to treat this with respect." — [[youtube-2022-09-07-makemore-1-bigram]] @44:10
- "we want to make sure that the broadcasting will do what we like" — [[youtube-2022-09-12-makemore-2-mlp]] @28:16
- "we have to scrutinize and be careful with the shapes" — [[youtube-2022-10-11-makemore-4-backprop-ninja]] @22:12
- "I like to be very explicit so that you get error messages" — [[youtube-2022-11-21-makemore-5-wavenet]] @32:49

**Independent sources:** 4 lectures (makemore 1, 2, 4, 5). Independent as separate lectures
of one series. All from 2022, PyTorch tensor work; the rule is scoped to array code.

**Proposed status:** promoted.

**Rests on:** [[check-shapes-and-broadcasting]], [[treat-broadcasting-with-respect]],
[[deep-learning-is-largely-shape-gymnastics]], [[verify-gradients-against-pytorch]] (steps 7, 9),
[[prototype-in-jupyter-then-repo]] (steps 1–2), [[broadcasting]], [[pytorch]].

**In practice**
- Teaching: write the shape of every tensor next to each line; walk both operands of a
  broadcast through the alignment rules before running it.
- Reviewing: flag `view(-1)`, bare `squeeze()`, reductions without `keepdim`, and silent
  broadcasts; suggest explicit dimensions so a wrong assumption fails loudly.
- Reviewing: push a tiny scratch batch through and print each layer's output shape.

**Hypothesis:** new. It overlaps H6 only in the narrow sense of making code assumptions
explicit; see rule 11.

---

## 5. check-against-a-known-good-reference

**Title:** When you reimplement something, check it against a known-good reference until
the numbers match.

**Quotes**
- "it's only a reference that we check correctness with respect to" — [[talk-2024-10-03-cuda-mode-keynote]] @05:00
- "This gives nice confidence for correctness and match to PyTorch!" — [[github-2024-05-24-llmc-pytorch-cross-checks]] §1 GPU training in FP32
- "I then wrote the Rust code against this implementation with tests for equality." — [[github-2026-01-03-rustbpe-readme]] §LLM Assistance note
- "you can encode the string and you should get these tokens" — [[youtube-2024-02-20-gpt-tokenizer]] @1:26:20

**Independent sources:** 4 (CUDA MODE keynote; llm.c Discussion #454; rustbpe README;
tokenizer lecture). All independent; the keynote and #454 are both about llm.c but are
different texts.

**Proposed status:** promoted.

**Rests on:** [[verify-against-a-reference-implementation]], [[verify-gradients-against-pytorch]],
[[port-a-pytorch-model-to-c-and-cuda]] (steps 1–3, 6–7), [[reproduce-a-published-model]]
(steps 9–13), [[counting-and-gradient-bigram-models-are-the-same-model]] (the counting model as
reference), [[spelled-out-build-from-scratch]] (steps 11, 23).

**In practice**
- Teaching and building: keep a slow, obvious implementation (PyTorch, a counting model,
  numeric gradients, the original library) and assert equality or `allclose` against it at
  each step, reporting the max difference.
- Reviewing: for a rewrite, optimisation or port, ask "what is it checked against?"; if
  nothing, write the equality test before reading further, and run it.
- Use non-trivial inputs (non-zero biases, edge-case strings) so the check can fail.

**Hypothesis:** rewords H5 ("Prove it, don't claim it"). The quotes support a specific way
of proving it, parity with a reference; "prove it, don't claim it" as a phrase is not his.
H5's other halves are rules 6 and 7.

---

## 6. report-every-result-with-its-baseline-and-caveats

**Title:** Report every result with its baseline, its setting and what might make it
unfair.

**Quotes**
- "in this constrained setting" — [[github-2024-04-22-llmc-state-of-the-union]] §intro
- "so it's not a super fair comparison" — [[github-2024-05-28-llmc-gpt-2-124m]] §intro
- "I wouldn't say I have full confidence that the PyTorch script is maximally tuned" — [[github-2024-07-11-llmc-gpt-2-1-6b]] §intro (PyTorch comparison)
- "this is not an exactly fair comparison but it's a good cross check" — [[youtube-2024-06-09-reproduce-gpt-2]] @3:44:15

**Independent sources:** 4 (llm.c Discussions #224, #481, #677; GPT-2 lecture). Separate
posts and a lecture, none repeating another's text. All are from 2024 and about llm.c or
GPT-2; a 2026 echo is [[only-actual-metrics-are-real-and-comparable]] (one source).

**Proposed status:** promoted. Caution for the verifier: each quote is a caveat on one
result; the general rule is the pattern across them, but at least four separate texts state
such a caveat in his own words, so it is not marked inferred.

**Rests on:** [[llm-c-trained-gpt-2-faster-than-pytorch-in-his-measurements]],
[[his-gpt-2-reproductions-beat-openais-checkpoints-on-hellaswag]],
[[only-actual-metrics-are-real-and-comparable]], [[inherited-gpt-3-hyperparameters-look-conservative]],
[[reproduce-a-published-model]] (steps 5–7, 14), [[verify-against-a-reference-implementation]]
(steps 7, 11), [[llm-evaluation]].

**In practice**
- Building: every reported number comes with the command, hardware, baseline and what the
  baseline may be missing (untuned, different data, stale version).
- Reviewing: reject "X% faster" or "better loss" claims that lack the baseline and setting;
  ask whether the comparison is fair and say so in the review.
- Teaching: when a learner's number beats a reference, name the reasons it might not be a
  like-for-like comparison before celebrating it.

**Hypothesis:** new. It takes the reporting half of H5 ("It works needs the real output")
and the results half of H6 ("say what you assumed").

---

## 7. keep-model-written-changes-small-and-check-them

**Title:** Keep model-written changes small enough to review, and check each one before
trusting it.

**Quotes**
- "we have to keep the AI on the leash" — [[youtube-2025-06-19-software-is-changing]] @22:43
- "use it as a tool in a toolbox don't trust it fully" — [[youtube-2025-02-05-deep-dive-into-llms]] @3:30:23
- "I would always encourage you to scrutinize the code" — [[youtube-2025-02-27-how-i-use-llms]] @1:05:46
- "This keeps the scope manageable and diffs reviewable." — [[github-2026-03-21-autoresearch-readme]] §Design choices

**Independent sources:** 4 (YC talk; Deep Dive lecture; How I use LLMs; autoresearch README).
All independent; the two 2025 videos are separate lectures.

**Proposed status:** promoted, with a dating caveat: from December 2025 he says he
delegates most coding to agents and reviews "as best you can" depending on how much he
cares about the code ([[he-now-delegates-most-coding-to-agents]], [[ai-assisted-coding-loop]]
§Parallel agents). The rule stands for code that matters; the agent should not claim he
reviews every line in 2026.

**Rests on:** [[ai-assisted-coding-loop]], [[verify-citations]], [[use-llms-as-tools-and-check-their-work]],
[[use-llms-as-copilots-with-human-oversight]], [[coding-models-are-weak-at-code-never-written-before]],
[[agentic-engineering-keeps-the-quality-bar-while-going-faster]], [[vibe-coding]], [[partial-autonomy-apps]].

**In practice**
- Building: the agent works in small, separately runnable diffs and runs each before
  writing the next; it does not hand back a 1,000-line change.
- Reviewing: for AI-written code, read for silent fills, invented defaults, deprecated APIs,
  defensive bloat and framework substitutions (his DDP example), and say which you found.
- Treat its own output as a first draft: run it, check it, then report.

**Hypothesis:** new. It overlaps H5 (prove it) for the AI-coding case.

---

## 8. cut-complexity-that-does-not-pay-for-itself

**Title:** Keep the main code small and readable; reject complexity that does not pay for
itself.

**Quotes**
- "but not at the cost of simplicity, readability or portability" — [[github-2024-05-29-llama2c-readme]] §contributing
- "I may reject the PR because the complexity is not worth it." — [[github-2024-09-24-llmc-readme]] §repo
- "it's too much complexity for not enough gain at this point" — [[talk-2024-10-03-cuda-mode-keynote]] @15:58
- "minGPT tries to be small, clean, interpretable and educational" — [[github-2023-01-08-mingpt-readme]] §intro

**Independent sources:** 4 (llama2.c README; llm.c README; CUDA MODE keynote; minGPT README).
All independent texts.

**Proposed status:** promoted. Scope note: in the llm.c README the trade is weighed (cuBLAS
is accepted as one line for a big gain), so the rule is "complexity must pay", not "always
the shortest code".

**Rests on:** [[small-hackable-educational-code]] (steps 1–4, 10–14), [[port-a-pytorch-model-to-c-and-cuda]]
(step 10), [[neural-net-training-should-not-be-complicated]], [[gpt-is-not-a-complicated-model]],
[[coding-models-are-weak-at-code-never-written-before]] (bloat he cleans out), [[compute-efficiency]].

**In practice**
- Reviewing: for each addition ask what it buys (speed, correctness, reach) against its
  lines, dependencies and knobs; propose deleting what does not pay, and run before and
  after to show behaviour is unchanged.
- Reviewing: prefer one hackable file and config in code over flags and frameworks; send
  platform-specific or scenario-specific code to a fork or a scratch folder (`dev/`).
- Teaching: keep the simple version alive next to the fast one.

**Hypothesis:** rewords H7 ("Simpler wins") to the trade he actually states.

---

## 9. let-the-learner-try-before-you-show-the-answer

**Title:** Let the learner try before you show the answer.

**Quotes**
- "I'm not going to present the solution before you guess." — [[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @2:19:57
- "see if you can figure it out yourself" — [[youtube-2022-08-16-micrograd]] @1:33:56
- "try to maybe implement this yourself if you'd like a fun exercise" — [[youtube-2024-02-20-gpt-tokenizer]] @48:38
- "This video is not super intended to be simply watched." — [[github-2024-02-20-nn-zero-to-hero-readme]] §intro, Lecture 5

**Independent sources:** 4 (Dwarkesh interview; micrograd lecture; tokenizer lecture;
Zero to Hero README). All independent. Attribution flag for the verifier: the Dwarkesh raw
has no speaker labels; the @2:19:57 block opens with Dwarkesh's remark about presenting the
pain before the solution, and the quoted sentence is the educator's reply that the method
page [[learn-by-building-and-explaining]] attributes to him. If the verifier doubts it, the
other three still promote the rule.

**Proposed status:** promoted.

**Rests on:** [[learn-by-building-and-explaining]] (step 4), [[spelled-out-build-from-scratch]]
(steps 7, 12, 21–22), [[education-is-building-ramps-to-knowledge]], [[ai-for-education]].

**In practice**
- Teaching: pose the next step as a question ("what should the local gradient be?") and
  wait for the learner's attempt before giving it; ship small exercises with each step.
- Teaching: when the learner is stuck, give the answer and say why it is the only one that
  fits the objective.
- Reviewing: not applicable, except that review comments can ask the author to predict a
  failure before being told it.

**Hypothesis:** new.

---

## 10. show-the-instructive-bug-failing-then-explain-it

**Title:** When a bug is instructive, leave it in, show it failing, then explain it.

**Quotes**
- "i could have reshot the whole thing but i think it's pretty funny" — [[youtube-2022-08-16-micrograd]] @2:10:28
- "you'd expect it to work but it doesn't you actually get garbage" — [[youtube-2022-09-07-makemore-1-bigram]] @46:21
- "hopefully this helps to scare you that you should have a respect for broadcasting" — [[youtube-2022-09-07-makemore-1-bigram]] @49:08

**Independent sources:** 2 (micrograd lecture; makemore 1 lecture). Independent as separate
lectures. The two makemore 1 quotes are one source.

**Proposed status:** promoted, narrowly. The micrograd line says he kept a real mistake in
the recording; the makemore 1 lines say he broke `keepdim` on purpose so viewers would see
the failure. Neither says to show the wrong version *first* as a general ordering, so that
word is dropped. The tokenizer lecture opening with tokenizer failures
([[spelled-out-build-from-scratch]] step 22) is supporting behaviour, not a quote. The
micrograd quote is weak on its own ("funny"); its next clause, about appreciating what
working with neural nets is like, is 15 words and could not be quoted under the limit.

**Rests on:** [[spelled-out-build-from-scratch]] (steps 8, 12, 22), [[check-shapes-and-broadcasting]]
(step 4), [[forgetting-to-zero-grad-is-a-common-neural-net-bug]], [[a-buggy-neural-net-can-still-train-on-a-simple-problem]],
[[treat-broadcasting-with-respect]].

**In practice**
- Teaching: introduce the common bug deliberately (drop `keepdim`, skip `zero_grad`), run
  it, show the wrong output, ask why, then fix.
- Reviewing: when reporting a bug, reproduce it by running the code and show the failing
  output next to the fixed one, rather than only describing it.

**Hypothesis:** rewords H4 ("Show the wrong version first").

---

## 11. surface-assumptions-and-ask-when-unclear

**Title:** State the assumptions you are making, and ask when the request leaves them open.

**Closest quotes**
- "it made an implicit assumption" — [[youtube-2025-02-27-how-i-use-llms]] @1:08:01
- "when to ask clarifying questions" — [[talk-2026-03-20-skill-issue]] @25:39
- "I have a bunch of assumptions in my code, and it's okay." — [[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @33:14

**Independent sources:** 3 (How I use LLMs; Skill Issue interview; Dwarkesh interview),
all independent, but none states the rule.

**Proposed status:** inferred. Why: each quote describes a failure he sees in models, not a
rule he gives. In How I use LLMs, ChatGPT's analysis code silently filled a missing value
and he says to scrutinise the code; in Skill Issue, he lists knowing when to ask clarifying
questions among things models struggle with; in the Dwarkesh interview, agents ignored the
deliberate assumptions in his repo. The imperative, say what you assumed and ask when
unsure, is this wiki's reading of those complaints. DESIGN.md's "his top complaint about
coding agents" is not supported by any raw file in the wiki and should not be repeated.

**Rests on:** [[verify-citations]] (step 4), [[coding-models-are-weak-at-code-never-written-before]],
[[agent-failures-mostly-feel-like-a-skill-issue]], [[ai-assisted-coding-loop]] (step 2, a
concrete prompt), [[check-shapes-and-broadcasting]] (step 11, be explicit).

**In practice**
- Building and teaching: before writing code, list the assumptions the request leaves open
  (data, shapes, scale, what "done" means); if one changes the result, ask.
- Reviewing: name the implicit assumptions in the code (defaults, filled values, assumed
  dimensions) and ask whether each was intended.
- The agent says it is leaning on an inferred rule when it does so.

**Hypothesis:** rewords H6 ("Say what you assumed"), kept as inferred.

---

## Hypotheses rejected or merged

None of the seven is rejected outright for lack of evidence; all are reworded, and two are
split or merged.

- **H1 Build it or you don't understand it** — kept as rule 1, reworded. The strongest line,
  "If I can't build it, I don't understand it", is a Feynman quote he endorses, not his own
  words, so the title follows his own instruction (build it yourself, no copy-paste).
- **H2 First-order term first** — kept as rule 2, reworded and merged with "build the ramp".
  The ramp idea (lay out the build-up, step by step) has its own quotes but is the same move
  seen from the publishing side.
- **H3 Predict, then run, then compare** — kept as rule 3. Only the illustrative phrase
  "silently work a bit worse" is dropped: it is not in any raw file in the wiki.
- **H4 Show the wrong version first** — kept as rule 10, reworded. The quotes support
  showing an instructive bug fail; none supports "first" as a general ordering.
- **H5 Prove it, don't claim it** — split. The parity check is rule 5; reporting results
  with their baseline is rule 6; checking model-written code is rule 7. The phrase itself is
  not his, and "it works needs the real output next to it" is closest to rules 5 and 10.
- **H6 Say what you assumed** — reworded as rule 11 and kept only as `inferred`: no quote
  states it; his words describe models failing at it. Its results half moves to rule 6. The
  DESIGN.md claim that wrong assumptions are "his top complaint about coding agents" has no
  supporting raw text in the wiki.
- **H7 Simpler wins** — kept as rule 8, reworded. He states a trade (complexity must pay),
  not "simplest always", and accepts complexity that buys enough (cuBLAS, `dev/` folder).

## Considered and dropped

- **Explain it to find what you don't understand** (Dwarkesh @2:24:31). One source only;
  bench at best, and it overlaps rule 1. Folded into rule 1's teaching practice instead.
- **Overfit a single batch first.** Done in makemore 2 and the GPT-2 lecture
  ([[diagnose-under-or-overfitting]]), but no quote gives it as a rule; a behaviour pattern,
  covered as a case of rule 3.
- **Validate at target scale / small-scale tuning does not transfer**
  ([[small-scale-tuning-does-not-always-transfer]]). One post, and the same post says many
  ideas do transfer; too narrow and too hedged for a general rule.
- **Trust benchmark metrics over validation loss** ("Only actual metrics are real and
  comparable.", nanochat miniseries v1). One source; a case of rule 6.
- **Write the few lines yourself rather than use an abstraction you cannot see into**
  (GPT-2 lecture @2:22:45, which he calls "personal style"). Single source, self-described
  as style; merged into rules 1 and 8.
- **Make it work, then make it cheap** ([[make-it-work-then-make-it-cheap]]). Two sources,
  but it is about building LLM applications, not how he teaches or reviews code.
- **Take yourself out of the agent loop** ([[take-yourself-out-of-the-agent-loop]]). One
  interview, scoped by him to tasks with an objective metric; an opinion about agent use
  that pulls against rule 7, not a teaching or review method.
- **Seed the randomness and publish the full command.** Consistent behaviour
  ([[spelled-out-build-from-scratch]] step 10, [[reproduce-a-published-model]] step 7) but no
  direct statement; folded into rule 6's practice.
- **Count the hours; publish projects good or bad** ([[build-and-publish-projects]]).
  Career advice from one talk, not a build or review method.
- **Avoid batch normalization; call F.cross_entropy.** Domain opinions about specific
  layers and APIs, not working rules; they can appear as review examples under rules 4 and 8.
- **Personal LLM-use habits** (new chat per topic, model tier, voice input, read with an
  LLM). His own tool habits, not how he builds, teaches or reviews.
