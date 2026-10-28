# API and upload security

Apply to server endpoints and integrations. Use [API guide](../docs/12-api-development.md) and [contracts](../templates/api/README.md).

## Request pipeline

1. Route exact method/path; reject unsupported methods/media. Bound streamed bytes and parsing depth/field count before expensive work. Proxy limits are not your application limits.
2. Authenticate, authorize action/object/tenant, then validate allowlisted fields and business rules. For public writes define explicit permitted behavior; a publishable key or Turnstile does not grant admin rights.
3. Apply trusted-origin/CSRF controls for ambient cookies. Restrict CORS to necessary exact origins; support Vary/preflight correctly. Browser CORS cannot protect endpoints from direct clients.
4. Parameterize SQL, enforce constraints/transactions, paginate and apply shared rate/abuse controls. Do not use module-global Worker counters for distributed limits.
5. Return stable redacted errors with request IDs, appropriate status codes and no-store for sensitive responses. Apply headers on errors and denials too.

## Upload pipeline

Only accept needed file categories. Enforce actual byte limits, inspect extension/MIME/signature together, generate names, and restrict count/dimensions/decompression workload. Re-encode images when appropriate. Quarantine and scan risky types; reject or sanitize SVG/HTML/active content. Keep originals private; separate user content origin and force download for untrusted documents. Signed upload/download URLs must be short-lived and constrained to authorized objects. Storage policy must prevent one user listing/replacing another user's objects.

## Outbound and webhook requests

Allowlist destinations for server fetches, reject local/private metadata targets, control redirects and bound response/time/retries. Verify provider webhook signatures on raw bytes with the correct environment secret, reject stale/invalid signatures using the provider library, deduplicate event IDs and make side effects idempotent/transactional. Server-side price/status is authoritative.

Verification: direct unauthorized/cross-user calls, malformed/oversized bodies, invalid content types, forged/replayed webhooks, concurrency and upload spoofing. Use isolated data; never fuzz production without explicit scope. Record failure codes and unchanged data.

Official sources: [REST security](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html), [file uploads](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html), [SSRF](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html), [CSRF](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html). Reviewed 2026-10-28 where in source register; consult current versions.
