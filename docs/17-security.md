# Security implementation

## Purpose

Apply practical protections proportional to the site’s attack surface and verify them after deployment.

## When needed

Every site; auth, API, uploads and database controls apply only when those features exist.

## Prerequisites

Architecture/trust boundaries, data classification, threat model, provider access and selected security owner.

## Recommended implementation

Use [security-baseline](../security/security-baseline.md) as the release contract. Defense is layered: HTTPS/headers and dependency/account security for static sites, then validation/authorization/session/data controls for dynamic modules.

## Setup

1. Complete the [threat model](../security/threat-model-template.md): assets, actors, entry points, trust boundaries and abuse cases. Assign each applicable control an owner, implementation location and verification.
2. Enforce HTTPS; stage HSTS after domain review. Add nosniff, a deliberate Referrer-Policy and Permissions-Policy, plus framing/CSP protection compatible with the actual site. Start CSP in Report-Only on preview, review violations, then enforce a tested policy; avoid `unsafe-eval`/broad wildcards as a shortcut.
3. Set headers for both static files and dynamic/API/error responses. [Static header template](../templates/security/_headers) is deliberately limited and must be adapted for scripts, styles, embeds, Auth and Turnstile. Framework inline scripts may need hashes/nonces; nonces must be generated per response.
4. For writes validate schema/actual byte limits, encode output, parameterize SQL, enforce server/object roles and rate limits. CORS is exact-origin opt-in, never an access-control replacement. Cookie writes require appropriate CSRF defenses.
5. Manage sessions, private no-store caching, upload validation and safe logging. Store server secrets in runtime secret storage with least privilege and separate preview credentials.
6. Enable dependency alerts/updates, inspect lockfiles and run relevant vulnerability checks. Plan encrypted backup/restore and incident response before storing important data.
7. Run [security audit checklist](../security/security-audit-checklist.md) in isolated preview; obtain production approval, deploy and verify actual headers and denial cases.

## Security considerations

Apply controls by architecture, not by blindly copying a restrictive header list. Turnstile is bot friction, not authorization; widget tokens require backend verification. SQL editor tests with privileged credentials do not prove RLS protects browser clients.

## Free-tier limitations

Basic security does not require paid WAF products. Advanced rate/WAF/logging features vary by plan; application-level protections remain required. Budget for recovery and specialist review if data risk demands it.

## Verification

Use actual GET responses as well as header-only requests: `curl -sS -D - -o /dev/null https://YOUR_HOST/` after substituting the hostname. Test HTML, API, redirect, 404 and denial responses; inspect CSP console violations and cookies in a browser. Avoid printing authenticated response headers containing session cookies in CI logs.

## Troubleshooting

Broken page after CSP: identify required origins/hashes/nonces from actual violations; do not remove CSP wholesale. Missing API headers: add runtime middleware. Auth data cached: contain leakage, disable shared caching and purge affected objects before release.

## Official documentation

[OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) · [OWASP headers](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html) · [CSP guidance](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html) · [Cloudflare asset headers](https://developers.cloudflare.com/workers/static-assets/headers/)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.
