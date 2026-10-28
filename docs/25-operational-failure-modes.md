# Operational failure modes and release evidence

## Purpose

Prevent a successful build, payment or dashboard update from hiding a broken user journey. These are generic engineering patterns; adopt only the modules selected in requirements. Use the [environment matrix](../planning/environment-matrix-template.md) and [release evidence template](../planning/release-evidence-template.md) alongside the existing deployment record.

## When needed

Review before significant hosted releases, when changing configuration or external integrations, and during failure recovery. Static sites need artifact/preview/evidence checks; payments, downloads, Access and databases remain optional.

## Prerequisites

An exact commit/provider version, non-secret resource inventory, isolated preview with synthetic identities/data, selected integration owners, current official documentation and explicit authorization for production-impacting changes. Do not copy another project's configuration, identifiers, URLs, content or code into a new blueprint consumer.

## Recommended implementation

Use one small release record that connects source commit, built artifact, runtime settings, provider configuration and observed user outcomes. Test failure cases in isolated preview. A queue/outbox is justified when reliable asynchronous side effects require it; a static site needs none. Keep infrastructure account security, site-user authentication and business authorization distinct.

## Setup

### 1. Track configuration lifecycle and parity

1. Classify each setting as public build-time, server build-time, runtime variable/secret, binding, database migration or external-provider setting. Record names and secret-store references, never secret values. Public build-time variables are embedded in artifacts and require a rebuild when changed.
2. For runtime changes inspect current provider behavior: a shared/base setting may be inherited only when a preview is created; changing it does not prove an existing instance changed. Verify the specific deployed preview and recreate/update it through supported operations if needed. Do not universally assume either snapshotting or live inheritance.
3. Record intended parity across environments: schema/migration versions, RLS/grants, Auth email subjects/templates and feature policy. Deliberate differences include identities/data, SMTP credentials, sender/test-recipient rules, callback URLs, payment mode and runtime secrets. Infrastructure dashboard MFA does not establish customer MFA.
4. Promote the same reviewed migration files through test then authorized production. Check migration history and drift first; do not repair bookkeeping or import a live schema blindly. Configuration sync must use an explicit allowlist and leave environment-specific secrets, URLs and customer rows untouched.
5. Shared preview data means shared state: namespace synthetic fixtures or serialize conflicting tests, document cleanup ownership and obtain approval for resets. Avoid public reset routes; never reset a paid/customer identity or copy customer data into preview.

### 2. Resolve and test the exact preview

1. Match deployment provider evidence to the full intended commit SHA and immutable version URL where supported. A branch URL alone may point at a newer or older build.
2. Poll with a finite deadline, modest interval/backoff and redacted progress. Size wait/job limits to measured provider build duration and budget; this blueprint's short health-job limits are not universal deployment-wait limits. Fail promptly on terminal build errors. A timeout is not a passed test and not proof of a code defect.
3. Re-query provider state before a bounded retry of a transient upload/API error. Avoid duplicate deployments and speculative code edits for an observed provider failure.
4. Test local and hosted behavior separately. Record expected version, actual version and test outcome. Prevent a later preview promotion from invalidating results; rerun affected checks when settings/artifacts change.

### 3. Make payment fulfillment recoverable

1. Define separate observable states: payment confirmed, entitlement/order stored, download/service access available, confirmation queued/sent. The user-facing success page should show pending/retry/support states accurately without granting access based on URL parameters.
2. Verify signed raw webhook bytes, derive authoritative transaction/product/user mappings and handle duplicate/out-of-order events. Use unique business keys and a durable event receipt; marking an event as processed before its side effects commit can lose fulfillment.
3. Acknowledge success only after the required work commits or the event is durably accepted for retry. In synchronous handling, transient persistence failures must return an appropriate retryable failure, not a false success. If using a durable queue, return success after reliable enqueue and monitor/retry downstream failures. Invalid signatures are rejected, not retried as trusted jobs.
4. Commit entitlement/order and durable email/outbox work transactionally where feasible. Process mail idempotently; an email outage must not charge twice, revoke a valid purchase or repeat entitlement creation. Provider idempotency windows are finite; keep business-level deduplication durable for your required retention.
5. Build a restricted reconciliation runbook comparing verified payment state with internal fulfillment and pending notifications. Replay only through authorized idempotent handling; never ask a customer to pay again to repair a lost entitlement. Define free/no-payment-required eligibility explicitly rather than accidentally granting a paid product.
6. Maintain an environment-specific webhook receiver inventory. A closed/deleted PR hostname can leave a sandbox endpoint stale. Prefer a stable isolated test receiver where suitable, or explicitly update/verify the active destination, subscribed events and paired signing secret. Disable stale receivers safely after checking pending deliveries and retention; never repoint live traffic to preview.

### 4. Protect files across every ingress

1. Keep paid/private originals outside public asset output by default. Serve through an authorized backend or constrained short-lived signed download after checking current entitlement. A UI-hidden link is not protection.
2. Inventory custom domains, provider subdomains, preview/version URLs, alternate origins and storage/public bucket URLs. Every reachable route to private bytes must enforce equivalent authorization; protect or disable alternate ingress.
3. In preview, use a known synthetic file and compare authorized success (expected bytes/hash and disposition) with anonymous, wrong-user and expired-session denial. Test direct paths, encoded segments/separators, duplicate slashes, case behavior, GET/HEAD, redirects, ranges and cache behavior where the stack supports them. Normalize consistently and reject ambiguous paths rather than relying on one literal prefix test.
4. A 404 alone proves only the observed response, not that the file existed or that authorization protected it. Pair denied and authorized evidence for the same known object. A 200 HTML login/error page is not a successful file download. Do not forward credentials across origins while following redirects.
5. Publish only the reviewed framework output directory. Inspect the artifact manifest for unintended fixtures, internal routes, backups, test reports, traces, source maps and private assets. Source maps are a deliberate disclosure decision. CI artifacts stay outside publicly served assets with bounded, restricted retention.

### 5. Use Access identities and external callbacks deliberately

1. If Cloudflare Access is selected, validate its signed JWT through current maintained library/provider guidance: signature/key selection, allowed algorithm, issuer, application audience, expiration and relevant time claims. Header presence or decoding alone is not authentication. Reject malformed tokens and unavailable verification safely; keep useful internal diagnostics redacted.
2. Separate user and machine identities. Cloudflare documents service-token application tokens whose subject can be empty; do not impose a human-email/nonempty-sub rule universally. Require claims appropriate to the expected token type, then authorize the intended role/action. Machine preview access must not automatically grant an application admin role.
3. Use scoped service credentials for authorized CI, stored in restricted secrets, never browser code/artifacts or untrusted PR jobs. Test no token, invalid/expired token, wrong audience and permitted machine access. Dashboard MFA, Access login and website member MFA are separate controls.
4. External webhook providers may not supply Access credentials. Prefer an appropriately protected receiver architecture. If a bypass is necessary, obtain production/security authorization and constrain it to the exact intended hostname/path/method scope supported by the product; verify policy precedence and require application-level signed-webhook validation. Never bypass the entire preview/admin/API subtree. Verify both valid sandbox delivery and unsigned/invalid rejection.

### 6. Keep failures and vulnerability claims honest

1. Required protections must fail closed on missing configuration, verification timeout or malformed input. A missing bot-verification secret must not silently disable a required challenge. Test missing success/action/hostname results according to the selected challenge contract. Rate limiting may be approximate/eventually consistent; transactional quotas and scarce inventory need authoritative controls.
2. Report pass, fail, skipped, unavailable and not-applicable distinctly. Missing/invalid scan reports, unreachable targets and unexecuted tests cannot become zero findings or green security claims. Explain scan scope, ignored rules and coverage exclusions. Fail required gates on absent evidence; optional skipped work remains explicitly unverified.
3. Triage advisories against actual deployment: build tools, browser dependencies, runtime server code and managed service components differ. Do not claim a server-only exploit applies solely because the package is installed, or dismiss build-chain risk because output is static. Record affected versions/exposure, update supported dependencies and retest relevant behavior.

## Security considerations

All mutation, replay, reset and hostile-path tests belong in an explicitly authorized isolated environment with synthetic data. Production smoke stays within approved read-only scope. Keep credentials and personal/event payloads out of source, reports and alerts. Never weaken Access, RLS, TLS or validation just to get a green result. Use a bounded retry plan and retain an incident trail when recovery affects real users.

## Free-tier limitations

Shared test projects may save money but require fixture coordination. Isolated databases, durable queues, retained event logs, email and file bandwidth have quotas/costs. Start with the simplest reliable selected workflow, document exhaustion behavior and obtain approval before paid usage. A provider's short idempotency window or limited log retention is not a durable recovery strategy.

## Verification

Record the environment matrix and exact-version release evidence. Where applicable, prove configuration changes reached the actual artifact/runtime; preview/production intended parity; duplicate/out-of-order and failed fulfillment recovery; mail outage independence; active webhook receiver; known-file authorized/denied access across ingress; Access user/machine separation; missing-security-config denial; artifact publication boundaries; and honest missing-report failure. These are required consumer checks, not tests executed by this documentation repository.

## Troubleshooting

Wrong public configuration: rebuild and inspect non-sensitive host/mode behavior, without printing keys. Wrong runtime setting: inspect the exact preview instance and provider inheritance rules. Paid but no access: trace verified transaction → internal receipt → entitlement/outbox, repair idempotently, and reconcile; do not repeat payment. Webhook absent: inspect receiver lifecycle, mode, signing-secret pairing and Access routing. Download test 404: establish a real synthetic fixture and permitted success first. Preview timeout: inspect actual provider state for the exact SHA, then adjust bounded wait or retry only the identified transient failure. Missing scan result: report unavailable and fix the job/report path instead of claiming a pass.

## Official documentation

- [Cloudflare preview configuration](https://developers.cloudflare.com/workers/previews/configuration/) and [secrets](https://developers.cloudflare.com/workers/configuration/secrets/): inspect current inheritance/update semantics.
- [Access JWT validation](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/validating-json/), [application token shapes](https://developers.cloudflare.com/cloudflare-one/access-controls/applications/http-apps/authorization-cookie/application-token/) and [service credentials](https://developers.cloudflare.com/cloudflare-one/access-controls/service-credentials/service-tokens/).
- [Stripe webhook handling](https://docs.stripe.com/webhooks) and [fulfillment](https://docs.stripe.com/checkout/fulfillment): current signature, retry, ordering and idempotency guidance.
- [Supabase migrations](https://supabase.com/docs/guides/deployment/database-migrations), [Auth SMTP](https://supabase.com/docs/guides/auth/auth-smtp), and [Storage access](https://supabase.com/docs/guides/storage/security/access-control).
- [OWASP authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) and [GitHub workflow security](https://docs.github.com/en/actions/reference/security/secure-use).

Reviewed official focused guidance: 2026-10-28 where marked in the [source register](sources.md). Match installed versions using the [freshness protocol](source-freshness.md). No cloud changes, payment/email flow, private-download service or Access integration was executed for this documentation update.
