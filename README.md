# karpathy-wiki

A personal "Karpathy brain": an LLM-compiled wiki of Andrej Karpathy's public ideas and
methods, plus a Claude Code agent that teaches and reviews code the way he does.

Built on his own [LLM Wiki pattern](https://x.com/karpathy): raw sources stay immutable,
the LLM owns the wiki, a `CLAUDE.md` schema governs it, and ingest / query / lint keep it
alive. Obsidian is the viewer.

- [DESIGN.md](DESIGN.md): how it works, with diagrams
- [specs/](specs/): mission, tech stack, roadmap and per-phase plans

`raw/` is not committed (it is his words). Rebuild it with the collectors in `scripts/`
using `raw/_manifest.json`.

## Setup

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m pytest tests      # lint checker's own tests
python3 scripts/lint_check.py         # wiki health; non-zero on any finding
```

Open the `karpathy-wiki/` folder as a vault in Obsidian to browse.
