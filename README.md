# karpathy-wiki

A personal "Karpathy brain": an LLM-compiled wiki of Andrej Karpathy's public ideas and
methods, plus (planned) a Claude Code agent that teaches and reviews code the way he does.

**Status:** phase 1 of 5 — schema and a six-source pilot wiki. The collectors, the agent,
the teach/review/ingest skills, scheduling and the run gate are designed but not built yet;
see [specs/roadmap.md](specs/roadmap.md).

Built on his own [LLM Wiki pattern](https://x.com/karpathy): raw sources stay immutable,
the LLM owns the wiki, a `CLAUDE.md` schema governs it, and ingest / query / lint keep it
alive. Obsidian is the viewer.

- [DESIGN.md](DESIGN.md): how it works, with diagrams
- [specs/](specs/): mission, tech stack, roadmap and per-phase plans

`raw/` is not committed (it is his words). `raw/_manifest.json` records what was fetched;
rebuild missing files with `python3 scripts/fetch_one.py --restore`. GitHub READMEs come
back exactly (pinned commit); other sources are only as stable as their URLs, and any
changed content is reported.

## Setup

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m pytest tests      # lint checker's own tests
python3 scripts/lint_check.py         # structural lint; non-zero on any finding
```

Open the `karpathy-wiki/` folder as a vault in Obsidian to browse.

A clean lint means the wiki is well-formed (links, frontmatter, citations present, quotes
found in raw, manifest hashes). It does not mean every summary is right; that takes the
semantic review described in `CLAUDE.md`.
