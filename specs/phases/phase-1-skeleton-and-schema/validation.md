# Phase 1 — Skeleton and schema: validation

## Done when

- [x] All folders from the plan exist; `tree -L 2` matches `specs/tech-stack.md`.
- [x] `CLAUDE.md` defines all eight page types with required frontmatter, the invariants,
      and procedures for ingest, query and lint.
- [x] Five raw files exist with complete frontmatter; `_manifest.json` lists them.
- [x] Ingest produced: five source pages (six after the nanoGPT README was added), at least three topic pages, at least one artifact
      page, at least one claim page, at least one method page.
- [x] Every wiki page has valid frontmatter per its type.
- [x] Zero orphan pages (every page has at least one inbound link).
- [x] Every evidence block (paragraph or list item) on topic, claim, artifact, method and
      timeline pages cites a source page; every source page cites its raw path. *(Structural
      lint.)*
- [x] Semantic pass: each cited passage supports its sentence at that strength. *(External
      review 2026-10-20 found 8 problems; all corrected 2026-10-21, see log.md.)*
- [x] At least one cross-link exists between pages that came from different sources.
- [x] `index.md` lists every page by type; `log.md` has one entry per ingested source;
      `hot.md` lists the pages touched.
- [x] Obsidian opens `karpathy-wiki/` as a vault, links resolve, graph shows the pages.
- [x] The user has reviewed the pages in Obsidian and approved the schema, or corrections
      were applied to CLAUDE.md and ingest re-run until approved.
- [x] `raw/` and `.env` are gitignored; `_manifest.json` is committed; repo is public.

## Manual checks

1. Open a topic page, click a cited source, click its raw path: two clicks to his words.
2. Pick a claim, check the date and the quoted sentence exist in the raw file.
3. Open graph view: no isolated nodes.

## Status (2026-10-21, after the review corrections)

- Structural lint: 30 pages, 6 raw files, 0 findings. `pytest tests`: 25 passed.
- Lint now also checks: empty required lists, allowed values, topic dates, body citations
  vs `sources`, Fed pages reciprocity, two-way `contradicts`/`extends` on a timeline,
  quotes verbatim in raw, manifest hashes. Both false negatives from the review are tests.
- `fetch_one.py --restore` rebuilt all six raw files from a manifest-only copy; all
  matched.
- Produced: 6 sources, 9 topics, 6 claims, 2 artifacts, 3 methods, 1 timeline.
- Repo visibility: public.
- **Approved by the user on 2026-10-21** after browsing the vault in Obsidian and reading
  the review corrections. Phase gate 1 → 2 passed.
