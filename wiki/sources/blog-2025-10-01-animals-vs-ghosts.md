---
type: source
raw_path: raw/blog/animals-vs-ghosts.md
published: 2025-10-01
medium: blog
summary: "His response to Richard Sutton on the Dwarkesh podcast: he grants Sutton that frontier LLMs are full of human input and not cleanly bitter-lesson pilled, but doubts animals learn from scratch, calls pretraining a crappy stand-in for evolution, and says today's LLM research summons ghosts rather than building animals."
url: https://karpathy.bearblog.dev/animals-vs-ghosts/
title: Animals vs Ghosts
---
# Animals vs Ghosts
Raw: [[raw/blog/animals-vs-ghosts]] · Original: https://karpathy.bearblog.dev/animals-vs-ghosts/

The body before the one heading is cited `§intro`; the bullets after it, `§Appendix`. The
same text, without the Appendix, is his X post [[x-2025-10-01-sutton-podcast]], posted the same day.

## Summary
He writes up his reaction to the Dwarkesh podcast with Richard Sutton, whose "The Bitter Lesson" he says has become near-biblical among frontier LLM researchers, and whom he reports as doubting that LLMs are bitter-lesson pilled because they train on human, finite data (§intro). He summarises Sutton's alternative, a child machine that learns only by interacting with the world through reinforcement learning, with intrinsic rewards and learning at test time, and no pretraining or supervised finetuning (§intro). He agrees with Sutton that frontier LLMs carry human input at every stage and that no clean "turn the crank" algorithm exists, and that animals do not do supervised learning (§intro, §Appendix). He disagrees that the two usual existence proofs carry over: Go is a simple closed environment, and animal brains are not blank slates, since much "learning" is maturation or finetuning on an initialization evolution encoded in DNA (§intro). So pretraining is "our crappy evolution", one practical answer to the cold-start problem, followed by RL finetuning; LLM research summons ghosts, statistical distillations of human documents, which may move toward animals or stay different, like planes and birds (§intro). The Appendix adds that in-context learning and memory files are test-time learning, and that he does not find Sutton's temporal-difference answer to long-horizon sparse rewards compelling (§Appendix).

## Key points
- Sutton's position, as he reports it: LLMs trained on human, finite data are not bitter-lesson pilled; learn from experience by RL like an animal → [[bitter-lesson]]
- He agrees frontier LLMs are not cleanly bitter-lesson pilled; the bitter lesson is correct but platonic, perhaps practically met → [[frontier-llms-are-not-platonically-bitter-lesson-pilled]]
- Animal brains are no blank slate: maturation plus finetuning on an evolved initialization; Go is closed and simple → [[bitter-lesson]]
- Pretraining as a crappy evolution, a candidate solution to cold start, then RL → [[pretraining-is-our-crappy-evolution]], [[pretraining-and-finetuning]]
- Frontier research summons ghosts, not animals; ghosts:animals :: planes:birds → [[llm-research-summons-ghosts-not-animals]], [[jagged-intelligence]]
- Animals do not do supervised learning; the human analogue is RL with an example in context → [[bitter-lesson]]
- Ideas to borrow from animals: intrinsic motivation, curiosity, empowerment, multi-agent self-play, culture; TD learning not compelling for long-horizon rewards → [[llm-self-improvement]]
- In-context learning and memory files as test-time learning → [[prompting-llms]], [[llm-knowledge-bases]]
- Researchers assume LLMs are bitter-lesson pilled because of scaling laws → [[scaling-laws]]

## Fed pages
- [[bitter-lesson]]
- [[frontier-llms-are-not-platonically-bitter-lesson-pilled]]
- [[pretraining-is-our-crappy-evolution]]
- [[llm-research-summons-ghosts-not-animals]]
- [[pretraining-and-finetuning]]
- [[jagged-intelligence]]
- [[llm-self-improvement]]
- [[prompting-llms]]
- [[llm-knowledge-bases]]
- [[scaling-laws]]
- [[rl-sucks-supervision-bits-through-a-straw]]
- [[llms-are-shaped-by-commercial-not-biological-evolution]]
