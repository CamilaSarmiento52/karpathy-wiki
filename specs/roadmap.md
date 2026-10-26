# Roadmap

One phase at a time, each on its own branch, each with plan → implement → validate.
Status: ⬜ not started · 🟨 in progress · ✅ done

| # | Phase | Status | Outcome |
|---|---|---|---|
| 1 | [Skeleton and schema](phases/phase-1-skeleton-and-schema/plan.md) | ✅ | Folders, CLAUDE.md, Obsidian config, and five hand-picked sources ingested so the page design can be checked before any pipeline exists |
| 2 | [Collectors and backfill](phases/phase-2-collectors-and-backfill/plan.md) | ✅ | Five idempotent collector scripts with versioned snapshots, manifest, a coverage queue (collected / pending / excluded, seeded from leads in existing sources), parallel backfill from 2023 onward prioritising his teaching material, coverage report |
| 3 | [Compile the wiki](phases/phase-3-compile-the-wiki/plan.md) | 🟨 | Batch ingest of the backfill, first lint, index, hot, log; free questions answered with citations. _All 82 sources compiled, 331 pages, lint 0 (2026-10-25); waiting on the user's gate check_ |
| 4 | [Rules and agent](phases/phase-4-rules-and-agent/plan.md) | 🟨 | Rule extraction with quotes, bench and promotion, karpathy sub-agent, teach and review skills, run-gate hook; validated with the real-task prompts. _Built 2026-10-26: 10 promoted rules + 1 bench, agent, skills, gate, installer; 5 prompts pass; waiting on the user's own run_ |
| 5 | [Keep it alive](phases/phase-5-keep-it-alive/plan.md) | 🟨 | `/karpathy-ingest`, weekday scheduled collection with morning brief, Sunday lint, sub-agent regeneration _Built 2026-10-26: daily runner, brief, `/karpathy-ingest`, weekday and Sunday scheduled tasks; waiting on a real new source for the gate_ |

## Phase gates

- **1 → 2**: the user has looked at the five ingested sources in Obsidian and approved (or
  corrected) the page types, frontmatter and linking. CLAUDE.md reflects the corrections.
- **2 → 3**: manifest counts per source match expectations; ten random raw files spot-checked
  against the originals.
- **3 → 4**: lint reports zero orphans and zero uncited claims; three free questions answered
  with correct citations.
- **4 → 5**: the five phase 4 validation prompts in `tests/prompts.md` pass (the sixth,
  Learning, needs `/karpathy-ingest` and moves to the 5 → done gate; approved 2026-10-26).
- **5 → done**: one real new post ingested end to end via the scheduled run, brief received,
  a bench rule promoted; the Learning prompt in `tests/prompts.md` passes. (Phase 5 decision 7,
  approved 2026-10-26: the promotion is proven on a fixture, since the only bench
  rule is inferred and cannot be promoted unless a new source states it directly.)

## Known gaps (from the phase 1 review, 2026-10-20)

- **Five sources are a pilot, not a corpus.** Coverage is concentrated on AI-assisted
  software and product ideas; there is almost no direct teaching evidence (tokenization,
  backprop, model code, training diagnostics). Phase 2 must prioritise his lectures and
  teaching repos.
- **The seven teaching rules in DESIGN.md are hypotheses.** They stay hypotheses until
  phase 4 finds quotes in independent sources; several paraphrases of one talk do not count
  as two sources.
- **This repo's choices are not his.** His post supports raw → compiled wiki → queries →
  health checks; the exact schema, page types and immutability policy here are ours.

## Later (not scheduled)

- A visual, beginner-friendly explorer of the wiki (an HTML page built from it), for
  sharing what the wiki contains with an audience.

- Backfill pre-2023 material (Zero to Hero lectures, older blog posts).
- Pre-commit review hook for client repos, calling `/karpathy-review --staged`.
- Reuse the schema for a second expert brain.
