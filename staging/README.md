# staging/

Working files for phase 3 ingest. Not part of the wiki; hidden from the Obsidian vault.

- `digests/<raw-stem>.md` — one per raw file, written by a digest step that reads only
  `CLAUDE.md`, the index files in `wiki/index/` and that raw file. Never writes to `wiki/`.
- `verify/batch-<n>.md` — a verification report per batch, written by a fresh reader
  after the merge, checking pages against the raw files. One `[[source-slug]]` per
  source checked; findings are fixed by merge and logged as corrections in `wiki/log.md`.

## Digest format

```
# Digest: <raw title>
- raw: raw/<medium>/<id>.md · published: YYYY-MM-DD · medium: <medium> · words: N
- source slug: <medium>-<yyyy-mm-dd>-<short-name>

## Source page
(the complete wiki/sources/<slug>.md, frontmatter included, following CLAUDE.md §4;
 `## Fed pages` lists the candidate slugs below; merge finalises it)

## Candidates
### <type>: <proposed-slug>            ← topic | claim | artifact | method | timeline
- existing: yes|no (yes = slug or alias already in a `wiki/index/` type file)
- aliases: ...
- statements:
  - <paraphrase, one sentence, no stronger than the source> (@h:mm:ss or §heading)
  - ...
- for a claim: the title as a sentence, `confidence` (stated|implied), and the quote
- relation to an existing page, if any: supports | extends | contradicts, and why

## Quotes
- "<verbatim, under 15 words, one sentence>" (@h:mm:ss or §heading)

## Notes for merge
caption misspellings, host vs him (talks), things mentioned but not explained,
anything a reviewer should know
```

Rules: paraphrase everything except quotes; quotes are copied verbatim from the raw file
and are under 15 words; timestamps come from the raw `[mm:ss]` / `[h:mm:ss]` markers.
A topic is a candidate only if the source explains it, not just mentions it.
