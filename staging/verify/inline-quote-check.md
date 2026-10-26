# Inline quote check (2026-10-25)

Quoted spans of 3+ words inside evidence blocks (outside claim blockquotes, which lint
already checks) that do not appear in any raw file cited in the same block. Found by a
script after the batch 4 fix pass. Format: page | quote (first 90 chars).


wiki/claims/a-cognitive-core-could-be-a-billion-parameters-or-less.md | I don't know, we'll see
wiki/topics/activation-functions.md | Gaussian error linear units
wiki/topics/ai-ecosystem.md | build the thing, build the ramp
wiki/topics/ai-ecosystem.md | not your weights, not your brain
wiki/claims/ai-will-not-show-up-as-a-jump-in-gdp.md | pretty willing to be convinced
wiki/artifacts/autoresearch.md | you are programming the  Markdown files that provide context to the AI agents
wiki/claims/coding-models-are-weak-at-code-never-written-before.md | never written before
wiki/claims/hallucinations-come-from-imitating-confident-answers.md | who is X
wiki/topics/llm-hallucinations.md | who is X
wiki/claims/llms-want-to-imitate-not-succeed.md | let's work this out in a step by step way to be sure we have the right answer
wiki/claims/llms-want-to-imitate-not-succeed.md | let's think step by step
wiki/artifacts/nanochat.md | time to GPT-2
wiki/topics/pretraining-and-finetuning.md | cat sat on a
wiki/topics/prompting-llms.md | Language Models are Few-Shot Learners
wiki/topics/prompting-llms.md | Transformers are capable of in-context learning or meta learning
wiki/methods/quick-experiment-loop.md | about five minutes
wiki/claims/rl-is-terrible-but-better-than-imitation.md | just have correct answers
wiki/topics/scaling-laws.md | how long to train a d12
wiki/claims/small-scale-tuning-does-not-always-transfer.md | Keep a change only if it works at every scale
wiki/topics/software-3-0.md | explicit rules / learned weights
wiki/timeline/vibe-coding-over-time.md | not for anything important

## Resolution

- wiki/claims/a-cognitive-core-could-be-a-billion-parameters-or-less.md | "I don't know, we'll see" | ok (raw @28:36 has no comma)
- wiki/topics/activation-functions.md | "Gaussian error linear units" | legit non-quote (paper title), captions garbled; quotation marks dropped
- wiki/topics/ai-ecosystem.md | "build the thing, build the ramp" | misquote; paraphrased
- wiki/topics/ai-ecosystem.md | "not your weights, not your brain" | ok (punctuation)
- wiki/claims/ai-will-not-show-up-as-a-jump-in-gdp.md | "pretty willing to be convinced" | ok (split by [1:27:37] marker)
- wiki/artifacts/autoresearch.md | "you are programming the `program.md`..." | ok (backticked filename stripped by script)
- wiki/claims/coding-models-are-weak-at-code-never-written-before.md | "never written before" | misquote; now "never been written before", @35:43 added
- wiki/claims/hallucinations-come-from-imitating-confident-answers.md | "who is X" | legit non-quote (example input), not verbatim; quotation marks dropped
- wiki/topics/llm-hallucinations.md | "who is X" | legit non-quote (example input), not verbatim; quotation marks dropped
- wiki/claims/llms-want-to-imitate-not-succeed.md | "let's work this out in a step by step way..." | legit non-quote (paper's prompt), verbatim bar hyphens; no change
- wiki/claims/llms-want-to-imitate-not-succeed.md | "let's think step by step" | legit non-quote (paper's prompt), verbatim bar hyphens; no change
- wiki/artifacts/nanochat.md | "time to GPT-2" | legit non-quote (metric name); absent from the cited 2026-01-31 post, quotation marks dropped there (README bullet fine)
- wiki/topics/pretraining-and-finetuning.md | "cat sat on a" | legit non-quote (example input), captions garbled; quotation marks dropped
- wiki/topics/prompting-llms.md | "Language Models are Few-Shot Learners" | legit non-quote (paper title), captions garbled; now italic, no quotation marks
- wiki/topics/prompting-llms.md | "Transformers are capable of in-context learning..." | misquote; replaced with verbatim @55:30 wording
- wiki/methods/quick-experiment-loop.md | "about five minutes" | misquote; replaced with verbatim "~5 min pretraining runs"
- wiki/claims/rl-is-terrible-but-better-than-imitation.md | "just have correct answers" | misquote; now "have just correct answers"
- wiki/topics/scaling-laws.md | "how long to train a d12" | misquote; paraphrased
- wiki/claims/small-scale-tuning-does-not-always-transfer.md | "Keep a change only if it works at every scale" | wiki method step presented as README wording; rewritten unquoted as the method page's step
- wiki/topics/software-3-0.md | "explicit rules / learned weights" | legit non-quote (host's words), not verbatim; quotation marks dropped
- wiki/timeline/vibe-coding-over-time.md | "not for anything important" | misquote; now "not a good idea for anything of actual importance"
