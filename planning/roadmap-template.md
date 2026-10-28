# Website roadmap

Updated: YYYY-MM-DD. Required release evidence: hosted preview Tested, then Verified in production for launch.

| ID | Milestone | State | Depends on | Acceptance criteria | Verification | Owner / blocker |
| --- | --- | --- | --- | --- | --- | --- |
| M1 | Requirements and architecture | Not started | None | Audience, journeys, exclusions, budget and ADR recorded | Review requirements and decisions against user answers | Assign owner |
| M2 | Frontend and content | Not started | M1 | Required pages and error states usable on mobile and keyboard | Build, responsive/keyboard checks, content journey smoke | Assign owner |
| M3 | Required dynamic modules | Not started | M1 | Only selected auth/admin/API/payment modules, with denial cases | API/integration/authorization tests in isolated environment; mark N/A with reason if static | Assign owner |
| M4 | Security and hosted preview | Not started | M2, M3 | Applicable baseline, SEO and accessibility evidence recorded | Preview smoke, headers, noindex, policy and quality checks | Assign owner |
| M5 | Authorized production release | Not started | M4 | Production checklist satisfied, rollback and backup documented | Exact commit/hostname read-only smoke and logs | Assign owner; approval pending |
| M6 | Operations and handoff | Not started | M5 | Monitoring owner, notifications and recurring reviews selected | Induced harmless monitor failure/test notification; handoff review | Assign owner |

Break milestones into tasks with ID, scope, dependencies, owner, acceptance criteria, verification command/manual procedure, expected result, state and evidence link. A task moves to Implemented when code exists, Tested only after checks pass, Deployed on provider success and Verified in production only after actual production checks. Blocked entries name reason and next action; do not hide them in completed milestones.
