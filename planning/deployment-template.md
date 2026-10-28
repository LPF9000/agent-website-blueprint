# Deployment record

## Configuration

Provider/account/project identifiers (non-secret); runtime/tool versions; root/build/output/deploy commands; preview/production branches; environment variable names and where set (never values); bindings and isolated data resources; domain/DNS/TLS and header ownership.

## Release ledger

| Date | Environment and URL | Commit / provider version | Approval scope | Build / tests | Post-deploy evidence | Rollback target |
| --- | --- | --- | --- | --- | --- | --- |
| YYYY-MM-DD | Local / preview / production | Identify exact artifacts | Record authorization reference | Commands/results | Journeys/headers/logs and limitations | Known-good version |

## Deployment and rollback runbook

Write numbered, provider-verified steps to build, test preview, review, authorize promotion, deploy, verify hostname and contain failures. Include who can execute rollback and how to confirm restored behavior. Database rollback is separate: describe backward-compatible migrations and recovery/export steps, backup age and restore evidence. State scheduled maintenance/notification ownership and unresolved blockers.
