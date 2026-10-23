#!/usr/bin/env python3
"""Collect his GitHub READMEs as versioned snapshots, and the Discussions he opened.

A README is a living document. Each snapshot is pinned to the last commit that touched
the README and dated by that commit. When a later run finds a newer README commit, it
writes a new snapshot `<repo-id>@<short-commit>` instead of skipping the repo; old
snapshots stay. Discussions are his opening post only (the nanochat walkthroughs). Gists
linked from his posts are kept when they hold markdown (e.g. llm-wiki), pinned to a revision.

Uses the `gh` CLI, so no token is needed beyond `gh auth login`.

Usage: python scripts/collect_github.py [--dry-run] [--limit N] [--priority teaching]
"""
import json
import re
import sys
import tempfile
from pathlib import Path

import rawstore as rs
from rawstore import Skip

USER = "karpathy"
DISCUSSION = re.compile(r"([\w.-]+)/([\w.-]+)/discussions/(\d+)")
GIST = re.compile(r"gist/([0-9a-f]+)")


def gh(path, raw=False):
    cmd = ["gh", "api", path] + (["-H", "Accept: application/vnd.github.raw"] if raw else [])
    out = rs.run(cmd)
    return out if raw else json.loads(out)


def graphql(query, **variables):
    cmd = ["gh", "api", "graphql", "-f", f"query={query}"]
    for k, v in variables.items():
        cmd += ["-F", f"{k}={v}"]
    return json.loads(rs.run(cmd))["data"]


def repos():
    out = rs.run(["gh", "api", "--paginate", f"users/{USER}/repos?per_page=100", "--jq",
                  ".[] | {full_name, fork, html_url, pushed_at, has_discussions}"])
    return [json.loads(line) for line in out.splitlines() if line.strip()]


def discussions(repo):
    owner, name = repo.split("/")
    d = graphql("query($o:String!,$n:String!){repository(owner:$o,name:$n){discussions("
                "first:100){nodes{number title createdAt author{login}}}}}", o=owner, n=name)
    return [n for n in d["repository"]["discussions"]["nodes"]
            if (n["author"] or {}).get("login") == USER]


def readme_commit(repo):
    try:
        path = gh(f"repos/{repo}/readme")["path"]
    except Exception:
        raise Skip("excluded", "no-readme")
    return gh(f"repos/{repo}/commits?path={path}&per_page=1")[0]["sha"]


def readme(repo, commit=None):
    info = gh(f"repos/{repo}")
    # a README is a living document: pin it to the last commit that touched it, and date it
    # by that commit, so the snapshot can be fetched again exactly
    commit = commit or readme_commit(repo)
    c = gh(f"repos/{repo}/commits/{commit}")
    body = gh(f"repos/{repo}/readme?ref={commit}", raw=True)
    return dict(id=repo.replace("/", "__"), url=info["html_url"], medium="github",
                author="Andrej Karpathy", published=c["commit"]["committer"]["date"][:10],
                title=f"{info['name']} README", duration_or_length=f"{len(body.split())} words",
                commit=commit, repo=repo), body


def discussion(ref):
    owner, name, number = DISCUSSION.fullmatch(ref).groups()
    d = graphql("query($o:String!,$n:String!,$k:Int!){repository(owner:$o,name:$n){"
                "discussion(number:$k){title body url createdAt author{login}}}}",
                o=owner, n=name, k=number)["repository"]["discussion"]
    if (d["author"] or {}).get("login") != USER:
        raise Skip("excluded", "not-karpathy")
    return dict(id=f"{owner}__{name}__discussion-{number}", url=d["url"], medium="github",
                author="Andrej Karpathy", published=d["createdAt"][:10], title=d["title"],
                duration_or_length=f"{len(d['body'].split())} words"), d["body"]


def gist_files(gid, commit=None):
    """A gist is a small git repo: clone it (the REST API returns 502 for some of his gists)
    and read its files at `commit`, or at the latest revision."""
    with tempfile.TemporaryDirectory() as d:
        rs.run(["git", "clone", "--quiet", f"https://gist.github.com/{gid}.git", d])
        if commit:
            rs.run(["git", "-C", d, "checkout", "--quiet", commit])
        sha = rs.run(["git", "-C", d, "rev-parse", "HEAD"]).strip()
        date = rs.run(["git", "-C", d, "log", "-1", "--format=%cI"]).strip()[:10]
        files = {p.name: p.read_text(encoding="utf-8", errors="replace")
                 for p in sorted(Path(d).iterdir()) if p.is_file()}
    return files, sha, date


def gist(ref, commit=None):
    """A gist's markdown files, pinned to a revision. Code-only gists are not collected
    (code is linked, not copied); their prose lives in the post that links them. Only
    gists linked as gist.github.com/karpathy/<id> reach the queue."""
    gid = GIST.fullmatch(ref).group(1)
    files, sha, date = gist_files(gid, commit)
    docs = [(name, text) for name, text in files.items() if name.endswith(".md")]
    if not docs:
        raise Skip("excluded", "code-only gist")
    body = "\n\n".join(text for _, text in docs)
    return dict(id=f"{USER}__gist-{gid}", url=f"https://gist.github.com/{USER}/{gid}",
                medium="github", author="Andrej Karpathy", published=date,
                title=docs[0][0].removesuffix(".md"),
                duration_or_length=f"{len(body.split())} words", commit=sha), body


def fetch(ref, commit=None):
    if GIST.fullmatch(ref):
        return gist(ref, commit)
    return discussion(ref) if DISCUSSION.fullmatch(ref) else readme(ref, commit)


def fetch_item(item, since):
    return fetch(item["ref"])


def snapshots(repo):
    m = rs.read_manifest()["items"]
    return sorted((i for i in m if i["medium"] == "github" and
                   rs.key(i.get("repo") or i["ref"]) == rs.key(repo)),
                  key=lambda i: i["published"])


def refresh(q, args):
    """New snapshot for every collected repo whose README changed since its last snapshot."""
    repos_ = [i for i in q.of("github", "collected")
              if not DISCUSSION.fullmatch(i["ref"]) and not GIST.fullmatch(i["ref"])]
    done = 0
    for i in repos_:
        if args.limit is not None and done >= args.limit:
            break
        snaps = snapshots(i["ref"])
        try:
            latest = readme_commit(i["ref"])
        except Exception as e:
            print(f"error {i['ref']}: {e}", file=sys.stderr)
            continue
        if not snaps or latest in {s.get("commit") for s in snaps}:
            continue
        if args.dry_run:
            print(f"would snapshot {i['ref']} @ {latest[:7]}")
            continue
        meta, body = readme(i["ref"], latest)
        meta["id"] = f"{meta['id']}@{latest[:7]}"
        path = rs.save(meta, body, i["ref"])
        print(f"wrote {path} (README changed since {snaps[-1].get('commit', '')[:7]})")
        done += 1


def main(argv=None):
    args = rs.parser(__doc__).parse_args(argv)
    q = rs.Queue()
    for r in repos():
        ref = r["full_name"]
        new = q.get(ref) is None
        q.add(ref, medium="github", url=r["html_url"], title=ref.split("/")[1],
              priority=rs.priority("github", ref, ""), found_in="discovery:github")
        prio = q.get(ref)["priority"]
        if new and r["fork"]:
            q.set(ref, status="excluded", reason="fork")
        elif new and not rs.in_scope(r["pushed_at"][:10], prio, args.since):
            # not pushed since the cut-off, so its README cannot be newer either
            q.set(ref, status="excluded", reason=f"before-{args.since[:4]}")
        if r["has_discussions"] and not r["fork"]:
            for d in discussions(ref):
                dref = f"{ref}/discussions/{d['number']}"
                q.add(dref, medium="github", url=f"https://github.com/{dref}", title=d["title"],
                      published=d["createdAt"][:10], priority=prio,
                      found_in="discovery:github")
    if not args.dry_run:
        q.save()
    status = rs.collect(q, "github", fetch_item, args)
    refresh(q, args)
    return status


if __name__ == "__main__":
    sys.exit(main())
