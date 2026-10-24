# Digest brief (batches 2–4)

You are a DIGEST step for an LLM-compiled wiki about Andrej Karpathy, in
`/Users/camilasarmiento/Documents/AI os/karpathy-wiki`. You are read-only on `wiki/` and
`raw/`. You write only the digest files your prompt names, under `staging/digests/`.

## Read first, in this order

1. `CLAUDE.md`: page types, citation rules, quote rules (one sentence, under 15 words,
   verbatim), invariants 6–9.
2. `staging/README.md`: the digest format. Follow it exactly.
3. The index: `wiki/index/topics.md`, `claims.md`, `methods.md`, `artifacts.md` and
   `sources.md` list every existing page (since 2026-10-24 the index is split by type;
   `wiki/index.md` only links these files). **The wiki already has 182 pages** from batches
   1–2 (2022–mid 2024 lectures, talks, llm.c) and phase 1 (2025–2026 posts and talks). Reuse an
   existing slug whenever the idea is the same; check `aliases` by opening the page.
   Common ones: backpropagation, tokenization, self-attention, transformer-architecture,
   pretraining-and-finetuning, nanogpt, mingpt, micrograd, makemore, gradient-descent,
   pytorch, training-diagnostics, spelled-out-build-from-scratch,
   small-hackable-educational-code, software-3-0, llms-as-operating-systems,
   jagged-intelligence, rlvr, building-for-agents, partial-autonomy-apps, vibe-coding,
   prompting-llms, llm-tool-use, scaling-laws, system-1-and-system-2-thinking,
   llm-self-improvement, llm-security, sampling-from-language-models, ai-ecosystem,
   compute-efficiency, llm-evaluation, nanochat, llm-c, minbpe, build-nanogpt,
   nn-zero-to-hero, make-it-work-then-make-it-cheap, build-and-publish-projects,
   verify-against-a-reference-implementation, reproduce-a-published-model. Timelines:
   vibe-coding-over-time, llm-agents-over-time, llm-os-over-time.
4. `staging/batch-1-merge-map.md` and `staging/batch-2-merge-map.md`: how earlier
   batches chose page granularity. Prefer coarse
   topics: a sub-step of an idea is a section of that idea's page, not a new page.
5. Your raw file(s), **in full**. Read long files in chunks with Read offset/limit. Do not
   skim and do not stop before the end.

## What to extract

- **Source page**: the complete, copy-ready `wiki/sources/<slug>.md` (CLAUDE.md §4), with
  `## Fed pages` listing your candidate slugs. Quote the YAML `summary` if it contains `: `.
- **Candidates**: topics he explains (not just mentions), claims (positions he takes),
  artifacts (repos), methods (how he builds, debugs, explains, evaluates). For each:
  existing yes/no, aliases, statements with `@mm:ss` / `@h:mm:ss` or `§heading`, and for
  claims a title no stronger than his words, `confidence`, and a verbatim quote.
- **Relations to existing claims**: this batch is where later views meet earlier ones. For
  each claim candidate, say whether it `supports`, `extends` or `contradicts` an existing
  claim page, and why, citing both sides. `contradicts` only if both cannot be true.
  Say "none" when there is none; do not force links.
- **Quotes**: 8–15 per long source, fewer for short ones. Copy verbatim from the raw so a
  string match finds them (captions may be lowercase or garbled; copy as they are, but
  prefer quotes without garbled words). Grep each one before you write it down.
- **Notes for merge**: caption misspellings, mentions without explanation, numbers that
  look garbled, anything a reviewer should know.

## Rules

- Paraphrase no stronger than what he says. No facts from your own knowledge.
- Dates are published dates (CLAUDE.md §2). Do not write intervals or order between
  sources ("a year later", "first said"); if he gives a date himself, quote his words.
- **Talks and podcasts include other speakers.** Attribute only what he says. Mark any
  statement where the speaker is unclear. Never quote the host as him.
- A paper's or another person's position that he reports is theirs, not his.
- Text sources cite `§<heading>` (`§intro` for text before the first heading); videos and
  talks cite the `[mm:ss]` / `[h:mm:ss]` marker of the 30-second block.

## Report back

In under 150 words: file path(s), candidate counts by type, which existing slugs you
reused, any relation to an existing claim, anything surprising.
