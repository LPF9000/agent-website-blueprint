# Uptime monitoring and notifications

Use [daily checks](daily-checks.md) as a low-frequency safety net. GitHub schedules may be delayed/dropped and are disabled after prolonged inactivity in public repos; they are not continuous monitoring. A $0 informational site can accept that tradeoff explicitly. A reliability-critical site needs independent monitoring with confirmed intervals/alerts and budget.

1. Name an owner and backup with a response expectation and runbook. Use safe unauthenticated GET endpoints and exact status/marker/header expectations.
2. In GitHub **Settings → Notifications**, locate System/Actions and enable web/email notifications, optionally failures only. Watch the repository and inspect current notification semantics for schedules/triggering owners. Configure the scheduled workflow owner appropriately; do not assume all collaborators receive alerts.
3. Run a harmless failing expectation on preview and confirm the intended owner actually receives it, then restore config. Review run summary/logs and failed-run history. Never send test secrets/customer records in notifications.
4. For continuous service, assess an existing monitor or a suitable provider with free limited checks. Verify check intervals, locations, retention, contacts and paid triggers before choosing. No external monitor is provisioned by this blueprint.
5. External email/chat notifications are optional. Use least-privilege secrets, fixed recipients and redacted messages with a link to the restricted run, never response bodies or credentials.
6. Review notifications and schedule activity monthly. A monthly summary reminder succeeds even if nobody reviews it; use a separate owned reminder process for overdue human reviews.

Troubleshooting: missing alerts require testing delivery preferences/ownership, not granting issue/write permission to a health job. Monitor failure can be a bad expectation, DNS/TLS failure, quota exhaustion or real outage; inspect redacted provider status/logs before retrying.

Official sources: [Actions notifications](https://docs.github.com/en/subscriptions-and-notifications/how-tos/managing-github-actions-notifications), [schedule behavior](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule), [usage limits](https://docs.github.com/en/actions/reference/limits). Reviewed 2026-10-28; notification delivery remains user/account-specific and untested here.
