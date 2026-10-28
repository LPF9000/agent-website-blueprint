# Website planning

## Purpose

Translate an idea into observable outcomes, scope and an executable roadmap.

## When needed

Before implementation and when requirements materially change.

## Prerequisites

A site owner who can decide audience, content and budget. Existing brand/content samples may help; do not upload real customer records.

## Recommended implementation

Use progressive discovery: purpose/audience first, then editing and interactions, then integrations/budget/privacy. Infer infrastructure from needs. Explain “a database stores shared changing data” rather than asking a beginner to choose SQL.

## Setup

1. Run the [master prompt](../prompts/website-builder.md) and answer one small group at a time.
2. Copy [requirements](../planning/requirements-template.md) into `.project/requirements.md`. Identify pages, journeys, editors and must-have/later/excluded features.
3. Make a role/action matrix for visitors, members and administrators. Identify data classification, retention/deletion, accessibility target and privacy reviewer.
4. Estimate visits, file sizes, update frequency, concurrency, email volume and budget. Mark uncertain estimates with an owner and review date.
5. Compare architectures in the next guide and record decisions. Create the roadmap from [its template](../planning/roadmap-template.md), giving every milestone acceptance criteria, dependencies, tests and owner.
6. Review the plan with the user. Convert vague “booking works” to “two concurrent attempts for one slot yield exactly one booking; cancellation releases it according to policy.”

## Security considerations

Collect the least data possible. Identify payments, personal data and privileged operations early. Record necessary consent/legal review without claiming that a generic checklist establishes compliance.

## Free-tier limitations

Choose a $0/month target only when projected usage and features fit free quotas. Document domain fees, agent costs and transaction charges separately. No optional account should require a card just to follow discovery.

## Verification

Every required feature maps to a milestone and test. Unknowns have owners; exclusions are explicit. A reader can identify who will edit content and whether accounts or live shared state are actually required.

## Troubleshooting

If scope expands, update requirements and dependencies before coding. If the user cannot answer a technical question, explain the user-facing tradeoff and recommend the simplest reversible option.

## Official documentation

[W3C planning accessibility](https://www.w3.org/WAI/planning/) · [OWASP threat modeling](https://owasp.org/www-community/Threat_Modeling)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.
