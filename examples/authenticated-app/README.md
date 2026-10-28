# Authenticated application

## Scope and components

Next.js or another justified app framework on a currently supported Workers path; Supabase Auth/PostgreSQL/RLS when selected; private storage only if needed.

## User journey

Member signs up/confirms/signs in, manages own records and recovers access. Admin has explicit restricted operations, not merely a hidden route.

## Implementation sequence

Plan identity/ownership/tenant schema and data lifecycle first. Implement current SSR token validation and no-store private responses. Apply migrations with RLS/grants/operation policies. Keep public publishable key distinct from server secret and use user-scoped database access ordinarily. Add roles through server-controlled membership. Build optional SaaS/community modules incrementally with moderation, privacy and audit requirements.

## Acceptance and operations

Direct API/Data API tests for anonymous/A/B/admin, recovery/logout/expiry, stale JWT role removal, uploaded object visibility and private cache separation. Test actual edge framework compatibility on hosted preview; record gaps and version.

## Why this architecture differs

Auth/shared data introduce sensitive trust boundaries, SMTP quotas, policy testing and recovery needs. $0 is a possible limited prototype target, not a high-availability production promise.

Read [architecture selection](../../docs/03-architecture-selection.md), [security baseline](../../security/security-baseline.md), [cost guide](../../docs/23-cost-management.md), and [production checklist](../../docs/24-production-checklist.md). Create requirements, roadmap and deployment records before implementation. This is a design recipe, not an executed application; provider compatibility and quotas must be rechecked through [current sources](../../docs/sources.md).
