# Release verification evidence

Release/date/owner: fill. Intended source SHA: full SHA. Provider artifact/version: identify. Immutable preview URL: non-secret. Actual deployed SHA/version evidence: link. Production target/authorization/rollback: record separately. Keep private details in restricted evidence storage.

| Gate | Local | Hosted preview | Authorized production smoke | Evidence or blocker |
| --- | --- | --- | --- | --- |
| Exact version/configuration | Built commit and output | Provider SHA/version, config instance/rebuild | Expected version and safe config behavior | Avoid branch URL ambiguity |
| Environment parity | Migrations/settings expectation | Schema/RLS/template parity; intended differences | Approved migration/configuration | No customer-data sync |
| Payment/fulfillment (optional) | Unit/transaction behavior | Signed sandbox paid/free/delayed/duplicate/out-of-order events, persistence failure, outbox/email retry | Approved observation only | No second charge to repair access |
| Receiver lifecycle (optional) | Mode/event inventory | Active URL, paired signing-secret reference, valid and invalid delivery | Correct production receiver | Pending retries/retirement owner |
| Private files (optional) | Known synthetic file/hash | Authorized bytes + anonymous/wrong-user denial across ingress, encoded paths, ranges/cache if applicable | Approved safe reads only | A 404 alone is inconclusive |
| Access/roles (optional) | JWT/config failure cases | Human/machine distinction, wrong audience, scoped CI; webhook boundary | Approved denial checks | Machine access is not admin permission |
| Artifact boundary | Intended output manifest | No private assets/fixtures/reports/traces | Actual public output scope | Source-map decision recorded |
| Required evidence | Relevant tests/reports exist | Failure/skip/unavailable explicit | Current smoke/log evidence | No missing report counted as pass |

For every entry record pass/fail/skipped/unavailable/N/A-with-reason, date, command/manual procedure, expected/actual outcome and environment/version. A later relevant code/config change invalidates affected evidence. Apply [production checklist](../docs/24-production-checklist.md), [operations guide](../docs/25-operational-failure-modes.md) and AGENTS task states. No live tests have been executed by filling out this template's headings.
