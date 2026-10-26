---
type: source
raw_path: raw/github/karpathy__gist-442a6bf555914893e9891c11519de94f.md
published: 2026-04-04
medium: github
summary: "His 'idea file' for the LLM wiki pattern, written to be pasted to an LLM agent: raw sources, an LLM-owned wiki and a schema document, with ingest, query and lint operations, index and log files, and why LLMs make the maintenance cheap."
url: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
title: llm-wiki
---
# llm-wiki
Raw: [[raw/github/karpathy__gist-442a6bf555914893e9891c11519de94f]] · Original: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

Dated by the gist's commit `ac46de1`. This is the idea file behind the pattern this wiki follows, but this wiki's own conventions (its CLAUDE.md, claim and timeline pages, quote and citation rules, split index, hot file, manifest) are this project's choices, not his; nothing here says he prescribes them. The gist's page kinds are summaries, entity pages, concept pages, comparisons, an overview and a synthesis (§Architecture). Its `CLAUDE.md` is an example file name for a schema, not a reference to this repo (§Architecture), and its example log line dated 2026-04-02 is illustrative, not a date for anything (§Indexing and logging).

## Summary
He calls this an idea file, meant to be pasted to your own LLM agent, which then builds the specifics with you (§intro). The core idea contrasts RAG, where the LLM rediscovers knowledge on every question, with an LLM that incrementally builds and maintains a persistent, interlinked markdown wiki that compounds as sources and questions are added (§The core idea). There are three layers, immutable raw sources, an LLM-owned wiki and a schema document, and three operations, ingest, query and lint, supported by a content index and a chronological log (§Architecture, §Operations, §Indexing and logging). He suggests search tools for when the wiki grows and Obsidian tips, and argues the pattern works because LLMs make the bookkeeping that makes humans abandon wikis nearly free, relating it to Vannevar Bush's Memex (§Optional: CLI tools, §Tips and tricks, §Why this works). He closes by saying the document is deliberately abstract and everything in it optional (§Note).

## What it adds to the 2026-04-02 post
Compared with [[x-2026-04-02-llm-knowledge-bases]] (published 2026-04-02), the gist (published 2026-04-04) adds: the idea-file form, abstract and optional, for an agent to instantiate (§intro, §Note); an argued contrast with RAG (§The core idea); a stated scale for the index, "~100 sources, ~hundreds of pages", where the post reported his own wiki of about 100 articles (§Indexing and logging); a schema layer (§Architecture); an example ingest flow and his preference to ingest one source at a time and stay involved (§Operations); a longer lint list with stale claims, orphan pages and missing concept pages (§Operations); a specified `index.md` and append-only `log.md` (§Indexing and logging); a recommendation of someone else's search tool, qmd, in place of a report of his own engine (§Optional: CLI tools); an image-reading caveat, graph view, Dataview and git tips (§Tips and tricks); an argument for why it works and the Memex comparison (§Why this works); and a list of use cases (§The core idea). The post's finetuning idea, product remark, token-use shift and his own wiki's size are not mentioned in the gist; that absence is not a withdrawal ([[x-2026-04-02-llm-knowledge-bases]] §Further explorations, §TLDR).

## Key points
- The pattern: three layers, ingest/query/lint, compounding instead of re-deriving → [[llm-knowledge-bases]]
- The workflow, with a schema, one-at-a-time ingest, index and log → [[llm-wiki-workflow]]
- RAG rediscovers; the wiki accumulates → [[a-wiki-compounds-where-rag-rediscovers]]
- An index file is enough at moderate scale; search as it grows → [[an-index-file-avoids-rag-at-moderate-scale]], [[no-rag-needed-for-a-small-wiki]]
- LLMs make wiki maintenance nearly free → [[llms-make-wiki-maintenance-nearly-free]]
- An idea file to paste to your agent, which builds the rest → [[building-for-agents]]

## Fed pages
- [[llm-knowledge-bases]]
- [[llm-wiki-workflow]]
- [[a-wiki-compounds-where-rag-rediscovers]]
- [[an-index-file-avoids-rag-at-moderate-scale]]
- [[no-rag-needed-for-a-small-wiki]]
- [[llms-make-wiki-maintenance-nearly-free]]
- [[building-for-agents]]
