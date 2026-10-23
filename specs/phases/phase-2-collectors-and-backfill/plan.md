# Phase 2 — Collectors and backfill: plan

_Drafted 2026-10-21. The user said "build phase 2" without answering the open decisions
at the end, so the recommended option was taken for each; see "Decisions taken"._

## Goal

Replace the phase 1 hand-fetch helper with one collector per medium, then use them to fill
`raw/` with Karpathy's public output from 2023 onward, teaching material first. At the end
we know, per medium, what was collected, what is still pending and what was deliberately
left out, and why.

No wiki pages are written in this phase. Compiling the backfill is phase 3.

## Why teaching material first

The six phase 1 sources are mostly about AI-assisted software and product ideas (vibe
coding, Software 3.0, LLM apps). The project's purpose is an agent that teaches the way he
does, and there is almost no direct teaching evidence yet: no tokenizer lecture, no
backprop, no model code walkthrough, no training diagnostics (roadmap, "Known gaps"). So
the backfill runs in priority order: lectures and teaching repos first, then everything
else.

## What this phase builds

### 1. A shared raw store (`scripts/rawstore.py`)

The bookkeeping that `fetch_one.py` does today, moved into one module every collector uses:

- `write(meta, body, path)`: raw file with standard frontmatter (CLAUDE.md §3).
- `digest(body)`: sha256 of the body only (unchanged, so existing hashes stay valid).
- Manifest read / add / save, **under a file lock**, re-reading the manifest inside the
  lock before saving, so collectors can run in parallel without losing each other's entries.
- `restore()`: rebuilds missing raw files from the manifest, for every medium. On restore,
  the path comes from the manifest entry, not from the id the fetcher would compute, so
  versioned snapshots restore to the right file.

`fetch_one.py` stays as a thin command-line wrapper (one-off fetches and `--restore`),
because CLAUDE.md and the README point at it.

### 2. Manifest format (unchanged fields, one addition)

Each entry keeps the phase 1 fields: `id, ref, url, medium, published, path, sha256`
(body hash), plus `commit` for GitHub. Added:

- `repo` (GitHub only, e.g. `karpathy/nanochat`): groups the snapshots of one README.
  Backfilled onto the two existing GitHub entries; this edits the manifest, not any raw file.
- `version` goes from 2 to 3.

### 3. Versioned GitHub snapshots

A README is a living document. Phase 1 pinned each README to the last commit that touched
it. Phase 2 keeps that and adds: when a collector run finds that a repo's README has a newer
commit than its latest snapshot, it writes a **new snapshot** instead of skipping the repo.

- The first snapshot keeps the plain id and path (`karpathy__nanochat`,
  `raw/github/karpathy__nanochat.md`), so the two existing raw files and their source pages
  are untouched (raw is immutable).
- Later snapshots get `<repo-id>@<short-commit>`, e.g. `raw/github/karpathy__nanochat@1a2b3c4.md`,
  dated by that commit.
- Old snapshots are never deleted; phase 3 can compare versions (a change in the README can
  be a change of view, which the wiki tracks on timeline pages).
- Backfill fetches the current README only; older README versions from 2023 to now are not
  reconstructed (possible later, since every version is in git history).

### 4. One idempotent collector per medium

Each collector does: **discover** candidates → **filter** (date, exclusions) → **fetch** only
what the manifest does not already have → write raw file and manifest entry → update the
coverage queue. Running it twice in a row fetches nothing the second time.

Common flags: `--dry-run` (print what would be fetched), `--limit N`, `--since 2023-01-01`,
`--priority teaching` (only items tagged teaching). Polite by default: a pause between
requests, retry with backoff, and a run that is cut off can simply be re-run.

| Script | Discovers from | Fetches | Notes |
|---|---|---|---|
| `collect_youtube.py` | his channel's video list (`yt-dlp --flat-playlist`) | captions with `[mm:ss]` blocks, metadata | same 30-second blocking as phase 1 |
| `collect_x.py` | twitterapi.io search `from:karpathy` since 2023 | one file per thread, posts in order | needs an API key (decision 1); without one, only fetches known post ids via fxtwitter, no discovery |
| `collect_github.py` | his public non-fork repos (`gh api users/karpathy/repos`) | README at its last commit; versioned snapshots | also GitHub Discussions he opened (e.g. the nanochat walkthroughs), via `gh api graphql`, his opening post only |
| `collect_blog.py` | karpathy.bearblog.dev post list and Atom feed | post body with links kept | phase 1 only read the feed, which holds recent posts; the post list covers older ones |
| `collect_talks.py` | the coverage queue only (no single feed exists) | captions for YouTube uploads on other channels; published transcripts from host pages | talks, podcasts, interviews; audio-only items without a transcript stay pending |

**Which medium is which:** `youtube` = a video on his own channel; `talk` = a talk, podcast or
interview hosted by someone else, wherever it is published. This rule goes into CLAUDE.md §3.
The phase 1 YC talk is on YC's channel but is filed as `youtube`; it stays as is and the
exception is recorded (decision 5).

Release notes and commit messages (listed in tech-stack) are out of scope for this phase;
READMEs and his discussion posts carry most of the explanatory text.

### 5. Coverage queue (`raw/_queue.json`, committed)

One list of everything we know exists, whether or not it has been fetched:

```json
{"ref": "karpathy/minbpe", "medium": "github", "url": "https://github.com/karpathy/minbpe",
 "status": "pending", "priority": "teaching", "found_in": "discovery:github",
 "reason": "", "title": "minbpe", "published": "2024-02-17"}
```

- `status`: `collected` (in the manifest), `pending` (known, not fetched yet), `excluded`
  (deliberately left out; `reason` is required, e.g. `before-2023`, `not-karpathy`,
  `reply-to-other`, `no-transcript`).
- `found_in`: where we learned about it, either a collector's discovery or a raw file path.
- `priority`: `teaching` or `other`. Teaching = lectures (his LLM and Zero to Hero series,
  the tokenizer and GPT-2 reproduction videos, "Intro to LLMs", "Deep Dive into LLMs") and
  teaching repos (nanoGPT, build-nanogpt, llm.c, minbpe, llama2.c, nanochat, LLM101n, and
  micrograd / makemore / minGPT if decision 2 allows them). The list is a starting point;
  the collectors tag anything else as `other` and the user can promote items.
- `collected` is derived, never hand-set: an item is collected exactly when the manifest
  has it. A test checks the two agree.

**Seeding from leads** (`scripts/seed_queue.py`): scan every raw file for links and classify
them. Links to his own posts, videos and repos become `pending` items with
`found_in: raw/...`. Known third-party sites (pytorch.org, huggingface.co, badges, Discord)
are dropped. Anything else that might be him (a podcast page, a talk write-up) becomes
`pending` with `reason: needs-triage` for a person to decide. The existing six raw files
already point at, for example, three more bearblog posts, nanochat discussions #1, #164,
#420 and #481, minGPT, llm-council, reader3, hn-time-capsule, the Zero to Hero page and
the Dwarkesh podcast. Seeding runs again after each collector, so new raw files add their
own leads.

The queue is `.json` so scripts can update it safely; a readable view is the coverage report.

### 6. Coverage report (`scripts/coverage.py`)

Writes `specs/phases/phase-2-collectors-and-backfill/coverage.md`: counts per medium and per
year by status, teaching vs other, the full pending list, and the excluded list with reasons.
This is the phase deliverable the user reviews, and the input for phase 3 batching.

### 7. Lint and the uncompiled backlog

Today `lint_check.py` reports every raw file without a source page as a finding. After the
backfill there will be many such files until phase 3 compiles them, so lint would fail for
a reason that is expected. Change: report them as an **uncompiled backlog** count, not as a
finding. Phase 3's gate then adds "backlog is zero". Every other raw check (manifest
present, hashes match) stays a finding.

## Approach and order

1. Shared raw store, `fetch_one.py` rewired onto it; existing tests still pass.
2. Manifest v3 (`repo` field) and the queue file; seed the queue from the six raw files.
3. Collectors, one at a time, each with stubbed-network tests, then a live `--limit 1` run.
   Order: github, youtube, blog, talks, x (x last because it depends on decision 1).
4. **Pilot batch**: `--priority teaching --limit` across collectors, about 10 items. The user
   spot-checks them before the full run.
5. Full backfill, collectors in parallel, teaching first. Re-seed; repeat until no new
   pending items appear that are in scope.
6. Coverage report; spot-check ten random raw files against the originals (phase gate).
7. Update specs in the same change as each decision: tech-stack (manifest v3, queue,
   medium rule), CLAUDE.md §3 (snapshot ids, medium rule, collectors replace fetch_one),
   roadmap.

## Out of scope

Writing wiki pages (phase 3); Whisper transcription of audio without captions (noted as
pending instead); release notes and commit messages; reconstructing old README versions;
scheduling and the morning brief (phase 5).

## Open decisions for the user

1. **X needs a twitterapi.io key.** There is none yet; phase 1 used the free fxtwitter API,
   which can fetch a post you already know the id of but cannot list his posts. To collect
   X from 2023 onward, you would create a twitterapi.io account, add credit (tech-stack
   estimates about a dollar for his archive; worth checking their current pricing first),
   and put the key in `.env` as `TWITTERAPI_IO_KEY` yourself. Without it, X coverage is
   limited to posts other sources link to.
2. **How far back.** The mission says 2023 onward, but much of his core teaching predates
   it: the Zero to Hero lectures on micrograd and makemore (2022) and repos like micrograd
   and minGPT. Options: (a) strict 2023 onward; (b) 2023 onward plus a teaching exception
   for the Zero to Hero series and its repos; (c) everything. Recommendation: (b), because
   teaching evidence is the gap phase 2 exists to close.
3. **Which X posts count.** Recommendation: his original posts, his own threads and quote
   posts; exclude retweets and replies to other people (recorded as `excluded`, so they can
   be added later).
4. **Which talks.** Recommendation: talks, podcasts and interviews that have captions or a
   published transcript; audio-only ones stay `pending: no-transcript` rather than being
   transcribed in this phase.
5. **The YC talk's medium.** It is a talk on another channel but filed as `youtube`.
   Recommendation: leave it (renaming would touch raw and its source page) and record it as
   a known exception.

## Decisions taken (2026-10-21)

The user asked to build without choosing, so the recommendations stand until changed:

1. X: the collector supports twitterapi.io, but no key exists, so X runs in fallback mode
   (known post ids via fxtwitter, no discovery). Adding `TWITTERAPI_IO_KEY` to `.env` and
   re-running `collect_x.py` fills the gap without code changes.
2. Scope: 2023 onward, plus a teaching exception for the Zero to Hero lectures and repos.
3. X posts: originals, own threads and quote posts; retweets and replies to others excluded.
4. Talks: only with captions or a published transcript; others stay `pending: no-transcript`.
5. The YC talk stays `medium: youtube`, recorded as a known exception.
