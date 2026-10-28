# Cost management

## Purpose

Target $0/month where realistic and make quota/paid boundaries explicit before commitments.

## When needed

Architecture planning, provisioning, launch and monthly review.

## Prerequisites

Traffic/request/CPU, storage/egress, email and editor estimates, account plan/region, annual domain budget and a spending owner.

## Recommended implementation

Begin with static Astro on a provider subdomain and no database/accounts/email/paid tooling. Add a service only for a required journey. Treat the following as a dated planning snapshot, not a guarantee; current official pricing and dashboard entitlements control.

## Setup

| Service | Free/limited starting point reviewed 2026-10-28 | What changes cost or availability |
| --- | --- | --- |
| Workers | Free dynamic requests: 100,000/day; 10 ms CPU/invocation | SSR/API/abuse can exhaust quota; paid plan and overages differ |
| Static assets / Pages | Static serving has favorable free pricing; Pages Free currently 500 builds/month, 20,000 files and 25 MiB/asset | Functions use Workers quota; Builds and other products have separate limits |
| Supabase (optional) | Free currently 2 active projects, 500 MB DB, 1 GB file storage, 50k MAUs and limited egress | Inactivity pause, database/files/bandwidth, email, backups, paid availability requirements |
| D1 / KV (optional) | Limited rows/operations and stored data | Query scans, write volume and storage; Free may fail rather than auto-scale |
| R2 (optional) | Standard storage/request free allowances | Billing activation may be required; storage, Class A/B operations and other storage classes differ |
| GitHub Actions | Standard public-repository runner use differs from private included minutes/storage | Larger runners, private quota, artifacts/cache, enabled spending |
| Resend (optional) | Free currently 3,000 transactional emails/month, 100/day | Sends beyond quota need plan review; sender/domain requirements apply |
| Stripe (optional) | Sandbox testing is not a real-money fee | Live transactions, FX, Billing/Tax/add-ons/refunds/disputes; country-specific fees |
| Domain | Provider subdomain avoids registration purchase | Custom domain annual registration/renewal and premium names |
| Monitoring/CMS/analytics/calendar | Basic tools may be free with limits | Check intervals, users, requests, storage, history, OAuth verification and operational hosting |

1. Record current plan/region and official pricing URL for each **selected** service in `.project/decisions.md` and deployment records. Skip unneeded accounts and avoid card-required services by default.
2. Estimate monthly usage plus abuse/spikes, build frequency, retention and preview resources. Keep a reserve and explicit review thresholds (for example 50/80/95% of a quota).
3. Configure available usage alerts/spend controls; confirm whether they are hard caps or notifications. A budget alert does not necessarily stop charges. Do not enable automatic overage or paid upgrades without approval.
4. Review actual usage monthly and after traffic/integration changes. Remove unused previews/integrations only after checking retention/recovery and obtaining destructive-change approval where necessary.

## Security considerations

Abuse can consume quota even when it cannot access private data. Rate-limit costly actions, cap payloads and paginate. Never weaken auth or delete required backups merely to meet a $0 target; revise requirements/budget instead.

## Free-tier limitations

No significant-traffic, database-heavy, payment-processing or paid-integration website is guaranteed free. Free plans may pause, throttle/fail and offer limited support/retention. Domain fees and agent subscriptions are separate from hosting.

## Verification

For each selected service, confirm dashboard plan, quotas, card requirement, spending behavior and alerts. Compare observed preview usage to estimates and document what happens at exhaustion. Recheck numbers at provisioning and launch.

## Troubleshooting

Unexpected bill: inspect per-product usage, preview duplication, build loops, image transforms and bot traffic. Quota failure: identify exact meter and reduce unnecessary load; obtain informed approval before upgrading. Never present a provider’s “unlimited” marketing label as unlimited overall infrastructure.

## Official documentation

[Workers pricing](https://developers.cloudflare.com/workers/platform/pricing/) · [Pages limits](https://developers.cloudflare.com/pages/platform/limits/) · [Supabase pricing](https://supabase.com/pricing) · [D1](https://developers.cloudflare.com/d1/platform/pricing/) · [KV](https://developers.cloudflare.com/kv/platform/pricing/) · [R2](https://developers.cloudflare.com/r2/pricing/) · [Actions billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions) · [Resend](https://resend.com/pricing) · [Stripe fees](https://stripe.com/pricing)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.
