# Phase 1 — Skeleton and schema: plan

## Goal

Stand up the folder structure and the constitution (`CLAUDE.md`), then ingest five
hand-picked sources by hand so the page design can be seen in Obsidian and corrected
before any collector code exists.

## What this phase builds

1. **Folders**: `raw/{youtube,x,github,blog,talks}`, `wiki/{sources,topics,claims,artifacts,timeline,principles,principles/_bench,methods,syntheses}`, `.claude/{agents,skills,hooks}`, `scripts/`, `tests/`.
2. **CLAUDE.md**: page types and required frontmatter, link rules, the invariants, and
   step-by-step procedures for ingest, query and lint (as prompts the LLM follows).
3. **Obsidian config**: `.obsidian/` with graph colours by folder, wikilinks on, new notes
   in `wiki/syntheses`.
4. **wiki/index.md, hot.md, log.md** with their fixed structure.
5. **Five hand-picked sources in raw/** (fetched manually, one per medium where possible):
   - one YouTube lecture or talk transcript (2023 or later)
   - two X threads on different topics
   - one GitHub README (nanochat or llm.c)
   - one blog post or essay
   Each gets the standard raw frontmatter and a manifest entry written by hand.
6. **First ingest**, run by Claude Code following CLAUDE.md, producing source pages and the
   first topic, claim, artifact and method pages with links.
7. `.gitignore`, `.env.example`, README.

## Approach

- Write CLAUDE.md first and treat it as the spec for the ingest; do not special-case the
  five sources.
- Pick sources that overlap in topic so the ingest has to create cross-links (for example
  a talk and an X thread that both discuss the same idea).
- After ingest, open the vault in Obsidian and review together: do the page types make
  sense, is the frontmatter useful, do the links go where a reader expects.
- Corrections go into CLAUDE.md, then re-run ingest on the same five sources until the
  output is right. The schema is the deliverable; the five pages are the test.

## Out of scope

Collector scripts, the agent, skills, hooks, scheduling, rule extraction. The
`principles/` folders exist but stay empty.
