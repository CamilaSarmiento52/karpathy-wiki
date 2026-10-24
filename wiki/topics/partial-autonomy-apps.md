---
type: topic
aliases: [Partial autonomy apps, LLM apps, Cursor for X, autonomy slider]
first_seen: 2025-02-27
last_updated: 2025-12-19
sources: ["[[youtube-2025-06-19-software-is-changing]]", "[[blog-2025-12-19-year-in-review-2025]]", "[[youtube-2025-02-27-how-i-use-llms]]"]
context: ["[[talk-2023-05-25-state-of-gpt]]", "[[talk-2024-03-26-sequoia-making-ai-accessible]]"]
related: ["[[llm-gui]]", "[[ai-assisted-coding-loop]]", "[[this-is-the-decade-of-agents]]"]
---
# Partial autonomy apps
His name for LLM products that sit between a traditional interface and a fully autonomous agent, with Cursor and Perplexity as the examples ([[youtube-2025-06-19-software-is-changing]] @18:17, @20:29).

## What he says
He lists four shared properties: the app manages context, orchestrates several LLM calls, provides an application-specific GUI, and offers an autonomy slider ([[youtube-2025-06-19-software-is-changing]] @19:23, @19:56). In Cursor the slider runs from tab completion to whole-repo agent mode ([[youtube-2025-06-19-software-is-changing]] @20:29).

The human verifies what the AI generates, so the product's job is to make that loop fast, by speeding up verification and keeping the AI "on the leash" ([[youtube-2025-06-19-software-is-changing]] @22:09, @22:43). He prefers Iron Man suits over Iron Man robots: augmentations now, with a slider that moves toward autonomy over time ([[youtube-2025-06-19-software-is-changing]] @27:44, @28:17).

His education example separates a course-authoring app from a course-serving app, so the course is an auditable artifact that keeps the AI on a syllabus ([[youtube-2025-06-19-software-is-changing]] @24:56, @25:29).

In December 2025 he repeats the four properties, now calling the first one context engineering, and says LLM apps will turn generally capable models into deployed professionals in specific verticals ([[blog-2025-12-19-year-in-review-2025]] §3).

**Note:** in May 2023, before he used "partial autonomy" or "autonomy slider", he already recommended LLMs as copilots under human oversight rather than autonomous agents, and described advanced prompting as Python glue code stringing many prompts together in a loop ([[talk-2023-05-25-state-of-gpt]] @28:21, @28:54, @39:57). That is background for the 2025 framing, not the same term.

**Note:** in March 2024, again without these terms, he says LLM systems are quite autonomous but not fully, so what oversight and evaluation look like still has to be worked out, over the next few years ([[talk-2024-03-26-sequoia-making-ai-accessible]] @06:20, @06:54). The sequence of his statements on agents is on [[llm-agents-over-time]] ([[talk-2023-05-25-state-of-gpt]] @39:57; [[youtube-2025-06-19-software-is-changing]] @27:09).

**Cursor (How I use LLMs, 2025-02-27).** For professional coding he does not ask a chat web page for snippets, which is too slow and lacks context; he uses an app on his file system, then Cursor, calling Claude 3.7 Sonnet through the API with the context of his files ([[youtube-2025-02-27-how-i-use-llms]] @1:14:07, @1:14:40, @1:15:12, @1:15:47). Its features went from Cmd-K, change this line, to Cmd-L, explain this chunk, to Cmd-I, Composer, which with agent integration is an autonomous agent on the codebase that runs commands and edits multiple files ([[youtube-2025-02-27-how-i-use-llms]] @1:16:51, @1:17:26, @1:18:01). Composer paused and waited for him to confirm commands explicitly ([[youtube-2025-02-27-how-i-use-llms]] @1:20:46). **Note:** these are concrete steps along the autonomy slider described above ([[youtube-2025-02-27-how-i-use-llms]] @1:17:26; [[youtube-2025-06-19-software-is-changing]] @22:43).

## Claims
- [[this-is-the-decade-of-agents]]
- [[use-llms-as-copilots-with-human-oversight]] — the 2023 version of the human-in-the-loop stance
- [[llm-products-will-take-years-to-figure-out]] — the 2024 version: oversight still to be designed

## Related
- [[llm-agents-over-time]] — his statements on agents by date
- [[llm-gui]]
- [[ai-assisted-coding-loop]]
- [[claude-code-is-the-first-convincing-llm-agent]]
