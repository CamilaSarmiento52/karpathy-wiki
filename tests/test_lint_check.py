"""Each test builds a tiny wiki in a temp dir, breaks one rule, and expects lint to say so."""
import importlib.util
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "lint_check", Path(__file__).resolve().parent.parent / "scripts" / "lint_check.py")
lint = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lint)

SOURCE = """---
type: source
raw_path: raw/blog/post.md
published: 2025-01-01
medium: blog
summary: A post.
---
# Post
Raw: [[raw/blog/post]]
Fed: [[tok]]
"""
TOPIC = """---
type: topic
aliases: [Tokenization]
first_seen: 2025-01-01
last_updated: 2025-01-01
sources: ["[[blog-post]]"]
---
# Tokenization
He says tokens are the atoms ([[blog-post]]).
"""
INDEX = "# Index\n- [[blog-post]]\n- [[tok]]\n"


def make(tmp_path, files):
    for rel, text in files.items():
        f = tmp_path / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(text)
    return tmp_path


def base():
    return {
        "raw/blog/post.md": "---\nid: post\n---\nwords",
        "wiki/sources/blog-post.md": SOURCE,
        "wiki/topics/tok.md": TOPIC,
        "wiki/index.md": INDEX,
    }


def run(tmp_path, capsys, files):
    code = lint.main(make(tmp_path, files))
    return code, capsys.readouterr().out


def test_clean_wiki_passes(tmp_path, capsys):
    code, out = run(tmp_path, capsys, base())
    assert code == 0, out


def test_missing_frontmatter_field(tmp_path, capsys):
    files = base()
    files["wiki/topics/tok.md"] = TOPIC.replace("first_seen: 2025-01-01\n", "")
    code, out = run(tmp_path, capsys, files)
    assert code == 1 and "missing frontmatter ['first_seen']" in out


def test_broken_link(tmp_path, capsys):
    files = base()
    files["wiki/topics/tok.md"] = TOPIC + "\nSee [[nowhere]] ([[blog-post]]).\n"
    code, out = run(tmp_path, capsys, files)
    assert "broken link: wiki/topics/tok.md -> [[nowhere]]" in out


def test_orphan_ignores_links_from_index(tmp_path, capsys):
    files = base()
    files["wiki/sources/blog-post.md"] = SOURCE.replace("Fed: [[tok]]\n", "")
    code, out = run(tmp_path, capsys, files)
    assert "orphan: wiki/topics/tok.md" in out


def test_missing_raw_path(tmp_path, capsys):
    files = base()
    del files["raw/blog/post.md"]
    code, out = run(tmp_path, capsys, files)
    assert "raw_path not found" in out


def test_raw_file_without_source_page(tmp_path, capsys):
    files = base()
    files["raw/x/123.md"] = "---\nid: 123\n---\npost"
    code, out = run(tmp_path, capsys, files)
    assert "raw file with no source page: raw/x/123.md" in out


def test_uncited_paragraph(tmp_path, capsys):
    files = base()
    files["wiki/topics/tok.md"] = TOPIC + "\nThis sentence has no citation.\n"
    code, out = run(tmp_path, capsys, files)
    assert "uncited paragraph: wiki/topics/tok.md" in out


def test_page_not_in_index(tmp_path, capsys):
    files = base()
    files["wiki/index.md"] = "# Index\n- [[blog-post]]\n"
    code, out = run(tmp_path, capsys, files)
    assert "not in index: wiki/topics/tok.md" in out


def test_wrong_folder(tmp_path, capsys):
    files = base()
    files["wiki/claims/tok.md"] = files.pop("wiki/topics/tok.md")
    code, out = run(tmp_path, capsys, files)
    assert "type topic in wrong folder" in out
