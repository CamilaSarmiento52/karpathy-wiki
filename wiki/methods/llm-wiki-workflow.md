---
type: method
steps:
  - Collect sources into raw/
  - Have the LLM compile a linked markdown wiki
  - Browse it in Obsidian; let the LLM own the edits
  - Ask complex questions against the wiki
  - Render answers as files and file them back in
  - Run LLM health checks to clean and extend it
  - Keep a schema document the LLM follows
  - Ingest one source at a time, logging each
  - Add proper search as the wiki grows
sources: ["[[x-2026-04-02-llm-knowledge-bases]]", "[[github-2026-04-04-llm-wiki-gist]]"]
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
7. **Schema.** The gist (2026-04-04) adds a schema document, for example CLAUDE.md or AGENTS.md, that tells the LLM the wiki's structure, conventions and workflows; you and the LLM co-evolve it ([[github-2026-04-04-llm-wiki-gist]] §Architecture).
8. **Ingest one at a time, and log it.** In the gist's example flow the LLM reads the source, discusses key takeaways with you, writes a summary page, updates the index and the relevant pages, and appends to the log; "A single source might touch 10-15 wiki pages.", an illustrative figure ([[github-2026-04-04-llm-wiki-gist]] §Operations). He prefers one source at a time, staying involved, though batch ingest with less supervision is possible ([[github-2026-04-04-llm-wiki-gist]] §Operations). Queries read `index.md` first and answer with citations; each log entry starts with a consistent prefix so unix tools can parse it ([[github-2026-04-04-llm-wiki-gist]] §Operations, §Indexing and logging). The gist's lint list adds stale claims superseded by newer sources, orphan pages and concepts lacking a page ([[github-2026-04-04-llm-wiki-gist]] §Operations).
9. **Search when it grows.** The index file is enough at small scale; as the wiki grows he suggests proper search, such as tobi's qmd, or a naive search script vibe-coded with the LLM ([[github-2026-04-04-llm-wiki-gist]] §Optional: CLI tools).

## Seen in
- [[x-2026-04-02-llm-knowledge-bases]]
- [[github-2026-04-04-llm-wiki-gist]]
- [[llm-knowledge-bases]]
