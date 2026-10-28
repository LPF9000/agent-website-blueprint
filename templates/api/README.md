# Product and event API design contracts

[products.openapi.json](products.openapi.json) and [events.openapi.json](events.openapi.json) are OpenAPI 3.1 **design contracts**, not deployed endpoints or complete handler examples. Paths belong to the generated application, not a vendor. Implement only selected entities and align schema/migrations/UI together.

## Contract behavior

- GET list/detail is public only for published non-deleted public fields; drafts/private data are never included. Bounded cursor pagination defaults 20, maximum 50. A cursor must encode/validate stable ordering, not raw SQL.
- POST creates content (draft default); PATCH edits/publishes/unpublishes; DELETE soft-deletes where retention/recovery policy allows. Every mutation requires validated server identity, admin role and object/tenant authorization. Hidden UI or a bearer token alone is insufficient.
- Cookie and bearer security schemes are alternative illustrative transports. Use the chosen identity provider's actual cookies/token validation. Cookie writes additionally require CSRF protection and exact trusted-origin checks. The OpenAPI security marker does not enforce either roles or CSRF by itself.
- Inputs reject unknown fields, enforce streamed body ≤16 KiB (adjust deliberately for your model), validate text/slug/date/business rules and parameterize SQL. Product prices are integer minor units plus currency; do not trust browser prices at payment time. Events require end after start and valid IANA zone/DST handling.
- Return ETag based on revision for detail/update and require If-Match for update/delete. Apply compare-and-update transactionally to prevent lost edits. Mutation responses are no-store; append redacted restricted audit entries. Do not expose DB exception text.
- Distinguish 401, 403/404, 409/412, 413, 415, 422 and 429. 204 has no body. Return stable error code/request ID in implementation; schema/error-body detail must be finalized for the selected framework.

## Example payloads

Product create: `{"slug":"field-notebook","name":"Field Notebook","price_minor":1800,"currency":"USD","published":false}`.

Event create: `{"slug":"community-workshop","title":"Community Workshop","starts_at":"2027-03-10T18:00:00-08:00","ends_at":"2027-03-10T19:30:00-08:00","time_zone":"America/Los_Angeles","location":"Community Hall","status":"scheduled","published":false}`. Validate the UTC offset against zone/date; examples are synthetic, not real event data.

## Implementation and verification

Use [API guide](../../docs/12-api-development.md), [admin guide](../../docs/11-admin-dashboard.md) and [database security](../../security/database-security.md). Add auth/role policy and tests before exposing routes. Test anonymous/non-admin/cross-tenant access, stale revision, oversized/invalid body, publication visibility and transaction rollback in isolated preview. Products/events are not permission to expose an unrestricted admin API.

JSON and local `$ref` integrity are checked here; full OpenAPI conformance and runtime contract tests require an implementation and a current official [OpenAPI validator/spec](https://spec.openapis.org/oas/latest.html). No endpoint was deployed or exercised by this blueprint.
