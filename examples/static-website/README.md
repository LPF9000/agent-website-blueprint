# Static portfolio

## Scope and components

Astro + TypeScript, Markdown/content collections, CSS or optional Tailwind; Cloudflare Workers static assets or Pages. No database, Auth, dashboard, email or custom API.

## User journey

Designer publishes project stories through GitHub edits/PR previews. Build creates public project/detail pages, sitemap and optimized images.

## Implementation sequence

Create home/about/projects/contact-link/404, use semantic layouts and route metadata, copy an adapted static header policy, configure preview noindex and deploy isolated preview. Git-based content has review history; updates require a build.

## Acceptance and operations

Build/type check, navigation/404/mobile/keyboard, social/canonical/sitemap and actual deployed headers. Test no client secrets. Source plus original media backup; daily public health and weekly dependency/link review.

## Why this architecture differs

Static output avoids runtime CPU/data recovery obligations. Add a CMS only when editing needs exceed Git workflow; add a form Worker only if contact-link is insufficient.

Read [architecture selection](../../docs/03-architecture-selection.md), [security baseline](../../security/security-baseline.md), [cost guide](../../docs/23-cost-management.md), and [production checklist](../../docs/24-production-checklist.md). Create requirements, roadmap and deployment records before implementation. This is a design recipe, not an executed application; provider compatibility and quotas must be rechecked through [current sources](../../docs/sources.md).
