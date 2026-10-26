---
type: claim
stated_on: 2026-04-02
confidence: stated
sources: ["[[x-2026-04-02-llm-knowledge-bases]]", "[[github-2026-04-04-llm-wiki-gist]]"]
topic: "[[llm-knowledge-bases]]"
supports: ["[[an-index-file-avoids-rag-at-moderate-scale]]"]
---
# His ~100-article wiki worked without RAG
> "I thought I had to reach for fancy RAG" — [[x-2026-04-02-llm-knowledge-bases]] §Q&A

## Context
At about 100 articles and 400K words, he says the LLM maintained its own index files and summaries well enough to answer complex questions by reading the relevant pages ([[x-2026-04-02-llm-knowledge-bases]] §Q&A). He limits this to a small scale ([[x-2026-04-02-llm-knowledge-bases]] §Q&A). This is one person's experience with one wiki, not a general result about retrieval ([[x-2026-04-02-llm-knowledge-bases]] §Q&A).

## Related claims
- Supports [[an-index-file-avoids-rag-at-moderate-scale]]: his ~100-article wiki working without RAG at a small scale ([[x-2026-04-02-llm-knowledge-bases]] §Q&A) is one case of what the gist, published 2026-04-04, states for the pattern: reading an LLM-maintained index first works surprisingly well at moderate scale, though a growing wiki wants proper search ([[github-2026-04-04-llm-wiki-gist]] §Indexing and logging, §Optional: CLI tools). Weakest true link per the map; no timeline.
