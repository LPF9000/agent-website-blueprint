# Production readiness checklist

## Purpose

Decide whether a specific commit is ready for authorized launch and track proof after it ships.

## When needed

Before each initial launch or material production change.

## Prerequisites

Requirements/roadmap, exact commit, build/test evidence, preview URL, deployment runbook and accountable owner.

## Recommended implementation

Copy the evidence table into the release record. Mark each row pass/fail/N/A with reason and evidence; unchecked/unknown is not pass. Local, hosted-preview and production are distinct environments.

## Setup

| Gate | Local / hosted preview evidence required | After authorized deployment |
| --- | --- | --- |
| Build and tests | Reproducible install, type/lint/build, relevant behavior tests | Expected commit/provider version |
| Config and secrets | Correct variable names/scopes; no credentials in Git/build/logs | Actual runtime bindings without printing secrets |
| Auth (if selected) | Verify confirmation/login/recovery/logout/expiry | Safe approved identity check or explicitly unverified |
| Authorization/API (if selected) | Negative role/ownership/RLS tests, input/size/rate/CSRF controls | Read-only denial/visibility checks |
| Security headers and HTTPS | CSP compatibility, cookies, no-store, static and dynamic/error headers | Actual hostname TLS, redirects and responses |
| SEO | Title/description/canonical/social/JSON-LD, sitemap/robots; preview noindex | Public routes indexable, private routes protected, production sitemap |
| UI and accessibility | Mobile/desktop, keyboard/screen reader, automated checks, content/error/404 states | Representative read-only route smoke |
| Performance | Representative budget/Lighthouse measurements | Watch production metrics; field data when available |
| Operations | Redacted logs, monitor config and tested failure notification | Monitor sees intended hostname and owner confirms delivery |
| Recovery | Document backup strategy, data/object coverage, isolated restore evidence, rollback | Known-good artifact and schema compatibility confirmed |
| Cost and access | Selected free/paid quotas, account MFA/least privilege, renewal owner | Usage limits and enabled spending confirmed |
| Release authority | Exact diff/target/migration/cost/rollback presented | Record approval scope, deployment time and verifier |

1. Resolve failed critical gates and record any narrow accepted limitations with owner/date.
2. Obtain missing explicit production authorization for exact scope. Do not deploy simply because a preview looks good.
3. Deploy, then record **Deployed** with provider evidence. Complete the actual production column before **Verified in production**.
4. If production fails, contain/rollback according to the documented runbook and repeat smoke checks. Update roadmap, progress, deployment and handoff.

## Security considerations

No production test fixtures, real charges, unsolicited emails or state-changing scheduled probes. “N/A” must follow architecture, not lack of time. Data authorization and secret leakage blockers cannot be waived by a green UI screenshot.

## Free-tier limitations

Confirm free-plan failure/pausing behavior and paid triggers before launch. Necessary recovery/reliability requirements may exceed free features; resolve that tradeoff explicitly.

## Verification

A reviewer can follow every evidence link/command for the exact commit and environment, see approval and rollback, and distinguish implemented/tested/deployed/production-verified. Record unavailable production checks as unverified.

## Troubleshooting

If evidence predates a relevant change, rerun affected checks. If no preview exists, significant changes remain blocked pending a safe runtime verification path. If deployment succeeds but domain does not, remain Deployed and investigate.

## Official documentation

[Cloudflare deployment docs](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/) · [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [WAI evaluation](https://www.w3.org/WAI/test-evaluate/)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.

## Operational cross-check

- [ ] [Operational failure-mode gates](25-operational-failure-modes.md) reviewed: exact preview SHA/configuration, environment parity, active webhook receivers, payment/entitlement/email recovery, known-file access across ingress, Access identity types, publication boundary and missing-report failures. Mark unselected modules N/A with a reason; link [release evidence](../planning/release-evidence-template.md).
