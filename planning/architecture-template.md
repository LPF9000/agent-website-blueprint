# Website architecture

Updated: YYYY-MM-DD. Decision references: list IDs.

## Components and data flow

Describe browser → hosting/static assets → optional API → database/storage/external service. Identify trust boundaries, where authentication/authorization happens, which responses are cacheable and which data is public/private. Include framework/tool versions and official compatibility references.

## Modules selected and excluded

| Module | Selected? | Reason / requirement | Data / permission owner | Alternative |
| --- | --- | --- | --- | --- |
| Static content | Decide | Update frequency | Content owner | Database/CMS only if needed |
| Auth / admin / API | Decide independently | User journey | Roles and per-object rules | No accounts |
| Database / uploads | Decide | Data model and recovery | Grants/RLS/storage policies | Markdown/JSON |
| Payments / email / calendar / analytics | Decide independently | Actual requirement | Restricted scopes and retention | Omit |

## Environments and operations

Local, isolated preview and production resource identifiers (non-secret), configuration variable names, migrations, deployment/promotion, rollback, backup RPO/RTO, monitor ownership and usage budgets. Document API contracts and data lifecycle. List known compatibility gaps and unresolved questions.
