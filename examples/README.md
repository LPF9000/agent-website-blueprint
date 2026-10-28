# Architecture recipes

These are lightweight design examples, **not complete applications and not integration-tested deployments**. Follow the guides and create project requirements/roadmap before implementing. Each recipe explains what changes as needs grow.

| Recipe | Primary difference |
| --- | --- |
| [Static portfolio](static-website/README.md) | No runtime data/auth; Git content and static hosting |
| [Business website](business-website/README.md) | Optional public form adds server validation/spam/email controls |
| [Product catalog](product-catalog/README.md) | Static browsing can stay simple; admin/payments add independent modules |
| [Events/calendar](events-calendar/README.md) | Temporal content, publication and optional CRUD; booking is separate |
| [Authenticated app](authenticated-app/README.md) | Identity/ownership/RLS and private cache boundaries |
| [Admin API](admin-api/README.md) | Server-authorized CRUD contract independent of UI |

Blogs/docs generally follow static content; communities/SaaS follow authenticated application patterns; appointments require transactional reservations and may add calendar/payment integrations. Never imply a calendar widget prevents double-booking.

## Runnable local walkthrough

[Worked static example](worked-static-site/README.md) adds a small fictional HTML/CSS fixture with actual requirements, decisions, roadmap, implementation, local HTTP tests and handoff. Unlike the architecture recipes above, this fixture has executed local evidence. It has no hosted deployment or browser/accessibility certification.
