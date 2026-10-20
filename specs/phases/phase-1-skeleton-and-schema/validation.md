# Phase 1 — Skeleton and schema: validation

## Done when

- [ ] All folders from the plan exist; `tree -L 2` matches `specs/tech-stack.md`.
- [ ] `CLAUDE.md` defines all eight page types with required frontmatter, the invariants,
      and procedures for ingest, query and lint.
- [ ] Five raw files exist with complete frontmatter; `_manifest.json` lists them.
- [ ] Ingest produced: five source pages, at least three topic pages, at least one artifact
      page, at least one claim page, at least one method page.
- [ ] Every wiki page has valid frontmatter per its type.
- [ ] Zero orphan pages (every page has at least one inbound link).
- [ ] Every factual sentence on a topic or claim page cites a source page; every source page
      cites its raw path.
- [ ] At least one cross-link exists between pages that came from different sources.
- [ ] `index.md` lists every page by type; `log.md` has one entry per ingested source;
      `hot.md` lists the pages touched.
- [ ] Obsidian opens `karpathy-wiki/` as a vault, links resolve, graph shows the pages.
- [ ] The user has reviewed the pages in Obsidian and approved the schema, or corrections
      were applied to CLAUDE.md and ingest re-run until approved.
- [ ] `raw/` and `.env` are gitignored; `_manifest.json` is committed; repo is public.

## Manual checks

1. Open a topic page, click a cited source, click its raw path: two clicks to his words.
2. Pick a claim, check the date and the quoted sentence exist in the raw file.
3. Open graph view: no isolated nodes.
