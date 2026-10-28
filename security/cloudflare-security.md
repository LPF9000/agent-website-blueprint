# Cloudflare security

Read [Cloudflare setup](../docs/05-cloudflare-setup.md) before making account/resource changes.

- Use MFA and scoped account/repository permissions. Inspect account, zone and existing deployment first; separate resource discovery from mutation. Never put a global API key in project configuration.
- Maintain isolated previews/bindings/secrets. A preview hostname is public unless deliberately protected. Add preview noindex on real responses and use Access/authentication where private content requires it; verify current plan entitlements.
- Enforce validated TLS. For external proxied origins use Full (strict), not Flexible. Verify domain/DNS/mail dependencies before changes; stage HSTS with deliberate subdomain/preload review.
- Apply `_headers` for static asset responses and middleware for generated API/SSR/error responses. CSP must match actual scripts/embeds. Do not assume CDN headers cover every product/response path.
- Select WAF/rate/bot controls actually available on the plan. Application authorization, size bounds, validation and shared rate controls are still required. Turnstile needs server Siteverify, success plus expected hostname/action validation, replay/timeout handling and an accessible retry path.
- Do not cache personalized/private HTML or auth responses in shared caches. Avoid putting user data in cache keys/logs/query strings. Verify cache headers and browser behavior with two identities in preview.
- Set a supported compatibility date and record tool/runtime versions. Validate bindings/config before deployment and inspect redacted runtime errors. Never disable TLS or authorization to fix an integration.

Production verification: actual hostname TLS/redirects, public/private routes, noindex separation, static/dynamic/error headers, limited permissions, provider usage alerts and rollback version. Audit account and app installation access monthly.

Sources: [Cloudflare TLS](https://developers.cloudflare.com/ssl/), [static headers](https://developers.cloudflare.com/workers/static-assets/headers/), [secrets](https://developers.cloudflare.com/workers/configuration/secrets/), [Turnstile Siteverify](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/), [rate limiting](https://developers.cloudflare.com/waf/rate-limiting-rules/). Recheck current capabilities and pricing; reviewed 2026-10-28.

## Operational cross-check

For Access-protected previews/admin, use [identity and callback checks](../docs/25-operational-failure-modes.md): validate signed JWTs, distinguish human from machine identities, scope CI credentials and any approved callback exception narrowly. Current Access service-token subjects can be empty; required claims must match the expected token type, not a universal human-identity rule.
