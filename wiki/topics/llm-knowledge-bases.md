---
type: topic
aliases: [LLM Knowledge Bases, LLM Wiki, personal wiki]
first_seen: 2026-04-02
last_updated: 2026-04-29
sources: ["[[x-2026-04-02-llm-knowledge-bases]]", "[[github-2026-04-04-llm-wiki-gist]]", "[[talk-2026-04-29-sequoia-ascent-2026]]"]
context: ["[[youtube-2025-06-19-software-is-changing]]", "[[blog-2025-10-01-animals-vs-ghosts]]", "[[github-2025-12-10-hn-time-capsule-readme]]"]
related: ["[[llm-wiki-workflow]]", "[[no-rag-needed-for-a-small-wiki]]", "[[a-wiki-compounds-where-rag-rediscovers]]", "[[an-index-file-avoids-rag-at-moderate-scale]]", "[[llms-make-wiki-maintenance-nearly-free]]", "[[jagged-intelligence]]"]
---
# LLM knowledge bases
His practice of having an LLM compile research sources into a linked markdown wiki that the LLM maintains and queries, which he says is shifting a large share of his recent token use from code toward knowledge ([[x-2026-04-02-llm-knowledge-bases]]).

## What he says
Sources go into a `raw/` folder and the LLM incrementally compiles a wiki of summaries, backlinks and concept articles ([[x-2026-04-02-llm-knowledge-bases]] §Data ingest). He views it in Obsidian and rarely edits it himself ([[x-2026-04-02-llm-knowledge-bases]] §IDE).

Outputs are filed back into the wiki, so his queries "add up" over time ([[x-2026-04-02-llm-knowledge-bases]] §Output). LLM health checks find inconsistencies and suggest new articles ([[x-2026-04-02-llm-knowledge-bases]] §Linting).

He sees finetuning on the wiki as a natural next step, so the model knows the data in its weights, and thinks there is room for a real product here ([[x-2026-04-02-llm-knowledge-bases]] §Further explorations, §TLDR).

**The idea file (gist, 2026-04-04).** The gist calls the pattern a way of building personal knowledge bases with LLMs and the document an idea file to paste to your own LLM agent, which builds the specifics with you; it is intentionally abstract, and directory structure, conventions, page formats and tooling are all optional ([[github-2026-04-04-llm-wiki-gist]] §intro, §Note). Rather than retrieving from raw documents at query time, the LLM incrementally builds and maintains a persistent wiki between you and the sources, integrating each new source into existing pages so knowledge is compiled once and kept current; see [[a-wiki-compounds-where-rag-rediscovers]] ([[github-2026-04-04-llm-wiki-gist]] §The core idea). You rarely or never write the wiki; you source, explore and ask, and he puts it as "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase." ([[github-2026-04-04-llm-wiki-gist]] §The core idea). He lists uses beyond research: personal tracking, a companion wiki while reading a book, modelled on fan wikis like Tolkien Gateway, a team wiki fed by Slack threads and meetings with humans possibly reviewing, and more ([[github-2026-04-04-llm-wiki-gist]] §The core idea).

The gist names three layers: immutable raw sources as the source of truth, a wiki the LLM owns entirely, and a schema document, such as CLAUDE.md or AGENTS.md, that sets structure, conventions and workflows and that you and the LLM co-evolve ([[github-2026-04-04-llm-wiki-gist]] §Architecture). Its operations are ingest, query and lint, navigated with a content index and an append-only log; at moderate scale the index avoids embedding-based RAG, see [[an-index-file-avoids-rag-at-moderate-scale]] ([[github-2026-04-04-llm-wiki-gist]] §Operations, §Indexing and logging). He argues it works because LLMs make the bookkeeping that makes humans abandon wikis nearly free, and relates it in spirit to Vannevar Bush's Memex; see [[llms-make-wiki-maintenance-nearly-free]] ([[github-2026-04-04-llm-wiki-gist]] §Why this works).

What the gist adds to the post, with both dates: the post (2026-04-02) describes his own practice; the gist (2026-04-04) generalises it into an idea file and adds the RAG argument, a stated scale for the index, the schema layer, his preference to ingest one source at a time, a longer lint list, a specified index and log, a recommended search tool (qmd) in place of his own engine, the why-it-works argument and the Memex comparison ([[x-2026-04-02-llm-knowledge-bases]] §Q&A, §Extra tools; [[github-2026-04-04-llm-wiki-gist]] §Architecture, §Operations, §Optional: CLI tools, §Why this works). The post's finetuning idea, product remark and token-use shift do not appear in the gist; that is absence, not a withdrawal ([[x-2026-04-02-llm-knowledge-bases]] §Further explorations, §TLDR; [[github-2026-04-04-llm-wiki-gist]] §Note).

**Tools for understanding (Sequoia Ascent, 2026-04-29).** He gives his LLM knowledge bases project as information processing that is not even a program: no code could create a knowledge base from a bunch of facts, but LLMs can recompile and reorder documents into a new reframing of the data ([[talk-2026-04-29-sequoia-ascent-2026]] @06:32, @07:04). They excite him as a way to process information, since every different projection onto information gives him insight, "a lot of prompts" for synthetic data generation over fixed data ([[talk-2026-04-29-sequoia-ascent-2026]] @28:27, @28:59). He has a wiki built up from the articles he reads, loves asking it questions, and calls these tools to enhance understanding; see [[understanding-cannot-be-outsourced]] ([[talk-2026-04-29-sequoia-ascent-2026]] @28:59).

**Note:** in the talk published 2025-06-19 he described context windows as working memory that must be programmed directly, because LLMs do not learn on the job; a knowledge base is one way of doing that ([[youtube-2025-06-19-software-is-changing]] @16:38, @17:10; [[x-2026-04-02-llm-knowledge-bases]]).

**Note:** in the Appendix of a post dated 2025-10-01 he says a lot of recent work is interested in memory, "think CLAUDE.md files", as test-time learning with text and context as the substrate instead of weights; he does not mention a wiki there, so the post is background here ([[blog-2025-10-01-animals-vs-ghosts]] §Appendix).

**Note:** the hn-time-capsule README, dated 2025-12-10, says the more general and interesting idea behind that grading pipeline is LLMs automatically scouring past human artifacts and synthesising them into knowledge and insights; it describes a pipeline, not a wiki, so it is background here; see [[hn-time-capsule]] ([[github-2025-12-10-hn-time-capsule-readme]] §What it does).

## Claims
- [[no-rag-needed-for-a-small-wiki]]
- [[a-wiki-compounds-where-rag-rediscovers]] — RAG rediscovers; the wiki accumulates (2026-04-04)
- [[an-index-file-avoids-rag-at-moderate-scale]] — the index suffices at moderate scale; search as it grows (2026-04-04)
- [[llms-make-wiki-maintenance-nearly-free]] — why the wiki stays maintained (2026-04-04)

## Related
- [[llm-wiki-workflow]]
- [[building-for-agents]]
- [[jagged-intelligence]]
- [[hn-time-capsule]] — LLMs synthesising past artifacts into knowledge, as a grading pipeline
