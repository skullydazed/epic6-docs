# EPIC6 Documentation

This repository contains documentation for EPIC6. More information on EPIC can be found at <https://epicsol.org/>.

## Checking documentation links

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then run these commands from the repository root:

```sh
uv sync --locked
uv run --locked python scripts/check_links.py
uv run --locked python -m unittest discover -s tests -v
```

The dev tooling uses Python 3.12, which uv can install automatically. The Python pin avoids a `github-slugger` docstring compatibility issue on Python 3.13 and newer. Dependencies are locked in `uv.lock`.

The checker scans Markdown files under `docs/` using GitHub Flavored Markdown. It checks local links and images, Markdown heading anchors, and explicit HTML anchors. Relative paths start from the containing document; paths beginning with `/` start from the repository root. Local destinations must exist and remain inside `docs/` after resolving symlinks. Fragments on non-Markdown files and directories are not checked. External URLs are skipped without network requests; `file:` URLs are rejected.

Failures include the source file, destination, and reason. When the parser provides a source position, the reported line is the start of the containing Markdown block. The checker exits nonzero for broken links, destinations outside `docs/`, and input errors. It checks the whole documentation tree and has no exception list, so existing broken links also fail. The [Check documentation links workflow](.github/workflows/check-doc-links.yml) runs the tests and checker on pull requests, pushes to `main`, and manual runs.

## Scheduled documentation updates

The [Update EPIC6 documentation workflow](.github/workflows/update-epic6-docs.yml) runs every Monday at 00:00 America/Los_Angeles, following daylight saving time. It sends the contents of `EPIC-UPDATE-PROMPT` to the [Copilot agent tasks API](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/use-cloud-agent-via-the-api) to prepare a documentation pull request for human review.

Add a repository Actions secret named `COPILOT_TOKEN` containing a fine-grained personal access token scoped to this repository with the **Agent tasks: read and write** permission. The API requires a user token; the workflow's built-in `GITHUB_TOKEN` cannot start Copilot tasks.

Allow `git.epicsol.org` in the Copilot cloud agent's [Internet access settings](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-the-firewall) so it can fetch the EPIC6 source specified in the prompt.

The schedule becomes active when the workflow is on the default branch. You can also start it manually from the repository's Actions tab. Each run links to its Copilot task in the workflow summary.
