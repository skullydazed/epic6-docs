"""Exercise the checker against small documentation trees and its command line."""

import shutil
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.check_links import check_links


class LinkCheckerTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.root = Path(self.temporary.name).resolve()
        self.docs = self.root / "docs"

        self.addCleanup(self.temporary.cleanup)
        self.docs.mkdir()
        self.write("docs/index.md", "# Home\n")

    def write(self, path, text):
        destination = self.root / path

        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(text, encoding="utf-8")

        return destination

    def test_existing_paths_queries_and_fragments(self):
        self.write("docs/nested/guide.md", "# Guide\n\n## Installation\n")
        self.write("docs/space name.md", "# Café\n")
        self.write("docs/picture.svg", "<svg></svg>\n")
        self.write("docs/index.md", """# Home

[same page](#home)
[guide](nested/guide.md?view=source#installation)
[repository root](/docs/nested/guide.md)
[encoded path](space%20name.md#caf%C3%A9)
[angle destination](<space name.md>)
[directory](nested/)
![image](picture.svg)
[asset fragment](picture.svg#some-id)
[empty fragment](nested/guide.md#)
[empty destination]()
""")

        self.assertEqual(check_links(self.root), (3, []))

    def test_nested_relative_destinations(self):
        self.write("docs/nested/guide.md", "[home](../index.md#home)\n")

        self.assertEqual(check_links(self.root), (2, []))

    def test_missing_destination_reports_containing_block_line(self):
        count = 0
        errors = []

        self.write("docs/index.md", "# Home\n\nA paragraph\nwith a [missing link](missing.md).\n")
        count, errors = check_links(self.root)

        self.assertEqual(count, 1)
        self.assertEqual(errors, ["docs/index.md:3: 'missing.md': destination does not exist"])

    def test_all_failures_are_reported_in_stable_order(self):
        count = 0
        errors = []

        self.write("docs/z.md", "[z](z-missing.md)\n")
        self.write("docs/a.md", "[a](a-missing.md)\n\n[another](another.md)\n")
        count, errors = check_links(self.root)

        self.assertEqual(count, 3)
        self.assertEqual(len(errors), 3)
        self.assertTrue(errors[0].startswith("docs/a.md:1:"))
        self.assertTrue(errors[1].startswith("docs/a.md:3:"))
        self.assertTrue(errors[2].startswith("docs/z.md:1:"))
        self.assertEqual(check_links(self.root), (count, errors))

    def test_relative_root_and_encoded_escapes_are_rejected(self):
        count = 0
        errors = []

        self.write("README.md", "# Outside\n")
        self.write("docs/index.md", """[relative](../README.md)
[root](/README.md)
[encoded](%2e%2e%2fREADME.md)
[missing outside](../missing.md)
""")
        count, errors = check_links(self.root)

        self.assertEqual(count, 1)
        self.assertEqual(len(errors), 4)
        self.assertTrue(all("destination resolves outside docs/" in error for error in errors))

    def test_heading_formatting_unicode_images_and_collisions(self):
        self.write("docs/guide.md", """# Hello, *World* & `Code`!

## Café 你好

## snake_case

## A  B

## ![A picture](picture.svg) title

## Repeat-1

## Repeat

## Repeat
""")
        self.write("docs/picture.svg", "<svg></svg>\n")
        self.write("docs/index.md", """[formatted](guide.md#hello-world--code)
[unicode](guide.md#caf%C3%A9-%E4%BD%A0%E5%A5%BD)
[underscore](guide.md#snake_case)
[spaces](guide.md#a--b)
[image heading](guide.md#-title)
[literal suffix](guide.md#repeat-1)
[first repeat](guide.md#repeat)
[second repeat](guide.md#repeat-2)
""")

        self.assertEqual(check_links(self.root), (2, []))

    def test_setext_headings_and_explicit_html_anchors(self):
        self.write("docs/index.md", """Home
====

<a id="custom"></a>
<a name="legacy"></a>

<div id="section">Section</div>

[heading](#home)
[custom](#custom)
[legacy](#legacy)
[element id](#section)
""")

        self.assertEqual(check_links(self.root), (1, []))

    def test_missing_same_page_and_cross_page_anchors(self):
        count = 0
        errors = []

        self.write("docs/guide.md", "# Guide\n")
        self.write("docs/index.md", "[same](#missing)\n\n[cross](guide.md#missing)\n")
        count, errors = check_links(self.root)

        self.assertEqual(count, 2)
        self.assertEqual(len(errors), 2)
        self.assertTrue(all("section anchor 'missing' does not exist" in error for error in errors))

    def test_gfm_tables_tasks_references_images_and_html_links(self):
        count = 0
        errors = []
        destinations = ["table.md", "task.md", "full.md", "collapsed.md", "shortcut.md", "picture.png", "html.md", "html-picture.png"]
        destination = ""

        self.write("docs/index.md", """# Home

| Page | Link |
| --- | --- |
| Missing | [table](table.md) |

- [x] [task](task.md)

[full][destination]
[collapsed][]
[shortcut]

[destination]: full.md "Title"
[collapsed]: collapsed.md
[shortcut]: shortcut.md

![missing image](picture.png)

<a href="html.md">HTML link</a>

<img src="html-picture.png" />
""")
        count, errors = check_links(self.root)

        self.assertEqual(count, 1)
        self.assertEqual(len(errors), len(destinations))

        for destination in destinations:
            self.assertTrue(any(repr(destination) in error for error in errors), destination)

    def test_escaped_and_balanced_destinations(self):
        self.write("docs/parentheses(test).md", "# Parentheses\n")
        self.write("docs/ampersand&name.md", "# Ampersand\n")
        self.write("docs/index.md", r"""[escaped](parentheses\(test\).md "Title")
[balanced](parentheses(test).md)
<a href="ampersand&amp;name.md">Entity</a>
""")

        self.assertEqual(check_links(self.root), (3, []))

    def test_code_comments_and_unused_definitions_are_ignored(self):
        self.write("docs/index.md", """# Home

`[inline](inline.md)`

```markdown
# Fake heading
[fenced](fenced.md)
<a href="fenced-html.md">Example</a>
```

    [indented](indented.md)

<!-- [comment](comment.md) <a href="comment-html.md">Comment</a> -->

[unused]: unused.md

[undefined][not-defined]

[real](#home)
""")

        self.assertEqual(check_links(self.root), (1, []))

    def test_code_headings_do_not_create_anchors(self):
        count = 0
        errors = []

        self.write("docs/index.md", "# Home\n\n```md\n# Fake\n```\n\n[broken](#fake)\n")
        count, errors = check_links(self.root)

        self.assertEqual(count, 1)
        self.assertEqual(len(errors), 1)
        self.assertIn("section anchor 'fake' does not exist", errors[0])

    def test_external_urls_never_open_network_connections(self):
        self.write("docs/index.md", """[http](http://nonexistent.invalid/missing#missing)
[https](https://nonexistent.invalid/missing#missing)
[protocol relative](//nonexistent.invalid/missing)
[email](mailto:example@example.invalid)
[irc](irc://nonexistent.invalid/channel)
![external image](https://nonexistent.invalid/image.png)
<https://nonexistent.invalid/autolink>
https://nonexistent.invalid/bare
www.nonexistent.invalid
""")

        with patch("socket.socket", side_effect=AssertionError("Unexpected network request")):
            self.assertEqual(check_links(self.root), (1, []))

    def test_file_urls_are_rejected(self):
        count = 0
        errors = []

        self.write("docs/index.md", "[file](file:///tmp/page.md)\n")
        count, errors = check_links(self.root)

        self.assertEqual(count, 1)
        self.assertEqual(len(errors), 1)
        self.assertIn("file: URLs are unsupported", errors[0])

    def test_invalid_encoded_destinations_are_reported(self):
        count = 0
        errors = []

        self.write("docs/index.md", "[invalid UTF-8](%FF.md)\n\n[null](%00.md)\n")
        count, errors = check_links(self.root)

        self.assertEqual(count, 1)
        self.assertEqual(len(errors), 2)
        self.assertTrue(all("cannot check destination:" in error for error in errors))

    def test_symlink_file_and_directory_escapes_are_rejected(self):
        count = 0
        errors = []

        self.write("outside/page.md", "# Outside\n")
        self.write("docs/index.md", "[file](alias.md)\n\n[directory](linked/page.md)\n")
        (self.docs / "alias.md").symlink_to(self.root / "outside/page.md")
        (self.docs / "linked").symlink_to(self.root / "outside", target_is_directory=True)
        count, errors = check_links(self.root)

        self.assertEqual(count, 2)
        self.assertEqual(len(errors), 3)
        self.assertIn("cannot read document: document resolves outside docs/", errors[0])
        self.assertTrue(all("destination resolves outside docs/" in error for error in errors[1:]))

    def test_symlinks_inside_docs_are_allowed(self):
        self.write("docs/guide.md", "# Guide\n\n[home](index.md#home)\n")
        self.write("docs/index.md", "# Home\n\n[alias](alias.md#guide)\n\n[directory](linked/guide.md#guide)\n")
        (self.docs / "alias.md").symlink_to("guide.md")
        (self.docs / "linked").symlink_to(self.docs, target_is_directory=True)

        self.assertEqual(check_links(self.root), (3, []))

    def test_symlinked_sources_use_their_own_directory(self):
        count = 0
        errors = []

        self.write("docs/nested/guide.md", "[local](index.md#home)\n")
        self.write("docs/nested/index.md", "# Nested\n")
        (self.docs / "alias.md").symlink_to("nested/guide.md")
        count, errors = check_links(self.root)

        self.assertEqual(count, 4)
        self.assertEqual(errors, ["docs/nested/guide.md:1: 'index.md#home': section anchor 'home' does not exist"])

    def test_markdown_symlink_to_other_extension_still_checks_anchors(self):
        count = 0
        errors = []

        self.write("docs/guide.txt", "# Guide\n")
        (self.docs / "guide.md").symlink_to("guide.txt")
        self.write("docs/index.md", "[good](guide.md#guide)\n\n[bad](guide.md#missing)\n")
        count, errors = check_links(self.root)

        self.assertEqual(count, 2)
        self.assertEqual(len(errors), 1)
        self.assertIn("section anchor 'missing' does not exist", errors[0])

    def test_dangling_and_looping_symlinks_are_reported(self):
        count = 0
        errors = []

        (self.docs / "dangling.md").symlink_to("missing.md")
        (self.docs / "loop.md").symlink_to("loop.md")
        self.write("docs/index.md", "[dangling](dangling.md)\n\n[loop](loop.md)\n")
        count, errors = check_links(self.root)

        self.assertEqual(count, 3)
        self.assertEqual(len(errors), 4)

    def test_invalid_utf8_document_is_reported(self):
        count = 0
        errors = []

        (self.docs / "invalid.md").write_bytes(b"\xff")
        count, errors = check_links(self.root)

        self.assertEqual(count, 2)
        self.assertEqual(len(errors), 1)
        self.assertIn("docs/invalid.md: cannot read document:", errors[0])

    def test_missing_or_empty_docs_cannot_pass(self):
        count, errors = check_links(self.root / "missing")

        self.assertEqual(count, 0)
        self.assertEqual(errors, ["docs/: documentation directory does not exist"])
        (self.docs / "index.md").unlink()
        self.assertEqual(check_links(self.root), (0, ["docs/: no Markdown documents found"]))

    def test_scan_errors_are_reported(self):
        with patch("scripts.check_links.os.walk", side_effect=PermissionError("Cannot list docs")):
            self.assertEqual(check_links(self.root), (0, ["docs/: cannot scan documentation: Cannot list docs"]))

    def test_markdown_extensions_are_case_insensitive(self):
        self.write("docs/GUIDE.MD", "# Guide\n")
        self.write("docs/other.markdown", "# Other\n")
        self.write("docs/index.md", "[guide](GUIDE.MD#guide)\n\n[other](other.markdown#other)\n")

        self.assertEqual(check_links(self.root), (3, []))

    def test_command_line_finds_repository_and_sets_exit_status(self):
        source_script = Path(__file__).resolve().parents[1] / "scripts/check_links.py"
        script = self.root / "scripts/check_links.py"
        success = None
        failure = None

        script.parent.mkdir()
        shutil.copyfile(source_script, script)
        success = subprocess.run([sys.executable, str(script)], cwd=self.root.parent, capture_output=True, text=True, check=False)
        self.assertEqual(success.returncode, 0, success.stderr)
        self.assertEqual(success.stderr, "")
        self.assertIn("Checked 1 Markdown file; found 0 errors.", success.stdout)

        self.write("docs/index.md", "[missing](missing.md)\n")
        failure = subprocess.run([sys.executable, str(script)], cwd=self.root.parent, capture_output=True, text=True, check=False)
        self.assertEqual(failure.returncode, 1)
        self.assertIn("docs/index.md:1: 'missing.md': destination does not exist", failure.stderr)
        self.assertIn("found 1 error.", failure.stdout)


if __name__ == "__main__":
    unittest.main()
