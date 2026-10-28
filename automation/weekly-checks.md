# Weekly checks

Purpose: review dependency and public-quality drift without expensive daily browser runs. Optional after launch; prerequisites are safe monitor config, named reviewer and an isolated preview for browser/quality tests.

## Setup and coverage

1. Copy [weekly.yml](workflows/weekly.yml), configure [monitor.json](../templates/environment/monitor.json) and set `ENABLE_WEEKLY_CHECKS=true` only after testing manually.
2. Included public jobs repeat health/TLS/header expectations, require sitemap/robots HTTP 200, validate namespaced sitemap XML/loc origins and basic robots directives/intended sitemap. An index is checked structurally; child maps are not recursively fetched.
3. Set at most 30 explicitly safe HTML paths in `weekly_paths`. The script checks those responses and links between them only; it never follows arbitrary discovered links, queries or anchors. Review omitted coverage in output and expand the allowlist or add a vetted static build link checker on preview where necessary. Redirect links should be replaced with canonical links or tested separately as daily endpoints.
4. Enable Dependabot/alerts for actual ecosystems and review updates/advisories/failed runs. `npm audit --audit-level=high` is included only in the optional npm job; triage findings and do not auto-force-fix.
5. To automate essential browser/Lighthouse/accessibility checks, install reviewed locked tools in the website, add `test:smoke` and `audit:quality` scripts and configure `QUALITY_PREVIEW_URL`. The latter script should run pinned Lighthouse on selected pages and a maintained axe-based accessibility smoke. Follow current [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) and [Playwright accessibility](https://playwright.dev/docs/accessibility-testing) guidance for your runtime. Verify actual scripts/coverage before `ENABLE_NPM_QUALITY=true`; no such application scripts exist in this blueprint.
6. Use browser template read-only journeys on isolated preview. Manually review headers semantically, mobile/keyboard/screen-reader behavior and serious accessibility issues. Optional checks disabled in config are **not executed**, not passed.
7. Optional ZAP baseline: only for an explicitly authorized owned preview target with synthetic data, exact host/path/rate/time scope and reviewed exclusions for logout/state-changing paths. Read current [baseline docs](https://www.zaproxy.org/docs/docker/baseline-scan/), pin the approved image digest and use passive/baseline configuration. Spider GETs can still cause effects in badly designed apps; no automated ZAP workflow is enabled here.

Security/cost: no production mutation fixtures or active attack scans; no deployment credentials. `npm ci` executes project install scripts, so enable only for trusted reviewed default-branch code with no secrets. Pin a compatible Node runtime before adoption. Jobs are time-bounded and no artifacts uploaded; if adding reports set retention at most the agreed window and exclude auth state.

Verification/troubleshooting: manually run each selected job, confirm dependency/browser/audit failures fail the job, review allowlist coverage and test notifications. Missing scripts/preview intentionally fail rather than silently skip. Basic robots checks cannot establish indexing/rankings; automated accessibility cannot replace manual review. Scheduled failure review needs a human owner.

External references reviewed 2026-10-28; runtime browser/Lighthouse/ZAP integrations were not executed here. See [source freshness](../docs/source-freshness.md).
