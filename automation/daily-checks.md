# Daily checks

Purpose: detect obvious public failures cheaply. Needed after launch if the owner selects this cadence; it is not continuous uptime monitoring.

## Setup

1. Follow [installation](README.md) and [monitor configuration](../templates/environment/README.md). Copy [daily.yml](workflows/daily.yml) and enable only after owner-authorized GET target review.
2. Configure 1–10 safe endpoints, exact expected status and a non-sensitive marker for critical pages/health responses. Choose canonical final HTTPS origin; intentional same-origin redirects must be explicitly mapped and are inspected without being followed.
3. Configure expected headers and TLS minimum remaining days. The script validates HTTPS chain/hostname and expiry threshold, status/marker, unexpected redirects and basic header presence/substring expectations. It bounds response size/time/request count and does not send auth credentials or submit forms.
4. Run `python scripts/health.py automation/monitor.json` against authorized preview first. Induce a harmless expected-marker failure, verify nonzero exit/notification, then restore. Enable schedule with `ENABLE_DAILY_CHECKS=true` on default branch.

Security: no login/logout/action/export endpoints, secret query strings or public verbose health diagnostics. A presence check does not prove correct CSP/HSTS/authorization. Internal secret/binding/configuration errors are only observable if a safe health response fails; review redacted provider logs/metrics separately.

Cost: standard public Actions differ from private minutes/storage and paid runners. Daily probes are bounded and no browser suite runs. Schedules can be delayed/dropped/disabled; use an independent continuous service for a real availability requirement.

Verification: inspect PASS/FAIL per explicit endpoint and actual Actions failure delivery. Troubleshooting: missing configuration/authorization fails closed; review origin/public DNS/TLS/status expectations without dumping env/response bodies. Redirect failure should trigger canonical/rule review, not automatic cross-origin following.

Official guidance: [schedules](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule), [TLS/headers](https://developers.cloudflare.com/ssl/), [notifications](https://docs.github.com/en/subscriptions-and-notifications/how-tos/managing-github-actions-notifications). Reviewed 2026-10-28; no live target was probed for this blueprint.
