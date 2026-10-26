---
type: claim
stated_on: 2026-04-04
confidence: stated
sources: ["[[github-2026-04-04-llm-wiki-gist]]"]
context: ["[[x-2026-04-02-llm-knowledge-bases]]"]
topic: "[[llm-knowledge-bases]]"
supports: ["[[no-rag-needed-for-a-small-wiki]]"]
---
# An LLM-maintained index works surprisingly well at moderate scale without embedding-based RAG, though a growing wiki wants proper search
> "This works surprisingly well at moderate scale (~100 sources, ~hundreds of pages)" — [[github-2026-04-04-llm-wiki-gist]] §Indexing and logging

## Context
In his pattern, `index.md` is a catalog of every page with a link and a one-line summary, updated by the LLM on every ingest; at query time the LLM reads the index first to find relevant pages, then drills into them ([[github-2026-04-04-llm-wiki-gist]] §Indexing and logging). He says this works surprisingly well at moderate scale, about 100 sources and hundreds of pages, and avoids the need for embedding-based RAG infrastructure; the scale is his estimate, not a measurement ([[github-2026-04-04-llm-wiki-gist]] §Indexing and logging). At small scale the index file is enough, but as the wiki grows "you want proper search", for which he suggests qmd or a vibe-coded naive search script ([[github-2026-04-04-llm-wiki-gist]] §Optional: CLI tools). A wiki might be small enough that the index is all you need ([[github-2026-04-04-llm-wiki-gist]] §Note).

## Related claims
- Supports [[no-rag-needed-for-a-small-wiki]]: in the post published 2026-04-02 his own wiki of about 100 articles and 400K words worked without RAG at a small scale ([[x-2026-04-02-llm-knowledge-bases]] §Q&A); the gist, published 2026-04-04, states the same for the pattern at moderate scale and names the mechanism, reading the index first ([[github-2026-04-04-llm-wiki-gist]] §Indexing and logging). The units differ: articles in the post, sources and pages in the gist. The map sets `supports` as the weakest true link, with no timeline.
