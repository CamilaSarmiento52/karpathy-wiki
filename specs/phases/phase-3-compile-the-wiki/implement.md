# Phase 3 — Compile the wiki: implementation notes

_Written during implementation, from 2026-10-23. What was actually built, decisions made
while building, deviations from the plan._

## Decisions taken (2026-10-23)

The user asked to implement without choosing, so the plan's recommendations stand:

1. Digests run as parallel helper agents (one per source; the three short batch 1 READMEs
   share one agent); merge and verify run one at a time.
2. Personal posts get full source pages; topic pages only where an idea recurs; claim
   pages only for a clear position.
3. Pilot gate after batch 1: stop for the user's review in Obsidian before batches 2–4.
4. Digests are committed under `staging/`.
5. External review after batch 1 and at the end of the phase, if the user wants one.

## Tooling

| File | What it does |
|---|---|
| `scripts/batches.py` | assigns every manifest item to a batch by `published` date (boundaries 2023-02-01, 2024-08-01, 2025-10-20); reports per-batch status: raw, digest, source page, verified |
| `tests/test_batches.py` | boundaries, status fields, stability, CLI listing |
| `staging/README.md` | the digest format and the verify report convention |
| `staging/digests/`, `staging/verify/` | digest per raw file (named by raw stem), verification report per batch |
| `.obsidian/app.json` | `staging/` added to the vault's ignore filters |

Batch sizes from the manifest are 10 / 21 / 23 / 28 (the plan's draft said 22 for batch 4;
the manifest has 28 items from 2025-10-24 on, six of them phase 1 sources).

## Batch 1 (pilot)
