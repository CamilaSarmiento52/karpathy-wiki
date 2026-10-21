"""Shared bookkeeping for the collectors: raw files, the manifest and the coverage queue.

raw/<folder>/<id>.md      verbatim source with standard frontmatter (CLAUDE.md §3)
raw/_manifest.json        one entry per raw file: how it was fetched and a hash of its body
raw/_queue.json           everything we know exists: collected / pending / excluded

Collectors may run in parallel, so every write to the manifest or queue happens under a
file lock and re-reads the file inside the lock before saving.
"""
import argparse
import contextlib
import datetime as dt
import fcntl
import hashlib
import json
import re
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
FOLDER = {"youtube": "youtube", "x": "x", "github": "github", "blog": "blog", "talk": "talks"}
MEDIA = set(FOLDER)
SINCE = "2023-01-01"
UA = {"User-Agent": "Mozilla/5.0 (karpathy-wiki collector)"}
ORDER = ["id", "url", "medium", "author", "published", "fetched", "title",
         "duration_or_length", "commit"]
PAUSE = 1.0  # seconds between network requests; tests set it to 0


def raw(*parts):
    return ROOT.joinpath("raw", *parts)


# --- network --------------------------------------------------------------------------

def get(url, headers=None, tries=4):
    """GET with retry and backoff on rate limits and server errors."""
    for attempt in range(tries):
        time.sleep(PAUSE * attempt * 2)
        try:
            req = urllib.request.Request(url, headers={**UA, **(headers or {})})
            with urllib.request.urlopen(req, timeout=30) as r:
                return r.read().decode("utf-8")
        except urllib.error.HTTPError as e:
            if e.code not in (429, 500, 502, 503, 504) or attempt == tries - 1:
                raise
        except urllib.error.URLError:
            if attempt == tries - 1:
                raise


def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, check=True).stdout


def stamp(seconds):
    s = int(seconds)
    h, m, s = s // 3600, s // 60 % 60, s % 60
    return f"{h}:{m:02d}:{s:02d}" if h else f"{m:02d}:{s:02d}"


class Text(HTMLParser):
    """HTML to plain text, keeping paragraph breaks, headings, list bullets and links."""
    BLOCK = {"p", "div", "br", "li", "h1", "h2", "h3", "h4", "pre", "blockquote", "tr"}
    SKIP = {"script", "style", "nav", "header", "footer"}

    def __init__(self, base):
        super().__init__()
        self.out, self.base, self.href, self.skip = [], base, None, 0

    def handle_starttag(self, tag, attrs):
        if tag in self.SKIP:
            self.skip += 1
        if self.skip:
            return
        if tag in self.BLOCK:
            self.out.append("\n\n")
        if tag in ("h1", "h2", "h3", "h4"):
            self.out.append("#" * int(tag[1]) + " ")
        if tag == "li":
            self.out.append("- ")
        if tag == "a" and dict(attrs).get("href"):
            # keep link targets: they are leads to his other posts
            self.href = urllib.parse.urljoin(self.base, dict(attrs)["href"])
            self.out.append("[")

    def handle_endtag(self, tag):
        if tag in self.SKIP:
            self.skip = max(0, self.skip - 1)
            return
        if tag == "a" and self.href and not self.skip:
            self.out.append(f"]({self.href})")
            self.href = None

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)

    def text(self):
        return re.sub(r"\n{3,}", "\n\n", "".join(self.out)).strip()


def html_text(html, base):
    p = Text(base)
    p.feed(html)
    return p.text()


def region(html):
    """The main content of a page: <article>, else <main>, else <body>, else everything."""
    for tag in ("article", "main", "body"):
        m = re.search(rf"<{tag}\b[^>]*>(.*)</{tag}>", html, re.S | re.I)
        if m:
            return m.group(1)
    return html


# --- raw files and manifest -----------------------------------------------------------

def clean(body):
    # GitHub Discussions use \r\n; reading a file back turns that into \n, so normalise
    # before hashing and writing or the hash would never match the file
    return body.replace("\r\n", "\n").replace("\r", "\n").strip()


def digest(body):
    # hash the verbatim body only, so a refetch on another day (new `fetched`) still matches
    return hashlib.sha256(clean(body).encode()).hexdigest()


def default_path(meta):
    return f"raw/{FOLDER[meta['medium']]}/{meta['id']}.md"


def write(meta, body, path=None):
    """Write a raw file; `path` (repo-relative) defaults to raw/<folder>/<id>.md."""
    meta["fetched"] = dt.date.today().isoformat()
    fm = yaml.safe_dump({k: meta[k] for k in ORDER if k in meta}, sort_keys=False,
                        allow_unicode=True)
    full = ROOT / (path or default_path(meta))
    full.parent.mkdir(parents=True, exist_ok=True)
    full.write_text(f"---\n{fm}---\n\n{clean(body)}\n", encoding="utf-8")
    return full.relative_to(ROOT)


@contextlib.contextmanager
def locked():
    raw().mkdir(parents=True, exist_ok=True)
    with open(raw(".lock"), "w") as f:
        fcntl.flock(f, fcntl.LOCK_EX)
        try:
            yield
        finally:
            fcntl.flock(f, fcntl.LOCK_UN)


def read_manifest():
    p = raw("_manifest.json")
    return json.loads(p.read_text()) if p.exists() else {"version": 3, "items": []}


def _save_manifest(m):
    m["version"] = 3
    m["items"].sort(key=lambda i: (i["published"], i["id"]))
    raw("_manifest.json").write_text(json.dumps(m, indent=2) + "\n")


def add_entry(entry):
    with locked():
        m = read_manifest()
        m["items"] = [i for i in m["items"] if i["id"] != entry["id"]] + [entry]
        _save_manifest(m)


def save(meta, body, ref, path=None, repo=None):
    """Write a raw file and its manifest entry. Returns the repo-relative path."""
    path = write(meta, body, path)
    repo = repo or meta.get("repo")
    entry = dict(id=meta["id"], ref=ref, url=meta["url"], medium=meta["medium"],
                 published=meta["published"], path=str(path), sha256=digest(body))
    if "commit" in meta:
        entry["commit"] = meta["commit"]
    if repo:
        entry["repo"] = repo
    add_entry(entry)
    return path


def restore(fetch):
    """Rebuild missing raw files from the manifest; report any whose content changed.

    `fetch(medium, ref, commit)` returns (meta, body). The file goes to the manifest's
    path with the manifest's id, so versioned snapshots restore to the right place.
    """
    changed = 0
    for item in read_manifest()["items"]:
        if (ROOT / item["path"]).exists():
            continue
        meta, body = fetch(item["medium"], item["ref"], item.get("commit"))
        meta["id"] = item["id"]
        write(meta, body, item["path"])
        same = digest(body) == item["sha256"]
        changed += not same
        print(f"restored {item['path']}" + ("" if same else " (CONTENT CHANGED since manifest)"))
    return 1 if changed else 0


# --- coverage queue -------------------------------------------------------------------

STATUS = {"collected", "pending", "excluded"}
QUEUE_FIELDS = ["ref", "medium", "url", "status", "priority", "found_in", "reason", "title",
                "published"]


def key(ref):
    # GitHub names are case-insensitive; video and post ids are not; a URL is the same
    # page over http or https, with or without a trailing slash
    if re.fullmatch(r"[\w.-]+/[\w.-]+(/discussions/\d+)?", ref):
        return ref.lower()
    if ref.startswith(("http://", "https://")):
        return "https://" + ref.split("://", 1)[1].rstrip("/")
    return ref


class Skip(Exception):
    """Raised by a fetcher: do not collect this item; record why in the queue."""

    def __init__(self, status, reason, **fields):
        super().__init__(reason)
        self.status, self.reason, self.fields = status, reason, fields


class Queue:
    """The coverage queue. Changes are recorded as operations and replayed onto a fresh
    read of the file under the lock, so parallel collectors do not overwrite each other."""

    def __init__(self):
        self.ops = []
        self.items = {key(i["ref"]): i for i in self._read()["items"]}

    @staticmethod
    def _read():
        p = raw("_queue.json")
        return json.loads(p.read_text()) if p.exists() else {"version": 1, "items": []}

    @staticmethod
    def _apply(items, op):
        kind, ref, fields = op
        k = key(ref)
        if kind == "drop":
            items.pop(k, None)
        elif kind == "add":
            if k not in items:
                items[k] = {f: "" for f in QUEUE_FIELDS} | {"ref": ref, "status": "pending",
                                                            "priority": "other"} | fields
            else:  # fill blanks only; never overwrite a status or a human decision
                for f, v in fields.items():
                    if not items[k].get(f) and f not in ("status", "reason", "priority"):
                        items[k][f] = v
                # discovery may recognise teaching material that a lead added as "other"
                if fields.get("priority") == "teaching":
                    items[k]["priority"] = "teaching"
        else:
            items.setdefault(k, {f: "" for f in QUEUE_FIELDS} | {"ref": ref,
                                                                "priority": "other"})
            items[k].update(fields)

    def add(self, ref, **fields):
        op = ("add", ref, fields)
        self._apply(self.items, op)
        self.ops.append(op)

    def set(self, ref, **fields):
        if fields.get("status") and fields["status"] not in STATUS:
            raise ValueError(f"bad status {fields['status']!r}")
        if fields.get("status") == "excluded" and not fields.get("reason"):
            raise ValueError(f"excluding {ref} needs a reason")
        op = ("set", ref, fields)
        self._apply(self.items, op)
        self.ops.append(op)

    def drop(self, ref):
        op = ("drop", ref, {})
        self._apply(self.items, op)
        self.ops.append(op)

    def get(self, ref):
        return self.items.get(key(ref))

    def of(self, medium, status=None):
        return [i for i in self.items.values()
                if i["medium"] == medium and (status is None or i["status"] == status)]

    def save(self):
        with locked():
            items = {key(i["ref"]): i for i in self._read()["items"]}
            for op in self.ops:
                self._apply(items, op)
            derive(items, read_manifest())
            self.items = items
            out = sorted(items.values(),
                         key=lambda i: (i["medium"], str(i["published"]), i["ref"]))
            raw("_queue.json").write_text(json.dumps({"version": 1, "items": out}, indent=2)
                                          + "\n")
        self.ops = []


def derive(items, manifest):
    """`collected` means exactly "in the manifest", in both directions."""
    have = {}
    for e in manifest["items"]:
        for k in (key(e["ref"]), key(e["id"]), key(e.get("repo", ""))):
            have.setdefault(k, e)
    have.pop("", None)
    for k, i in items.items():
        e = have.get(k)
        if e:
            i.update(status="collected", reason="", medium=i["medium"] or e["medium"])
            i["published"] = i["published"] or e["published"]
            i["url"] = i["url"] or e["url"]
        elif i["status"] == "collected":
            i.update(status="pending", reason="")
    known = set(items)
    for e in manifest["items"]:
        ks = {key(e["ref"]), key(e["id"]), key(e.get("repo", ""))} - {""}
        if not ks & known:
            ref = e.get("repo") or e["ref"]
            items[key(ref)] = {f: "" for f in QUEUE_FIELDS} | dict(
                ref=ref, medium=e["medium"], url=e["url"], status="collected",
                priority=priority(e["medium"], ref, ""), found_in="manifest",
                published=e["published"])
            known.add(key(ref))


# --- scope ----------------------------------------------------------------------------

# His teaching material is prioritised (roadmap, "Known gaps"). The pre-2023 Zero to Hero
# lectures and their repos are in scope as an exception (phase 2 decision 2).
TEACHING_REPOS = {"nanogpt", "build-nanogpt", "llm.c", "minbpe", "llama2.c", "nanochat",
                  "llm101n", "micrograd", "makemore", "mingpt", "nn-zero-to-hero",
                  "ng-video-lecture"}
TEACHING_TITLE = re.compile(r"spelled-out|let's build|let's reproduce|building makemore|"
                            r"intro to large language models|deep dive into llms|"
                            r"how i use llms|microgpt", re.I)


def priority(medium, ref, title):
    if medium == "github":
        parts = ref.lower().split("/")
        if parts[1] in TEACHING_REPOS:
            return "teaching"
    if title and TEACHING_TITLE.search(title):
        return "teaching"
    return "other"


def in_scope(published, prio, since=SINCE):
    return str(published) >= since or prio == "teaching"


# --- shared collector loop ------------------------------------------------------------

def parser(doc):
    ap = argparse.ArgumentParser(description=doc)
    ap.add_argument("--dry-run", action="store_true", help="print what would be fetched")
    ap.add_argument("--limit", type=int, default=None, help="fetch at most N items")
    ap.add_argument("--since", default=SINCE, help="cut-off date (teaching items exempt)")
    ap.add_argument("--priority", choices=["teaching", "other"], default=None)
    return ap


def todo(q, medium, args):
    items = [i for i in q.of(medium, "pending") if i["reason"] != "needs-triage"]
    if args.priority:
        items = [i for i in items if i["priority"] == args.priority]
    items.sort(key=lambda i: (i["priority"] != "teaching", str(i["published"]), i["ref"]))
    return items


def collect(q, medium, fetch, args):
    """Fetch every pending queue item of `medium`, teaching first.

    `fetch(item, since)` returns (meta, body) or raises Skip. Saves the queue after each item, so
    an interrupted run keeps its progress and a re-run continues where it stopped.
    """
    items = todo(q, medium, args)
    if args.limit is not None:
        items = items[:args.limit]
    if args.dry_run:
        for i in items:
            print(f"would fetch {medium} {i['ref']} [{i['priority']}] {i['title']}")
        return 0
    errors = 0
    for i in items:
        try:
            if i["published"] and not in_scope(i["published"], i["priority"], args.since):
                raise Skip("excluded", f"before-{args.since[:4]}")
            meta, body = fetch(i, args.since)
            if not meta["published"]:
                raise Skip("pending", "no-date")
            if not in_scope(meta["published"], i["priority"], args.since):
                raise Skip("excluded", f"before-{args.since[:4]}", published=meta["published"])
            path = save(meta, body, meta.pop("ref", i["ref"]))
            q.set(i["ref"], title=i["title"] or meta["title"], published=meta["published"],
                  url=meta["url"])
            print(f"wrote {path} ({meta['duration_or_length']})")
        except Skip as s:
            q.set(i["ref"], status=s.status, reason=s.reason, **s.fields)
            print(f"{s.status} {i['ref']}: {s.reason}")
        except Exception as e:  # stays pending; a re-run retries it
            errors += 1
            print(f"error {i['ref']}: {type(e).__name__}: {e}", file=sys.stderr)
        q.save()
        time.sleep(PAUSE)
    q.save()
    return 1 if errors else 0
