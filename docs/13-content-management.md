# Content management and optional integrations

## Purpose

Give editors an appropriate publishing workflow and add external services only for explicit requirements.

## When needed

Content changes over time; external CMS, payments, email, calendar and analytics are independently optional.

## Prerequisites

Content types, editorial roles, preview/publication expectations, data retention and integration-specific budget.

## Recommended implementation

Use Git content first for small sites. For non-source editors compare a database dashboard with external CMS. Prefer payment-hosted checkout, minimal email payloads, read-only calendar scope where possible and analytics without user identifiers by default.

## Setup

1. Define content schema, author/reviewer roles, draft/publish/archive states, media ownership and export/recovery. Use Markdown/JSON/content collections with PR previews when sufficient.
2. If editors need no source changes, implement the [database dashboard](11-admin-dashboard.md) or assess a CMS. Decap CMS is Git-backed and needs secure Git authentication; Sanity is managed with plan quotas; Directus is self-hostable with hosting, license and operational tradeoffs. These are options to assess, not preconfigured services. Inspect current official pricing/licenses before choosing.
3. Model CMS webhook/rebuild flow: verify signatures or shared-secret authentication using provider guidance, limit payload/rate and avoid exposing deploy hooks. Validate remote content at ingestion and sanitize HTML. Keep preview tokens server-only.
4. Payments (optional): simplest suitable Stripe Payment Links/hosted Checkout first. Use a separate sandbox; derive price/currency/items from server-owned catalog. Use restricted server credentials, verify webhook signatures on raw bytes, deduplicate events and fulfill only from verified paid state. Success pages are not proof of payment. Document refunds, failed/asynchronous payments and reconciliation before launch. See [integrations](integrations.md).
5. Transactional email (optional): Resend or existing SMTP via backend only. Verify sending domain records, fixed sender, recipient policy, template escaping, bounded submissions, idempotency and bounce handling. Never accept arbitrary mail headers/recipients from an unauthenticated contact form.
6. Calendars (optional): static event list/ICS export for display; provider OAuth only for actual sync/booking. Request minimal scopes, encrypt refresh tokens server-side, handle expiry/time zones/DST and use transactional reservations to prevent double-booking.
7. Analytics (optional): choose privacy-conscious aggregate metrics, omit identifying query strings/events, document retention and any consent/legal review. Cloudflare Web Analytics or server metrics may be sufficient. Third-party embeds can change privacy/CSP requirements.
8. Test publication, preview, sanitization, webhook retries and exports in isolated preview. Reconfirm quotas and costs before live integration.

## Security considerations

CMS tokens, webhook secrets, email keys, calendar refresh tokens and payment keys are server-only. Minimize stored customer data and never handle raw card numbers. Provider authentication does not replace local authorization/entitlement checks.

## Free-tier limitations

Git content mainly consumes builds. CMS free tiers limit editors/content/API/media; self-hosting adds compute/backup cost. Resend has daily/monthly sending limits; payment processing has fees and is not free hosting. Calendar quotas and analytics retention vary. See the [integration matrix](integrations.md) for alternatives and links.

## Verification

An editor can publish/unpublish and public content matches policy. Sandbox webhook duplicate/replay tests do not duplicate fulfillment. Email sends only to intended test recipients. Calendar cancellation/timezone conflict behavior is tested; analytics sends no personal identifiers.

## Troubleshooting

Build not triggered: inspect authenticated webhook delivery and provider logs. Mail rejected: verify DNS sender and recipient limits. Calendar duplicates: deduplicate provider IDs and update events idempotently. Payment pending: rely on verified asynchronous events, not redirect state.

## Official documentation

[Astro collections](https://docs.astro.build/en/guides/content-collections/) · [Decap CMS](https://decapcms.org/docs/) · [Sanity docs](https://www.sanity.io/docs) · [Directus docs](https://directus.io/docs/) · [Resend docs](https://resend.com/docs) · [Stripe Checkout](https://docs.stripe.com/payments/checkout) · [Google Calendar API](https://developers.google.com/workspace/calendar/api/guides/overview) · [Cloudflare Web Analytics](https://developers.cloudflare.com/web-analytics/)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.
