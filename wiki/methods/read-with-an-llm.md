---
type: method
steps:
  - Get the raw text of the paper or chapter
  - Paste or upload it into the context window
  - Ask for a summary first
  - Read and ask questions as you go
  - Ask for a conceptual diagram of the chapter
sources: ["[[youtube-2025-02-27-how-i-use-llms]]", "[[github-2025-11-18-reader3-readme]]", "[[x-2025-11-18-reading-with-llms]]", "[[github-2025-11-22-llm-council-readme]]"]
aliases: [reading papers with an LLM, reading books with an LLM, don't read books alone, file uploads, read everything with LLMs, three-pass reading]
---
# Read with an LLM
How he reads papers and books: he says it is rarely the case any more that he reads books by himself; he always involves an LLM ([[youtube-2025-02-27-how-i-use-llms]] @54:30, @55:03). His advice is "don't read books alone" ([[youtube-2025-02-27-how-i-use-llms]] @58:28).

## Steps
1. **Get the raw text.** For The Wealth of Nations, from 1776, he gets the chapter from Project Gutenberg, because the model probably does not remember the chapter exactly ([[youtube-2025-02-27-how-i-use-llms]] @55:37, @56:13, @56:47).
2. **Put it in the context.** He uploads a paper such as the Evo 2 paper as a file, or copies the chapter into Claude; he thinks an uploaded PDF is probably converted to text and its images may be discarded, but is not sure ([[youtube-2025-02-27-how-i-use-llms]] @52:18, @52:50, @53:22, @55:37).
3. **Summary first.** He starts by asking for a summary ([[youtube-2025-02-27-how-i-use-llms]] @53:22, @57:22).
4. **Read and ask.** Then he reads, asking questions as he goes, which he finds helps most with other fields or old texts ([[youtube-2025-02-27-how-i-use-llms]] @54:30, @57:22, @57:55). The copy-paste back and forth is clunky; he knows of no tool that lets him highlight a passage and ask about it ([[youtube-2025-02-27-how-i-use-llms]] @58:28).
5. **Diagram it.** He asks Claude for a conceptual diagram of a chapter, which it draws with the Mermaid library, because as a visual thinker he likes to see how an argument is laid out as a tree ([[youtube-2025-02-27-how-i-use-llms]] @1:11:53, @1:12:26, @1:13:33).

He also uses NotebookLM to turn uploaded sources into an on-demand podcast on niche topics for walks or drives; the podcast hosts are AI-generated voices, not his ([[youtube-2025-02-27-how-i-use-llms]] @1:37:06, @1:38:12, @1:38:46).

**A three-pass variant (X, 2025-11-18).** He says he is getting into a habit of reading everything, blogs, articles and book chapters, with LLMs, and that it is growing to be among his top use cases ([[x-2025-11-18-reading-with-llms]] #1). Usually pass 1 is manual, pass 2 "explain/summarize" and pass 3 Q&A, and he usually ends up with a better, deeper understanding than if he had moved on ([[x-2025-11-18-reading-with-llms]] #1). **Note:** the steps above, from 2025-02-27, put the summary first and then reading with questions; the 2025-11-18 post puts a manual read first. Both are his "usually", given with their dates as variants, not a change of mind ([[youtube-2025-02-27-how-i-use-llms]] @53:22, @57:22; [[x-2025-11-18-reading-with-llms]] #1).

His [[reader3]] (README dated 2025-11-18) exists for the paste step: a self-hosted EPUB reader that shows one chapter at a time so its text is easy to copy into an LLM and read along; he 90% vibe coded it to illustrate how easily one can read books together with LLMs ([[github-2025-11-18-reader3-readme]] §intro). **Note:** step 4 records that on 2025-02-27 he found the copy-paste back and forth clunky and knew of no tool for it; reader3 is his own tool for pasting a chapter, and it adds no highlight-and-ask ([[youtube-2025-02-27-how-i-use-llms]] @58:28; [[github-2025-11-18-reader3-readme]] §intro).

He built [[llm-council]] (README dated 2025-11-22) because he wanted to explore and evaluate several LLMs side by side while reading books together with LLMs ([[github-2025-11-22-llm-council-readme]] §Vibe Code Alert).

## Seen in
- [[youtube-2025-02-27-how-i-use-llms]]
- [[parameters-are-vague-recollection-context-is-working-memory]] — **Note:** why pasting the text beats the model's memory
- [[llm-gui]] — the diagrams
- [[reader3]] — his chapter-at-a-time EPUB reader for pasting into an LLM
- [[llm-council]] — several LLMs side by side while reading
