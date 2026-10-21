"""Each test builds a tiny wiki in a temp dir, breaks one rule, and expects lint to say so."""
import hashlib
import importlib.util
import json
from pathlib import Path

spec = importlib.util.spec_from_file_location(
    "lint_check", Path(__file__).resolve().parent.parent / "scripts" / "lint_check.py")
lint = importlib.util.module_from_spec(spec)
spec.loader.exec_module(lint)

RAW = "---\nid: post\n---\n\nTokens are the atoms of the model, he wrote.\n"
SOURCE = """---
type: source
raw_path: raw/blog/post.md
published: 2025-01-01
medium: blog
summary: A post.
---
# Post
Raw: [[raw/blog/post]]

## Fed pages
- [[tok]]
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

## What he says
- Tokens come first ([[blog-post]]).
"""
INDEX = "# Index\n- [[blog-post]]\n- [[tok]]\n"


def manifest(raw_text):
    body = raw_text.split("---", 2)[2].strip()
    return json.dumps({"items": [{"id": "post", "path": "raw/blog/post.md",
                                  "sha256": hashlib.sha256(body.encode()).hexdigest()}]})


def base():
    return {
        "raw/blog/post.md": RAW,
        "raw/_manifest.json": manifest(RAW),
        "wiki/sources/blog-post.md": SOURCE,
        "wiki/topics/tok.md": TOPIC,
        "wiki/index.md": INDEX,
    }


def run(tmp_path, capsys, files):
    for rel, text in files.items():
        f = tmp_path / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(text)
    code = lint.main(tmp_path)
    return code, capsys.readouterr().out


def claim(quote, relation=""):
    return f"""---
type: claim
stated_on: 2025-01-01
confidence: stated
sources: ["[[blog-post]]"]
{relation}---
# Tokens are atoms
> "{quote}" — [[blog-post]]

## Context
He said so ([[blog-post]]).
"""


def with_claim(files, slug, text):
    files[f"wiki/claims/{slug}.md"] = text
    files["wiki/index.md"] += f"- [[{slug}]]\n"
    files["wiki/sources/blog-post.md"] += f"- [[{slug}]]\n"
    files["wiki/topics/tok.md"] += f"\n## Claims\n- [[{slug}]]\n"
    return files


def test_clean_wiki_passes(tmp_path, capsys):
    code, out = run(tmp_path, capsys, base())
    assert code == 0, out


def test_missing_frontmatter_field(tmp_path, capsys):
    files = base()
    files["wiki/topics/tok.md"] = TOPIC.replace("first_seen: 2025-01-01\n", "")
    code, out = run(tmp_path, capsys, files)
    assert code == 1 and "missing or empty frontmatter ['first_seen']" in out


def test_empty_sources_list(tmp_path, capsys):
    # review false negative: `sources: []` passed
    files = base()
    files["wiki/topics/tok.md"] = TOPIC.replace('sources: ["[[blog-post]]"]', "sources: []")
    code, out = run(tmp_path, capsys, files)
    assert "missing or empty frontmatter ['sources']" in out


def test_uncited_bullet(tmp_path, capsys):
    # review false negative: an uncited bullet in "What he says" passed
    files = base()
    files["wiki/topics/tok.md"] = TOPIC + "- An uncited fact.\n"
    code, out = run(tmp_path, capsys, files)
    assert "uncited block: wiki/topics/tok.md §What he says: '- An uncited fact.'" in out


def test_uncited_paragraph(tmp_path, capsys):
    files = base()
    files["wiki/topics/tok.md"] = TOPIC + "\nThis sentence has no citation.\n"
    code, out = run(tmp_path, capsys, files)
    assert "uncited block: wiki/topics/tok.md" in out


def test_invalid_enum_value(tmp_path, capsys):
    files = base()
    files["wiki/sources/blog-post.md"] = SOURCE.replace("medium: blog", "medium: podcast")
    code, out = run(tmp_path, capsys, files)
    assert "invalid medium 'podcast'" in out


def test_topic_dates_follow_sources(tmp_path, capsys):
    files = base()
    files["wiki/topics/tok.md"] = TOPIC.replace("first_seen: 2025-01-01", "first_seen: 2024-01-01")
    code, out = run(tmp_path, capsys, files)
    assert "first_seen should be 2025-01-01" in out


def test_source_cited_but_not_listed(tmp_path, capsys):
    files = base()
    files["wiki/topics/tok.md"] = TOPIC.replace('sources: ["[[blog-post]]"]', "sources: []\ncontext: []")
    code, out = run(tmp_path, capsys, files)
    assert "cited in body but not in sources: wiki/topics/tok.md -> blog-post" in out


def test_fed_pages_must_match(tmp_path, capsys):
    files = base()
    # tok cites the source and is linked from Key points, but is left out of Fed pages
    files["wiki/sources/blog-post.md"] = SOURCE.replace(
        "## Fed pages\n- [[tok]]\n", "## Key points\n- [[tok]]\n\n## Fed pages\n")
    code, out = run(tmp_path, capsys, files)
    assert "cites blog-post but missing from its Fed pages: tok" in out


def test_quote_must_be_in_raw(tmp_path, capsys):
    files = with_claim(base(), "atoms", claim("Tokens are the bricks of the model"))
    code, out = run(tmp_path, capsys, files)
    assert "quote not found in raw: wiki/claims/atoms.md" in out


def test_quote_found_passes(tmp_path, capsys):
    files = with_claim(base(), "atoms", claim("Tokens are the atoms of the model"))
    code, out = run(tmp_path, capsys, files)
    assert code == 0, out


def test_long_quote(tmp_path, capsys):
    files = with_claim(base(), "atoms", claim(" ".join(["word"] * 15)))
    code, out = run(tmp_path, capsys, files)
    assert "quote over 14 words" in out


def test_contradicts_must_be_two_way(tmp_path, capsys):
    files = with_claim(base(), "atoms", claim("Tokens are the atoms of the model",
                                              'contradicts: ["[[bricks]]"]\n'))
    files = with_claim(files, "bricks", claim("Tokens are the atoms of the model"))
    code, out = run(tmp_path, capsys, files)
    assert "contradicts not set on both sides: atoms -> bricks" in out
    assert "contradicts pair not on a timeline: atoms, bricks" in out


def test_manifest_hash_mismatch(tmp_path, capsys):
    files = base()
    files["raw/blog/post.md"] = RAW.replace("atoms", "bricks")
    code, out = run(tmp_path, capsys, files)
    assert "raw file does not match manifest hash: raw/blog/post.md" in out


def test_broken_link(tmp_path, capsys):
    files = base()
    files["wiki/topics/tok.md"] = TOPIC + "- See [[nowhere]] ([[blog-post]]).\n"
    code, out = run(tmp_path, capsys, files)
    assert "broken link: wiki/topics/tok.md -> [[nowhere]]" in out


def test_orphan_ignores_links_from_index(tmp_path, capsys):
    files = base()
    files["wiki/sources/blog-post.md"] = SOURCE.replace("- [[tok]]\n", "")
    code, out = run(tmp_path, capsys, files)
    assert "orphan: wiki/topics/tok.md" in out


def test_missing_raw_path(tmp_path, capsys):
    files = base()
    del files["raw/blog/post.md"]
    code, out = run(tmp_path, capsys, files)
    assert "raw_path not found" in out
    assert "manifest entry with no raw file" in out


def test_raw_file_without_source_page(tmp_path, capsys):
    files = base()
    files["raw/x/123.md"] = "---\nid: 123\n---\npost"
    code, out = run(tmp_path, capsys, files)
    assert "raw file with no source page: raw/x/123.md" in out
    assert "raw file not in manifest: raw/x/123.md" in out


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
