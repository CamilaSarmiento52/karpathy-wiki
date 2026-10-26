"""run_gate.py: block a stop when code was written and not run afterwards."""
import importlib.util
import io
import json
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "run_gate", Path(__file__).resolve().parent.parent / ".claude" / "hooks" / "run_gate.py")
gate = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gate)


def call(mode, event, capsys):
    gate.main(["run_gate.py", mode], io.StringIO(json.dumps(event)))
    return capsys.readouterr().out


def write(path, agent="a1"):
    return {"agent_id": agent, "tool_name": "Write", "tool_input": {"file_path": path}}


def bash(command, agent="a1"):
    return {"agent_id": agent, "tool_name": "Bash", "tool_input": {"command": command}}


def stop(agent="a1", active=False):
    return {"agent_id": agent, "stop_hook_active": active}


def blocked(out):
    return bool(out) and json.loads(out)["decision"] == "block"


def setup(tmp_path, monkeypatch):
    monkeypatch.setenv("KARPATHY_RUN_GATE_DIR", str(tmp_path))


def test_code_written_never_run_blocks(tmp_path, monkeypatch, capsys):
    setup(tmp_path, monkeypatch)
    call("log", write("/w/bpe.py"), capsys)
    out = call("check", stop(), capsys)
    assert blocked(out) and "bpe.py" in json.loads(out)["reason"]


def test_code_written_then_run_allows(tmp_path, monkeypatch, capsys):
    setup(tmp_path, monkeypatch)
    call("log", write("/w/bpe.py"), capsys)
    call("log", bash("cd /w && python bpe.py"), capsys)
    assert not blocked(call("check", stop(), capsys))


def test_no_code_allows(tmp_path, monkeypatch, capsys):
    setup(tmp_path, monkeypatch)
    call("log", write("/w/notes.md"), capsys)
    assert not blocked(call("check", stop(), capsys))


def test_edit_after_run_blocks_again(tmp_path, monkeypatch, capsys):
    setup(tmp_path, monkeypatch)
    call("log", write("/w/bpe.py"), capsys)
    call("log", bash("python bpe.py"), capsys)
    call("log", {"agent_id": "a1", "tool_name": "Edit", "tool_input": {"file_path": "/w/bpe.py"}}, capsys)
    assert blocked(call("check", stop(), capsys))


def test_looking_at_a_file_is_not_running_it(tmp_path, monkeypatch, capsys):
    setup(tmp_path, monkeypatch)
    call("log", write("/w/bpe.py"), capsys)
    call("log", bash("cat bpe.py && ls -la"), capsys)
    assert blocked(call("check", stop(), capsys))


def test_blocks_up_to_three_times_then_lets_through(tmp_path, monkeypatch, capsys):
    setup(tmp_path, monkeypatch)
    call("log", write("/w/bpe.py"), capsys)
    outs = [call("check", stop(active=i > 0), capsys) for i in range(4)]
    assert [blocked(o) for o in outs] == [True, True, True, False]
    assert "block 3 of 3" in json.loads(outs[2])["reason"]
    assert "even if the request said not to run" in json.loads(outs[0])["reason"]


def test_agents_are_kept_apart(tmp_path, monkeypatch, capsys):
    setup(tmp_path, monkeypatch)
    call("log", write("/w/bpe.py", agent="a1"), capsys)
    assert not blocked(call("check", stop(agent="a2"), capsys))


def test_runs_something():
    assert gate.runs_something("FOO=1 python x.py")
    assert gate.runs_something("cd /w && pytest -q")
    assert not gate.runs_something("cat x.py | head -5")
    assert not gate.runs_something("git status; ls")


def test_answer_that_admits_code_was_not_run_may_finish(tmp_path, monkeypatch, capsys):
    setup(tmp_path, monkeypatch)
    call("log", write("/w/add.py"), capsys)
    ev = stop(); ev["last_assistant_message"] = "done. The file was never run, so it is unverified."
    assert not blocked(call("check", ev, capsys))
    ev["last_assistant_message"] = "done, it works."
    assert blocked(call("check", ev, capsys))
