# Maintenance

## Purpose

Keep dependencies, access, content and operations healthy without endless automation.

## When needed

After launch and whenever an advisory/incident changes risk.

## Prerequisites

Named owner/backup owner, roadmap, release/rollback records and selected checks.

## Recommended implementation

Use daily lightweight checks, weekly change review and monthly human operational review. Automate evidence collection and reminders, not approvals, restores or production data mutations.

## Setup

1. Select [daily](../automation/daily-checks.md), [weekly](../automation/weekly-checks.md) and [monthly](../automation/monthly-checks.md) modules appropriate to the site. Document who reviews failed runs and the response window.
2. Enable Dependabot with only applicable ecosystems. Read advisories/release notes, prioritize exploitable vulnerabilities and test focused updates in preview. Do not blindly auto-merge major or auth/runtime updates.
3. Review content accuracy, broken links, access logs/abuse, performance/accessibility regressions, SEO reports and quota usage. Track findings as roadmap tasks.
4. Monthly, review permissions, unused integrations, backups and restore evidence, RLS/storage rules, domain renewal, secrets policy, provider pricing and response documentation. Rotate based on compromise/policy/provider needs rather than gratuitous monthly churn.
5. Re-read current official sources/changelogs before changes. Record versions and dates, and update ADRs when a previously accepted architecture assumption changes.
6. Use [maintenance prompt](../prompts/maintenance-agent.md). After work update progress/deployment/handoff, preserving evidence of what was actually checked and unresolved owners.

## Security considerations

Dependency install scripts run code; review unexpected lockfile/maintainer changes and avoid privileged runners/secrets. Do not let scheduled bots silently weaken policy or expand access to make checks pass.

## Free-tier limitations

Reviews take human time even when tools are free. Limit open update PRs and schedule frequency. More observability, backups and reliable production SLAs may require budget.

## Verification

A monthly record includes reviewer, date, findings, next due date and evidence, especially restore/notification tests. A generated workflow summary alone does not complete an access review.

## Troubleshooting

Unreviewed alerts: assign owner and triage by real exposure, not only scanner count. Too many update PRs: group low-risk changes and limit count without ignoring security advisories. Outdated guidance: record uncertainty and check current official sources before acting.

## Official documentation

[Dependabot options](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference) · [GitHub advisories](https://github.com/advisories) · [Cloudflare changelog](https://developers.cloudflare.com/changelog/) · [Supabase changelog](https://supabase.com/changelog)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.
