# Authentication and session security

Use only when accounts/admin access are required. Follow [authentication setup](../docs/10-authentication.md) and current provider SSR documentation. Review identity and authorization separately.

1. Validate identity on the server using supported cryptographic claim/user validation, not a browser flag or an unchecked session object. Restrict accepted issuer/audience and expiry through the library/provider's documented flow.
2. Authorize each action and object. Store roles in server-controlled membership/app metadata, never user-editable profile metadata. Tenant/user IDs supplied by clients are untrusted. Consider token freshness and session invalidation on role changes.
3. Require verified email where applicable, rate-limit sign-up/login/recovery and use generic errors. Enable admin MFA and sensitive-action reauthentication when supported. Do not build a password hashing/session system from scratch.
4. Use exact callback/redirect allowlists, maintained OAuth state/PKCE handling and minimum provider scopes. Validate any return path as a local allowed path; reject open redirects.
5. Use Secure and appropriate SameSite cookies; HttpOnly for server-only session secrets. Provider SSR browser clients may require a documented readable-cookie/token model; treat XSS defense as essential and do not blindly break SDK refresh behavior. Never expose secret/admin API keys to the browser.
6. Protect cookie-authenticated unsafe methods against CSRF with framework defenses, tokens and trusted-origin validation as appropriate. Exclude personalized/auth responses from CDN and service-worker caching.
7. Test confirmation, login, recovery completion, logout, expiry, revoked/disabled users, A/B data access and admin removal. Deleting an identity may not invalidate issued access tokens immediately; document the provider's revocation semantics.

No tokens/passwords/recovery links in logs, screenshots, URLs in state files, fixtures or CI artifacts. Test with synthetic identities in preview. Record actual denial results, not just UI redirects.

Official sources: [OWASP authentication](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html), [sessions](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html), [Supabase SSR](https://supabase.com/docs/guides/auth/server-side), [redirects](https://supabase.com/docs/guides/auth/redirect-urls). Recheck advisories/version guidance; reviewed 2026-10-28.
