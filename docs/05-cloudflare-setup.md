# Cloudflare setup and connector workflow

## Purpose

Create only the hosting resources required by the selected architecture, with isolated previews and a documented rollback.

## When needed

At infrastructure phase. Local planning/development does not require a Cloudflare account.

## Prerequisites

A Cloudflare account, authorized account owner, GitHub repository, successful build, chosen framework/runtime, and non-secret deployment plan. Read [architecture selection](03-architecture-selection.md).

## Recommended implementation

Prefer an available official Cloudflare connector for supported operations. Use dashboard or locally pinned Wrangler when capabilities are missing. Discover operations; never assume support for project creation, GitHub linkage, DNS, secrets or previews.

## Setup

1. **Read-only discovery:** inspect the agent’s available plugins/connectors. If Cloudflare is absent or disconnected, guide the user to their agent’s Apps/Connectors settings, select the official Cloudflare connection, complete its authorization flow and return. Labels differ by agent; do not fabricate a universal connect command. Never ask for a pasted global API key.
2. Discover exposed tools and their schemas. List accessible accounts and existing Workers/Pages projects/zones with supported read operations. Confirm account/project identifiers with the owner. Record an operation capability matrix in `.project/deployment.md`.
3. Select Workers static assets or Pages for static Astro output; select the current documented compatible Workers deployment for server frameworks. Read the current [framework guide](https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/) before Next.js integration.
4. **Configuration:** present planned resources, scope and costs. Obtain missing authorization for production-impacting changes; previews must use isolated data. Create the chosen project using supported operations, otherwise dashboard **Workers & Pages → Create application** and the matching Workers/Pages flow.
5. If using Git deployment, connect GitHub through Cloudflare’s authorization UI with only the intended repository, choose root/build/output settings from the actual framework and commit lockfile. Static Astro normally uses `npm run build` and `dist`; confirm your project. For Workers Builds, use its documented deploy command; do not paste Pages output settings into it.
6. Configure distinct preview and production variables/bindings. Put secrets in provider secret fields, not plain-text vars or committed config. Runtime secrets and build-time variables differ: ensure only intended public values reach client bundles. See [environment template](../templates/environment/README.md).
7. Configure non-production branch/preview deployments using the chosen product’s current preview controls. Use a separate preview Worker/project if isolation is unclear. Protect preview content, return `X-Robots-Tag: noindex, nofollow`, and verify it on actual responses. Preview uses sandbox payments/email and a separate database.
8. Fallback CLI: install a reviewed Wrangler version as a local dev dependency; inspect `npx wrangler --help` and the relevant subcommand help. Use `npx wrangler login` for local OAuth. For static assets copy [wrangler.static.json](../templates/cloudflare/wrangler.static.json), set the real name/date and build `dist` before `npx wrangler dev`. Before an authorized deployment inspect `npx wrangler deploy --help`, then deploy to the intended preview target. Discover Pages commands from current help if choosing Pages. Never run a generic deploy against an unknown default target.
9. Attach a domain and DNS only after [DNS review](06-domain-and-dns.md), with production authorization. Verify managed TLS is active, HTTPS behavior and security controls. Preserve mail/verification DNS records.
10. Run hosted-preview tests, record commit/provider version/URL/configuration and rollback. For production, follow [deployment](19-deployment.md) and verify actual hostname after authorized promotion.

## Security considerations

Use scoped OAuth/API permissions; do not expose account tokens in logs. Preview secrets must not access production. `_headers` covers static assets only; Worker/SSR/API responses require response middleware. Rate limits/WAF features vary by plan; verify availability instead of promising paid controls on Free.

## Free-tier limitations

Workers/Pages free tiers have request/CPU/build/file limits. Functions, storage and Builds are separate metered products. R2 activation may require billing details. Do not enable a paid plan or paid service as a prerequisite for a static site.

## Verification

Check the provider reports the expected commit, inspect the preview URL in a browser, test main/error/API responses, confirm preview noindex and isolated bindings, verify secret absence in built files, and rehearse rollback to a known-good preview version. Record what was inspected versus executed.

## Troubleshooting

Wrong account: stop and reselect, do not create duplicates. Build failures: inspect root, lockfile, Node version and output. Missing runtime variable: check target environment and build/runtime distinction. Domain pending: check zone/DNS/certificate status before changing records. Unsupported plugin operation: use documented dashboard/CLI fallback, not a guessed tool.

## Official documentation

[Workers getting started](https://developers.cloudflare.com/workers/get-started/guide/) · [Wrangler configuration](https://developers.cloudflare.com/workers/wrangler/configuration/) · [GitHub integration](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/github-integration/) · [Pages Git integration](https://developers.cloudflare.com/pages/get-started/git-integration/) · [Workers secrets](https://developers.cloudflare.com/workers/configuration/secrets/) · [Workers previews](https://developers.cloudflare.com/workers/previews/) · [Rollbacks](https://developers.cloudflare.com/workers/versions-and-deployments/rollbacks/)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.
