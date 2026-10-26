# Digest: llm-council README
- raw: raw/github/karpathy__llm-council.md · published: 2025-11-22 · medium: github · words: 489 (frontmatter); 512 by wc
- source slug: github-2025-11-22-llm-council-readme
- commit: 92e1fccb1bdcf1bab7221aa9ed90f9dc72529131

Locations: `§intro` (text under `# LLM Council`, including the three stages), `§Vibe Code Alert`, `§Setup`, `§Running the Application`, `§Tech Stack`.

## Source page
```
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

Dated by the README's commit (92e1fcc).

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
```

## Candidates

### artifact: llm-council
- existing: no as an artifact. **Careful:** "LLM council" is already an alias on the method [[choose-a-model-tier]] (from his 2025-02-27 "llm Council" phrase). Slugs are unique, so `llm-council` as an artifact slug is free, but merge should consider moving the alias or leaving it on the method and not on the artifact, to avoid two pages answering to the same name. Suggest artifact aliases: [LLM Council].
- frontmatter: repo_url https://github.com/karpathy/llm-council · language: Python and JavaScript (README §Tech Stack: FastAPI, Python 3.10+; React + Vite) · status: as with rendergit, not deprecated but explicitly unsupported.
- statements:
  - Instead of asking one LLM provider, you group several into your "LLM Council" (§intro).
  - A simple local web app that looks like ChatGPT but uses OpenRouter to send the query to multiple LLMs, asks them to review and rank each other's work, and has a Chairman LLM produce the final response (§intro).
  - Stage 1, first opinions: each LLM answers the query separately; the answers appear in a tab view for inspection (§intro).
  - Stage 2, review: each LLM gets the others' responses, with identities anonymised so it can't play favourites, and ranks them on accuracy and insight (§intro).
  - Stage 3, final response: the Chairman compiles all responses into one final answer (§intro).
  - 99% vibe coded as a fun Saturday hack, to explore and evaluate a number of LLMs side by side while reading books together with LLMs (§Vibe Code Alert).
  - He finds it nice and useful to see multiple responses side by side, and the LLMs' cross-opinions of each other's outputs (§Vibe Code Alert).
  - Not supported, provided as is for inspiration, no plans to improve it (§Vibe Code Alert).
  - Setup needs an OpenRouter API key with purchased credits; default council models are openai/gpt-5.1, google/gemini-3-pro-preview, anthropic/claude-sonnet-4.5 and x-ai/grok-4, with google/gemini-3-pro-preview as Chairman, editable in `backend/config.py` (§Setup).
  - Stack: FastAPI with async httpx and the OpenRouter API; React + Vite with react-markdown; conversations stored as JSON files; uv and npm (§Tech Stack).

### method: choose-a-model-tier (existing; step 6 "Ask a council")
- statement: the app automates asking several LLMs the same question and adds a peer-review and Chairman stage (§intro).
- **Note:** the method's step 6 records that on 2025-02-27 he often paid for several providers, asked them all the same question and called them his "llm Council" (youtube-2025-02-27-how-i-use-llms @21:48, @22:22, per that page). The README does not mention that video. Write it as a connection, dates only.
- The user prompt says the former page "he-asks-several-llms-the-same-question" is now part of choose-a-model-tier; its alias is there. Do not recreate it.

### method: read-with-an-llm (existing)
- statement: he built llm-council because he wanted to compare LLMs side by side while reading books with LLMs, linking his reading post (§Vibe Code Alert).

### method: verify-citations (existing) — checked, no fit
- The README's stage 2 ranks answers "in accuracy and insight" by other LLMs (§intro); it says nothing about citations, primary sources or human checking. Not a source for this method. At most a **Note:** in llm-council's Related; I would not add one.

### topic: vibe-coding (existing) and timeline: vibe-coding-over-time (existing)
- statement: he says llm-council was 99% vibe coded as a fun Saturday hack, and will not support or improve it (§Vibe Code Alert).
- timeline entry: **2025-11-22** — Shares llm-council, 99% vibe coded as a Saturday hack, unsupported; repeats that code is ephemeral now ([[github-2025-11-22-llm-council-readme]] §Vibe Code Alert)

### claim: code-is-ephemeral-now-and-libraries-are-over (proposed in the reader3 digest)
- second location: the same two sentences, "Code is ephemeral now and libraries are over, ask your LLM to change it in whatever way you like." (§Vibe Code Alert). Repeat text, add to `sources` as a second location, not as independent evidence.

## Quotes
- "you can group them into your \"LLM Council\"" (§intro)
- "finally a Chairman LLM produces the final response" (§intro)
- "so that the LLM can't play favorites when judging their outputs" (§intro)
- "The LLM is asked to rank them in accuracy and insight." (§intro)
- "This project was 99% vibe coded as a fun Saturday hack" (§Vibe Code Alert)
- "It's nice and useful to see multiple responses side by side" (§Vibe Code Alert)
- "Code is ephemeral now and libraries are over" (§Vibe Code Alert)

## Notes for merge
- "eg.c" in the provider list is his typo for "etc."; do not quote it.
- The intro lists "OpenAI GPT 5.1, Google Gemini 3.0 Pro, Anthropic Claude Sonnet 4.5, xAI Grok 4" as examples; config strings differ slightly (gemini-3-pro-preview). Use the config strings for defaults.
- The API key in §Setup is a placeholder (`sk-or-v1-...`); do not reproduce it.
- No statement in the README that the council gives better answers than one model; he says only that side-by-side responses are "nice and useful". Do not write a claim stronger than that.
- Year-in-review: the 2025-12-19 review names llm-council among projects he vibe coded as quick app demos (§5). Dates only.
