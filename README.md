# Agent Website Blueprint

A practical instruction system for an AI coding agent to turn an idea into a secure, deployed, maintainable website. This repository is a blueprint, not a website framework or a promise of automatic production readiness. MIT licensed.

**Start with [START-HERE](prompts/START-HERE.md), then give your agent the [website-builder prompt](prompts/website-builder.md).** No database, accounts, paid services, or application framework is required by default.

## Beginner quick start

1. Sign in to GitHub and install Git, an editor/agent, and the current Node.js LTS supported by your selected framework. See [getting started](docs/01-getting-started.md).
2. Fork this repository into a **new repository for your website**, then clone your fork. Alternatively clone this blueprint as a reference and have the agent create a separate empty website repository. Never reuse someone else's production repository.
3. Open that folder with Codex or another coding agent. Paste: “Read AGENTS.md and prompts/website-builder.md. Help me plan my website. Ask a few plain-language questions at a time. Create .project/requirements.md and .project/roadmap.md before writing application code.”
4. Review the requirements and architecture. The agent creates `.project/` state records from [planning templates](planning/README.md) and implements small milestones with evidence.
5. Connect Cloudflare using [the setup guide](docs/05-cloudflare-setup.md). Test a hosted preview before authorizing production deployment.
6. In a future session, give the agent [resume-project.md](prompts/resume-project.md). Progress is recorded in Git, not dependent on chat history.

## Choose only what you need

| Need | Starting architecture | Optional additions |
| --- | --- | --- |
| Portfolio, blog, documentation | Astro + static content + Cloudflare | Search, CMS |
| Business or event information | Astro + static content | Worker form, Turnstile, email, event administration |
| Catalog | Static product data first | Admin API/database; Stripe only for purchases |
| Accounts, communities, SaaS | App framework justified by requirements | Supabase Auth/Postgres, role policies, storage |
| Bookings | Availability UI + authoritative backend | Calendar OAuth, atomic reservations, payments |

Next.js is appropriate for substantial application behavior, not a universal default. Tailwind is optional. [Architecture selection](docs/03-architecture-selection.md) explains alternatives. [Examples](examples/README.md) are architectural recipes, not tested applications.

## Repository map

- [Agent operating contract](AGENTS.md): scope, safe changes, task states, evidence and handoffs.
- [Prompts](prompts/START-HERE.md): build, resume, audit, deployment review and maintenance.
- [Planning](planning/README.md): requirements, roadmap, progress, decisions, architecture, deployment and handoff templates; [ADR template](planning/adr-template.md).
- [Implementation guide path](docs/README.md): planning through operations, including Cloudflare, optional Supabase, admin/API, SEO, accessibility, testing and costs.
- [Security baseline](security/security-baseline.md) and [audit checklist](security/security-audit-checklist.md): architecture-specific controls and incident response.
- [Automation](automation/README.md): opt-in daily health checks, weekly quality checks and monthly human review.
- [Templates](templates/README.md): environment, GitHub, Cloudflare, Supabase, API contracts and headers.
- [Validation report](docs/validation-report.md) and [source register](docs/sources.md): what was actually checked and what remains unverified.

## Current guidance for coding agents

Start at [source freshness](docs/source-freshness.md) and the [official source register](docs/sources.md). [sources.json](docs/sources.json) maps topic-specific official references to docs, changelogs, review dates and execution status; [llms.txt](llms.txt) is the repository navigation index. Agents must recheck installed versions, security advisories, compatibility and pricing before using integration instructions. A reachable page is not automatically reviewed or tested.

## Free-first, with limits

A modest static website can target $0/month using a provider subdomain. Custom domains have annual fees. Dynamic compute, storage, databases, email, monitoring, payment processing and greater traffic may cost money. Free tiers have quotas, availability limitations and changing terms. Do not enable billing or provision optional services without an explained need. See [cost management](docs/23-cost-management.md).

## Validate this blueprint

Requires Python 3.11+ and PyYAML 6.0.3 for YAML parsing. The documentation-only CI installs the pinned validator dependency; website dependencies are not installed here.

```sh
python -m pip install -r scripts/requirements.txt
python scripts/validate.py
python -m unittest discover -s tests -v
```

The validator checks internal links/anchors, required structure, JSON, workflow safety and guide sections. It is not a security audit or a test of a deployed website. Scheduled website workflows live in `automation/workflows/` and do not run until copied/configured. The only active workflow validates the blueprint on pull requests, pushes and manual requests.

## Contribute and report problems

Read [CONTRIBUTING](CONTRIBUTING.md), [SECURITY](SECURITY.md), and the [changelog](CHANGELOG.md). Never include customer data or credentials in issues, examples, screenshots or agent state files.
