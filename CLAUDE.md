# CLAUDE.md — the constitution

You maintain an LLM-compiled wiki of Andrej Karpathy's public output. Read this file before
every ingest, query or lint. When this file and an existing page disagree, this file wins
and the page is migrated.

Project docs: `specs/mission.md` (why), `specs/tech-stack.md` (how), `specs/roadmap.md`
(what's next), `DESIGN.md` (diagrams).

## 1. Invariants

1. **`raw/` is immutable.** Read it; never create, edit, rename or delete anything in it.
   The one exception is a fetch step that a human or a collector script runs, which writes
   a new raw file and its `_manifest.json` entry.
2. **You own `wiki/`.** Humans read it; corrections arrive as edits to this file, then a
   re-run of ingest or lint.
3. **Every factual sentence cites a source page.** Every source page cites its raw file.
   Opinions, connections and summaries you add yourself are labelled (see §5).
4. **No orphans.** Every page except `index.md`, `hot.md` and `log.md` has at least one
   inbound wikilink from another content page. Links from the three fixed files do not count.
5. **Wikilinks only.** `[[slug]]` or `[[slug|Display text]]`. No markdown links between
   wiki pages. External URLs are fine as plain markdown links.
6. **Never overwrite a position.** If a new source conflicts with an existing claim, write a
   new claim page and link the two with `contradicts`. The timeline page explains the change.
7. **Short quotes only.** The repo is public and `raw/` is gitignored for copyright reasons,
   so the wiki must not leak his words in bulk. A quote is at most one sentence and under
   15 words, always in quotation marks with its citation. Everything else is paraphrase.
8. **Say when the sources are silent.** If no source supports something, do not write it.

## 2. Naming

- File names are kebab-case slugs, unique across all of `wiki/` (a basename resolves a link).
- Display names and alternative spellings go in `aliases`.
- Source slugs: `<medium>-<yyyy-mm-dd>-<short-name>`, e.g. `youtube-2025-06-17-software-is-changing`.
- Claim slugs read as the claim, e.g. `english-is-the-new-programming-language`.
- Dates are ISO `YYYY-MM-DD`.

## 3. raw/ files (read-only reference)

Path: `raw/<medium-folder>/<id>.md`, where medium folders are `youtube, x, github, blog, talks`.

```yaml
---
id: LCEmiRjPEtQ            # stable id (video id, tweet id, repo name, url slug)
url: https://...
medium: youtube            # youtube | x | github | blog | talk
author: Andrej Karpathy
published: 2025-06-17
fetched: 2026-10-20
title: "..."
duration_or_length: "39:31"   # video length, or word count for text
---
```

Body is verbatim. YouTube bodies carry `[mm:ss]` (or `[h:mm:ss]`) markers per caption
block. X threads are one file per thread, posts in order, separated by `---`.

`raw/_manifest.json` lists every raw file: `id, url, medium, published, path, sha256`.

## 4. Page types

Every wiki page starts with YAML frontmatter. `type` is always first. List values that point
at pages are quoted wikilinks, e.g. `sources: ["[[youtube-2025-06-17-software-is-changing]]"]`,
so Obsidian shows them as links.

| type | folder | required frontmatter | optional |
|---|---|---|---|
| `source` | `wiki/sources/` | `type, raw_path, published, medium, summary` | `url, title` |
| `topic` | `wiki/topics/` | `type, aliases, first_seen, last_updated, sources` | `related` |
| `claim` | `wiki/claims/` | `type, stated_on, confidence, sources` | `contradicts, supports, topic` |
| `artifact` | `wiki/artifacts/` | `type, repo_url, language, status, sources` | `aliases` |
| `timeline` | `wiki/timeline/` | `type, topic` | |
| `principle` | `wiki/principles/` or `wiki/principles/_bench/` | `type, status, quotes, inferred` | `sources` |
| `method` | `wiki/methods/` | `type, steps, sources` | `aliases` |
| `synthesis` | `wiki/syntheses/` | `type, question, answered_on, sources, rules_applied` | |

Field meanings:

- `raw_path`: repo-relative path to the raw file, e.g. `raw/youtube/LCEmiRjPEtQ.md`.
- `summary`: one sentence, your words.
- `first_seen` / `last_updated`: earliest and latest `published` date among the topic's sources.
- `confidence` (claim): `stated` (he says it directly), `implied` (clearly follows from what he
  says), `inferred` (your reading; say so in the body).
- `status` (artifact): `active | archived | superseded`. `status` (principle): `bench | promoted`.
- `quotes` (principle): list of `{text, source, location}`; `location` is `mm:ss`, a post
  number, or a section heading.
- `inferred` (principle): `true` when no quote states the rule directly.
- `steps` (method): ordered list of short imperative phrases.

### Body structure

**source**
```
# <title>
Raw: [[raw/<medium>/<id>]] · Original: <url>

## Summary            3–6 sentences, your words, cite locations: (@12:30)
## Key points         bullets; each links the page it fed: … → [[topic-slug]]
## Fed pages          bullet list of every topic/claim/artifact/method this source fed
```

**topic**
```
# <Display name>
One-paragraph definition in his framing, cited.

## What he says       paragraphs, each sentence cited
## Claims             bullet links to claim pages
## Related            links to artifacts, methods, other topics
```

**claim**
```
# <The claim as a sentence>
> "short quote" — [[source-slug]] @mm:ss

## Context            what he was talking about, cited
## Supports / contradicts   links, with one line on how
```

**artifact**: `# name`, what it is, what it demonstrates (cited), `## Related`.
**method**: `# name`, when he uses it, `## Steps` (expands `steps`, each step cited),
`## Seen in` (links to sources/artifacts).
**timeline**: `# <topic> over time`, dated bullets oldest first, each linking a claim or source.
**principle**: `# rule as an imperative`, quotes block, `## In practice`, `## Sources`.
**synthesis**: `# question`, the answer with citations, `## Rules applied`.

## 5. Citations

- Cite with a wikilink to the source page in parentheses at the end of the sentence:
  `He calls this Software 3.0 ([[youtube-2025-06-17-software-is-changing]] @03:10).`
- Video and talk citations carry `@mm:ss` taken from the raw `[mm:ss]` markers. Text
  sources carry a section heading or post number when the source is long: `§Quick start`, `#3`.
- One sentence can cite several sources: `([[a]], [[b]])`.
- Sentences you write that are not in any source (a connection between two pages, a
  summary across sources) start with **Note:** and still link the pages they connect.
- Every paragraph on a topic or claim page contains at least one source citation. Lint
  checks this.

## 6. Fixed files

- `wiki/index.md`: every page, grouped under `## Sources`, `## Topics`, `## Claims`,
  `## Artifacts`, `## Methods`, `## Timelines`, `## Principles`, `## Syntheses`;
  one line per page: `- [[slug|Title]] — one-line summary`. Alphabetical within a group.
- `wiki/hot.md`: the last 20 page changes, newest first:
  `- YYYY-MM-DD [[slug]] — created|updated: what changed (from [[source-slug]])`.
- `wiki/log.md`: append-only. Never edit past entries. One entry per operation:
  ```
  ## YYYY-MM-DD ingest [[source-slug]]
  - created: [[a]], [[b]]
  - updated: [[c]]
  - notes: anything a reviewer should know
  ```

## 7. Procedures

### Ingest (one raw file at a time, in `published` order)

1. Read this file, `wiki/index.md` and `wiki/hot.md`.
2. Read the raw file in full. List the topics, specific claims, artifacts and methods
   (how he explains, debugs, builds, reviews) it contains.
3. For each item, search the index for an existing page (check `aliases`). Prefer updating
   an existing page over creating a near-duplicate.
4. Write the source page.
5. Create or update each topic, claim, artifact and method page. Add this source to the
   page's `sources`, update `first_seen`/`last_updated`, add cited sentences. Never remove a
   cited sentence; if it is now wrong, add a contradicting claim.
6. Link both ways: the source page lists every page it fed; each fed page cites the source.
   Where two sources discuss the same idea, link their pages to each other.
7. If a claim conflicts with an existing claim, link with `contradicts` on both, and create
   or update `wiki/timeline/<topic>.md`.
8. Principles are not extracted until phase 4. Do not write principle pages during ingest yet.
9. Update `index.md`, prepend to `hot.md`, append to `log.md`.
10. Run `python3 scripts/lint_check.py` and fix every finding before moving on.

### Query

1. Read `wiki/index.md`, then the relevant topic, claim and timeline pages.
2. Open the raw file only when you need exact wording or a timestamp.
3. Answer with citations to wiki source pages. If the wiki has nothing, say "the wiki has
   nothing on this" and stop; do not answer from general knowledge as if it were his view.
4. If the answer is reusable, save it as `wiki/syntheses/<slug>.md`, link it from the pages
   it cites, update index, hot and log.

### Lint

1. Run `python3 scripts/lint_check.py`. Fix every finding.
2. Then check by reading what the script cannot: uncited sentences, unresolved
   `contradicts` without a timeline, near-duplicate pages to merge, frontmatter drift from §4.
3. Append a `## YYYY-MM-DD lint` entry to `log.md` with what was found and fixed.
