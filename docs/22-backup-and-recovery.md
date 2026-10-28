# Backup and recovery

## Purpose

Recover content, data, files and configuration within agreed loss/time limits.

## When needed

All sites need source recovery. Any irreplaceable data/uploads require more than Git.

## Prerequisites

Data inventory, owner, retention/deletion requirements, encrypted backup destination and RPO/RTO (maximum acceptable data loss/recovery time).

## Recommended implementation

Git protects versioned source, not runtime database/object contents or secrets. Back up each data class separately, keep exports off-provider where appropriate, restrict access and rehearse restore into isolated resources.

## Setup

1. Inventory source/media/database/object files, DNS/configuration, external integration state and secret recovery ownership. Define RPO/RTO per class and retention/legal deletion policy.
2. Ensure source exists in remote Git and identify a clean clone/build procedure. Keep important original media with an independent recovery copy when not tracked.
3. Supabase: Free projects require your own regular exports; inspect current CLI `db dump --help` and backup docs. Include needed roles/schema/data according to provider procedure, exclude platform-managed schemas where instructed, encrypt exports and verify contents. Database backups do not include Storage object bytes; back those up separately.
4. D1: inspect current export/Time Travel availability and retention for your plan; document how to restore to an isolated database. R2/storage: inventory object keys, content hashes and version/deletion strategy; sync an independent protected copy. Do not treat object metadata as object backup.
5. Store exports outside the public source repo and outside ordinary public CI artifacts. Restrict access, separate encryption-key recovery and retention cleanup. Never publish a database dump for convenience.
6. Restore into a disposable isolated target with integrations disabled/sandboxed. Verify counts, schema/policies, selected object hashes, critical journeys and auth/permissions; record achieved RPO/RTO and missing items.
7. Document production restore authority, containment, communication and verification. A code rollback is a separate procedure and does not recover deleted rows/files.

## Security considerations

Backups contain sensitive data and can outlive deletion requests. Encrypt, minimize retention, audit access and test least privilege after restore. Do not restore a production dump into a public preview or reconnect real email/payments during rehearsal.

## Free-tier limitations

Supabase automatic daily backup access/PITR are plan-dependent; Free must not assume them. Object copies and retention consume storage/requests. GitHub artifact retention is not a durable backup strategy.

## Verification

At agreed cadence record backup age/completeness and a real isolated restore result with row/object checks and recovery timing. “Export succeeded” without restore evidence is not verified recovery.

## Troubleshooting

Empty/missing storage: database dumps contain metadata only. Restore auth fails: inspect provider-managed schema guidance and secret/key differences without printing values. Expired backup: treat as an operational incident and repair scheduling/notifications.

## Official documentation

[Supabase backups](https://supabase.com/docs/guides/platform/backups) · [Supabase CLI](https://supabase.com/docs/reference/cli/introduction) · [D1 export](https://developers.cloudflare.com/d1/best-practices/import-export-data/) · [D1 Time Travel](https://developers.cloudflare.com/d1/reference/time-travel/) · [R2 docs](https://developers.cloudflare.com/r2/)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.
