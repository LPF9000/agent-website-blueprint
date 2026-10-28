# API development

## Purpose

Expose the smallest secure server interface necessary for the chosen site.

## When needed

Forms, protected administration, live database workflows or integrations. Static sites may need no custom API.

## Prerequisites

Contracts, role/object matrix, input bounds, rate-limit strategy, runtime and safe test environment.

## Recommended implementation

Use small Cloudflare Worker/framework endpoints with explicit methods and validated contracts. Application-owned example paths in this repository are design examples, not vendor API endpoints. Deny by default and prefer same-origin requests.

## Setup

1. Define routes, methods, request/response schemas, maximum sizes, pagination, errors and permissions in an API contract. Start with [products and events](../templates/api/README.md).
2. Route only allowed methods; return 405 plus Allow for others. Require JSON where relevant and reject unsupported media (415), malformed input (400/422) and oversized payload (413). Enforce actual streamed byte limits; do not trust Content-Length alone.
3. Validate authentication, required role and per-object/tenant ownership before reading/writing protected data. Parameterize SQL and explicitly allow editable fields to prevent mass assignment.
4. For cookie-authenticated writes validate CSRF token/trusted origin per framework; use no state-changing GET. CORS only permits configured exact origins when cross-origin calls are needed; it is not authentication. Use Vary: Origin where responses vary.
5. Enforce per-user and abuse-aware IP rate limits in an appropriate shared store/provider control; in-memory Worker counters are not reliable across isolates. Use Turnstile for abuse-prone public submissions where appropriate, with mandatory server verification and expected hostname/action checks.
6. Use transactional updates, unique constraints and idempotency for retry-prone operations. Handle optimistic conflicts as 409/412. Never let the browser supply authoritative price/role/owner.
7. Return a stable redacted error code plus request ID. Log action/outcome/latency safely. Set no-store on sensitive data and apply security headers on dynamic/error responses.
8. For outbound requests use allowed destinations, timeout/body limits and bounded retries; prevent SSRF. Verify webhook signatures over raw bytes and deduplicate events before side effects.

## Security considerations

Credentials belong in headers/server secret storage, never URL query strings. CSRF depends on credential transport; bearer headers reduce classic cookie CSRF but do not remove XSS/token theft risk. Preview tests must not write production data.

## Free-tier limitations

Worker CPU/request and rate-control limits apply. Outbound email/calendar/payment API quotas are separate. Do not add queues or an API gateway until traffic/reliability requirements justify them.

## Verification

Exercise valid/invalid/authenticated/anonymous/cross-user/unsupported-method cases, byte limits, retry/concurrency and rate behavior. Test protected routes directly without the UI and confirm failures do not leak stack traces or SQL.

## Troubleshooting

Preflight failures: compare exact origins/methods/headers and include OPTIONS only where needed. Intermittent throttling: inspect shared limiter scope. Duplicate side effects: check idempotency constraints and webhook event ledger.

## Official documentation

[Workers best practices](https://developers.cloudflare.com/workers/best-practices/workers-best-practices/) · [OWASP REST](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html) · [CSRF](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) · [Turnstile validation](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.
