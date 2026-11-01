# EPIC6 Documentation

This repository contains documentation for EPIC6. More information on EPIC can be found at <https://epicsol.org/>.

## Scheduled documentation updates

The [Update EPIC6 documentation workflow](.github/workflows/update-epic6-docs.yml) runs every Monday at 00:00 America/Los_Angeles, following daylight saving time. It sends the contents of `EPIC-UPDATE-PROMPT` to the [Copilot agent tasks API](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/use-cloud-agent-via-the-api) to prepare a documentation pull request for human review.

Add a repository Actions secret named `COPILOT_TOKEN` containing a fine-grained personal access token scoped to this repository with the **Agent tasks: read and write** permission. The API requires a user token; the workflow's built-in `GITHUB_TOKEN` cannot start Copilot tasks.

Allow `git.epicsol.org` in the Copilot cloud agent's [Internet access settings](https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/customize-the-firewall) so it can fetch the EPIC6 source specified in the prompt.

The schedule becomes active when the workflow is on the default branch. You can also start it manually from the repository's Actions tab. Each run links to its Copilot task in the workflow summary.
