---
type: artifact
repo_url: https://github.com/karpathy/llm-council
language: Python, JavaScript
status: active
sources: ["[[github-2025-11-22-llm-council-readme]]", "[[blog-2025-12-19-year-in-review-2025]]", "[[youtube-2025-02-27-how-i-use-llms]]"]
aliases: [LLM Council]
---
# llm-council
His simple local web app that looks like ChatGPT but sends a query through OpenRouter to several LLMs, has them review and rank each other's work, and has a Chairman LLM produce the final response; instead of asking one provider, he says, "you can group them into your “LLM Council”" ([[github-2025-11-22-llm-council-readme]] §intro).

## What it demonstrates
- **Stage 1, first opinions.** Each LLM answers the query separately, and the answers appear in a tab view for inspection one by one ([[github-2025-11-22-llm-council-readme]] §intro).
- **Stage 2, review.** Each LLM is given the others' responses with identities anonymised, "so that the LLM can't play favorites when judging their outputs", and ranks them on accuracy and insight ([[github-2025-11-22-llm-council-readme]] §intro).
- **Stage 3, final response.** The Chairman compiles all responses into one final answer for the user ([[github-2025-11-22-llm-council-readme]] §intro).
- **Why he built it.** It was 99% vibe coded as a fun Saturday hack because he wanted to explore and evaluate a number of LLMs side by side while reading books together with LLMs; see [[read-with-an-llm]] ([[github-2025-11-22-llm-council-readme]] §Vibe Code Alert). He finds it nice and useful to see multiple responses side by side, and the LLMs' cross-opinions of each other's outputs; the README does not say the council's answer beats a single model's ([[github-2025-11-22-llm-council-readme]] §Vibe Code Alert).
- **Unsupported.** He will not support it, provides it as is for inspiration and does not intend to improve it, repeating that code is ephemeral now and libraries are over; see [[code-is-ephemeral-now-and-libraries-are-over]] ([[github-2025-11-22-llm-council-readme]] §Vibe Code Alert).
- **Setup.** It needs an OpenRouter API key with purchased credits; the default council is `openai/gpt-5.1`, `google/gemini-3-pro-preview`, `anthropic/claude-sonnet-4.5` and `x-ai/grok-4`, with `google/gemini-3-pro-preview` as Chairman, editable in `backend/config.py` ([[github-2025-11-22-llm-council-readme]] §Setup).
- **Stack.** FastAPI with async httpx and the OpenRouter API on the backend, React with Vite and react-markdown on the frontend, conversations stored as JSON files, managed with uv and npm ([[github-2025-11-22-llm-council-readme]] §Tech Stack).
- **Note:** on 2025-02-27 he described paying for several providers, asking them all the same question and calling them his "llm Council"; the README does not mention that video, and the app automates the asking and adds peer review and a Chairman ([[youtube-2025-02-27-how-i-use-llms]] @21:48, @22:22; [[github-2025-11-22-llm-council-readme]] §intro). The habit is step 6 of [[choose-a-model-tier]] ([[youtube-2025-02-27-how-i-use-llms]] @22:22).
- **Note:** the 2025-12-19 review lists llm-council among projects he vibe coded as quick app demos of something he wanted to exist; dates only ([[blog-2025-12-19-year-in-review-2025]] §5; [[github-2025-11-22-llm-council-readme]] §Vibe Code Alert).
- **Note:** `status: active` because nothing marks it deprecated, despite the support disclaimer, as for [[rendergit]] and [[reader3]]; `language` follows the README's stack, Python 3.10+ with FastAPI and JavaScript with React ([[github-2025-11-22-llm-council-readme]] §Tech Stack).

## Related
- [[choose-a-model-tier]] — the ask-several-models habit it automates
- [[read-with-an-llm]] — what he was doing when he built it
- [[vibe-coding]] — how he built it
- [[reader3]] — the companion reading tool
