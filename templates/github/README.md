# GitHub templates

Copy [dependabot.yml](dependabot.yml) to `.github/dependabot.yml` and retain only the ecosystems/paths present in the website. This blueprint's own active Dependabot file covers its validator and Actions; website npm updates are a separate opt-in.

For a website requiring browser tests:

1. Install a reviewed current `@playwright/test` as a dev dependency, commit its lockfile and inspect `npx playwright --help` / browser installation guidance. Add scripts to your website package.json; this blueprint has no application package.json.
2. Copy [playwright.config.ts](playwright.config.ts) and [smoke.spec.ts](smoke.spec.ts) into the indicated root/tests location. Set an explicitly authorized local or hosted-preview base URL via `E2E_BASE_URL`.
3. Run `npx playwright install chromium` and `npx playwright test` with your locked dependency. On CI follow the documented `--with-deps` installation for the selected runner. Browser binaries and dependencies consume minutes/storage.
4. Replace the generic main-landmark expectation with meaningful site journeys. Add preview-only login/admin/mutation tests as required. Never store auth state or fixtures in publicly served directories.
5. The optional weekly workflow assumes reviewed `test:smoke` and `audit:quality` npm scripts. `audit:quality` should run a pinned Lighthouse/axe setup on a representative **preview**; do not label it passed until configured and executed. See [weekly instructions](../../automation/weekly-checks.md).

These TS examples are not executed here; no browser dependency/application was installed for this documentation repository. See [Playwright configuration](https://playwright.dev/docs/test-configuration) and [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview), rechecking current versions before adoption.
