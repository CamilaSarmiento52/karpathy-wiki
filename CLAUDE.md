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
4. **No orphans.** Every page except the fixed files (`index.md`, the type files in
   `wiki/index/`, `hot.md` and `log.md`) has at least one inbound wikilink from another
   content page. Links from fixed files do not count.
5. **Wikilinks only.** `[[slug]]` or `[[slug|Display text]]`. No markdown links between
   wiki pages. External URLs are fine as plain markdown links.
6. **Never overwrite a position; always fix a mistake.** Two different things:
   - *He changed his mind.* Keep the old claim, write a new dated claim, link them, and
     explain the change on a timeline page.
   - *The wiki got it wrong* (bad paraphrase, wrong citation, overstated wording, invented
     link). Fix the page in place and append a `correction` entry to `log.md` saying what
     changed and why. A compilation error is not a change in his opinion.
7. **Short quotes only.** The repo is public and `raw/` is gitignored for copyright reasons,
   so the wiki must not leak his words in bulk. A quote is at most one sentence and under
   15 words, always in quotation marks with its citation. Everything else is paraphrase.
8. **Say when the sources are silent.** If no source supports something, do not write it.
9. **A citation is not proof.** A link shows where to look, not that the source says it.
   The sentence must be something the cited passage actually supports, no stronger.

## 2. Naming

- File names are kebab-case slugs, unique across all of `wiki/` (a basename resolves a link).
- Display names and alternative spellings go in `aliases`.
- Source slugs: `<medium>-<yyyy-mm-dd>-<short-name>`, e.g. `youtube-2025-06-19-software-is-changing`.
- Claim slugs read as the claim, e.g. `english-is-the-new-programming-language`.
- Dates are ISO `YYYY-MM-DD`.
- A source's date is its `published` date, which for a talk or lecture can be months after
  he gave it (the CS25 lecture was given around January 2023 and published in May). Do not
  write intervals or order between sources ("four months later", "a week after", "first
  said in") from published dates alone. Write the dates themselves, and say "published"
  when a recording date is known to differ.

## 3. raw/ files (read-only reference)

Path: `raw/<medium-folder>/<id>.md`, where medium folders are `youtube, x, github, blog, talks`.

```yaml
---
id: LCEmiRjPEtQ            # stable id (video id, tweet id, repo name, url slug)
url: https://...
medium: youtube            # youtube | x | github | blog | talk
author: Andrej Karpathy
published: 2025-06-19
fetched: 2026-10-20
title: "..."
duration_or_length: "39:31"   # video length, or word count for text
commit: 3adf61e…           # github only: the commit the README was read at
---
```

Body is verbatim; blog bodies keep link targets as `[text](url)`. YouTube bodies carry
`[mm:ss]` (or `[h:mm:ss]`) markers per ~30-second caption block. X threads are one file per
thread, posts in order, separated by `---`. `medium: talk` covers talks, podcasts and
interviews.

`medium: youtube` is a video on his own channel; `medium: talk` is anything hosted by
someone else (the YC talk `LCEmiRjPEtQ` is a known exception, filed as `youtube`). Talk
transcripts include the other speakers: attribute only what he says.

**AI-written text in a source is not his.** Some sources he published are partly or wholly
written by a model: autoresearch Discussion #43 was written by the agent; most of the
Sequoia Ascent 2026 blog post is a summary and cleaned transcript produced by Codex, with
only the intro his own. The source page says which parts are AI-written. Nothing in those
parts is cited as his view, quote or wording; cite the part he wrote, or the original
recording, instead. An AI-written result he reports (an agent's experiment log) may be
described as that agent's output, labelled as such.

GitHub READMEs are versioned: the first snapshot is `raw/github/<owner>__<repo>.md`, later
ones `raw/github/<owner>__<repo>@<short-commit>.md`, each dated by its commit. A newer
snapshot is a new source, not a correction of the old one. Discussions he opened are
`raw/github/<owner>__<repo>__discussion-<n>.md`; gists, `raw/github/karpathy__gist-<id>.md`.

`raw/_manifest.json` lists every raw file: `id, ref, url, medium, published, path, sha256`,
plus `commit` and `repo` for GitHub READMEs. `ref` is what was passed to the fetcher (for
an X thread, its post ids in order); `sha256` is of the body only.
`python3 scripts/fetch_one.py --restore` rebuilds missing raw files from it.
`raw/_queue.json` lists everything known to exist, collected or not; it is the collectors'
bookkeeping, not a source. A raw file with no source page yet is the ingest backlog.

## 4. Page types

Every wiki page starts with YAML frontmatter. `type` is always first. List values that point
at pages are quoted wikilinks, e.g. `sources: ["[[youtube-2025-06-19-software-is-changing]]"]`,
so Obsidian shows them as links.

| type | folder | required frontmatter | optional |
|---|---|---|---|
| `source` | `wiki/sources/` | `type, raw_path, published, medium, summary` | `url, title` |
| `topic` | `wiki/topics/` | `type, aliases, first_seen, last_updated, sources` | `context, related` |
| `claim` | `wiki/claims/` | `type, stated_on, confidence, sources` | `contradicts, supports, extends, topic` |
| `artifact` | `wiki/artifacts/` | `type, repo_url, language, status, sources` | `aliases` |
| `timeline` | `wiki/timeline/` | `type, topic` | |
| `principle` | `wiki/principles/` or `wiki/principles/_bench/` | `type, status, quotes, inferred` | `sources` |
| `method` | `wiki/methods/` | `type, steps, sources` | `aliases` |
| `synthesis` | `wiki/syntheses/` | `type, question, answered_on, sources, rules_applied` | |

Field meanings:

- `raw_path`: repo-relative path to the raw file, e.g. `raw/youtube/LCEmiRjPEtQ.md`.
- `summary`: one sentence, your words.
- `sources` (topic): sources that discuss the topic directly. `context`: sources cited only
  for background or a **Note:** connection; they do not count as evidence for the topic.
- `first_seen` / `last_updated`: earliest and latest `published` date among `sources`
  (not `context`).
- `confidence` (claim): `stated` (he says it directly), `implied` (clearly follows from what he
  says), `inferred` (your reading; say so in the body). The title must not claim more than
  the evidence: "his wiki worked without RAG", not "wikis don't need RAG".
- `contradicts`: only when both statements cannot be true at once. `extends`: a later claim
  broadens or adds to an earlier one without denying it. `supports`: one gives evidence for
  the other. All three are set on both pages (`extends` pairs with `extends`).
- `status` (artifact): `active | archived | superseded`. `status` (principle): `bench | promoted`.
- `quotes` (principle): list of `{text, source, location}`; `location` is `mm:ss`, a post
  number, or a section heading.
- `inferred` (principle): `true` when no quote states the rule directly.
- `steps` (method): ordered list of short imperative phrases.
- Allowed values (lint enforces): `medium` ∈ youtube, x, github, blog, talk; artifact
  `status` ∈ active, archived, superseded; principle `status` ∈ bench, promoted.
- List fields that are required (`sources`, `steps`, `quotes`, `rules_applied`) must not be
  empty.

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
## Related claims   supports / extends / contradicts, one line each on how, citing both sides
```

**artifact**: `# name`, what it is, what it demonstrates (cited), `## Related`.
**method**: `# name`, when he uses it, `## Steps` (expands `steps`, each step cited),
`## Seen in` (links to sources/artifacts).
**timeline**: `# <topic> over time`, dated bullets oldest first, each linking a claim or source.
**principle**: `# rule as an imperative`, quotes block, `## In practice`, `## Sources`.
**synthesis**: `# question`, the answer with citations, `## Rules applied`.

## 5. Citations

- Cite with a wikilink to the source page in parentheses at the end of the sentence:
  `He calls this Software 3.0 ([[youtube-2025-06-19-software-is-changing]] @03:10).`
- Video and talk citations carry `@mm:ss` taken from the raw `[mm:ss]` markers. Text
  sources carry a section heading or post number when the source is long: `§Quick start`, `#3`.
- One sentence can cite several sources: `([[a]], [[b]])`.
- Sentences you write that are not in any source (a connection between two pages, a
  summary across sources) start with **Note:** and still link the pages they connect.
- **Evidence blocks** must cite a source page: every paragraph and list item in a topic's
  definition and `## What he says`, a claim's `## Context` and `## Related claims`, an
  artifact's definition and `## What it demonstrates`, a method's definition and `## Steps`,
  and every timeline entry. Lint checks that each block has a citation; it cannot check
  that the citation supports the sentence.
- A sentence comparing two sources cites both.
- Every source cited in a page body is listed in its `sources` (or `context`), and every
  listed source is cited in the body. A source page's `## Fed pages` lists exactly the
  pages that cite it.

## 6. Fixed files

- **Index** (split on 2026-10-24, when it reached 110 lines with ~80 pages to come):
  - `wiki/index.md`: a short top-level page linking the eight type files below, plus
    `[[hot]]` and `[[log]]`. It does not list pages.
  - `wiki/index/<type>.md`, one per page type: `sources`, `topics`, `claims`, `artifacts`,
    `methods`, `timelines`, `principles`, `syntheses`. Each lists every page of that type,
    one line per page: `- [[slug|Title]] — one-line summary`, alphabetical.
  - Index files are fixed files: no frontmatter, and links from them do not count as
    inbound links. Lint checks that every page is in its own type's file.
- `wiki/hot.md`: the last 20 page changes, newest first:
  `- YYYY-MM-DD [[slug]] — created|updated: what changed (from [[source-slug]])`.
- `wiki/log.md`: append-only. Never edit past entries. One entry per operation:
  ```
  ## YYYY-MM-DD ingest [[source-slug]]
  - created: [[a]], [[b]]
  - updated: [[c]]
  - notes: anything a reviewer should know
  ```
  Corrections use `## YYYY-MM-DD correction` with one bullet per page: what was wrong,
  what it says now, and why (e.g. "cited the talk for an argument made in the blog").

## 7. Procedures

### Ingest (one raw file at a time, in `published` order)

1. Read this file, `wiki/hot.md`, and the index type files you need (`wiki/index/topics.md`,
   `claims.md`, `methods.md`, `artifacts.md` at least).
2. Read the raw file in full. List the topics, specific claims, artifacts and methods
   (how he explains, debugs, builds, reviews) it contains.
3. For each item, search for an existing page: the type's index file, then file names and
   `aliases` (`grep -ril "<term>" wiki/topics wiki/claims wiki/methods wiki/artifacts`).
   Prefer updating an existing page over creating a near-duplicate.
4. Write the source page.
5. Create or update each topic, claim, artifact and method page. Add this source to the
   page's `sources` (or `context` if it is only background), update
   `first_seen`/`last_updated`, add cited sentences. If he has changed his mind, add a new
   claim (invariant 6); if an existing sentence was compiled wrong, correct it and log it.
6. Link both ways: the source page lists every page it fed; each fed page cites the source.
   Where two sources discuss the same idea, link their pages to each other.
7. If a claim relates to an existing claim, pick the weakest true link: `supports`,
   `extends`, or `contradicts` only if both cannot hold. For `extends` and `contradicts`,
   create or update `wiki/timeline/<topic>.md`.
8. Principles are not extracted until phase 4. Do not write principle pages during ingest yet.
9. Add each new page to its type's file in `wiki/index/`, prepend to `hot.md`, append to
   `log.md`.
10. Run `python3 scripts/lint_check.py` and fix every finding before moving on.
11. Lint is structural only. Before finishing, re-read each sentence you wrote against the
    cited passage: does the source say this, at this strength?

### Query

1. Read `wiki/index.md` and the type files it links, then the relevant topic, claim and
   timeline pages.
2. Open the raw file only when you need exact wording or a timestamp.
3. Answer with citations to wiki source pages. If the wiki has nothing, say "the wiki has
   nothing on this" and stop; do not answer from general knowledge as if it were his view.
4. If the answer is reusable, save it as `wiki/syntheses/<slug>.md`, link it from the pages
   it cites, add it to `wiki/index/syntheses.md`, update hot and log. A synthesis is never evidence: no page may cite a
   synthesis as a source, and its claims must trace to source pages like any other page.

### Lint

1. Run `python3 scripts/lint_check.py` (structural lint). Fix every finding.
2. Then the semantic pass the script cannot do: does each cited passage support its
   sentence at that strength; are `contradicts` links real conflicts; near-duplicate pages
   to merge. Fix compilation errors in place and log them as corrections.
3. Append a `## YYYY-MM-DD lint` entry to `log.md` with what was found and fixed.
