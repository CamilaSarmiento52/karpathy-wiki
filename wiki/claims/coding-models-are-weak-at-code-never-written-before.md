---
type: claim
stated_on: 2025-10-17
confidence: stated
sources: ["[[talk-2025-10-17-dwarkesh-ghosts-not-animals]]", "[[github-2026-01-03-rustbpe-readme]]"]
context: ["[[blog-2025-12-19-year-in-review-2025]]"]
topic: "[[vibe-coding]]"
---
# Coding models are not very good at code that has never been written before
> "They're not very good at code that has never been written before" — [[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @35:43

## Context
He built nanochat over a bit more than a month, and says it is not an example of where agents help, because it is not boilerplate but "intellectually intense" code in which everything has to be precisely arranged ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @30:43, @31:58). The models kept misunderstanding his code because of their memory of the typical internet way of doing things: he had written his own gradient synchronisation inside the optimizer step, and they kept trying to get him to use PyTorch's DDP container ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @31:58, @32:36, @33:14). They were over-defensive with try-catch statements, tried to make a production codebase, bloated the code and used deprecated APIs; he could clean it up, but "It's just not net useful." ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @33:14). Asked about adding known tweaks such as RoPE, he says the models know but do not fully know how to integrate them into the repo's style and assumptions ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @36:20). He agrees with Dwarkesh that this is relevant to how soon an "AI 2027"-type explosion could happen, Dwarkesh's framing, and says it is why his timelines are a bit longer ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @35:43).

The limit is scoped: agents are pretty good at boilerplate and at things that occur very often on the internet, and they helped him in an unfamiliar language, Rust ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @31:21, @34:26). The rustbpe README, dated 2026-01-03, gives the Rust side in his own disclosure: he wrote the Python reference personally and from scratch and understands it fully, wrote the Rust against it with equality tests, and, not being a Rust developer by background, had significant help from ChatGPT and Claude Code Opus 4.5 ([[github-2026-01-03-rustbpe-readme]] §LLM Assistance note). This is evidence for the scoped part, help in an unfamiliar language, not for the "never written before" half: BPE has been written before, by him ([[github-2026-01-03-rustbpe-readme]] §LLM Assistance note; [[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @34:26). For some questions he pastes his whole repo into GPT-5 Pro and finds it surprisingly good compared with a year before ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @36:20, @36:57).

## Related claims
- **Note:** [[claude-code-is-the-first-convincing-llm-agent]] (2025-12-19) and this claim both hold: an agent can be the first convincing demonstration of what an agent looks like and still be weak off the internet's distribution, and in this interview he calls the early agents he uses daily extremely impressive ([[blog-2025-12-19-year-in-review-2025]] §4; [[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @01:25, @35:43). No relation is set.
- **Note:** the December review's example of vibe coding helping a professional is nanochat's Rust tokenizer, the same place where he says here the models helped ([[blog-2025-12-19-year-in-review-2025]] §5; [[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @34:26).
- **Note:** what he uses instead is [[autocomplete-is-his-coding-sweet-spot]]; the dated sequence is on [[vibe-coding-over-time]] ([[talk-2025-10-17-dwarkesh-ghosts-not-animals]] @37:33).
