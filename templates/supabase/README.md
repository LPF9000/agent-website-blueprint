# Supabase published-content SQL example

Use only if Supabase was selected. [content.sql](content.sql) is an illustrative migration body defining products/events, constraints, RLS and narrow published-only SELECT policies. It has **no client INSERT/UPDATE/DELETE grants/policies and no executable admin API**. Browser writes deliberately fail. Do not broaden grants to make an unfinished dashboard work.

1. Read [setup](../../docs/09-supabase-setup.md) and [database security](../../security/database-security.md). Check current changelog, installed CLI version/help and isolated target identity.
2. Create a migration using `supabase migration new public_content`, review its generated file, then copy/adapt this body. Do not run against an existing production schema unchanged; names may conflict and assumptions may differ.
3. Apply only to local/isolated preview using the current documented CLI workflow. The exact migration command depends on local/remote workflow; verify help and target before running.
4. Seed synthetic draft/published/deleted rows using a privileged local test fixture outside public routes. Through real anonymous and ordinary-user clients, prove only published non-deleted rows can be read and writes fail. Run database advisors if supported.
5. For custom admin CRUD, separately design server-controlled roles and action/object authorization plus a user-scoped RLS policy model, or a tightly authorized privileged backend. Never rely on user_metadata, public keys or hidden UI. Record the chosen model and negative tests. The example does not implement that layer.
6. Add private fields only in a separate private table/schema or reviewed column projection/grants. RLS filters rows, not columns. Validate IANA zones and safe slug syntax in application schema as well as DB constraints; add revisions/transaction handling in implementation.
7. Back up schema/data and storage objects independently, rehearse isolated restore and document migration/rollback before production approval.

Validation here covers documentation/static SQL safety assertions only. No Postgres server, Supabase project, migration apply, auth flow or RLS runtime test was executed. [RLS docs](https://supabase.com/docs/guides/database/postgres/row-level-security) and [API exposure/grants](https://supabase.com/docs/guides/api/securing-your-api) must be rechecked before adoption.
