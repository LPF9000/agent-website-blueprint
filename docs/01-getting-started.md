# Getting started

## Purpose

Prepare a safe workspace and give an agent enough context to plan a site.

## When needed

Every new website, including a tiny portfolio. No infrastructure account beyond source control is needed for initial planning.

## Prerequisites

A GitHub account, Git, editor/agent and a terminal. Framework development later needs a supported Node.js LTS and npm. Python 3.11+ is needed only to run this blueprint’s validators/monitor scripts. Install software from official sources.

## Recommended implementation

Use a new website repository. Fork this blueprint for an independent copy, or keep it as a reference alongside a new empty website repository. Do not turn the upstream blueprint itself into your personal production site.

## Setup

1. In GitHub, open this repository and choose **Fork**. Select your own account and a new website name. For a private project, create a separate private repository and copy the blueprint files instead of assuming a public fork is private.
2. Copy the fork’s HTTPS clone URL from **Code**. Run `git clone YOUR_COPIED_URL` and open the resulting folder. Replace that command argument; do not type it literally. Confirm `git remote -v` targets your own repository and `git status --short` shows expected files.
3. Check `git --version`, `node --version`, and `npm --version`. Match Node to the chosen framework’s current supported versions; record it in the generated website.
4. Read [START-HERE](../prompts/START-HERE.md). Give the agent [website-builder](../prompts/website-builder.md), with a one-sentence idea. It creates `.project/` records before application code.
5. Review requirements, budget and milestones. Start locally; add Cloudflare only at the infrastructure milestone. Store code in Git after reviewing `git diff --cached`.
6. To check the blueprint itself, install `scripts/requirements.txt` and run the two validation commands in the README. These do not build a website.

## Security considerations

Enable GitHub account MFA. Commit only non-secret examples; ignored files are not automatically safe if already tracked. Verify the remote before pushing and never paste credentials into chat.

## Free-tier limitations

Planning and local development do not require a paid service. Agent subscriptions and development computers are separate costs. A provider subdomain avoids a domain registration purchase.

## Verification

Confirm you can read README/AGENTS, see your own remote, and find `.project/requirements.md` plus a roadmap after discovery. A meaningful first milestone has a user journey and a test, not just a scaffold.

## Troubleshooting

Authentication errors: use GitHub’s supported credential flow rather than a token embedded in a URL. Unsupported Node errors: use the framework’s supported LTS. Existing files: ask the agent to inspect and preserve them before scaffolding.

## Official documentation

[Git installation](https://git-scm.com/downloads) · [Node.js downloads](https://nodejs.org/en/download) · [GitHub forks](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) · [Astro installation](https://docs.astro.build/en/install-and-setup/)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.
