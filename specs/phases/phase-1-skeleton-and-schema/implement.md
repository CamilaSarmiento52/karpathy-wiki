# Phase 1 — Skeleton and schema: implementation notes

_Written during implementation. What was actually built, decisions made while building,
deviations from the plan._

## What was built

- **Folders** per `specs/tech-stack.md`, with `.gitkeep` in the empty ones.
- **`CLAUDE.md`**: invariants, naming, raw format, the eight page types with required
  frontmatter and body skeletons, citation rules, fixed files, and ingest / query / lint
  procedures.
- **`.obsidian/`**: `app.json` (wikilinks, new notes go to `wiki/syntheses`, hides
  `.claude/ scripts/ tests/`), `graph.json` (one colour per page-type folder, raw in grey),
  `core-plugins.json`.
- **`scripts/lint_check.py`** + **`tests/test_lint_check.py`** (9 tests).
- **`scripts/fetch_one.py`**: fetches one source into `raw/` with frontmatter and a manifest
  entry (see deviations).
- **Five raw sources** and **29 wiki pages**: 5 sources, 9 topics, 6 claims, 2 artifacts,
  3 methods, 1 timeline, plus index, hot and log.

### The five sources

| Medium | Source | Why it was picked |
|---|---|---|
| x | 2025-02-02 "vibe coding" post | coins a term the other sources return to |
| youtube | 2025-06-19 YC talk "Software Is Changing (Again)" | broadest source; touches every other one |
| blog | 2025-12-19 "2025 LLM Year in Review" | revisits the talk's ideas six months on, so it produces a contradiction and a timeline |
| x | 2026-04-02 "LLM Knowledge Bases" | the pattern this project implements |
| github | nanochat README (last commit 2026-07-03) | an artifact, and a method (his experiment loop) |

They overlap on purpose: vibe coding appears in four of the five, and the talk and the
essay share LLM apps, jagged intelligence, the LLM OS and the LLM GUI.

## Decisions made while building

- **Quotes are short.** The repo is public and `raw/` is gitignored for copyright reasons,
  so the wiki would leak his words if pages quoted at length. CLAUDE.md caps a quote at one
  sentence under 15 words; everything else is paraphrase with a citation. Every quote on
  the 29 pages was checked against the raw text by script: all match and all are short.
- **Citation format**: `([[source-slug]] @mm:ss)` for video, `§Section` for long text.
  Lint checks it per paragraph; it cannot check per sentence.
- **Orphans ignore the fixed files.** Otherwise `index.md` would make every page
  non-orphan and the check would mean nothing.
- **Bare slugs, unique across `wiki/`**, so `[[slug]]` resolves without paths. Source pages
  link raw files by path (`[[raw/x/<id>]]`), which is the second click to his words.
- **The "superseded" status on nanoGPT is an inference** and the page says so.
- **Contradiction modelled once**: the Feb 2025 "weekend projects" claim and the Dec 2025
  "terraform software" claim are linked with `contradicts`, and the timeline explains
  it as a widening of scope, not a reversal.
- **No principle pages yet**, per plan; the procedure says so explicitly.

## Deviations from the plan

- **Sources were fetched by a script, not by hand.** `scripts/fetch_one.py` writes the raw
  file and manifest entry, so the verbatim text goes from the source to disk without being
  retyped. It is a throwaway phase 1 helper; phase 2 replaces it with per-medium collectors.
  X posts come from the public fxtwitter API (no key needed), blog posts from the bearblog
  Atom feed, GitHub through `gh`, YouTube through `youtube-transcript-api` + `yt-dlp`.
- **"Two X threads" became two long single posts.** Both are self-contained long-form posts
  and serve the same purpose.
- **Two fetch fixes, then refetched**: X titles were cut mid-word, and the GitHub
  `published` date was the repo creation date (2025-10-13) while the README text is current.
  It is now the README's last commit date; recorded in tech-stack.
- **`requirements.txt` and `.venv/`** added; the machine has Python 3.13, which the spec
  now allows (3.12+).
- **YouTube published date** is the upload date (2025-06-19); the talk was given on 06-17.

## Known gaps

- Obsidian is not installed on this machine, so the vault has not been opened yet.
- On a fresh clone without `raw/`, lint reports every raw link as broken. That is correct
  until the collectors rebuild `raw/`.
- Auto-captions misspell names ("Andre Carpathy", "menu.app"); pages use correct spellings.
