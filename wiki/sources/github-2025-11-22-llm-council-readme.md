---
type: source
raw_path: raw/github/karpathy__llm-council.md
published: 2025-11-22
medium: github
summary: "README of llm-council, his vibe-coded local web app that sends one question to several LLMs, has them anonymously review and rank each other, and has a Chairman model write the final answer."
url: https://github.com/karpathy/llm-council
title: llm-council README
---
# llm-council README
Raw: [[raw/github/karpathy__llm-council]] · Original: https://github.com/karpathy/llm-council

Dated by the README's commit (92e1fcc). It links his reading post, [[x-2025-11-18-reading-with-llms]].

## Summary
Instead of asking one provider, the repo groups several LLMs into an "LLM Council": a local web app that looks like ChatGPT but sends the query through OpenRouter to multiple models (§intro). In stage 1 each model answers separately and the answers are shown in tabs; in stage 2 each model sees the others' answers, with identities anonymised so it cannot play favourites, and ranks them for accuracy and insight; in stage 3 a Chairman model compiles a single final answer (§intro). He says it was 99% vibe coded as a Saturday hack, because he wanted to compare LLMs side by side while reading books with LLMs, and that seeing the responses and the models' cross-opinions side by side is useful (§Vibe Code Alert). He will not support or improve it, and repeats that code is ephemeral now and libraries are over (§Vibe Code Alert). The default council is GPT-5.1, Gemini 3 Pro preview, Claude Sonnet 4.5 and Grok 4, with Gemini as Chairman; the stack is FastAPI and React with JSON storage (§Setup, §Tech Stack).

## Key points
- Three stages: first opinions, anonymised peer review, Chairman's answer → [[llm-council]]
- Asking several LLMs the same question, built into an app → [[choose-a-model-tier]]
- Built for comparing models while reading books with LLMs → [[read-with-an-llm]]
- 99% vibe coded; code is ephemeral, libraries are over → [[vibe-coding]], [[vibe-coding-over-time]], [[code-is-ephemeral-now-and-libraries-are-over]]

## Fed pages
- [[llm-council]]
- [[choose-a-model-tier]]
- [[read-with-an-llm]]
- [[vibe-coding]]
- [[vibe-coding-over-time]]
- [[code-is-ephemeral-now-and-libraries-are-over]]
