# Product catalog

## Scope and components

Astro static product JSON/collections for infrequent changes; optional database/admin dashboard when live editing is required; optional Stripe for actual purchases.

## User journey

Visitor browses categories/details and accurate price/availability; editor changes description, images, minor-unit price/currency, status and category.

## Implementation sequence

Begin with typed content and Product JSON-LD matching visible facts. Select Git, database dashboard or CMS. If database-backed, implement product API contract with authenticated admin roles, public published-only projection, safe uploads, revisions and audit. A browse-only catalog needs no payment service. Stripe requires sandbox, server-owned prices, signed idempotent webhooks and fulfillment/reconciliation.

## Acceptance and operations

Test browsing/filter pagination, drafts invisible, non-admin direct writes denied, cross-user/tenant checks if relevant, price validation/concurrency and upload rules. If payments selected test duplicate/delayed/failed sandbox events and do not fulfill from the success page.

## Why this architecture differs

A catalog can remain static. Instant admin updates introduce database/policy/cache/backup needs; purchases add financial state and fees. Do not add both solely because products are listed.

Read [architecture selection](../../docs/03-architecture-selection.md), [security baseline](../../security/security-baseline.md), [cost guide](../../docs/23-cost-management.md), and [production checklist](../../docs/24-production-checklist.md). Create requirements, roadmap and deployment records before implementation. This is a design recipe, not an executed application; provider compatibility and quotas must be rechecked through [current sources](../../docs/sources.md).
