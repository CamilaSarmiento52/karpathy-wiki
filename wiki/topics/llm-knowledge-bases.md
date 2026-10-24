---
type: topic
aliases: [LLM Knowledge Bases, LLM Wiki, personal wiki]
first_seen: 2026-04-02
last_updated: 2026-04-02
sources: ["[[x-2026-04-02-llm-knowledge-bases]]"]
context: ["[[youtube-2025-06-19-software-is-changing]]"]
related: ["[[llm-wiki-workflow]]", "[[no-rag-needed-for-a-small-wiki]]", "[[jagged-intelligence]]"]
---
# LLM knowledge bases
His practice of having an LLM compile research sources into a linked markdown wiki that the LLM maintains and queries, which he says is shifting a large share of his recent token use from code toward knowledge ([[x-2026-04-02-llm-knowledge-bases]]).

## What he says
Sources go into a `raw/` folder and the LLM incrementally compiles a wiki of summaries, backlinks and concept articles ([[x-2026-04-02-llm-knowledge-bases]] §Data ingest). He views it in Obsidian and rarely edits it himself ([[x-2026-04-02-llm-knowledge-bases]] §IDE).

Outputs are filed back into the wiki, so his queries "add up" over time ([[x-2026-04-02-llm-knowledge-bases]] §Output). LLM health checks find inconsistencies and suggest new articles ([[x-2026-04-02-llm-knowledge-bases]] §Linting).

He sees finetuning on the wiki as a natural next step, so the model knows the data in its weights, and thinks there is room for a real product here ([[x-2026-04-02-llm-knowledge-bases]] §Further explorations, §TLDR).

**Note:** in the talk published 2025-06-19 he described context windows as working memory that must be programmed directly, because LLMs do not learn on the job; a knowledge base is one way of doing that ([[youtube-2025-06-19-software-is-changing]] @16:38, @17:10; [[x-2026-04-02-llm-knowledge-bases]]).

## Claims
- [[no-rag-needed-for-a-small-wiki]]

## Related
- [[llm-wiki-workflow]]
- [[building-for-agents]]
- [[jagged-intelligence]]
