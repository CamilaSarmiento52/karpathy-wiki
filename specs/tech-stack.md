# Tech stack

## Principles

- **Markdown is the database.** Every piece of state is a `.md` file (plus the JSON manifest
  and coverage queue in `raw/`).
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
| YouTube | `youtube-transcript-api` for captions, `yt-dlp` (pinned in requirements) for metadata and channel listing; Whisper fallback not built (items without captions stay `pending: no-transcript`) | free; timestamps kept so rules can cite `video@mm:ss` |
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
│   ├── _manifest.json   id, ref, url, medium, published, path, body sha256, commit, repo; committed
│   └── _queue.json      coverage queue: collected / pending / excluded with reasons; committed
├── wiki/                LLM-owned pages; committed
├── .claude/             agent, skills, hooks
├── scripts/             rawstore.py, collect_{youtube,x,github,blog,talks}.py, fetch_one.py
│                        (one-offs, --restore), coverage_queue.py, coverage_report.py,
│                        spot_check.py, lint_check.py, quote_check.py (inline quotes
│                        vs raw, report-only), batches.py (phase 3 batch bookkeeping),
│                        build_agent.py (generates the karpathy agent), install.py
│                        (user-level agent copy + skill links), independence.json
├── staging/             phase 3 working files: digests, merge maps, briefs, verify reports
├── tests/               test_lint_check.py; prompts.md (real-task validation, phase 4)
└── .obsidian/           vault config: graph colours by folder, wikilinks on
```

### raw/ file

Frontmatter: `id, url, medium (youtube|x|github|blog|talk), author, published, fetched,
title, duration_or_length`, plus `commit` for GitHub. GitHub READMEs are living documents,
so each is read at a pinned commit (the last one that touched it) and dated by that commit.
When a README changes, the GitHub collector stores a new snapshot `<repo-id>@<short-commit>`
next to the earlier ones instead of skipping the repo; the first snapshot keeps the plain
`<repo-id>`. GitHub Discussions he opened are stored as `<owner>__<repo>__discussion-<n>`,
and gists he links that contain markdown as `karpathy__gist-<id>` (fetched with `git clone`).
`medium: youtube` is a video on his own channel; `medium: talk` is a talk, podcast or
interview hosted by someone else (the phase 1 YC talk is a recorded exception, filed as
`youtube`). Body: verbatim text. YouTube bodies keep `[mm:ss]` markers per
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

Plus fixed files: `index.md` (top-level table of contents), `index/<type>.md` (every page
of one type, one file per type), `hot.md` (recent changes), `log.md` (append-only journal).
The index was split on 2026-10-24, between phase 3 batches 1 and 2, at 110 lines with
about 80 pages to come in batch 2; lint checks that each page is listed in its type's file
and treats index files like hot and log (not inbound links).

### Invariants

`scripts/lint_check.py` checks the structural ones; `scripts/quote_check.py` reports quoted
spans in evidence text that are not verbatim in a cited raw file (lint itself checks only
each claim's opening quote); the semantic ones (does the citation support the sentence, is
a `contradicts` link a real conflict) need a reading pass.

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
| ingest | weekday scheduled run (`daily.py`, then `/karpathy-ingest <raw path>` per new file) or `/karpathy-ingest <url>` | new raw files, index, hot, related pages | pages, source page, index, hot, log (fields read by `brief.py`); principle quotes and promotions; a fresh verifier's report; one local commit per source |
| query | a free question in Claude Code | index, relevant pages, raw on demand | optional synthesis page, log |
| lint | Sunday scheduled run (`daily.py --weekly` first) or on request | all pages; a fresh reader on the week's changed pages | fixes, promotions, log report; regenerates the agent and reinstalls the user-level copy if rules changed |
| brief | end of the weekday run | `reports/collect-DATE.json`, the day's log entries | `reports/briefs/DATE.md` only when there is news |
| extract-rules | end of phase 4, then by lint | topics, claims, methods | principles pages |

## Agent layer

- `.claude/agents/karpathy.md`: promoted principles with quotes, bench and inferred rules
  labelled, voice steps from `methods/how-he-explains`, the eight-step task loop (define
  done, state assumptions, smallest version, predict, run and compare, break it, fix and
  trim, report per rule), grounding rules and a one-line disclosure. Generated by
  `scripts/build_agent.py`, never hand-edited; the repo copy uses relative paths.
- `.claude/skills/karpathy-teach`, `karpathy-review` (phase 4): `context: fork`,
  `agent: karpathy`, so each runs in the sub-agent's own context. `karpathy-ingest` is
  phase 5.
- `.claude/hooks/run_gate.py`, declared in the agent's own frontmatter, so it runs only
  while that sub-agent is active: a PostToolUse hook logs code writes and commands per
  `agent_id`, and the agent's Stop hook (SubagentStop at runtime) blocks if code was
  written and not run since. Built on documented hook input fields, not the transcript
  format.
- User level: `scripts/install.py` writes a copy of the agent to `~/.claude/agents/` with
  absolute paths (agent symlinks are not documented) and links the two skill folders into
  `~/.claude/skills/` (skill symlinks are), so the skills work from any project.

## Constraints

- Public GitHub repository. `raw/` is gitignored for copyright reasons; `_manifest.json` is
  committed so the corpus is reproducible by running the collectors.
- No secrets in the repo. `.env` is gitignored; `.env.example` lists the variable names.
- Collectors must be idempotent: re-running fetches only what the manifest does not have,
  plus a new snapshot of any README that changed. They may run in parallel; manifest and
  queue writes are serialised by a file lock in `scripts/rawstore.py`.
- Scope: 2023 onward, plus the pre-2023 Zero to Hero lectures and teaching repos (phase 2
  decision). Anything left out is in `raw/_queue.json` as `excluded` with a reason.
- X discovery needs `TWITTERAPI_IO_KEY` in `.env`; without it the X collector fetches only
  posts already in the queue (via the free fxtwitter API, which also serves restores).
- Ingest batches of 20 to 30 sources so the schema can be corrected early.
