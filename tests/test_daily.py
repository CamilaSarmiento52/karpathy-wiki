"""daily.py: report what is new since the last run, with collectors mocked."""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import daily  # noqa: E402


def write_manifest(root, paths):
    items = [{"path": p, "medium": "blog", "published": f"2026-11-0{i + 1}", "url": f"https://x/{i}"}
             for i, p in enumerate(paths)]
    (root / "raw").mkdir(exist_ok=True)
    (root / "raw" / "_manifest.json").write_text(json.dumps({"items": items}))


def write_queue(root, triage):
    items = [{"ref": r, "status": "pending", "reason": "needs-triage", "title": r, "url": r}
             for r in triage]
    (root / "raw" / "_queue.json").write_text(json.dumps({"items": items}))


def fake(adds=(), triage=(), fail=(), pending=()):
    def runner(root, name, weekly):
        if name == "blog" and adds:
            write_manifest(root, ["raw/blog/old.md", *adds])
        if name == "talks" and triage:
            write_queue(root, ["old-talk", *triage])
        tail = [f"pending {p}: rate-limited" for p in pending] if name == "youtube" else []
        return {"exit": 1 if name in fail else 0, "tail": tail or ["ok"]}
    return runner


def setup(tmp_path):
    write_manifest(tmp_path, ["raw/blog/old.md"])
    write_queue(tmp_path, ["old-talk"])
    return tmp_path


def report(root, date="2026-11-03"):
    return json.loads((root / "reports" / f"collect-{date}.json").read_text())


def test_first_run_reports_nothing_new(tmp_path, capsys):
    root = setup(tmp_path)
    daily.main(["--root", str(root), "--date", "2026-11-03"], runner=fake())
    r = report(root)
    assert r["new_raw"] == [] and r["new_triage"] == []
    assert capsys.readouterr().out.strip().endswith("new raw files: 0")


def test_new_raw_files_and_triage_since_last_run(tmp_path):
    root = setup(tmp_path)
    daily.main(["--root", str(root), "--date", "2026-11-03"], runner=fake())
    daily.main(["--root", str(root), "--date", "2026-11-04"],
               runner=fake(adds=["raw/blog/new.md"], triage=["new-talk"]))
    r = report(root, "2026-11-04")
    assert [x["path"] for x in r["new_raw"]] == ["raw/blog/new.md"]
    assert [x["ref"] for x in r["new_triage"]] == ["new-talk"]
    daily.main(["--root", str(root), "--date", "2026-11-05"], runner=fake())
    assert report(root, "2026-11-05")["new_raw"] == []


def test_failures_and_rate_limits_are_reported_not_raised(tmp_path):
    root = setup(tmp_path)
    code = daily.main(["--root", str(root), "--date", "2026-11-03"],
                      runner=fake(fail=["github"], pending=["vid1"]))
    r = report(root)
    assert code == 0
    assert r["collectors"]["github"]["ok"] is False
    assert r["collectors"]["youtube"]["pending"] == ["pending vid1: rate-limited"]


def test_weekly_flag_reaches_the_talks_collector(tmp_path):
    root, seen = setup(tmp_path), []
    daily.main(["--root", str(root), "--weekly", "--skip", "x"],
               runner=lambda r, n, w: seen.append((n, w)) or {"exit": 0, "tail": []})
    assert ("talks", True) in seen and all(n != "x" for n, _ in seen)
