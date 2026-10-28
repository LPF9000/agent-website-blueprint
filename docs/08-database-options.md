# Database and storage options

## Purpose

Choose persistence by data and consistency needs rather than habit.

## When needed

Only when content files or existing services cannot meet the required editing/shared-state workflow.

## Prerequisites

Data model, expected size/read/write rates, role rules, region/residency needs and recovery objectives.

## Recommended implementation

| Option | Use for | Avoid / tradeoff |
| --- | --- | --- |
| Markdown/JSON/content collections | Infrequent editorial publishing | Live concurrent writes; changes need a build |
| D1 (SQLite semantics) | Worker-owned relational data | Not a built-in user-auth/RLS service; backend owns authorization |
| KV | Cache/configuration/read-heavy data | Eventual consistency; not authoritative balances, bookings or strict rate counters |
| R2 | Images/files/object blobs | Not a relational database; signed access/policies and object backups required |
| Supabase PostgreSQL/Auth/storage | Shared relational data with managed auth | Quotas, policy/backup/email and vendor dependencies |

Do not install both D1 and Supabase without a concrete reason. A calendar display may use static event data; a scarce-slot booking system requires authoritative transactional conflict handling.

## Setup

1. Model entities, identifiers, constraints, ownership, publication status and retention. Separate public published content from drafts/private fields.
2. Estimate storage plus indexes, file bandwidth and write/read volume. Compare plan quotas and billing activation.
3. Choose one authoritative datastore. Define transactions/uniqueness for inventory, prices, ordering and reservations; do not rely on a UI availability check.
4. Create version-controlled migrations with least-privilege grants/policies. Apply first to local/isolated preview; seed only synthetic data.
5. Define backup/export, object backup, restore test, RPO/RTO and a provider exit path. Add indexes based on actual queries and bounded pagination.
6. Record the ADR and implement only selected bindings/clients. See [Supabase](09-supabase-setup.md) when chosen.

## Security considerations

No database may be reachable with unrestricted public writes. RLS is Supabase-specific defense; a D1 backend must enforce equivalent operation/object authorization itself. Keep admin keys server-side and use parameterized queries.

## Free-tier limitations

D1 has rows-read/written and storage allowances; poorly indexed queries consume quota. KV limits reads/writes/storage and fails operations when quotas are exhausted. R2 meters storage and request classes; billing setup can be required. Supabase limits database, file storage, egress and active projects. Recheck the live pricing pages.

## Verification

Test positive and denied reads/writes with distinct identities, concurrent updates, uniqueness, pagination and restore. Record query plans for slow/high-volume queries and usage observed under realistic sample data.

## Troubleshooting

Empty rows are not proof of no data: check filters/policies and identity. Slow queries: inspect indexes and explain plans. Stale KV reads: revisit consistency needs rather than adding arbitrary sleeps. Quota errors: reduce cost or obtain informed plan approval.

## Official documentation

[D1 pricing](https://developers.cloudflare.com/d1/platform/pricing/) · [KV pricing](https://developers.cloudflare.com/kv/platform/pricing/) · [KV consistency](https://developers.cloudflare.com/kv/concepts/how-kv-works/) · [R2 pricing](https://developers.cloudflare.com/r2/pricing/) · [Supabase pricing](https://supabase.com/pricing) · [PostgreSQL constraints](https://www.postgresql.org/docs/current/ddl-constraints.html)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.
