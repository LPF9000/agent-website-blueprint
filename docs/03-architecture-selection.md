# Architecture selection

## Purpose

Choose a small, maintainable system rather than forcing every site into one stack.

## When needed

After requirements, before installing frameworks or provisioning services.

## Prerequisites

Requirements, content update frequency, role model, traffic estimate and budget.

## Recommended implementation

| Requirement | Start with | Add only when justified |
| --- | --- | --- |
| Portfolio, business information, blog, docs | Astro static generation + Markdown/content collections | Search, CMS or form endpoint |
| Dynamic accounts or SaaS | Next.js or another maintained application framework | Auth, SQL database, protected API |
| Catalog/events with infrequent edits | Static JSON/collections | Database/admin when editors need instant changes |
| Booking/inventory | Backend with transactions and uniqueness constraints | Calendar/payment integration |
| Tiny existing site | Keep plain HTML/CSS if sufficient | Build tooling only for a clear benefit |

TypeScript is the default. CSS modules/plain CSS or optional Tailwind are styling choices, not backend requirements. Cloudflare Workers static assets or Pages can serve static output. Next.js server features require an explicitly compatible Workers deployment path. As reviewed 2026-10-28, Cloudflare’s Next.js guide recommends vinext for new projects and describes OpenNext for compatibility gaps in existing apps. This can change: verify framework/runtime support rather than copying an old adapter recipe.

## Setup

1. Draw browser, static host, optional API, storage and external services with trust boundaries.
2. Start with no database/auth. Add each module only for a named requirement; record rejected alternatives in an ADR.
3. Choose Workers static assets for a new straightforward static deployment, or Pages for its suitable existing Git workflow. Select server runtime using current framework docs. Pages is not a general Node.js server.
4. Compare [storage options](08-database-options.md). Decide Git content, custom dashboard or external CMS separately from frontend.
5. Test required runtime features in a small isolated preview before committing to the stack. Record versions, compatibility gaps, exit/data-export and rollback approach.

## Security considerations

A smaller public static attack surface still needs safe headers, dependency hygiene and account security. Dynamic APIs add authorization, validation and rate controls; adding a database adds policy and recovery obligations.

## Free-tier limitations

Static output is typically the lowest-cost route. SSR executes compute and may exceed free CPU/request budgets. A managed auth/database reduces coding but adds quotas and service dependencies. See [cost guide](23-cost-management.md).

## Verification

The ADR maps choices to requirements, rejects unnecessary modules and includes a hosted compatibility spike for required server features. Do not label architectural recipes as executed applications.

## Troubleshooting

If a Node library fails in Workers, inspect its runtime assumptions and the current adapter support table. Consider replacing the library, static generation or a documented alternative host before adding infrastructure.

## Official documentation

[Astro Cloudflare](https://docs.astro.build/en/guides/deploy/cloudflare/) · [Cloudflare Next.js](https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/) · [Workers static assets](https://developers.cloudflare.com/workers/static-assets/) · [Next.js docs](https://nextjs.org/docs)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.
