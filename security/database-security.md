# Database and storage security

Applies only to persisted shared data. Start from [database choices](../docs/08-database-options.md) and [Supabase setup](../docs/09-supabase-setup.md) if selected.

1. Model ownership, tenant and publication rules per table/operation. Use least-privilege grants, constraints, parameterized queries and transactional business invariants. Database defaults are not an application permission model.
2. Supabase: enable RLS on every table in every exposed schema, review grants separately and add narrow policies. Public SELECT must expose only intended public data; use column grants/public projections for private columns. Public keys are identifiers, not authorization.
3. INSERT checks constrain allowed owner/tenant; UPDATE requires appropriate SELECT plus USING and WITH CHECK; DELETE is separately authorized. Ensure users cannot edit roles/ownership into an unauthorized state. Never disable RLS as a troubleshooting shortcut.
4. Review views, functions/triggers and storage separately. Views may bypass RLS; use security-invoker where supported or remove exposure. Avoid SECURITY DEFINER; if unavoidable, restrict schema/EXECUTE/search_path, validate caller and audit carefully. User-editable metadata must never define admin roles. JWT app metadata can be stale after role changes.
5. A backend secret/service credential bypasses RLS. Authenticate/authorize before any privileged operation and prefer user-scoped clients for ordinary requests. D1 does not provide Supabase RLS/Auth; all equivalent access controls must be implemented in the backend.
6. Keep private storage buckets private, constrain object owner/path/size/type and signed URL lifetime. Review SELECT/INSERT/UPDATE/DELETE separately. Upsert needs additional permissions; do not broadly grant them just to fix a failure.
7. Test migrations locally/preview, review advisors, back up data and rehearse restore. Keep previews separate, restrict logs/backups and apply retention/deletion requirements.

Verification matrix: anonymous cannot write; user A cannot read/update B; ordinary user cannot promote self or publish; drafts and private objects are hidden; admin actions succeed only with the intended identity; role revocation is tested with known JWT freshness. Run through actual Data API/client credentials, not the privileged SQL editor. The example SQL is intentionally read-only to public users and includes no browser/admin write policy.

Sources: [Supabase RLS](https://supabase.com/docs/guides/database/postgres/row-level-security), [API security](https://supabase.com/docs/guides/api/securing-your-api), [Storage access](https://supabase.com/docs/guides/storage/security/access-control), [PostgreSQL privileges](https://www.postgresql.org/docs/current/ddl-priv.html). Recheck current docs; reviewed 2026-10-28.
