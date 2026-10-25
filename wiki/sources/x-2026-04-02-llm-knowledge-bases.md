---
type: source
raw_path: raw/x/2039805659525644595.md
published: 2026-04-02
medium: x
summary: Describes his workflow of having an LLM compile raw sources into an Obsidian markdown wiki that it queries, lints and grows, without RAG.
url: https://x.com/karpathy/status/2039805659525644595
title: LLM Knowledge Bases
---
# LLM Knowledge Bases
Raw: [[raw/x/2039805659525644595]] · Original: https://x.com/karpathy/status/2039805659525644595

The pattern this project is built on.

## Summary
A long X post in labelled sections. Sources go into `raw/`, and an LLM incrementally
compiles a linked `.md` wiki of summaries and concept articles (§Data ingest). Obsidian is
the frontend; the LLM writes the wiki and he rarely touches it (§IDE). At about 100 articles
he queries it without RAG (§Q&A), files outputs back in (§Output), runs LLM health checks
(§Linting), and vibe-coded a small search tool the LLM can call (§Extra tools). He suggests
finetuning as a next step and a product opportunity (§Further explorations, §TLDR).

## Key points
- The workflow itself → [[llm-knowledge-bases]], [[llm-wiki-workflow]]
- No RAG at small scale → [[no-rag-needed-for-a-small-wiki]]
- Output as markdown, slides and plots rather than terminal text → [[llm-gui]]
- A vibe-coded search engine → [[vibe-coding]], [[vibe-coding-over-time]]
- Tools handed to the LLM via CLI → [[building-for-agents]]

## Fed pages
- [[llm-knowledge-bases]]
- [[llm-wiki-workflow]]
- [[no-rag-needed-for-a-small-wiki]]
- [[llm-gui]]
- [[vibe-coding]]
- [[vibe-coding-over-time]]
- [[building-for-agents]]
- [[a-wiki-compounds-where-rag-rediscovers]]
- [[an-index-file-avoids-rag-at-moderate-scale]]
