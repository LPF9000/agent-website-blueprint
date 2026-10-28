# Agent Website Blueprint

[![Blueprint checks](https://github.com/LPF9000/agent-website-blueprint/actions/workflows/blueprint-checks.yml/badge.svg)](https://github.com/LPF9000/agent-website-blueprint/actions/workflows/blueprint-checks.yml)

Instructions, planning templates and optional checks for building websites with an AI coding agent. Start with an idea; record the requirements, choose the smallest suitable architecture, and verify each milestone before calling it complete.

For people new to web development and developers who want a repeatable agent workflow. Works with Codex and other coding agents that can read repository files. MIT licensed; independently maintained.

## Start a website

1. Fork this repository into a new repository for your website, then clone your fork. See [getting started](docs/01-getting-started.md) for prerequisites and alternatives.
2. Open the folder with your coding agent and paste:

   > Read AGENTS.md and prompts/website-builder.md. Help me plan my website. Ask a few questions at a time. Create requirements and a roadmap before writing application code.

3. Review the plan. The agent records decisions and evidence in `.project/`, builds in small increments, and tests an isolated preview before an authorized production release.

For the next session, use [resume-project.md](prompts/resume-project.md). For a concrete example first, follow the [locally verified walkthrough](examples/worked-static-site/README.md).

## What is included

| Area | Start here |
| --- | --- |
| Agent rules, task states and evidence | [AGENTS.md](AGENTS.md) |
| Build, resume, security, deployment and maintenance prompts | [Prompt entry point](prompts/START-HERE.md) |
| Requirements, roadmap, decisions and handoff records | [Planning templates](planning/README.md) |
| Frameworks, Cloudflare, optional data/auth/admin, SEO, accessibility and operations | [25 implementation guides](docs/README.md) |
| Applicable controls and release review | [Security baseline](security/security-baseline.md), [production checklist](docs/24-production-checklist.md) |
| Configuration, contracts and small architecture recipes | [Templates](templates/README.md), [examples](examples/README.md) |
| Optional daily/weekly checks and monthly human review | [Automation](automation/README.md) |

## Architecture and current guidance

Content sites start with Astro, TypeScript, static content and Cloudflare. Accounts, databases, administration, payments and email are added only when requirements justify them. Next.js is an option for application functionality; Tailwind is optional. See [architecture selection](docs/03-architecture-selection.md).

Agents must consult current official documentation, compatibility notes and advisories before using version-sensitive instructions. The [source register](docs/sources.md), [machine-readable sources](docs/sources.json) and [retrieval protocol](docs/source-freshness.md) make those checks explicit. Review dates do not guarantee that a source remains current.

## Project status

Early-stage documentation release. The [worked example](examples/worked-static-site/README.md) is built and checked over local HTTP. Other examples are architectural recipes; cloud, Auth, database and payment integrations have not been executed by this repository. [Validation report](docs/validation-report.md) records the boundaries.

A modest static site may fit free service tiers. Quotas, custom domains and optional integrations can add costs; see [cost management](docs/23-cost-management.md). Generated websites still require their own testing and release approval.

## Check or contribute

```sh
python -m pip install -r scripts/requirements.txt
python scripts/validate.py
python -m unittest discover -s tests -v
```

These commands validate the blueprint and run its tooling/example tests. Operational workflow templates remain inactive until configured in a generated website.

See [roadmap](ROADMAP.md), [contributing](CONTRIBUTING.md), [release policy](docs/releases.md), [changelog](CHANGELOG.md), [license](LICENSE) and [security reporting](SECURITY.md). Keep credentials and private project details out of issues and examples.
