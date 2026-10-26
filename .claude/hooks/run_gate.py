#!/usr/bin/env python3
"""Run gate for the karpathy sub-agent: "You have to run this before you say it works."

Two modes, both wired in the agent's own frontmatter so they apply only while that
sub-agent is running (Claude Code converts a sub-agent's Stop hook to SubagentStop):

  run_gate.py log    PostToolUse, matcher Write|Edit|Bash|NotebookEdit. Appends one line
                     per tool call to a per-agent log.
  run_gate.py check  Stop. Blocks the stop if the last code write in this agent's log was
                     never followed by a command that runs something.

The log lives in $KARPATHY_RUN_GATE_DIR (default: <tmp>/karpathy-run-gate), one file per
agent_id. Uses only documented hook input fields, not the transcript format.
"""
import json
import os
import re
import sys
import tempfile
from pathlib import Path

CODE_EXT = {".py", ".ipynb", ".js", ".mjs", ".ts", ".tsx", ".jsx", ".c", ".h", ".cc",
            ".cpp", ".cu", ".rs", ".go", ".java", ".rb", ".sh", ".swift", ".kt", ".jl"}
# commands that only look at or move files: they do not count as running the code
NON_RUNNING = {"ls", "cat", "head", "tail", "less", "more", "grep", "rg", "find", "echo",
               "printf", "pwd", "cd", "mkdir", "touch", "cp", "mv", "rm", "wc", "diff",
               "git", "tree", "stat", "file", "which", "true", "sed", "awk", "sort", "uniq"}
REASON = ("You have to run this before you say it works. You wrote or edited code ({files}) "
          "and have not run it since. Run it on a tiny input, show the real output next to "
          "what you predicted, then finish.")


def log_dir():
    return Path(os.environ.get("KARPATHY_RUN_GATE_DIR")
                or Path(tempfile.gettempdir()) / "karpathy-run-gate")


def log_path(agent_id):
    safe = re.sub(r"[^A-Za-z0-9_.-]", "_", agent_id or "main")
    return log_dir() / f"{safe}.jsonl"


def runs_something(command):
    """True if any segment of a shell command does more than look at or move files."""
    for segment in re.split(r"&&|\|\||;|\||\n", command or ""):
        words = [w for w in segment.strip().split() if "=" not in w.split("/")[0]]
        if words and os.path.basename(words[0]) not in NON_RUNNING:
            return True
    return False


def record(event):
    name, inp = event.get("tool_name"), event.get("tool_input") or {}
    if name in ("Write", "Edit", "MultiEdit", "NotebookEdit"):
        path = inp.get("file_path") or inp.get("notebook_path") or ""
        if Path(path).suffix.lower() not in CODE_EXT:
            return None
        return {"kind": "write", "path": path}
    if name == "Bash" and runs_something(inp.get("command", "")):
        return {"kind": "run", "command": inp.get("command", "")[:200]}
    return None


def unrun_writes(lines):
    """Code files written after the last command that ran something."""
    pending = []
    for line in lines:
        if line["kind"] == "run":
            pending = []
        elif line["path"] not in pending:
            pending.append(line["path"])
    return pending


def main(argv, stdin=sys.stdin):
    mode = argv[1] if len(argv) > 1 else ""
    try:
        event = json.load(stdin)
    except ValueError:
        return 0
    path = log_path(event.get("agent_id"))
    if mode == "log":
        line = record(event)
        if line:
            path.parent.mkdir(parents=True, exist_ok=True)
            with path.open("a") as f:
                f.write(json.dumps(line) + "\n")
        return 0
    if mode == "check":
        if event.get("stop_hook_active"):
            return 0  # already blocked once this stop; let it through rather than loop
        lines = []
        if path.exists():
            lines = [json.loads(l) for l in path.read_text().splitlines() if l.strip()]
        pending = unrun_writes(lines)
        if pending:
            names = ", ".join(Path(p).name for p in pending[:5])
            print(json.dumps({"decision": "block", "reason": REASON.format(files=names)}))
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
