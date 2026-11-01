"""Check local links in the documentation without requesting external URLs."""

import os
import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

from cmarkgfm import github_flavored_markdown_to_html
from cmarkgfm.cmark import Options
from github_slugger import GithubSlugger


MARKDOWN_SUFFIXES = {".md", ".markdown"}
HEADING_TAGS = {"h1", "h2", "h3", "h4", "h5", "h6"}
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}


class DocumentParser(HTMLParser):
    """Collect destinations and anchors while tracking enclosing source blocks."""

    def __init__(self):
        self.links = []
        self.anchors = set()
        self.elements = []
        self.heading = None
        self.slugger = GithubSlugger()

        super().__init__(convert_charrefs=True)

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        position = re.fullmatch(r"(\d+):\d+-\d+:\d+", attributes.get("data-sourcepos") or "")
        line = self.elements[-1][1] if self.elements else None
        target = None

        if position:
            line = int(position[1])

        if tag == "a":
            target = attributes.get("href")
        elif tag == "img":
            target = attributes.get("src")

        if tag not in VOID_TAGS:
            self.elements.append((tag, line))

        if tag in HEADING_TAGS:
            self.heading = []

        if target is not None:
            self.links.append((line, target))

        if attributes.get("id"):
            self.anchors.add(attributes["id"])

        if tag == "a" and attributes.get("name"):
            self.anchors.add(attributes["name"])

    def handle_startendtag(self, tag, attrs):
        self.handle_starttag(tag, attrs)

        if tag not in VOID_TAGS:
            self.handle_endtag(tag)

    def handle_data(self, data):
        if self.heading is not None:
            self.heading.append(data)

    def handle_endtag(self, tag):
        index = 0

        if tag in HEADING_TAGS and self.heading is not None:
            self.anchors.add(self.slugger.slug("".join(self.heading)))
            self.heading = None

        for index in range(len(self.elements) - 1, -1, -1):
            if self.elements[index][0] == tag:
                del self.elements[index:]
                break


def read_document(path, docs_root, cache):
    resolved = path.resolve()
    document = cache.get(resolved)
    text = ""
    rendered = ""

    if not resolved.is_relative_to(docs_root):
        raise ValueError("document resolves outside docs/")

    if document is not None:
        return document

    text = path.read_text(encoding="utf-8")
    # Preserve raw HTML destinations for inspection. HTMLParser never executes it.
    rendered = github_flavored_markdown_to_html(text, options=Options.CMARK_OPT_SOURCEPOS | Options.CMARK_OPT_UNSAFE)
    document = DocumentParser()
    document.feed(rendered)
    document.close()
    cache[resolved] = document

    return document


def check_destination(source, target, repository_root, cache):
    docs_root = repository_root / "docs"
    url = urlsplit(target)
    path = ""
    fragment = ""
    destination = source
    document = None
    is_markdown = False

    if url.scheme == "file":
        return "file: URLs are unsupported; use a path inside docs/"

    if url.scheme or url.netloc:
        return None

    path = unquote(url.path, errors="strict")
    fragment = unquote(url.fragment, errors="strict")

    if path.startswith("/"):
        destination = repository_root / path.lstrip("/")

    elif path:
        destination = source.parent / path

    is_markdown = destination.suffix.lower() in MARKDOWN_SUFFIXES
    destination = destination.resolve()
    is_markdown = is_markdown or destination.suffix.lower() in MARKDOWN_SUFFIXES

    if not destination.is_relative_to(docs_root):
        return "destination resolves outside docs/"

    if not destination.exists():
        return "destination does not exist"

    if fragment and is_markdown and destination.is_file():
        document = read_document(destination, docs_root, cache)

        if fragment not in document.anchors:
            return f"section anchor {fragment!r} does not exist"

    return None


def raise_walk_error(error):
    raise error


def find_documents(docs_root):
    documents = []
    directory = ""
    subdirectories = []
    filenames = []
    filename = ""

    for directory, subdirectories, filenames in os.walk(docs_root, onerror=raise_walk_error, followlinks=False):
        for filename in filenames:
            if Path(filename).suffix.lower() in MARKDOWN_SUFFIXES:
                documents.append(Path(directory) / filename)

    return sorted(documents)


def check_links(repository_root):
    repository_root = repository_root.resolve()
    docs_root = repository_root / "docs"
    documents = []
    pages = {}
    cache = {}
    errors = []
    source = None
    document = None
    line = None
    target = ""
    reason = None
    location = ""

    if not docs_root.is_dir():
        return 0, ["docs/: documentation directory does not exist"]

    try:
        documents = find_documents(docs_root)

    except OSError as error:
        return 0, [f"docs/: cannot scan documentation: {error}"]

    if not documents:
        return 0, ["docs/: no Markdown documents found"]

    for source in documents:
        try:
            pages[source] = read_document(source, docs_root, cache)

        except (OSError, ValueError, RuntimeError) as error:
            errors.append(f"{source.relative_to(repository_root)}: cannot read document: {error}")

    for source, document in pages.items():
        for line, target in document.links:
            location = str(source.relative_to(repository_root))

            if line is not None:
                location = f"{location}:{line}"

            try:
                reason = check_destination(source, target, repository_root, cache)

            except (OSError, ValueError, RuntimeError) as error:
                reason = f"cannot check destination: {error}"

            if reason:
                errors.append(f"{location}: {target!r}: {reason}")

    return len(documents), errors


def main():
    repository_root = Path(__file__).resolve().parents[1]
    document_count, errors = check_links(repository_root)
    file_label = "file" if document_count == 1 else "files"
    error_label = "error" if len(errors) == 1 else "errors"
    error = ""

    for error in errors:
        print(error, file=sys.stderr)

    print(f"Checked {document_count} Markdown {file_label}; found {len(errors)} {error_label}.")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
