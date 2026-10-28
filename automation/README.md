# Optional operational automation

Nothing in `automation/workflows/` runs here automatically. Only `.github/workflows/blueprint-checks.yml` is active for the blueprint. Enable operational templates in a generated website only after target/configuration review.

| Cadence | Included automation | Human or project-specific work |
| --- | --- | --- |
| [Daily](daily-checks.md) | Bounded HTTPS/TLS/header/status/marker/redirect GET checks | Internal configuration/error-log review where not publicly observable |
| [Weekly](weekly-checks.md) | Health, sitemap/robots and allowlisted internal-link checks; optional configured npm/browser/quality job | Review advisories, update PRs, full header semantics/accessibility and failed runs |
| [Monthly](monthly-checks.md) | Workflow summary reminder with review checklist | Actual backup/restore, access, RLS, cost, domain and secret-policy reviews |

## Install only selected modules

1. Copy chosen `.yml` files to the website's `.github/workflows/`. Keep scripts/health.py and scripts/weekly.py with their import relationship.
2. Copy `templates/environment/monitor.json` to `automation/monitor.json`; review safe paths, set real canonical HTTPS origin, expectations and explicit authorization. The shipped example deliberately refuses to run.
3. Add repository variables under GitHub **Settings → Secrets and variables → Actions → Variables**: `ENABLE_DAILY_CHECKS`, `ENABLE_WEEKLY_CHECKS`, `ENABLE_MONTHLY_REVIEW` as `true` only for selected templates. These variables are not secrets. Optional weekly npm checks additionally require `ENABLE_NPM_QUALITY=true` and `QUALITY_PREVIEW_URL`.
4. Inspect runtime compatibility and configure required website package scripts before enabling npm quality. Pin Node with an official full-SHA setup action or selected stable runner/runtime after reviewing current requirements. The template reports versions but cannot know your framework's supported Node version.
5. Run manually on the default branch, inspect status/summary and deliberately test a harmless failure in preview. Configure [notifications](uptime-monitoring.md). Schedules execute on the default branch, can be delayed/dropped, and public-repo inactivity can disable them.
6. Review [usage](../docs/23-cost-management.md), owner/response policy and next due date. Workflows have read-only permissions and timeouts; no credentials, artifact uploads, production writes or automatic merges are required.

Actions are pinned to official checkout v7.0.1 commit verified 2026-10-28. Keep pins reviewed/updated; Dependabot may not update inactive workflow templates outside `.github/workflows/`. No artifacts are uploaded by these templates. If adding reports, use bounded retention (for example seven days), exclude secrets/auth state and do not treat artifacts as backups.

These workflows do not automatically prove a site is secure, restore backups, audit cloud permissions or discover internal configuration errors. See [validation report](../docs/validation-report.md) for what was executed here.
