# Admin API recipe

## Scope and components

Cloudflare Worker or framework routes + selected relational datastore. Dashboard is a separate frontend client; no unrestricted administrative endpoints.

## User journey

Admin creates/edits/publishes products/events, ordinary visitor reads only published public fields.

## Implementation sequence

Use templates/api OpenAPI contracts as app-owned design examples. Add server identity/role/object authorization, bounded JSON validation, CSRF for cookie writes, shared rate controls, parameterized SQL, transactions, ETag revision checks and audit logging. Keep production secrets server-only; RLS/grants protect exposed Supabase tables too. No executable handler is supplied because identity and data policy must be selected first.

## Acceptance and operations

Test unauthenticated 401, non-admin 403, invalid body 422/413/415, conflicts 409/412, not-found 404, correct CRUD and unpublish visibility. All mutation tests run on isolated preview with synthetic data; scheduled production checks never write.

## Why this architecture differs

API contracts let implementation vary without making a dummy insecure handler look deployable. D1 and Supabase require different data/identity implementations; neither should be assumed from the UI.

Read [architecture selection](../../docs/03-architecture-selection.md), [security baseline](../../security/security-baseline.md), [cost guide](../../docs/23-cost-management.md), and [production checklist](../../docs/24-production-checklist.md). Create requirements, roadmap and deployment records before implementation. This is a design recipe, not an executed application; provider compatibility and quotas must be rechecked through [current sources](../../docs/sources.md).
