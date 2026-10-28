# Blueprint validation report

Validation date: 2026-10-28. Scope: documentation repository and its offline Python tooling. No cloud integration was deployed to claim production readiness. The later worked example has local-only evidence below.

## Executed checks

| Check | Result / evidence scope |
| --- | --- |
| Required structure | All requested root documents, 24 guides, six prompts, planning/security/automation modules, six recipe folders and template modules checked by scripts/validate.py |
| Markdown links/anchors | Relative Markdown destinations and heading anchors checked; empty files and links escaping the repository rejected. Generated website .project paths described in prose are intentionally not required as template destinations. |
| Guide completeness | All 24 guides include purpose, applicability, prerequisites, recommendation, ordered setup, security, free-tier limitations, verification, troubleshooting and official references. |
| JSON | Parsed with duplicate-key rejection; internal JSON references resolved; product/event mutation contracts require explicit security. Full OpenAPI specification validation is not claimed. |
| YAML | PyYAML 6.0.3 with duplicate-key detection and correct handling of GitHub on; workflow permissions, timeouts, checkout credential persistence and full action SHA pins checked. Not a complete GitHub Actions schema/expression validator. |
| Secret/configuration review | Empty env example values; high-confidence credential/private-key patterns; static SQL RLS/read-only grant assertions; manual unsafe-default review. This is not exhaustive secret scanning or SQL execution. |
| Python regression suite | 18 tests passed: 14 safety/parser cases for unsafe/missing config, credential/path/DNS rejection, redirect rules, body bounds, expected headers/markers, sitemap/robots parsing, links/anchors, JSON refs and workflow pins/permissions, plus 4 worked-example artifact/escaping/HTML/loopback HTTP tests. No external website probes are made. |
| Source review | Official focused docs reviewed as marked in sources.json; 78 registered sources with review versus discovery status and no integration-executed claims. |
| Additional external links | 81 URLs requested through web retrieval; 80 returned retrievable results, npm audit content unavailable/empty. Some returned shells/sparse content and are not treated as reviewed. See external-link-checks.json. |
| Action pin | Official actions/checkout v7.0.1 Git ref and action.yml retrieved; pinned SHA is 3d3c42e5aac5ba805825da76410c181273ba90b1. |

Reproduce locally:

```sh
python -m pip install -r scripts/requirements.txt
python scripts/validate.py
python -m unittest discover -s tests -v
python scripts/sources.py --topic security
```

The final validator output gives current file/Markdown/JSON/YAML counts. The publication check in GitHub is recorded separately in project progress when available; a local result must not be mislabeled as a hosted Actions run.

## Manual consistency review

README points to START-HERE and the standalone master workflow. All eight phases and required discovery topics are covered. AGENTS defines state transitions/evidence/update triggers; resume checks Git/code/PR reality. Architecture recipes retain optional modules and avoid a universal framework. Public client keys are not authorization, RLS is never disabled, admin mutations require server roles, private caching/CSRF/upload risks are explicit, and preview indexing is distinguished from access control. Production/destructive/spending approval scope is explicit. Free tiers are dated, limited and not promised as unlimited operating cost. No unrelated website is used as a source.

## Known limitations and unverified integrations

- No Cloudflare/Supabase account resources, DNS, production secrets or deployments were created or modified. Dashboard/connector instructions must be applied using actual supported capabilities and current plan. Wrangler schema validation, dry-run and hosted preview have not run.
- No Astro/Next/Tailwind website, browser/Lighthouse/axe suite or ZAP scan was executed. TypeScript examples are illustrative and require locked tooling/application setup.
- SQL was reviewed statically only; it was not parsed/applied by PostgreSQL and RLS/Auth/storage flows were not exercised. It deliberately grants no client admin writes.
- API JSON contracts were parsed and refs/security markers checked, not validated with a full OpenAPI validator or a live server.
- Stripe, Resend, CMS, calendar and analytics setup/payment/email flows were not executed. No charges, real emails, bookings or user data were used.
- Notification delivery and scheduled workflows require user target/config/ownership; operational templates are inactive here. A monthly reminder does not complete human reviews.
- Monitoring is intentionally bounded and read-only, expects trusted owner-reviewed config and is not a hardened hostile-input network sandbox. Header substring checks, allowlisted links and sitemap syntax do not establish full security/SEO/availability. It rejects unsafe/local targets but must not be run with attacker-controlled config on privileged networks.
- Some external pages are discovery-only or may have moved; review dates are not freshness guarantees. Source review must precede version-sensitive changes. Astro root llms.txt and a guessed OWASP incident URL failed and were not retained as working instructions; alternative official navigation/publication is documented.

## Remaining consumer setup

Fork/clone, run discovery, create the actual website plan, select only needed modules, connect authorized providers, verify isolated preview and approve production release. Enable selected operational workflows only after safe target/notification testing and quota review. No further credentials are needed to read or use this blueprint.


## 0.1.1 operational documentation update

Adds one supplementary guide plus environment/release evidence templates and cross-links in existing agent, deployment and security documents. Source register includes focused Access token-type/service/JWT and preview-configuration references. No application, infrastructure, payment, email, download or identity changes were made. Offline validation and the existing 14 safety/parser tests are rerun before publication; hosted CI status is verified separately. Public documentation uses generic examples and official vendor references only; no unrelated site information or project identifiers are included.


## 0.2.0 repository presentation and worked example

A new fictional static fixture is built with Python 3.12.14 and checked by four actual local tests. The full suite now has 18 passing tests. See [walkthrough evidence](../examples/worked-static-site/evidence.md). It verifies artifact scope/repeatability, escaping, representative semantic/metadata structure and loopback HTTP 200/404 behavior. It does not prove hosted TLS/headers, visual accessibility or production readiness.

README/navigation, issue forms, PR template, roadmap and release policy were reviewed and checked for internal links/configuration syntax. The validator also checks issue-form fields and ignores generated dist output. No public website or service account was created. Public files remain generic and contain no unrelated site information. Release publication is verified separately in GitHub.
