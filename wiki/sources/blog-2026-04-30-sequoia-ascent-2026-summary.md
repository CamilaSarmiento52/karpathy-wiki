---
type: source
raw_path: raw/blog/sequoia-ascent-2026.md
published: 2026-04-30
medium: blog
summary: "His post of the Sequoia Ascent 2026 fireside chat: a short intro in his own words on having an LLM write it, then an AI-written first-person summary and an AI-cleaned transcript of the same conversation; only the intro is his."
url: https://karpathy.bearblog.dev/sequoia-ascent-2026/
title: "Sequoia Ascent 2026 summary"
---
# Sequoia Ascent 2026 summary
Raw: [[raw/blog/sequoia-ascent-2026]] · Original: https://karpathy.bearblog.dev/sequoia-ascent-2026/

**Mostly AI-written (CLAUDE.md §3).** Only §intro, about 130 words before the first heading, is his own writing. The first-person summary (§1. to §12. and §The Big Picture, about 2,050 words) and the cleaned transcript (the unnumbered sections under "Sequoia Ascent 2026: Andrej Karpathy in Conversation with Stephanie Zhan", about 3,930 words) were produced by Codex 5.5, which he says he read and found to read ok without glaring mistakes (§intro). The summary's "I" is the model's. Nothing in those parts is cited in this wiki as his view, quote or wording; what he said at the event is cited to the recording, [[talk-2026-04-29-sequoia-ascent-2026]], published 2026-04-29. This post was published 2026-04-30.

## Summary
In §intro he says he did a fireside chat at Sequoia Ascent 2026 and links the video (§intro). As an experiment he fed an LLM all his recent blog posts and tweets, had it read the video's transcript and produce a summary and a cleaned-up transcript, correcting transcription mistakes and removing filler words (§intro). He posts both for people who would rather read than watch, and also for LLMs, "so that my content is legible and available to them" (§intro). He used a top-capability model, Codex 5.5, read the content and says "it reads ok without glaring mistakes" (§intro). The rest of the post is the AI-written text described below.

## What the AI-written parts add or soften
Compared with the recording, these are the model's, not his; none is cited elsewhere in the wiki.
- **Added in the summary, not said at the event:** the year "December 2025" (§1.); the programmer as "an orchestrator of agents" and a list of macro actions (§1.); "less precise, but more adaptive" for the agent-pasted installer (§2.); "Some apps should stop existing as apps." as a founder lesson (§3.); a contrast of the LLM Wiki pattern with RAG (§4.), which is in the llm-wiki gist, not the talk; tasks that are "resettable, repeatable, and rewardable" (§5.); a capability-spike formula and "on the model's rails" (§6.); vibe coding as "fine for prototypes and personal tools" and agentic engineering as "what serious teams need", with a list of agentic-engineer practices (§7.); a hiring checklist (§8.); a "startup wedge" (§9.); a list of agent-native surfaces and definitions of sensors and actuators (§10.); "empirical familiarity" (§11.); microGPT as a single-file teaching artifact (§12.); and all of §The Big Picture.
- **Changed or softened:** the talk's ceiling is "extrapolating" with a very high ceiling (talk @16:22, @16:55), the summary's "Agentic engineering raises the ceiling." (§7.); the summary's "I distinguish two related but different ideas" (§7.) hides that the host said "agentic engineering" first (talk @15:49); the outsourcing line, a tweet by someone else in the talk (@27:55), becomes "a line I keep returning to" (§12.); the list of what LLMs lack, which was the host's question (talk @23:30), is written as his view (§11.).
- **Softened in the cleaned transcript:** "certainly don't excel at understanding" (talk @28:59) becomes "do not fully excel" (§Education and Understanding); "will tell you to walk" (@11:24) becomes "may tell you to walk", and "Opus 4.7" becomes "a state-of-the-art model" (§Verifiability and Jagged Intelligence). It adds an introduction by another speaker not in the video (§Introduction), links, and corrected names such as Claude Code for the caption's "Alpha code" (§The December 2025 Agentic Inflection).
- **Omitted by the summary:** the neural-computers extrapolation (talk @08:07–@09:13), the car-wash example, the council of LLM judges, the setup and plan-mode remarks, the code "heart attack", yelling at models and agent-to-agent meetings; all are in the cleaned transcript.

## Key points
- He has an LLM summarise and clean his talk so his content is legible to LLMs, and reviews it lightly → [[building-for-agents]]

## Fed pages
- [[building-for-agents]]
