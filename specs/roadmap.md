# Roadmap

One phase at a time, each on its own branch, each with plan → implement → validate.
Status: ⬜ not started · 🟨 in progress · ✅ done

| # | Phase | Status | Outcome |
|---|---|---|---|
| 1 | [Skeleton and schema](phases/phase-1-skeleton-and-schema/plan.md) | 🟨 | Folders, CLAUDE.md, Obsidian config, and five hand-picked sources ingested so the page design can be checked before any pipeline exists |
| 2 | Collectors and backfill | ⬜ | Five idempotent collector scripts, manifest, parallel backfill from 2023 onward, coverage report |
| 3 | Compile the wiki | ⬜ | Batch ingest of the backfill, first lint, index, hot, log; free questions answered with citations |
| 4 | Rules and agent | ⬜ | Rule extraction with quotes, bench and promotion, karpathy sub-agent, teach and review skills, run-gate hook; validated with the real-task prompts |
| 5 | Keep it alive | ⬜ | `/karpathy-ingest`, weekday scheduled collection with morning brief, Sunday lint, sub-agent regeneration |

## Phase gates

- **1 → 2**: the user has looked at the five ingested sources in Obsidian and approved (or
  corrected) the page types, frontmatter and linking. CLAUDE.md reflects the corrections.
- **2 → 3**: manifest counts per source match expectations; ten random raw files spot-checked
  against the originals.
- **3 → 4**: lint reports zero orphans and zero uncited claims; three free questions answered
  with correct citations.
- **4 → 5**: all six validation prompts in `tests/prompts.md` pass.
- **5 → done**: one real new post ingested end to end via the scheduled run, brief received,
  a bench rule promoted.

## Later (not scheduled)

- Backfill pre-2023 material (Zero to Hero lectures, older blog posts).
- Pre-commit review hook for client repos, calling `/karpathy-review --staged`.
- Reuse the schema for a second expert brain.
