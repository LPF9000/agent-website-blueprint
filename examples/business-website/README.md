# Small business website

## Scope and components

Astro static content + Cloudflare; optional small Worker contact endpoint and Turnstile. Resend/existing SMTP only if requested. No accounts or database by default.

## User journey

Visitor browses services/location/hours, then submits a contact request or uses a phone/email link. Editor updates content through Git or selected CMS.

## Implementation sequence

Start with static pages and business/Organization structured data using true facts. If a form is required, bound/validate input, verify Turnstile server-side with hostname/action, enforce shared rate limits and fixed recipient/sender. Use test delivery on preview and clear failure/success states. Do not retain contact data without purpose.

## Acceptance and operations

Test missing/invalid/replayed challenge, oversized input, rate failure, keyboard errors and delivery to intended test recipient only. Production scheduled checks use GET only and must never submit forms/send emails.

## Why this architecture differs

The form adds abuse/cost/privacy exposure, unlike a static portfolio. A mailto/phone link avoids that server module. Email quotas and domain verification may require setup/cost even with free hosting.

Read [architecture selection](../../docs/03-architecture-selection.md), [security baseline](../../security/security-baseline.md), [cost guide](../../docs/23-cost-management.md), and [production checklist](../../docs/24-production-checklist.md). Create requirements, roadmap and deployment records before implementation. This is a design recipe, not an executed application; provider compatibility and quotas must be rechecked through [current sources](../../docs/sources.md).
