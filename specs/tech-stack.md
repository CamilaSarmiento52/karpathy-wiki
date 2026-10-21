# Tech stack

## Principles

- **Markdown is the database.** Every piece of state is a `.md` file (plus one JSON manifest).
  No vector store, no SQL. Anything can be read in a text editor or Obsidian.
- **raw/ is immutable.** Collectors write it; the LLM only reads it. Nothing else touches it.
- **The LLM owns wiki/.** Humans browse it; they do not edit it. Fixes go through ingest or lint.
- **CLAUDE.md is the constitution.** Page types, frontmatter, link rules and operation
  procedures live there. The LLM reads it before every operation.
- **Prove, don't claim.** Code the agent hands over has been run; the Stop hook enforces it.

## Components

| Layer | Choice | Why |
|---|---|---|
| Engine | Claude Code (sub-agent, skills, hooks in `.claude/`) | already runs code, supports sub-agents with separate context, hooks for the run gate |
| Viewer | Obsidian, vault = `karpathy-wiki/` | wikilinks, backlinks, graph; zero lock-in |
| Collectors | Python 3.12+ scripts in `scripts/`, deps pinned in `requirements.txt`, local `.venv/` | small, inspectable, runnable on a schedule |
| YouTube | `youtube-transcript-api` for captions, `yt-dlp` for metadata, Whisper fallback | free; timestamps kept so rules can cite `video@mm:ss` |
| X | `twitterapi.io` | full archive since 2023 for about a dollar |
| GitHub | GitHub REST API | READMEs, release notes, commit messages; code linked, not copied |
| Blog / newsletters | RSS, Obsidian Web Clipper for one-offs | free |
| Scheduling | Claude Code scheduled task (weekday morning) plus a Sunday lint | fits the user's morning-brief rhythm |
| Secrets | `.env`, never committed | twitterapi.io key, GitHub token |

## Data model

### Folders

```
karpathy-wiki/
├── CLAUDE.md            constitution for the LLM
├── DESIGN.md            explanatory design with diagrams
├── specs/               mission, tech stack, roadmap, phases
├── raw/                 immutable sources, one .md per item, by medium; gitignored
│   └── _manifest.json   id, ref, url, medium, published, path, body sha256, commit; committed
├── wiki/                LLM-owned pages; committed
├── .claude/             agent, skills, hooks
├── scripts/             collectors, run_ingest.sh, lint_check.py (fetch_one.py in phase 1)
├── tests/               test_lint_check.py; prompts.md (real-task validation, phase 4)
└── .obsidian/           vault config: graph colours by folder, wikilinks on
```

### raw/ file

Frontmatter: `id, url, medium (youtube|x|github|blog|talk), author, published, fetched,
title, duration_or_length`, plus `commit` for GitHub. GitHub READMEs are living documents,
so each is read at a pinned commit (the last one that touched it) and dated by that commit.
Phase 2 collectors should store a new versioned snapshot when a README changes, rather than
skipping a repo already seen. Body: verbatim text. YouTube bodies keep `[mm:ss]` markers per
caption block (grouped into ~30-second blocks so citations stay readable). X threads are one file per thread, posts in order.

### wiki/ page types

| Type | Folder | Required frontmatter |
|---|---|---|
| source | `sources/` | `type, raw_path, published, medium, summary` |
| topic | `topics/` | `type, aliases, first_seen, last_updated, sources[]`, optional `context[]` (background only; not counted for dates) |
| claim | `claims/` | `type, stated_on, confidence, sources[]`, optional `supports[], extends[], contradicts[]` |
| artifact | `artifacts/` | `type, repo_url, language, status, sources[]` |
| timeline | `timeline/` | `type, topic` |
| principle | `principles/` or `principles/_bench/` | `type, status (bench|promoted), quotes[{text, source, location}], inferred` |
| method | `methods/` | `type, steps[], sources[]` |
| synthesis | `syntheses/` | `type, question, answered_on, sources[], rules_applied[]` |

Plus three fixed files: `index.md` (TOC by type), `hot.md` (recent changes), `log.md`
(append-only journal).

### Invariants

`scripts/lint_check.py` checks the structural ones; the semantic ones (does the citation
support the sentence, is a `contradicts` link a real conflict) need a reading pass.

- Every factual sentence cites a source page; every source page cites a raw path.
- No orphan pages: every page has an inbound link from another content page (links from
  `index.md`, `hot.md`, `log.md` do not count). Wikilinks only.
- Quotes in `wiki/` are one sentence and under 15 words; everything else is paraphrase,
  because the repo is public and `raw/` is not.
- A principle is promoted only with two or more independent sources; otherwise it stays on
  the bench. A principle without a quote is `inferred: true`.
- A change of view is never overwritten: claims are linked with `contradicts` (cannot both
  hold) or `extends` (broadens), and a timeline page explains the evolution. A compilation
  error is different: it is fixed in place and logged as a correction.
- Frontmatter matches the current schema; lint reports drift and the LLM migrates it.

## Operations

| Operation | Trigger | Reads | Writes |
|---|---|---|---|
| ingest | collectors (scheduled) or `/karpathy-ingest <url>` | new raw files, index, hot, related pages | pages, source page, index, hot, log; bench promotions |
| query | a free question in Claude Code | index, relevant pages, raw on demand | optional synthesis page, log |
| lint | Sunday schedule or on request | all pages | fixes, promotions/demotions, log report; regenerates sub-agent if rules changed |
| extract-rules | end of phase 4, then by lint | topics, claims, methods | principles pages |

## Agent layer

- `.claude/agents/karpathy.md`: promoted principles with quotes, voice notes from
  `methods/how-he-explains`, and the eight-step task loop (define done, state assumptions,
  smallest version, predict, run and compare, break it, fix and trim, report per rule).
  Regenerated from the wiki, never hand-edited.
- `.claude/skills/karpathy-teach`, `karpathy-review`, `karpathy-ingest`.
- `.claude/hooks/run_gate.sh`: Stop hook that blocks a turn which wrote code but ran none.

## Constraints

- Public GitHub repository. `raw/` is gitignored for copyright reasons; `_manifest.json` is
  committed so the corpus is reproducible by running the collectors.
- No secrets in the repo. `.env` is gitignored; `.env.example` lists the variable names.
- Collectors must be idempotent: re-running fetches only what the manifest does not have.
- Ingest batches of 20 to 30 sources so the schema can be corrected early.
