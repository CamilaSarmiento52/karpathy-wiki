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


def test_raw_file_without_source_page_is_backlog(tmp_path, capsys):
    # phase 2: collectors add raw files before ingest compiles them; that is not an error
    files = base()
    files["raw/x/123.md"] = "---\nid: 123\n---\n\npost\n"
    items = json.loads(files["raw/_manifest.json"])["items"]
    items.append({"id": "123", "path": "raw/x/123.md",
                  "sha256": hashlib.sha256(b"post").hexdigest()})
    files["raw/_manifest.json"] = json.dumps({"items": items})
    code, out = run(tmp_path, capsys, files)
    assert code == 0
    assert "(1 not yet compiled)" in out


def test_uncompiled_raw_file_still_needs_manifest(tmp_path, capsys):
    files = base()
    files["raw/x/123.md"] = "---\nid: 123\n---\npost"
    code, out = run(tmp_path, capsys, files)
    assert "raw file not in manifest: raw/x/123.md" in out


def test_link_to_versioned_snapshot_resolves(tmp_path, capsys):
    files = base()
    snap = "raw/github/k__repo@1a2b3c4.md"
    files[snap] = "---\nid: k__repo@1a2b3c4\n---\n\nreadme\n"
    items = json.loads(files["raw/_manifest.json"])["items"]
    items.append({"id": "k__repo@1a2b3c4", "path": snap,
                  "sha256": hashlib.sha256(b"readme").hexdigest()})
    files["raw/_manifest.json"] = json.dumps({"items": items})
    files["wiki/topics/tok.md"] = TOPIC + "- Readme [[raw/github/k__repo@1a2b3c4]] ([[blog-post]]).\n"
    code, out = run(tmp_path, capsys, files)
    assert "broken link" not in out


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


SPLIT_TOP = "# Index\n" + "".join(f"- [[{n}]]\n" for n in sorted(set(lint.TYPE_INDEX.values())))


def split_index(**overrides):
    files = {f"wiki/index/{n}.md": f"# {n}\n" for n in set(lint.TYPE_INDEX.values())}
    files["wiki/index/sources.md"] = "# Sources\n- [[blog-post]]\n"
    files["wiki/index/topics.md"] = "# Topics\n- [[tok]]\n"
    files["wiki/index.md"] = SPLIT_TOP
    files.update(overrides)
    return files


def test_split_index_counts_as_coverage(tmp_path, capsys):
    files = base()
    files.update(split_index())
    code, out = run(tmp_path, capsys, files)
    assert code == 0, out


def test_split_index_links_are_not_inbound(tmp_path, capsys):
    files = base()
    files["wiki/sources/blog-post.md"] = SOURCE.replace("- [[tok]]\n", "")
    files["wiki/topics/tok.md"] = TOPIC.replace("[[blog-post]]", "[[blog-post]]")
    files.update(split_index())
    code, out = run(tmp_path, capsys, files)
    assert "orphan: wiki/topics/tok.md" in out


def test_page_missing_from_its_type_index(tmp_path, capsys):
    files = base()
    files.update(split_index(**{"wiki/index/topics.md": "# Topics\n",
                                "wiki/index/sources.md": "# Sources\n- [[blog-post]]\n- [[tok]]\n"}))
    code, out = run(tmp_path, capsys, files)
    assert "not in index/topics.md: wiki/topics/tok.md" in out


def test_split_index_needs_every_type_file(tmp_path, capsys):
    files = base()
    files.update(split_index())
    del files["wiki/index/methods.md"]
    code, out = run(tmp_path, capsys, files)
    assert "missing index file: wiki/index/methods.md" in out


RAW2 = "---\nid: talk\n---\n\n[00:00] Always predict the loss before you run it.\n"


def principle(status, quotes, inferred="false", body="Predict first."):
    q = "".join(f'  - {{text: "{t}", source: "[[{s}]]", location: "{loc}"}}\n' for t, s, loc in quotes)
    return f"---\ntype: principle\nstatus: {status}\ninferred: {inferred}\nquotes:\n{q}---\n# Predict the loss\n{body}\n"


def principle_repo(status, quotes, folder=None, **kw):
    files = base()
    files["raw/talks/talk.md"] = RAW2
    items = json.loads(manifest(RAW))["items"] + [{"id": "talk", "path": "raw/talks/talk.md",
        "sha256": hashlib.sha256(RAW2.split("---", 2)[2].strip().encode()).hexdigest()}]
    files["raw/_manifest.json"] = json.dumps({"items": items})
    files["wiki/sources/talk-a.md"] = SOURCE.replace("raw/blog/post.md", "raw/talks/talk.md").replace(
        "[[raw/blog/post]]", "[[raw/talks/talk]]").replace("- [[tok]]", "- [[predict]]")
    files["wiki/sources/blog-post.md"] = SOURCE.replace("- [[tok]]\n", "- [[tok]]\n" + (
        "- [[predict]]\n" if any(s == "blog-post" for _, s, _ in quotes) else ""))
    folder = folder or ("wiki/principles/_bench" if status == "bench" else "wiki/principles")
    files[f"{folder}/predict.md"] = principle(status, quotes, **kw)
    files["wiki/topics/tok.md"] = TOPIC + "\n## Related\n- [[predict]] ([[blog-post]])\n"
    files["wiki/index.md"] = INDEX + "- [[talk-a]]\n- [[predict]]\n"
    return files


Q_TALK = ("Always predict the loss before you run it.", "talk-a", "00:00")
Q_BLOG = ("Tokens are the atoms of the model", "blog-post", "§intro")


def test_promoted_principle_with_two_sources_passes(tmp_path, capsys):
    code, out = run(tmp_path, capsys, principle_repo("promoted", [Q_TALK, Q_BLOG]))
    assert "independent" not in out and "principle" not in out.split("findings")[0], out


def test_promoted_principle_with_one_source_fails(tmp_path, capsys):
    code, out = run(tmp_path, capsys, principle_repo("promoted", [Q_TALK]))
    assert "needs quotes from 2+ independent sources (has 1)" in out


def test_same_text_sources_count_once(tmp_path, capsys):
    files = principle_repo("promoted", [Q_TALK, Q_BLOG])
    files["scripts/independence.json"] = json.dumps({"same_text": [["talk-a", "blog-post"]]})
    code, out = run(tmp_path, capsys, files)
    assert "(has 1)" in out


def test_ai_written_part_does_not_count(tmp_path, capsys):
    files = principle_repo("promoted", [Q_TALK, Q_BLOG])
    files["scripts/independence.json"] = json.dumps({"ai_written": {"blog-post": ["§mine"]}})
    code, out = run(tmp_path, capsys, files)
    assert "quotes an AI-written part of blog-post" in out and "(has 1)" in out


def test_bench_principle_with_two_sources_is_promotable(tmp_path, capsys):
    code, out = run(tmp_path, capsys, principle_repo("bench", [Q_TALK, Q_BLOG]))
    assert "promote it" in out


def test_principle_in_wrong_folder(tmp_path, capsys):
    code, out = run(tmp_path, capsys, principle_repo("bench", [Q_TALK], folder="wiki/principles"))
    assert "in wrong folder" in out


def test_inferred_principle_must_say_so(tmp_path, capsys):
    code, out = run(tmp_path, capsys, principle_repo("bench", [Q_TALK], inferred="true"))
    assert "must say so in its body" in out
    code, out = run(tmp_path, capsys, principle_repo(
        "bench", [Q_TALK], inferred="true", body="Inferred: no quote states this directly."))
    assert "must say so" not in out


def test_principle_quote_needs_location(tmp_path, capsys):
    code, out = run(tmp_path, capsys, principle_repo("bench", [(Q_TALK[0], "talk-a", "")]))
    assert "without a location" in out


def test_inferred_principle_cannot_be_promoted(tmp_path, capsys):
    code, out = run(tmp_path, capsys, principle_repo(
        "promoted", [Q_TALK, Q_BLOG], inferred="true", body="Inferred: closest quotes only."))
    assert "inferred principle cannot be promoted" in out


def test_inferred_bench_principle_with_two_sources_is_not_promotable(tmp_path, capsys):
    code, out = run(tmp_path, capsys, principle_repo(
        "bench", [Q_TALK, Q_BLOG], inferred="true", body="Inferred: closest quotes only."))
    assert "promote it" not in out
