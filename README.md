# karpathy-wiki

A personal "Karpathy brain": an LLM-compiled wiki of Andrej Karpathy's public ideas and
methods, plus (planned) a Claude Code agent that teaches and reviews code the way he does.

**Status:** phase 2 of 5 — collectors built and the backfill collected into `raw/`; the
wiki still holds the six-source pilot until phase 3 compiles the rest. The agent, the
teach/review/ingest skills, scheduling and the run gate are designed but not built yet;
see [specs/roadmap.md](specs/roadmap.md).

Built on his own [LLM Wiki pattern](https://x.com/karpathy): raw sources stay immutable,
the LLM owns the wiki, a `CLAUDE.md` schema governs it, and ingest / query / lint keep it
alive. Obsidian is the viewer.

- [DESIGN.md](DESIGN.md): how it works, with diagrams
- [specs/](specs/): mission, tech stack, roadmap and per-phase plans

`raw/` is not committed (it is his words). `raw/_manifest.json` records what was fetched
and `raw/_queue.json` what is known but pending or excluded, with reasons; rebuild missing
files with `.venv/bin/python scripts/fetch_one.py --restore`. GitHub READMEs come
back exactly (pinned commit); other sources are only as stable as their URLs, and any
changed content is reported.

## Setup

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m pytest tests      # lint and collector tests (no network)
python3 scripts/lint_check.py         # structural lint; non-zero on any finding
```

Collecting (each is idempotent; `--dry-run` shows what it would fetch):

```bash
.venv/bin/python scripts/collect_github.py     # also collect_youtube, _blog, _talks, _x
.venv/bin/python scripts/collect_talks.py --search  # queue YouTube search results for triage
.venv/bin/python scripts/coverage_queue.py seed     # add leads found in raw files
.venv/bin/python scripts/coverage_report.py         # write the coverage report
```

X discovery needs a twitterapi.io key in `.env` as `TWITTERAPI_IO_KEY`.

Open the `karpathy-wiki/` folder as a vault in Obsidian to browse.

A clean lint means the wiki is well-formed (links, frontmatter, citations present, quotes
found in raw, manifest hashes). It does not mean every summary is right; that takes the
semantic review described in `CLAUDE.md`.
