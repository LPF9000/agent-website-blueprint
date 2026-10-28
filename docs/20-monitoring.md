# Monitoring and notifications

## Purpose

Detect public failures and give a named owner enough information to act.

## When needed

Any launched site; depth depends on reliability and data requirements.

## Prerequisites

Canonical HTTPS URL, safe public endpoints, expected redirects/header policy, operations owner and notification preference.

## Recommended implementation

Use low-frequency GitHub checks as a safety net and provider metrics/logs for diagnosis. Add continuous uptime monitoring only when required; scheduled Actions can be delayed, dropped or disabled and are not an uptime SLA.

## Setup

1. Define safe GET endpoints and expected status/marker, excluding logout/delete/action links. Do not send credentials or customer data. Keep health responses minimal and avoid exposing database/version internals.
2. Copy [monitor config](../templates/environment/monitor.json) and set the exact owned HTTPS origin plus explicit paths, status/header expectations, TLS expiry warning and redirect allowlist. Use the [daily workflow](../automation/daily-checks.md) only after authorization to check that target.
3. Add [weekly](../automation/weekly-checks.md) and [monthly](../automation/monthly-checks.md) options selectively. Configure budget/timeouts, no write permissions and bounded artifacts. Run manually before enabling a schedule.
4. In GitHub notification settings enable Actions failure notifications for the workflow owner/participants and test delivery with a harmless intentionally wrong expected marker, then restore configuration. Watching a repository does not by itself prove someone receives failed schedule notifications. Review Actions run summaries and assign backup owner.
5. Configure redacted provider logs/metrics for error rate, latency and usage; define thresholds and runbook links. Public monitors cannot observe internal resource binding/secret misconfiguration unless it changes a safe public endpoint; review provider dashboards separately.
6. If continuous monitoring is required, evaluate independent uptime services or an existing monitor. Confirm free check intervals, monitored endpoint limits, retention and notification channels. External email/chat notifications are optional and must not embed secrets.
7. Document incident response owner, escalation, planned maintenance and periodic review of failed runs.

## Security considerations

Monitor only explicitly authorized public targets. Never crawl arbitrary discovered links, authentication routes or third-party APIs by default. Logs/alerts must omit tokens, response bodies with personal data and cookie headers.

## Free-tier limitations

Actions schedules/runners/storage have plan-specific limits and public-repo inactivity disablement. External monitors have limited free intervals/checks/retention. Provider logs may be sampled or short-lived and advanced retention paid.

## Verification

Run the monitor manually against isolated preview, induce a harmless expected-failure, confirm nonzero status and notification/summary delivery, then restore. Record actual schedule health and owner. A green HTTP response does not prove all business behavior.

## Troubleshooting

No schedule runs: verify workflow is on default branch, schedules enabled, opt-in variable set and recent repository activity. TLS warning on a healthy browser: inspect certificate chain/expiry and network; never disable verification. Alert noise: adjust endpoint contract, not blanket ignore failures.

## Official documentation

[GitHub schedules](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule) · [Actions notifications](https://docs.github.com/en/subscriptions-and-notifications/how-tos/managing-github-actions-notifications) · [Workers observability](https://developers.cloudflare.com/workers/observability/)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.
