---
type: method
steps:
  - Collect sources into raw/
  - Have the LLM compile a linked markdown wiki
  - Browse it in Obsidian; let the LLM own the edits
  - Ask complex questions against the wiki
  - Render answers as files and file them back in
  - Run LLM health checks to clean and extend it
sources: ["[[x-2026-04-02-llm-knowledge-bases]]"]
aliases: [LLM Wiki pattern]
---
# LLM wiki workflow
The steps of his knowledge-base practice, and the pattern this project follows ([[x-2026-04-02-llm-knowledge-bases]] §TLDR).

## Steps
1. **Collect.** Index articles, papers, repos, datasets and images into `raw/`, using Obsidian Web Clipper for web pages ([[x-2026-04-02-llm-knowledge-bases]] §Data ingest).
2. **Compile.** The LLM writes summaries, backlinks and concept articles ([[x-2026-04-02-llm-knowledge-bases]] §Data ingest).
3. **Browse.** Obsidian is the frontend; the LLM maintains the data ([[x-2026-04-02-llm-knowledge-bases]] §IDE).
4. **Ask.** Query the wiki directly once it is big enough ([[x-2026-04-02-llm-knowledge-bases]] §Q&A).
5. **File back.** Render answers as markdown, slides or plots and add them to the wiki ([[x-2026-04-02-llm-knowledge-bases]] §Output).
6. **Lint.** Health checks find inconsistencies, fill gaps and suggest new articles ([[x-2026-04-02-llm-knowledge-bases]] §Linting).

## Seen in
- [[x-2026-04-02-llm-knowledge-bases]]
- [[llm-knowledge-bases]]
