---
type: source
raw_path: raw/talks/kwSVtQ7dziU.md
published: 2026-03-20
medium: talk
summary: "No Priors interview: since December he delegates nearly all his coding to agents and wants to run many in parallel, runs a home claw, built autoresearch to take himself out of the research loop, and talks about jaggedness, speciation, open models, jobs, robotics and explaining things to agents."
url: https://www.youtube.com/watch?v=kwSVtQ7dziU
title: "Skill Issue: Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI"
---
# Skill Issue: Andrej Karpathy on Code Agents, AutoResearch, and the Loopy Era of AI
Raw: [[raw/talks/kwSVtQ7dziU]] · Original: https://www.youtube.com/watch?v=kwSVtQ7dziU

An interview on the No Priors podcast. The host's questions and remarks are not cited as his; the opening at @00:00 is a montage of clips from later in the recording, so later blocks are cited instead. Spans where the speaker is unclear (parts of @06:02, @21:51, @25:05, @31:08, @37:06–@37:40, the months-behind figures at @49:39, the opening of @58:59) are not attributed to him. Caption errors: "Claude" is written where he says "claw" (@07:07, "Open Claude" = OpenClaw), and at @08:12 it is unclear which is meant; "scale issue" = skill issue; "Nan Chat" and "data chat" = nanochat; "program MD" = program.md; "Quinn" is probably Qwen; "write coding" (@14:13, @14:47) is probably "vibe coding" but is not asserted. He says "December" and "January" with no year.

## Summary
He says that in December something flipped: he went from writing about 80% of his code himself to delegating most of it to agents, and thinks he has hardly typed a line of code since (@01:41). He describes running several agents in parallel as "macro actions" over a repository, asks how he can run more of them, feels that failures are mostly a skill issue, and wants to maximise his token throughput (@03:20, @04:25, @05:30). He describes claws, a persistent looping layer above agents, and his home claw Dobby, which replaced six smart-home apps (@07:07, @09:16, @11:26). Autoresearch, his loop that tunes nanochat against an objective metric overnight, found tunings he had missed, and he argues researchers should be removed from the loop wherever results can be evaluated (@17:32, @18:36, @19:40, @24:02). He keeps caveats: models are jagged, strong where RL has verifiable rewards and stuck elsewhere, and pushing agents too far ahead is net not useful (@24:02, @24:34, @26:44). He also covers speciation of models, open models trailing the frontier as a decent power balance, the Jevons paradox for software, bits before atoms in robotics, and microGPT, after which he explains things to agents rather than to people (@29:29, @52:59, @42:34, @55:09, @1:02:46).

## Key points
- Since December he says he has hardly typed code and delegates most of it to agents → [[he-now-delegates-most-coding-to-agents]], [[autocomplete-is-his-coding-sweet-spot]], [[vibe-coding]], [[vibe-coding-over-time]], [[vibe-coding-will-terraform-software]]
- Parallel agent sessions as macro actions over a repo, reviewed as much as he cares about the code → [[ai-assisted-coding-loop]]
- When agents fail it mostly feels like a skill issue, though he hedges → [[agent-failures-mostly-feel-like-a-skill-issue]]
- Take yourself out of the loop to raise leverage → [[take-yourself-out-of-the-agent-loop]], [[partial-autonomy-apps]], [[llm-agents-over-time]]
- Claws: persistent agents with their own sandbox and memory; Dobby runs his home → [[claws]]
- Apps should be APIs, agents the glue; explain things to agents, who explain them to people → [[building-for-agents]]
- Autoresearch tunes nanochat overnight; it needs an objective metric → [[autoresearch]], [[nanochat]], [[autoresearch-needs-an-objective-metric]], [[software-2-0-automates-what-you-can-verify]]
- The labs are all trying, roughly, to have LLMs improve LLMs → [[all-frontier-labs-will-autoresearch]], [[llm-self-improvement]], [[llm-self-improvement-over-time]]
- What RL does not optimise, such as jokes, does not improve → [[what-rl-does-not-optimize-does-not-improve]], [[verifiability-drives-the-jagged-frontier]], [[jagged-intelligence]]
- Expect more speciation of models; open models months behind as a decent balance; not independent inside a lab → [[expect-more-speciation-of-models]], [[ai-ecosystem]]
- Cheaper software should raise demand for it (Jevons paradox); the BLS jobs data → [[cheaper-software-will-raise-demand-for-it]], [[ai-and-the-economy]]
- Digital change first, physical later → [[physical-automation-will-lag-digital-automation]]
- microGPT, 200 lines; all the rest is efficiency; an agent cannot write it → [[microgpt]], [[micrograd-is-all-you-need-everything-else-is-efficiency]], [[coding-models-are-weak-at-code-never-written-before]]

## Fed pages
- [[he-now-delegates-most-coding-to-agents]]
- [[agent-failures-mostly-feel-like-a-skill-issue]]
- [[take-yourself-out-of-the-agent-loop]]
- [[autoresearch-needs-an-objective-metric]]
- [[what-rl-does-not-optimize-does-not-improve]]
- [[expect-more-speciation-of-models]]
- [[cheaper-software-will-raise-demand-for-it]]
- [[all-frontier-labs-will-autoresearch]]
- [[autocomplete-is-his-coding-sweet-spot]]
- [[coding-models-are-weak-at-code-never-written-before]]
- [[vibe-coding-will-terraform-software]]
- [[physical-automation-will-lag-digital-automation]]
- [[micrograd-is-all-you-need-everything-else-is-efficiency]]
- [[software-2-0-automates-what-you-can-verify]]
- [[verifiability-drives-the-jagged-frontier]]
- [[claws]]
- [[vibe-coding]]
- [[partial-autonomy-apps]]
- [[building-for-agents]]
- [[llm-self-improvement]]
- [[jagged-intelligence]]
- [[ai-ecosystem]]
- [[ai-and-the-economy]]
- [[autoresearch]]
- [[nanochat]]
- [[microgpt]]
- [[ai-assisted-coding-loop]]
- [[vibe-coding-over-time]]
- [[llm-agents-over-time]]
- [[llm-self-improvement-over-time]]
