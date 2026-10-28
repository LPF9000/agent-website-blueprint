# Testing strategy

## Purpose

Collect meaningful evidence that required journeys and denial cases work without imposing a giant CI system.

## When needed

Every change, with depth proportional to behavior/data risk.

## Prerequisites

Acceptance criteria, declared package scripts, isolated fixtures/test identities, hosted preview and explicit production smoke scope.

## Recommended implementation

Minimum baseline: framework type checks, focused lint/build, essential Playwright journey plus manual mobile/keyboard review. Add unit tests for real logic and integration/API/auth/authorization tests when those modules exist. Prefer hosted preview before significant production changes.

## Setup

1. Map every acceptance criterion to local, hosted-preview or production verification. Record which environment proves each claim. Avoid tests that only restate implementation.
2. Add explicit package scripts for type checking, lint, build and tests. Use `npm ci` with the committed lockfile. Do not assume an Astro/Next build alone checks every type or lint rule.
3. Unit-test transformations, validation, time/currency/business rules. Integration/API tests cover transactions, error handling, migrations and signature/idempotency behavior against isolated resources.
4. Authentication tests cover confirmation/login/logout/recovery/session expiry. Authorization tests directly call APIs/data with anonymous/A/B/admin identities and attempt horizontal/vertical privilege escalation. Include draft/file visibility.
5. Playwright smoke: public page/navigation/error route; required form behavior; selected auth/admin journeys in preview only. Use accessible locators, isolated browser contexts and deterministic fixtures. See [test template](../templates/github/README.md).
6. Test desktop/mobile widths, touch targets, keyboard focus and real content overflow. Add automated accessibility checks plus manual screen-reader review; use Lighthouse for representative pages and inspect sitemap/robots/structured data.
7. Test security controls, headers, private caching and secret absence. Keep test fixtures/helpers outside public routes and exclude test auth state from Git/artifacts.
8. After authorized deployment run a small read-only production smoke. Never run fixture creation, deletes, real checkout or form/email submission from scheduled production tests. Report skipped/unavailable checks explicitly.

## Security considerations

No test-only bypass route should exist in production. Auth storage-state files contain credentials; ignore them and do not upload them as artifacts. Mask logs, bound concurrency and restrict scan targets. Do not run untrusted PR code with deployment secrets.

## Free-tier limitations

Local/open-source testing is generally free, but hosted CI minutes, artifact storage, browser installs and database/email quotas apply. Keep browser suites on meaningful changes/weekly cadence rather than every daily health run.

## Verification

A release evidence entry names command, commit, environment, actual outcome and manual observations. Add negative tests for each protected data boundary. A blueprint SQL/schema/contract example is not runtime-tested merely because JSON parses.

## Troubleshooting

Flaky tests: isolate state and wait for observable UI conditions rather than fixed sleeps. CI-only failure: compare runtime/browser versions and environment names without dumping env. Preview-only failure: inspect edge runtime/cache/redirect differences.

## Official documentation

[Playwright configuration](https://playwright.dev/docs/test-configuration) · [Playwright best practices](https://playwright.dev/docs/best-practices) · [Accessibility tests](https://playwright.dev/docs/accessibility-testing) · [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.

## Operational cross-check

For hosted release tests, use [exact-version release evidence](../planning/release-evidence-template.md) and [operational failure modes](25-operational-failure-modes.md). Include missing-required-secret denial, unavailable scan reports, known-file authorized/denied pairs and selected integration failure recovery. Missing/skipped/unreachable checks never become zero findings or a pass.
