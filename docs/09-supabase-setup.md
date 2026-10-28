# Optional Supabase setup

## Purpose

Add managed PostgreSQL, authentication or storage only when requirements justify it.

## When needed

Accounts, frequent shared content editing or relational data. Skip this guide for a simple informational site.

## Prerequisites

Supabase account, isolated development/preview project plan, schema and role matrix, quota review and a recovery owner. Read current changelog before implementation.

## Recommended implementation

Use publishable keys in public clients and user-scoped operations with RLS. Secret keys are privileged and bypass RLS: keep them server-only and use only when a justified operation cannot use the caller’s identity.

## Setup

1. Discover the available Supabase connector and connection state. Use supported read-only project inspection first; confirm project/org identity. If absent, use the documented dashboard/OAuth setup. Never assume the connector can provision projects or manage keys.
2. Create a Free development/preview project in the chosen organization/region after checking quotas and scope. Store generated database passwords in a password manager, not in project records. Production must use separate resources or an explicitly documented isolation model.
3. From the project Connect/API keys interface obtain URL and publishable key. Put only public-safe values behind Astro `PUBLIC_` or Next `NEXT_PUBLIC_` prefixes. Store any required server secret in runtime secret storage. Most user-scoped operations do not need it.
4. Initialize the supported CLI/local workflow only after checking its installed version and `--help`. Create migration files through `supabase migration new NAME`, review the SQL and test on local/isolated resources. [The SQL example](../templates/supabase/content.sql) demonstrates a narrow published-content/read-only access model, not a complete admin system.
5. For **every table in an exposed schema**, enable RLS, review grants and write operation-specific policies for actual identities/roles. Deny by default. Public SELECT policies expose only intended published rows; never expose private columns by assuming RLS is column protection. Views/functions and Storage policies need separate review.
6. Configure Auth as in [authentication](10-authentication.md): email verification, exact site/redirect URLs, recovery and optional OAuth. Configure production email delivery/rate limits before launch; built-in test delivery is not a production mail service.
7. Protect administrator access with server-managed roles/membership, MFA where practical and server/API checks. Never let users assign their own role through editable metadata. Review JWT freshness for role removal.
8. Run positive and negative authorization tests with anonymous, ordinary A/B users and admins through the actual client/API, not SQL editor superuser. Apply migrations through the reviewed release path and run available advisors.
9. Set up encrypted external exports and independent storage-object backup where needed. Free plan recovery is your responsibility; rehearse restore in an isolated project. Record migration/version, policy matrix and recovery evidence.

## Security considerations

Public client keys are **not authorization controls**. Never disable RLS to fix a permission failure. UPDATE needs appropriate SELECT and USING/WITH CHECK policies; audit grants, views (security invoker where supported), functions, storage buckets and server secret use. Do not trust user_metadata for roles.

## Free-tier limitations

Free plan quotas include limited active projects, database/storage/egress and auth usage; inactivity pausing can affect availability. Automatic downloadable backups/PITR and higher availability may require paid plans. Confirm production SMTP provider cost and regional constraints.

## Verification

Prove an anonymous client cannot write; user A cannot access B’s private data; a non-admin cannot publish; admin revocation takes effect according to the documented session model; drafts stay private. Test recovery/email on hosted preview, then authorized production read-only checks. No hosted SQL/auth flow was executed by this blueprint.

## Troubleshooting

Permission denied: inspect grants then RLS, identity and exposed-schema configuration. Zero updates: check SELECT policy and filters. Recovery redirects: compare exact allowlist URL and callback exchange. Never “fix” by switching the browser to a secret key.

## Official documentation

[Supabase changelog](https://supabase.com/changelog) · [API keys](https://supabase.com/docs/guides/getting-started/api-keys) · [RLS](https://supabase.com/docs/guides/database/postgres/row-level-security) · [Auth SSR](https://supabase.com/docs/guides/auth/server-side) · [MCP setup](https://supabase.com/docs/guides/getting-started/mcp) · [Backups](https://supabase.com/docs/guides/platform/backups)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.
