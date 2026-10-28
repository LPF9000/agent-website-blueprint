# Security audit checklist

Record commit, date, environment, reviewer, result and evidence per item. Unknown is not passed. Applicable failures block release until resolved or an explicit, documented risk decision is made by the accountable owner.

- [ ] Trust boundaries/data classes and abuse cases documented; optional modules match actual requirements.
- [ ] Correct account/project/domain; MFA, least-privilege permissions and recovery owners verified.
- [ ] HTTPS, certificate and intentional redirects; HSTS staging/subdomain scope reviewed.
- [ ] CSP works with actual scripts/styles/widgets; no blind wildcard/unsafe-eval exceptions. Static, API, denied and error responses covered.
- [ ] MIME/nosniff, referrer, permissions and framing policy verified on actual responses.
- [ ] Secrets absent from staged files/history/build/logs/screenshots; preview/production credentials isolated.
- [ ] Auth verified server-side; confirmation/recovery/logout/expiry/revocation tested if selected.
- [ ] Direct unauthorized, cross-user and non-admin API/data operations denied; role self-promotion impossible.
- [ ] Every exposed Supabase table has RLS and correct grants/policies; views/functions/storage separately audited. Secret-key bypass usage justified.
- [ ] SQL parameterization, field allowlists, schema/business validation, actual byte bounds, shared rate control and transactional invariants tested.
- [ ] CORS exact origins only where necessary; cookie writes have applicable CSRF protection; GETs do not mutate.
- [ ] Untrusted content escaped/sanitized; upload size/signature/type/access/quarantine rules tested.
- [ ] Private data excluded from shared caches/service workers; A/B tests show no leakage.
- [ ] Webhooks signature-verified and deduplicated; payment fulfillment based on verified state, not return URL.
- [ ] Dependency/lockfile/advisory review, pinned Actions and minimal time/permission/artifact settings pass.
- [ ] Redacted restricted logs, backup/restore evidence, incident plan and notification ownership present.
- [ ] Preview private content protected and noindex; public production SEO does not reveal private data.
- [ ] Known limitations, unexecuted checks and safe remediation tasks recorded in progress/handoff.

Use [baseline](security-baseline.md), [auth](authentication-security.md), [API](api-security.md), [database](database-security.md), [Cloudflare](cloudflare-security.md), [dependencies](dependency-security.md) and [incident response](incident-response.md). Review [OWASP ASVS](https://owasp.org/www-project-application-security-verification-standard/) for requirements appropriate to actual risk. Automated scanners cannot complete this review alone.

## Operational cross-check

- [ ] [Operational failure modes](../docs/25-operational-failure-modes.md) tested for selected modules: required configuration absent, exact preview version, private bytes across ingress, signed user/machine Access identities, webhook/entitlement/outbox recovery and missing-report failure. Tests use synthetic isolated data and record unknowns honestly.
