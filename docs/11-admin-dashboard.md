# Optional administration

## Purpose

Let authorized editors manage products, events, content and files without changing application code.

## When needed

Frequent updates or nontechnical editors. A custom dashboard is not mandatory for every site.

## Prerequisites

Editor workflow, content schema, role/action matrix, publication lifecycle, audit/retention requirements and chosen authentication.

## Recommended implementation

| Approach | Choose when | Tradeoff |
| --- | --- | --- |
| A: Git-based Markdown/JSON/collections | Small editorial workload | Reviewable/versioned; GitHub editor works without local tools, but source changes and builds still occur |
| B: Database-backed dashboard | Immediate changes and custom workflows | Custom secure CRUD, migrations, audit and recovery responsibilities |
| C: External CMS | Dedicated visual/editor experience | Vendor/self-hosting cost, schema/API integration, roles and export limits |

For B, start with one protected content type, then extend common patterns to announcements, categories, visibility, image management, products/prices and event/calendar entries. The dashboard must cover create/edit/publish/unpublish/delete with confirmation and useful error states.

## Setup

1. Define each entity and editable field. Prices use integer minor units plus currency; events record time/zone, start/end and cancellation status. Separate internal notes from public fields.
2. Implement server authentication and an administrator/editor policy on every API operation. Use server-controlled roles or membership tables, not browser flags/user-editable metadata. Keep public queries restricted to published, non-deleted content.
3. Add list/search, bounded cursor pagination, create/edit forms, validation, drafts, preview and explicit publish/unpublish. Reference the [product/event API contracts](../templates/api/README.md).
4. Enforce schema/field allowlists, request size and rate limits server-side. For cookie writes apply CSRF tokens and trusted-origin checks appropriate to framework. Reject unexpected fields and unauthorized object identifiers.
5. Store multi-entity changes in a transaction. Add revision/ETag optimistic concurrency and return conflict rather than silently overwriting another editor. Use soft deletion where recovery/retention warrants it, with separate approved hard-deletion policy.
6. Add private file uploads with size/type/signature validation, generated names and short-lived signed access. Sanitize rich content; do not serve arbitrary active content from the site origin.
7. Write append-only, access-controlled audit events with actor/action/object/time/result and no secrets/raw request bodies. Restrict who can read logs. Handle success, empty state, denial, stale revision and server errors clearly.
8. Apply versioned migrations to isolated preview first. Test all roles and denial cases, restore content and verify audit records before production authorization.

## Security considerations

Hidden admin navigation is not security. Use no-store for private responses and CSRF protection where cookies authorize actions. Apply RLS/least privilege at the database; ensure a privileged backend explicitly authorizes before using a secret key.

## Free-tier limitations

A custom dashboard consumes auth/database/storage/compute quotas and engineering time. Git editing may be simpler and cheaper. CMS free plans can limit editors, documents, requests, media and roles; advanced permissions are often paid.

## Verification

Non-admin direct POST/PATCH/DELETE must fail. Test drafts invisible to public, invalid prices/dates, oversized uploads, duplicate requests, concurrent edits, paging and soft-delete restore. Verify an editor can complete the whole workflow without source-code editing for B/C.

## Troubleshooting

UI succeeds but public content stale: inspect cache invalidation/build publish hook. Empty update: inspect authorization/policies and revision. Unauthorized content visible: immediately restrict public projection/query and purge relevant caches.

## Official documentation

[OWASP authorization](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) · [REST security](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html) · [File uploads](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) · [PostgreSQL transactions](https://www.postgresql.org/docs/current/tutorial-transactions.html)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.
