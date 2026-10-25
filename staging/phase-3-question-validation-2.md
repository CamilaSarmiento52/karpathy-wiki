# Phase 3 fresh-reader question and citation validation (second run)

Date: 2026-10-25. Scope: the compiled wiki available during this check. Compare with `staging/phase-3-question-validation.md` (2026-10-23).

## Method and limits

This check used a fresh subagent that had not seen how the wiki was built. It read `CLAUDE.md` §7 Query, `wiki/index.md` and every type file under `wiki/index/`, then the relevant topic, claim, timeline and artifact pages. The answers below come only from compiled wiki content. Raw files were opened afterwards, only to check the selected citations at the cited `[mm:ss]` block or §heading. No uncompiled raw material was used to fill gaps. `wiki/` and `raw/` were read-only; this file is the only one written.

This report sits outside `staging/verify/` on purpose: spot checks at the question level must not count as verifying whole sources.

**This check does not replace the user's own fresh-session test and click-through, which the phase gate requires.**

## 1. How does he explain backpropagation, and what does he build to teach it?

He explains backpropagation as recursively applying the chain rule backward through an expression graph. It starts at the output and works back to every internal node and input ([[youtube-2022-08-16-micrograd]] @03:14, @50:37). He says it is more general than neural networks: it works on arbitrary mathematical expressions, and neural nets are just one class of them ([[youtube-2022-08-16-micrograd]] @04:51). Each node knows only its local derivative, and the chain rule multiplies that onto the incoming gradient. He makes this intuitive with Wikipedia's example: a car twice as fast as a bicycle, which is four times as fast as a walker, is eight times as fast as the walker ([[youtube-2022-08-16-micrograd]] @42:53, @44:33). A plus node distributes the gradient to its inputs, and gradients are accumulated with `+=` because a variable used more than once gets a contribution from each path ([[youtube-2022-08-16-micrograd]] @45:05, @1:24:33, @1:25:05).

To teach it he rebuilds micrograd from a blank notebook. Micrograd is a scalar autograd engine (about 100 lines) plus a small neuron/layer/MLP library (about 50 lines), and he trains a tiny net with it ([[youtube-2022-08-16-micrograd]] @00:00, @07:03, @07:35). He then removes `loss.backward()` in makemore Part 4 and writes the MLP's backward pass by hand at tensor level, including closed-form cross-entropy and batchnorm gradients. His reason is that backprop is "a leaky abstraction" and the scalar engine alone is not enough ([[youtube-2022-10-11-makemore-4-backprop-ninja]] @00:31, @02:43). In 2026 microgpt reuses the same idea: "each operation as a little lego block" that knows its local gradient ([[blog-2026-02-12-microgpt]] §Autograd).

Wiki route: `wiki/topics/backpropagation.md`, `wiki/artifacts/micrograd.md`, `wiki/claims/backpropagation-is-more-general-than-neural-networks.md`, `wiki/claims/understand-backprop-even-with-autograd.md`.

Citation verification:

| Citation | Raw passage | Sentence it supports | Result |
|---|---|---|---|
| `youtube-2022-08-16-micrograd` @04:51 | [raw/youtube/VMj-3S1tku0.md:30](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/youtube/VMj-3S1tku0.md:30>) | Backprop works on arbitrary expressions; neural nets are one class of them. | Correct |
| `youtube-2022-08-16-micrograd` @42:53 | [raw/youtube/VMj-3S1tku0.md:168](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/youtube/VMj-3S1tku0.md:168>) | The car / bicycle / walking-man chain-rule intuition (2 × 4 = 8). | Correct |
| `youtube-2022-08-16-micrograd` @1:24:33, @1:25:05 | [raw/youtube/VMj-3S1tku0.md:318–320](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/youtube/VMj-3S1tku0.md:318>) | A variable used more than once has its gradient overwritten; the multivariate chain rule says accumulate with `+=`. | Correct |
| `youtube-2022-10-11-makemore-4-backprop-ninja` @00:31 | [raw/youtube/q8SA3rM6ckI.md:14](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/youtube/q8SA3rM6ckI.md:14>) | He removes `loss.backward()`, writes the backward pass at tensor level, and calls backprop a leaky abstraction. | Correct |

Coverage: **Sufficient**. Coverage is broader than on 2026-10-23: the tensor-level Part 4 lecture and microgpt are now compiled. Nothing missing for this question.

## 2. How did his view of LLM agents change between 2023 and 2026?

The wiki's timeline reads it as a view that **built up rather than reversed**. It labels this its own editorial reading, not something he states ([[llm-agents-over-time]]; [[talk-2023-05-25-state-of-gpt]] @39:57; [[blog-2025-12-19-year-in-review-2025]] §4).

- **2023:** He recommends low-stakes uses with human oversight: "think co-pilots, instead of completely autonomous agents", because it is not clear the models are there yet. He says AutoGPT does not work well in practice ([[talk-2023-05-25-state-of-gpt]] @39:24, @39:57, @29:28).
- **2024:** LLM systems are quite autonomous but not fully, and oversight will take the next few years to work out ([[talk-2024-03-26-sequoia-making-ai-accessible]] @06:54). He draws a demo-to-product gap lesson from self-driving, there about AGI rather than agents ([[talk-2024-09-05-no-priors-ep-80]] @01:07, @01:39).
- **2025:** "This is the decade of agents", not the year. Agents need humans in the loop, as self-driving still does ([[youtube-2025-06-19-software-is-changing]] @27:09, @27:44). In October he restates this with reasons. He uses Claude and Codex daily and finds them extremely impressive, but they lack intelligence, multimodality, computer use and continual learning ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @01:25, @01:59). They still feel like "this elementary-grade student" ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @1:43:07). In December he calls Claude Code "the first convincing demonstration of what an LLM Agent looks like" ([[blog-2025-12-19-year-in-review-2025]] §4).
- **2026:** His practice changes sharply. Since December he went from about 80/20 to 20/80 writing code versus delegating to agents, and says he has hardly typed a line since ([[talk-2026-03-20-skill-issue]] @01:41). He reports agents tuning nanochat by themselves ([[x-2026-03-09-autoresearch-tuning-nanochat]] #1). He says you must take yourself out of the loop and arrange things to run autonomously ([[talk-2026-03-20-skill-issue]] @16:28). He limits this to tasks that can be evaluated and says the whole thing "doesn't fully work" ([[talk-2026-03-20-skill-issue]] @24:02). In April he defines agentic engineering: coordinating "spiky", fallible but extremely powerful agents to go faster without lowering the quality bar ([[talk-2026-04-29-sequoia-ascent-2026]] @16:22).

**Note:** the wiki's reading is that his caution about full autonomy holds from 2023 to 2026. What changes is his own practice, from human-reviewed copilot use to delegating most coding and running agents unattended on tasks that can be evaluated. Nothing in the wiki shows him withdrawing the decade-of-agents horizon ([[llm-agents-over-time]]).

Wiki route: `wiki/timeline/llm-agents-over-time.md`, `wiki/claims/use-llms-as-copilots-with-human-oversight.md`, `wiki/claims/this-is-the-decade-of-agents.md`, `wiki/claims/claude-code-is-the-first-convincing-llm-agent.md`, `wiki/claims/he-now-delegates-most-coding-to-agents.md`, `wiki/claims/take-yourself-out-of-the-agent-loop.md`, `wiki/topics/agentic-engineering.md`.

Citation verification:

| Citation | Raw passage | Sentence it supports | Result |
|---|---|---|---|
| `talk-2023-05-25-state-of-gpt` @39:24, @39:57 | [raw/talks/bZQun8Y4L2A.md:154–156](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/talks/bZQun8Y4L2A.md:154>) | Low-stakes uses, human oversight, copilots not autonomous agents, models "not there right now". | Correct |
| `talk-2025-10-17-dwarkesh-ghosts-not-animals` @01:25 | [raw/talks/lXUZvyajciY.md:14](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/talks/lXUZvyajciY.md:14>) | Uses Claude and Codex daily, finds them extremely impressive, "we'll be working with these things for a decade". | Correct (the list of what they lack runs on into @01:59, which was not opened) |
| `talk-2025-10-17-dwarkesh-ghosts-not-animals` @1:43:07 | [raw/talks/lXUZvyajciY.md:332](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/talks/lXUZvyajciY.md:332>) | Claude Code / Codex "still feel like this elementary-grade student". | Correct |
| `blog-2025-12-19-year-in-review-2025` §4 | [raw/blog/year-in-review-2025.md:62](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/blog/year-in-review-2025.md:62>) | Claude Code as the first convincing demonstration of an LLM agent. | Correct |
| `talk-2026-03-20-skill-issue` @01:41 | [raw/talks/kwSVtQ7dziU.md:19](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/talks/kwSVtQ7dziU.md:19>) | 80/20 to 20/80 since December, hardly a line typed since. | Correct |
| `talk-2026-03-20-skill-issue` @16:28 | [raw/talks/kwSVtQ7dziU.md:73](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/talks/kwSVtQ7dziU.md:73>) | Remove yourself as the bottleneck; arrange things to be completely autonomous. | Correct |
| `talk-2026-03-20-skill-issue` @24:02 | [raw/talks/kwSVtQ7dziU.md:101](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/talks/kwSVtQ7dziU.md:101>) | Limited to tasks that can be evaluated; "it doesn't fully work". | Correct |
| `talk-2026-04-29-sequoia-ascent-2026` @16:22 | [raw/talks/96jN2OCOfLs.md:72](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/talks/96jN2OCOfLs.md:72>) | Agentic engineering as coordinating spiky, fallible, powerful agents without sacrificing the quality bar. | Correct |

Coverage: **Sufficient**, up from Incomplete on 2026-10-23. The 2023 baseline, a dated agent timeline and the 2026 change in practice are now compiled. Minor gaps on the timeline page, none of which blocks the answer:
- It stops at 2026-03-20. The 2026-04-29 agentic-engineering material is on its own topic page but has no timeline entry.
- It does not link `he-now-delegates-most-coding-to-agents`, which is the clearest 2026 change.
- Its first Note says "Across these six sources", but the page now has nine dated entries, so the count is stale.

## 3. What does he say about tokenization being a source of LLM problems?

He opens the tokenizer lecture by saying tokenization is "at the heart of a lot of weirdness" in LLMs. Many issues that look like problems with the architecture or the model itself actually trace back to tokenization ([[youtube-2024-02-20-gpt-tokenizer]] @00:00, @04:27). His list: spelling and string processing, non-English languages, simple arithmetic, GPT-2's trouble with Python, trailing-whitespace warnings, SolidGoldMagikarp, and preferring YAML over JSON ([[youtube-2024-02-20-gpt-tokenizer]] @04:27, @05:00, @05:33). He gives the root cause as models working on tokens, which are chunks of text, rather than characters ([[youtube-2024-02-20-gpt-tokenizer]] @2:01:10). At the end of the lecture he explains each item:
- "Hello how are you" is 5 tokens but 15 in translation, because the tokenizer is not trained enough on non-English data ([[youtube-2024-02-20-gpt-tokenizer]] @1:54:20).
- Numbers are split arbitrarily, which is a headwind for arithmetic; Llama 2 splits all digits partly for this reason ([[youtube-2024-02-20-gpt-tokenizer]] @1:55:27, @1:56:36).
- In GPT-2 every Python indentation space is its own token, which shrinks the usable context. He calls this almost a tokenization bug, fixed in GPT-4 ([[youtube-2024-02-20-gpt-tokenizer]] @1:56:36, @1:57:09).
- GPT-4 halts at `<|endoftext|>`, which he suspects is special-token parsing of user input ([[youtube-2024-02-20-gpt-tokenizer]] @1:57:09, @1:57:44).
- A trailing space splits the next token and pushes the model out of distribution ([[youtube-2024-02-20-gpt-tokenizer]] @1:58:52, @2:00:34).
- He hedges SolidGoldMagikarp: what "is thought to have happened" is a Reddit username common in the tokenizer's data but absent from the model's, so its embedding row was never trained ([[youtube-2024-02-20-gpt-tokenizer]] @2:07:16, @2:07:50).
- JSON took 116 tokens against 99 for YAML ([[youtube-2024-02-20-gpt-tokenizer]] @2:09:31).

He calls the stage full of "foot guns, sharp edges", security and AI-safety issues ([[youtube-2024-02-20-gpt-tokenizer]] @2:10:06). Later he repeats the diagnosis for a general audience: models "don't see the characters they see tokens", so spelling tasks fail ([[youtube-2025-02-05-deep-dive-into-llms]] @2:01:07). He also builds a fix around it in nanochat, formatting training answers so a word is spelled out as single-letter tokens ([[github-2025-10-24-nanochat-strawberry-guide]] §Spelling). The remedy he wishes for, tokenization-free modelling, is in his view unproven ([[youtube-2024-02-20-gpt-tokenizer]] @2:10:39).

Wiki route: `wiki/claims/a-lot-of-llm-oddness-traces-back-to-tokenization.md`, `wiki/topics/tokenization.md` (§"The failures he traces to tokenization"), `wiki/artifacts/minbpe.md`, `wiki/claims/tokenization-free-modeling-would-be-amazing-but-is-unproven.md`.

Citation verification:

| Citation | Raw passage | Sentence it supports | Result |
|---|---|---|---|
| `youtube-2024-02-20-gpt-tokenizer` @04:27, @05:00 | [raw/youtube/zduSFxRajkE.md:28–30](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/youtube/zduSFxRajkE.md:28>) | "At the heart of a lot of weirdness"; issues that look architectural trace to tokenization; spelling, non-English, arithmetic, GPT-2 Python, trailing whitespace. | Correct |
| `youtube-2024-02-20-gpt-tokenizer` @1:54:20 | [raw/youtube/zduSFxRajkE.md:420](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/youtube/zduSFxRajkE.md:420>) | 5 vs 15 tokens; tokenizer not trained enough on non-English data. | Correct |
| `youtube-2024-02-20-gpt-tokenizer` @1:56:36, @1:57:09 | [raw/youtube/zduSFxRajkE.md:428–430](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/youtube/zduSFxRajkE.md:428>) | Each Python space is a token; "almost like a tokenization bug for GPT-2", fixed in GPT-4. | Correct |
| `youtube-2024-02-20-gpt-tokenizer` @2:07:16 | [raw/youtube/zduSFxRajkE.md:466](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/youtube/zduSFxRajkE.md:466>) | Hedged SolidGoldMagikarp mechanism (tokenizer data differed from LM data; Reddit user). | Correct (the untrained-embedding step continues at @2:07:50, which was not opened) |
| `youtube-2024-02-20-gpt-tokenizer` @2:09:31, @2:10:06 | [raw/youtube/zduSFxRajkE.md:474–476](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/youtube/zduSFxRajkE.md:474>) | JSON 116 vs YAML 99 tokens; "foot guns, sharp edges", security and AI-safety issues. | Correct |
| `youtube-2025-02-05-deep-dive-into-llms` @2:01:07 | [raw/youtube/7xTGNNLPyMI.md:446](</Users/camilasarmiento/Documents/AI os/karpathy-wiki/raw/youtube/7xTGNNLPyMI.md:446>) | Models don't see characters, they see tokens, so spelling tasks fail. | Correct |

Coverage: **Sufficient**, up from Incomplete on 2026-10-23. The tokenizer lecture and the claim that collects its failure list are now compiled. Nothing missing for this question.

## 4. What does he recommend for pruning apple trees? (negative control)

The wiki has nothing on this.

Negative-control check: no topic, claim, method or source in the index touches gardening or fruit trees. A case-insensitive search for `apple|prun` over `wiki/` matches only Apple Notes (append-and-review note), Apple Watch (sleep-tracker pages) and Apple silicon (PyTorch device). None is relevant. This says the compiled wiki has no coverage. It does not prove he has never discussed the subject. There are no answer citations to check.

Coverage: **Missing**, as expected. The negative control behaves correctly.

## Gate result

| Dimension | 2026-10-23 | 2026-10-25 (this check) |
|---|---|---|
| Question 1 coverage | Sufficient | Sufficient |
| Question 2 coverage | Incomplete: no 2023 baseline or agent timeline | Sufficient. Minor timeline-page gaps: no 2026-04-29 entry, `he-now-delegates-most-coding-to-agents` not linked, stale "six sources" count |
| Question 3 coverage | Incomplete: tokenizer lecture not compiled | Sufficient |
| Question 4 negative control | Correctly says the wiki has nothing on this | Correctly says the wiki has nothing on this |
| Selected citations checked against raw | 10 checked, all Correct | 18 checked: 18 Correct, 0 Overstated, 0 Wrong |
| Fresh session opened by the user | Not done | Not done; a fresh subagent was used instead |
| User clicks two citations per answer and confirms | Pending | Pending; automated raw checks do not replace it |
| Phase gate 3 → 4 | Not passed by this validation | Not passed by this validation alone |

This check does not replace the user's own fresh-session test and click-through, which the phase gate requires. It validates selected citations and shows coverage. It does not mark any source as fully verified, and it does not settle the other Phase 3 completion requirements.
