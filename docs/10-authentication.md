# Authentication and sessions

## Purpose

Identify users and protect private journeys without inventing a home-grown identity system.

## When needed

Only if members or administrators need private access. Public content should not require accounts unnecessarily.

## Prerequisites

Role/action matrix, chosen managed identity provider, isolated email delivery and exact local/preview/production URL plan.

## Recommended implementation

Use a maintained managed Auth flow and current framework SSR integration. Authenticate server requests with validated claims/user identity, then authorize each action/object. A route redirect is a convenience, not the access-control boundary.

## Setup

1. Enable only required sign-in methods. For email/password require verified email, sensible password controls and generic failure messages that reduce account enumeration.
2. Set production Site URL and exact allowed callback/recovery URLs; add explicit local/preview destinations only where necessary. Avoid broad production wildcards and arbitrary user-supplied next URLs.
3. Implement sign-up, confirmation, sign-in, session refresh and logout using the current provider SDK. For SSR, follow the provider’s cookie/token refresh model; do not treat an unvalidated client session object as proof of identity.
4. Implement recovery request, callback code/token exchange, new-password page and successful completion. Rate-limit attempts and use non-enumerating responses. Do not log recovery tokens.
5. For OAuth requested by the user, create the provider app with minimum scopes, exact callback URI and separate preview credentials. Keep client secrets server-only; validate state/PKCE through maintained libraries.
6. Provision initial admin through an authorized server/database operation; users cannot self-promote. Require reauthentication/MFA for sensitive admin actions when supported.
7. Test expired/revoked sessions, logout, blocked/unverified users, callback tampering and cross-account access. Document role revocation and JWT refresh behavior.

## Security considerations

Use Secure, appropriately SameSite cookies and CSRF defenses where cookies authorize writes. HttpOnly is the default for server-only sessions; some provider SSR browser SDKs intentionally need token access and require their documented cookie model plus strong XSS defense. Never blindly override SDK cookie requirements. Do not cache auth/personalized responses publicly.

## Free-tier limitations

Auth MAUs, rate limits, OAuth provider quotas, MFA methods and email delivery may be limited or paid. Supabase default email sending is restricted; production often needs custom SMTP. Accounts add maintenance and privacy responsibilities.

## Verification

Use test identities A/B/admin and attempt protected APIs directly. Confirm unverified login policy, password reset, correct callback, session expiry, logout and denial after role revocation. Distinguish UI hiding from server denial.

## Troubleshooting

Login loop: inspect cookie domain, HTTPS, redirect allowlist and token refresh integration. 401: validate token and expiry on server. 403: inspect roles/policies; do not broaden access. Missing mail: check SMTP, recipient restrictions, bounce logs and rate limits.

## Official documentation

[Supabase passwords](https://supabase.com/docs/guides/auth/passwords) · [Redirect URLs](https://supabase.com/docs/guides/auth/redirect-urls) · [Auth SSR](https://supabase.com/docs/guides/auth/server-side) · [Custom SMTP](https://supabase.com/docs/guides/auth/auth-smtp) · [OWASP sessions](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.
