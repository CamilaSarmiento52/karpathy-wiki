# Phase 2 — Collectors and backfill: implementation notes

_Written during implementation, 2026-10-21. What was built, decisions made while building,
deviations from the plan._

## What was built

| File | What it does |
|---|---|
| `scripts/rawstore.py` | shared bookkeeping: raw file writing, body hash, manifest and queue under a file lock, restore, the shared collect loop, teaching tags and the date cut-off |
| `scripts/collect_youtube.py` | lists his channel with yt-dlp, captions via youtube-transcript-api in ~30 s `[mm:ss]` blocks |
| `scripts/collect_github.py` | his non-fork repos (README pinned to its last commit, new `@<commit>` snapshot when it changes), Discussions he opened, markdown gists |
| `scripts/collect_blog.py` | karpathy.bearblog.dev (list page + feed) and the old karpathy.github.io (feed) |
| `scripts/collect_talks.py` | talks/podcasts from the queue: YouTube uploads on other channels, or pages with a transcript; `--search` queues YouTube search results for triage |
| `scripts/collect_x.py` | twitterapi.io discovery with thread grouping; post text from fxtwitter; known posts only without a key |
| `scripts/fetch_one.py` | now a thin wrapper: one-off fetches and `--restore` for all five media |
| `scripts/coverage_queue.py` | `seed` (leads from raw files), `add`, `set`, `check` |
| `scripts/coverage_report.py` | writes `coverage.md` in this folder |
| `scripts/spot_check.py` | prints N random raw files for the phase-gate spot check |
| `scripts/lint_check.py` | raw files without a source page are now an "uncompiled backlog" count, not findings |
| `raw/_queue.json` | the coverage queue, committed (gitignore exception) |

Manifest is version 3: GitHub README entries carry `repo`; X thread entries carry all post
ids in `ref`. The two phase 1 GitHub entries were given `repo` in place.

## The backfill

82 raw files (6 from phase 1, 76 new); 205 queue items: 82 collected, 0 pending, 123
excluded. Full numbers in [coverage.md](coverage.md).

- **Teaching material**: all 12 lecture videos on his channel (Zero to Hero series,
  Intro to LLMs, tokenizer, GPT-2 reproduction, Deep Dive, How I use LLMs), 25 GitHub items
  (READMEs of nanoGPT, minGPT, micrograd, makemore, minbpe, llm.c, llama2.c, build-nanogpt,
  nanochat, LLM101n, nn-zero-to-hero, ng-video-lecture, and his walkthrough Discussions in
  llm.c, nanochat and minbpe), the microgpt post, and three teaching talks: Stanford CS25,
  State of GPT (Microsoft Build 2023) and the CUDA MODE keynote on building llm.c.
- **Talks**: 9 collected (CS25, State of GPT, CUDA MODE keynote, Sequoia 2024 and 2026,
  No Priors x2, Berkeley hackathon, Dwarkesh), all official uploads by the host.
- **Talk search (2026-10-22, at the user's request)**: `collect_talks.py --search` ran
  eight YouTube searches for his name and kept long videos (15 min+) with "Karpathy" in the
  title that are not on his own channel: 48 candidates, 40 new. Triage approved one (the
  CUDA MODE keynote, uploaded by Accel) and excluded 39: 17 unofficial re-uploads of talks
  already collected (matched by length and opening), 11 videos about him by others
  (summaries, commentary, news), 10 Tesla-era or older talks, 1 dubbed copy. Both videos
  the user pointed at were already covered: `96jN2OCOfLs` is the collected Sequoia 2026
  talk, `EsQ_bmXKA4A` a re-upload of the collected Stanford CS25 lecture.
- **X**: 10 posts, all leads from other sources (no API key, so no discovery).
- **Independent counts** (phase gate 1): GitHub profile shows 63 public repos, the queue
  has 63 (21 collected, 33 before 2023, 9 forks). His channel lists 17 videos, all 17 are
  in the queue (12 collected, 5 excluded 2022 non-teaching). The bearblog post list has 13
  posts, all collected; the old blog feed has 10 entries, 1 collected (microgpt, 2026), 9
  before 2023.
- **Spot check** (phase gate 2): ten random files read against expectations; right
  author, dates, complete bodies, timestamps running to the end of each video. It caught
  the blog page-fallback problem below.

## Decisions made while building

- **The five decisions** were taken as recommended (plan.md, "Decisions taken"), because
  the user asked to build without choosing.
- **One queue key per item, across media.** A YouTube id is the same item whether it was
  seen as a lead or on his channel; GitHub names compare case-insensitively; a URL is the
  same over http or https. The queue records operations and replays them on a fresh read
  under the lock, so parallel collectors do not overwrite each other.
- **`collected` is derived from the manifest**, never set by hand, and
  `coverage_queue.py check` verifies it in both directions.
- **Discovery may raise priority to teaching but never lowers it**, and never overwrites a
  status or reason a person set.
- **Lead triage is narrow.** Only links that could be his own writing (his domains, his
  gists, his Medium) go to a person; product, paper and docs links are dropped. The first
  version sent ~100 product links to triage, which is noise.
- **Gists are fetched with `git clone`**, not the REST API, which returned HTTP 502 for two
  of his gists. A gist is kept only if it contains markdown (`llm-wiki` is: the idea file of
  the pattern this project implements); code-only gists are excluded with a reason, as the
  code is linked, not copied.
- **X Articles have no text in the post.** The one found duplicates his blog post
  "Power to the people", so it is excluded as a duplicate; the collector now leaves empty
  posts pending as `no-text (X article)` instead of writing an empty file.
- **YouTube rate limits are a pending reason, not an error.** After ~25 transcript
  requests YouTube blocked both the transcript API and yt-dlp subtitle downloads (HTTP 429).
  Items stay `pending: rate-limited`; a later re-run collects them.
- **Talk transcripts include other speakers.** CLAUDE.md §3 now says to attribute only
  what he says.

## Deviations from the plan

- **Tools renamed**: `seed_queue.py` → `coverage_queue.py` (also add/set/check) and
  `coverage.py` → `coverage_report.py`, because `queue` and `coverage` would shadow a
  standard-library module and a common package when scripts import each other.
- **One test file for the collectors** (`tests/test_collectors.py`) instead of one per
  medium; they share fixtures.
- **Gists added** to the GitHub collector (not in the plan), for `llm-wiki`.
- **`--search` added** to the talks collector after the user asked for interviews and
  lectures on other channels (the plan had talks as queue-only).
- **The pilot was spot-checked by me, not the user**, before the full run, since the user
  asked for the phase to be built. Raw files are reproducible and uncompiled, so nothing
  downstream depends on them yet.
- **Raw files rewritten by the collector three times** while fixing collector bugs, before
  anything was compiled from them: the empty X Article file was removed; three blog posts
  read from their web page were refetched without the repeated title/date line; 14
  Discussion files were refetched after the line-ending fix below.

## Bugs found by running it for real

1. **Discussion hashes never matched.** GitHub Discussion bodies use `\r\n`; the hash was
   taken before writing, but reading the file back turns `\r\n` into `\n`. The restore
   check passed anyway because it compared two hashes of the same unnormalised text; only
   lint, which reads the files, caught it. Bodies are now normalised before hashing and
   writing.
2. **Blog list regex** missed every post: real markup closes an `<i>` between the date and
   the link.
3. **State of GPT captions** are labelled `en-US`, not `en`; the collector now accepts both.
4. **YouTube captions were downloaded for videos then excluded by date**; the date is now
   checked from metadata first.

## Known gaps

- **X has no discovery** until a `TWITTERAPI_IO_KEY` is in `.env`. The search, thread
  grouping and exclusions are tested against the documented response shape but have never
  run against the live API.
- **Nothing pending.** State of GPT was collected once YouTube lifted its rate limit; the
  last linked video turned out to be removed and is excluded as unavailable.
- **Pre-2023 teaching writing is excluded by decision 2**, e.g. "A Recipe for Training
  Neural Networks" (2019) and "Deep Reinforcement Learning: Pong from Pixels" (2016) on the
  old blog, and his 2017 Medium posts. Promoting them is one `coverage_queue.py set`.
- **Talk discovery is search-based and needs a person**: YouTube search is not exhaustive
  and is mostly re-uploads and commentary, so every result waits in triage. Talks whose
  title does not name him, and podcasts not on YouTube, are only found through leads.
- **README history before the first snapshot** is not reconstructed.
- **A repo excluded as before-2023 is not re-checked** if its README later changes; only
  collected repos get new snapshots.
