# Deployment and rollback

## Purpose

Release an identified artifact safely and prove behavior at the real hostname.

## When needed

Every initial launch and significant production change.

## Prerequisites

Passing relevant local tests, isolated hosted preview evidence, deployment records, non-secret config inventory and production authorization.

## Recommended implementation

Use provider Git integration or pinned local Wrangler; do not add redundant CI deploys. Promote a reviewed commit through local → hosted preview → authorized production. Plan database and application recovery separately.

## Setup

1. Inspect working tree and identify exact commit to release. Reproduce install/build from lockfile with supported tool versions. Record artifact/output and environment.
2. Configure preview with separate secrets/data, sandbox services and noindex. Run functional, auth/authorization, accessibility, SEO, header/cache and mobile smoke checks. Store redacted evidence.
3. Complete [production checklist](24-production-checklist.md), including budget/quotas, notifications, backups/restore and rollback. Resolve blockers; document narrowly accepted noncritical gaps with an owner.
4. Present exact production target/resources, migration/DNS/secret changes, cost implications, test evidence and rollback. Obtain missing explicit authorization for that scope before promotion. Disable unintended automatic production deployment while approval is pending.
5. Apply backward-compatible migrations via the reviewed process; expand/contract risky schema changes rather than breaking the previous app version. Snapshot/export important data first. Never assume redeploying old code reverses schema/data changes.
6. Deploy through the configured supported mechanism; record provider version and commit. Provider success advances to Deployed only.
7. Verify production domain/TLS/canonical redirects, representative routes/error pages, public read-only journeys, protected denials, headers, indexing controls, logs and current bindings. Record time and result before Verified in production.
8. If release criteria fail, contain access as needed and use the provider’s documented rollback/version controls to restore the known-good artifact. Verify again. For incompatible database changes use the separately rehearsed migration/recovery procedure. Document incident and follow-up.

## Security considerations

Use environment-scoped secrets and least-privilege deploy identity. Review build-time exposure, preview service access and source-map privacy. Do not merge/deploy automatically from untrusted PRs. Private pages and APIs must remain uncached and unauthorized users denied after deployment.

## Free-tier limitations

Builds, compute and storage consume quotas; rollback/version retention and logs vary by plan. A paid upgrade must be an explicit budget decision, not a hidden launch requirement.

## Verification

For both initial launch and rollback, evidence includes actual hostname, provider version/commit, core journey results, TLS/header/SEO checks and redacted logs. Confirm the rollback target still works with current schema.

## Troubleshooting

Green build but wrong site: inspect connected repo/branch/root/output and provider version. Missing secret: check target environment. Rollback code incompatible with data: stop and follow recovery runbook rather than repeated deploys.

## Official documentation

[Workers deployments](https://developers.cloudflare.com/workers/configuration/versions-and-deployments/) · [Workers rollbacks](https://developers.cloudflare.com/workers/versions-and-deployments/rollbacks/) · [Pages rollback](https://developers.cloudflare.com/pages/configuration/rollbacks/) · [Wrangler commands](https://developers.cloudflare.com/workers/wrangler/commands/)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.
