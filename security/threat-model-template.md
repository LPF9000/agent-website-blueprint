# Threat model template

Date / owner / architecture version: fill before exposing dynamic data and revise after trust-boundary changes. For a static site, source/deploy accounts and third-party scripts remain important assets.

## Scope and data flow

List browser, DNS/CDN, static host, APIs, database, storage, CMS, identity, email/payment/calendar providers and administrators. For each connection record identity, credentials, data class, allowed operations and trust boundary. Classify personal data, secrets, financial state and unpublished content; define retention/deletion.

## Abuse cases and controls

| Asset / entry point | Actor and precondition | Abuse / impact | Preventive control | Detection / recovery | Owner / verification |
| --- | --- | --- | --- | --- | --- |
| Admin API | Ordinary or anonymous user | Direct CRUD request bypasses hidden UI | Server role/object checks and data policies | Redacted audit, revoke access | Negative direct API tests |
| Booking/inventory | Concurrent/replayed requests | Oversell/double-book or duplicate charge | Transactions, uniqueness, idempotency | Reconcile ledger and alerts | Concurrent preview tests |
| Content/uploads | Editor or public submitter | Stored XSS/active file hosting | Escaping, sanitization, type/signature/size limits, isolated serving | Quarantine/remove, review logs | Hostile payload preview tests |
| Source/deploy identity | Stolen credential/dependency | Malicious production deployment | MFA, least privilege, reviewed updates | Revoke, rollback, audit | Access/recovery exercise |
| Private data/cache | Cross-user requests | Tenant data leak | RLS/server ownership/no-store | Contain, purge and notify as required | User A/B tests |

Add site-specific threats, not only these examples. Rate/abuse costs, webhook forgery, OAuth redirect manipulation, recovery-token leaks and backup exposure matter when those modules exist.

## Risk decisions

Rank likelihood and impact; map mitigations to roadmap acceptance criteria. List residual risk with named owner and review date. Define incident contact path and safe test environment. Do not include real exploit tokens or customer data.

Reference: [OWASP threat modeling](https://owasp.org/www-community/Threat_Modeling), [baseline](security-baseline.md), [incident response](incident-response.md). This template is not a completed assessment.
