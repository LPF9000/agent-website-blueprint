# Events website

## Scope and components

Astro listing/details/calendar + typed static events; optional database/admin event CRUD for frequent editors. No accounts for attendees unless required.

## User journey

Visitor finds an event in local time, opens an accessible detail and optional ICS export. Admin creates/edits/publishes/cancels event.

## Implementation sequence

Store timestamps with explicit offsets plus IANA zone, location, status, category and visibility. Render an accessible list alongside calendar grid. Add accurate Event JSON-LD and stable URLs/redirects. Use event contract for database CRUD and published-only public reads. Calendar sync is optional; bookings/tickets require separate transactional backend and possibly payment.

## Acceptance and operations

Test time zones/DST, end-before-start validation, cancellation, pagination and public draft hiding; admin denials/concurrent edits where selected. Check structured data and keyboard calendar fallback.

## Why this architecture differs

Temporal content needs date/zone validation, but display alone needs no database. Authoritative booking adds conflicts, idempotency, notification and recovery requirements beyond calendar rendering.

Read [architecture selection](../../docs/03-architecture-selection.md), [security baseline](../../security/security-baseline.md), [cost guide](../../docs/23-cost-management.md), and [production checklist](../../docs/24-production-checklist.md). Create requirements, roadmap and deployment records before implementation. This is a design recipe, not an executed application; provider compatibility and quotas must be rechecked through [current sources](../../docs/sources.md).
