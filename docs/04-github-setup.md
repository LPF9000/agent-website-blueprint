# GitHub setup

## Purpose

Establish source history, review and a recoverable change process.

## When needed

Every generated website and the blueprint itself.

## Prerequisites

Authenticated GitHub account; unique repository name; Git installed. Inspect available GitHub connector operations and existing repositories before mutations.

## Recommended implementation

Use a new repository with a main branch, meaningful commits and lightweight PR checks. Do not require a deployment workflow when the host’s Git integration already covers deployment.

## Setup

1. Check whether the intended `owner/name` already exists. Inspect its contents, default branch and permissions. Never overwrite unrelated content or create a duplicate because a connector returned an ambiguous error.
2. Create the repository with desired visibility using a supported connector operation or GitHub’s **New repository** page. A connector may edit files but lack creation capability; explain and use an authorized fallback.
3. Clone the actual repository URL, verify `git remote -v`, and inspect status before copying blueprint files.
4. Keep README, AGENTS, license, ignore rules and `.project/` records. Use a branch for reviewable changes to an existing project. Review `git diff` and staged changes before committing.
5. Enable dependency graph/Dependabot alerts where available. Copy [Dependabot template](../templates/github/dependabot.yml) and keep only applicable ecosystems/paths.
6. Add the minimal relevant checks and, where the account plan permits, branch protection/rulesets with required review/checks. Do not promise these features are available on every private plan.
7. Enable account MFA, restrict collaborators and document recovery ownership. Never force-push shared history without specific approval.

## Security considerations

Use least-privilege connector installation/repository scopes. PRs from forks must never execute untrusted code with deployment secrets; avoid `pull_request_target` checkout patterns. Set workflow permissions explicitly and pin actions.

## Free-tier limitations

Public repositories and standard hosted runners have different billing from private repos, larger runners and paid features. Check Actions minutes/storage and repository plan rather than assuming all automation is free.

## Verification

Confirm intended visibility, default branch, remote and push permission. Open a test PR/change and check the relevant validation runs. Verify a fork contributor cannot access production credentials.

## Troubleshooting

403: check app installation repository access and token scopes; do not request full-account access reflexively. If main advanced, fetch and reconcile changes without force-pushing. Empty repositories need an initial commit before some Git API operations.

## Official documentation

[Creating a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository) · [Actions secure use](https://docs.github.com/en/actions/reference/security/secure-use) · [Dependabot options](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.
