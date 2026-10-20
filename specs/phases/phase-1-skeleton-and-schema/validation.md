# Phase 1 — Skeleton and schema: validation

## Done when

- [x] All folders from the plan exist; `tree -L 2` matches `specs/tech-stack.md`.
- [x] `CLAUDE.md` defines all eight page types with required frontmatter, the invariants,
      and procedures for ingest, query and lint.
- [x] Five raw files exist with complete frontmatter; `_manifest.json` lists them.
- [x] Ingest produced: five source pages, at least three topic pages, at least one artifact
      page, at least one claim page, at least one method page.
- [x] Every wiki page has valid frontmatter per its type.
- [x] Zero orphan pages (every page has at least one inbound link).
- [x] Every factual sentence on a topic or claim page cites a source page; every source page
      cites its raw path.
- [x] At least one cross-link exists between pages that came from different sources.
- [x] `index.md` lists every page by type; `log.md` has one entry per ingested source;
      `hot.md` lists the pages touched.
- [ ] Obsidian opens `karpathy-wiki/` as a vault, links resolve, graph shows the pages.
- [ ] The user has reviewed the pages in Obsidian and approved the schema, or corrections
      were applied to CLAUDE.md and ingest re-run until approved.
- [x] `raw/` and `.env` are gitignored; `_manifest.json` is committed; repo is public.

## Manual checks

1. Open a topic page, click a cited source, click its raw path: two clicks to his words.
2. Pick a claim, check the date and the quoted sentence exist in the raw file.
3. Open graph view: no isolated nodes.

## Status (2026-10-20)

- Lint: 29 pages, 5 raw files, 0 findings. `pytest tests`: 9 passed.
- Produced: 5 sources, 9 topics, 6 claims, 2 artifacts, 3 methods, 1 timeline.
- Every quote checked against raw by script: all verbatim, all under 15 words.
- Citations checked automatically per paragraph; per sentence by reading.
- Repo visibility: public.
- **Open:** Obsidian check and the user's schema review — both need the user (Obsidian is
  not installed on this machine). This is the 1 → 2 phase gate.
