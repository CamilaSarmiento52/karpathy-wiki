---
type: source
raw_path: raw/youtube/EWvNQjAaOHw.md
published: 2025-02-27
medium: youtube
summary: "A practical, general-audience tour of LLM apps as he uses them: the chat as a token window, model tiers, thinking models, search, deep research, file uploads, the Python interpreter, Claude artifacts, Cursor, voice, images, video, memory, custom instructions and custom GPTs."
url: https://www.youtube.com/watch?v=EWvNQjAaOHw
title: "How I use LLMs"
---
# How I use LLMs
Raw: [[raw/youtube/EWvNQjAaOHw]] · Original: https://www.youtube.com/watch?v=EWvNQjAaOHw

## Summary
A follow-up in his general-audience series to [[youtube-2025-02-05-deep-dive-into-llms]] that moves from how LLMs are trained to how he uses the apps, with examples from his own life (@00:00). He describes the ecosystem of ChatGPT and its competitors, then frames a chat as user and model writing into one token sequence, the context window, which "new chat" wipes, and the model itself as a lossy, slightly out-of-date "zip file" of the internet with a post-trained assistant persona (@01:08, @06:15, @06:48, @07:55, @10:41, @12:20). He advises starting a new chat per topic, knowing which model and pricing tier you are on, and trying a non-thinking model before switching to a thinking model for hard math and code (@16:14, @20:07, @29:41). Most of the video tours tools: internet search for recent or niche facts, deep research, file uploads for reading papers and books, the Python interpreter and Advanced Data Analysis, Claude artifacts and diagrams, and Cursor's Composer, where he names vibe coding (@31:20, @39:03, @42:26, @51:13, @55:03, @59:02, @1:04:39, @1:09:07, @1:14:07, @1:18:01). He then covers modalities and quality-of-life features (memory, custom instructions, custom GPTs as saved few-shot prompts), and closes with a summary of what to keep track of across apps (@1:23:04, @1:27:32, @1:40:30, @1:53:21, @1:58:48, @2:07:46). Long stretches are AI-generated voices (ChatGPT's advanced voice, Grok, NotebookLM's podcast hosts), not him. Throughout he cautions that outputs can be hallucinated and should be checked against sources, citations and code (@13:58, @48:26, @1:06:19).

## Key points
- A rich ecosystem of ChatGPT-like apps; ChatGPT is the incumbent and most feature-rich; leaderboards help track them → [[ai-ecosystem]], [[choose-a-model-tier]]
- A chat is a one-dimensional token sequence both sides write into; the context window is working memory → [[tokenization]], [[start-a-new-chat-per-topic]]
- The model is a lossy zip file of the internet with an assistant persona from post-training, and a knowledge cutoff → [[pretraining-and-finetuning]]
- Ask it directly only about common, non-recent knowledge, and check primary sources → [[llm-tool-use]], [[verify-citations]]
- Know which model and tier you are using; he asks several LLMs the same question → [[choose-a-model-tier]]
- Thinking models, tuned with RL, help on hard math and code; try a non-thinking model first → [[system-1-and-system-2-thinking]], [[transformers-need-tokens-to-think]], [[choose-a-model-tier]]
- Search for recent, changing or niche information; deep research as a first draft → [[llm-tool-use]], [[verify-citations]], [[use-llms-as-tools-and-check-their-work]]
- Upload papers and book chapters into the context and read them with the LLM → [[read-with-an-llm]]
- The Python interpreter and Advanced Data Analysis act like a junior data analyst whose code you must read → [[llm-tool-use]], [[verify-citations]]
- Claude artifacts write small custom apps and diagrams that render in the chat → [[llm-gui]]
- For professional coding he uses Cursor; Composer is an agent on the codebase, and giving it control is vibe coding → [[partial-autonomy-apps]], [[vibe-coding]]
- Use voice input; about half his queries are spoken → [[voice-input]]
- Audio and images can be tokenized and modelled natively, unlike speech-to-text "fake audio" → [[llm-tool-use]], [[tokenization]]
- Custom GPTs save a few-shot prompt; few-shot examples always increase accuracy in his experience → [[prompting-llms]]

## Fed pages
- [[ai-ecosystem]]
- [[tokenization]]
- [[pretraining-and-finetuning]]
- [[system-1-and-system-2-thinking]]
- [[llm-tool-use]]
- [[prompting-llms]]
- [[partial-autonomy-apps]]
- [[llm-gui]]
- [[vibe-coding]]
- [[choose-a-model-tier]]
- [[start-a-new-chat-per-topic]]
- [[verify-citations]]
- [[read-with-an-llm]]
- [[voice-input]]
- [[use-llms-as-tools-and-check-their-work]]
- [[transformers-need-tokens-to-think]]
