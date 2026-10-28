# Official source register for agents

Use [sources.json](sources.json) for machine-readable topic IDs, official URLs, documentation indexes, changelogs, review dates and execution status. Read the [freshness protocol](source-freshness.md) before using external instructions. Major guides also include direct feature links; this register is the navigation hub, not an exhaustive copy of vendor docs.

**Reviewed 2026-10-28** means relevant official content was retrieved/read during blueprint creation, not that it is still current, that every linked subsection was read, or that an integration was executed. **Discovery only** means a legitimate official starting point was identified but its content was not fully verified in this environment. Check entry notes in the JSON. No integration has been executed just because a page was retrieved.

| ID / topic | Official starting point | Use for | Review status |
| --- | --- | --- | --- |
| cloudflare-workers / hosting | [cloudflare-workers](https://developers.cloudflare.com/workers/static-assets/) · [agent index](https://developers.cloudflare.com/workers/llms.txt) · [changes](https://developers.cloudflare.com/changelog/) | Static hosting model | 2026-10-28; no integration executed |
| cloudflare-next / frameworks | [cloudflare-next](https://developers.cloudflare.com/workers/framework-guides/web-apps/nextjs/) | Current Next.js deployment/adapter compatibility | 2026-10-28; no integration executed |
| cloudflare-config / deployment | [cloudflare-config](https://developers.cloudflare.com/workers/wrangler/configuration/) | Config fields and installed schema | 2026-10-28; no integration executed |
| cloudflare-headers / security | [cloudflare-headers](https://developers.cloudflare.com/workers/static-assets/headers/) | Static vs generated-response headers | 2026-10-28; no integration executed |
| cloudflare-best / security | [cloudflare-best](https://developers.cloudflare.com/workers/best-practices/workers-best-practices/) | Worker patterns and unsafe defaults | 2026-10-28; no integration executed |
| cloudflare-preview / deployment | [cloudflare-preview](https://developers.cloudflare.com/workers/previews/) | Preview isolation, settings and access | 2026-10-28; no integration executed |
| cloudflare-github / deployment | [cloudflare-github](https://developers.cloudflare.com/workers/ci-cd/builds/git-integration/github-integration/) | Git deployment connection | 2026-10-28; no integration executed |
| cloudflare-rollback / recovery | [cloudflare-rollback](https://developers.cloudflare.com/workers/versions-and-deployments/rollbacks/) | Rollback versions, constraints | 2026-10-28; no integration executed |
| cloudflare-price / costs | [cloudflare-price](https://developers.cloudflare.com/workers/platform/pricing/) | Requests/CPU/static asset billing boundaries | 2026-10-28; no integration executed |
| cloudflare-limits / costs | [cloudflare-limits](https://developers.cloudflare.com/workers/platform/limits/) | Runtime limits and quotas | 2026-10-28; no integration executed |
| pages-limits / costs | [pages-limits](https://developers.cloudflare.com/pages/platform/limits/) | Build/files/function limits | 2026-10-28; no integration executed |
| d1-price / costs | [d1-price](https://developers.cloudflare.com/d1/platform/pricing/) · [agent index](https://developers.cloudflare.com/d1/llms.txt) | Rows read/written and storage | 2026-10-28; no integration executed |
| kv-price / costs | [kv-price](https://developers.cloudflare.com/kv/platform/pricing/) · [agent index](https://developers.cloudflare.com/kv/llms.txt) | Operation/storage quotas | 2026-10-28; no integration executed |
| r2-price / costs | [r2-price](https://developers.cloudflare.com/r2/pricing/) · [agent index](https://developers.cloudflare.com/r2/llms.txt) | Storage classes/operation pricing | 2026-10-28; no integration executed |
| turnstile-validation / security | [turnstile-validation](https://developers.cloudflare.com/turnstile/get-started/server-side-validation/) | Mandatory backend token verification | 2026-10-28; no integration executed |
| astro-install / frameworks | [astro-install](https://docs.astro.build/en/install-and-setup/) · [changes](https://github.com/withastro/astro/releases) | Supported Node/scaffolding/versions | 2026-10-28; no integration executed |
| astro-cloudflare / frameworks | [astro-cloudflare](https://docs.astro.build/en/guides/deploy/cloudflare/) | Framework hosting instructions | 2026-10-28; no integration executed |
| astro-ai / frameworks | [astro-ai](https://docs.astro.build/en/guides/build-with-ai/) | Current agent/docs discovery | 2026-10-28; no integration executed |
| next-docs / frameworks | [next-docs](https://nextjs.org/docs) · [agent index](https://nextjs.org/docs/llms.txt) · [changes](https://github.com/vercel/next.js/releases) | Framework APIs, versions and upgrade guidance | 2026-10-28; no integration executed |
| tailwind / frameworks | [tailwind](https://tailwindcss.com/docs/installation/using-vite) · [changes](https://github.com/tailwindlabs/tailwindcss/releases) | Current integration; styling optional | 2026-10-28; no integration executed |
| typescript / frameworks | [typescript](https://www.typescriptlang.org/docs/) · [changes](https://github.com/microsoft/TypeScript/releases) | Type system/compiler config | Discovery only; no integration executed |
| node / tools | [node](https://nodejs.org/en/download) · [changes](https://nodejs.org/en/blog/release) | Current supported LTS runtime | Discovery only; no integration executed |
| supabase-keys / database | [supabase-keys](https://supabase.com/docs/guides/getting-started/api-keys) · [agent index](https://supabase.com/llms.txt) · [changes](https://supabase.com/changelog) | Publishable vs secret key boundaries | 2026-10-28; no integration executed |
| supabase-rls / security | [supabase-rls](https://supabase.com/docs/guides/database/postgres/row-level-security) | Row/operation authorization | 2026-10-28; no integration executed |
| supabase-grants / security | [supabase-grants](https://supabase.com/docs/guides/api/securing-your-api) | Data API exposure, grants and RLS | 2026-10-28; no integration executed |
| supabase-auth / auth | [supabase-auth](https://supabase.com/docs/guides/auth/server-side) | Framework SSR/cookie integration | 2026-10-28; no integration executed |
| supabase-passwords / auth | [supabase-passwords](https://supabase.com/docs/guides/auth/passwords) | Verification and recovery flows | 2026-10-28; no integration executed |
| supabase-redirects / auth | [supabase-redirects](https://supabase.com/docs/guides/auth/redirect-urls) | Exact callback/site URL controls | 2026-10-28; no integration executed |
| supabase-backups / recovery | [supabase-backups](https://supabase.com/docs/guides/platform/backups) | Plan backup behavior and object exclusions | 2026-10-28; no integration executed |
| supabase-price / costs | [supabase-price](https://supabase.com/pricing) | Active projects/storage/egress/auth and pausing | 2026-10-28; no integration executed |
| supabase-changelog / database | [supabase-changelog](https://supabase.com/changelog) | Breaking/security/platform updates | 2026-10-28; no integration executed |
| supabase-mcp / tools | [supabase-mcp](https://supabase.com/docs/guides/getting-started/mcp) | Official connector setup/scoping | Discovery only; no integration executed |
| postgres / database | [postgres](https://www.postgresql.org/docs/current/) | Constraints, transactions, privileges and RLS semantics | Discovery only; no integration executed |
| github-schedules / automation | [github-schedules](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#schedule) | Delay/default-branch/inactivity behavior | 2026-10-28; no integration executed |
| github-secure-use / security | [github-secure-use](https://docs.github.com/en/actions/reference/security/secure-use) | Pinning/untrusted code/permissions | 2026-10-28; no integration executed |
| github-dependabot / automation | [github-dependabot](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference) | Update ecosystem/schedule config | 2026-10-28; no integration executed |
| github-billing / costs | [github-billing](https://docs.github.com/en/billing/concepts/product-billing/github-actions) | Public/private runner, minutes and storage | 2026-10-28; no integration executed |
| github-limits / automation | [github-limits](https://docs.github.com/en/actions/reference/limits) | Runner/job limits | 2026-10-28; no integration executed |
| github-notifications / automation | [github-notifications](https://docs.github.com/en/subscriptions-and-notifications/how-tos/managing-github-actions-notifications) | Actual notification preferences | 2026-10-28; no integration executed |
| checkout-pin / automation | [checkout-pin](https://github.com/actions/checkout/releases/tag/v7.0.1) | Action release/pin review | 2026-10-28; no integration executed |
| owasp-rest / security | [owasp-rest](https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html) | API security and CORS guidance | 2026-10-28; no integration executed |
| owasp-csrf / security | [owasp-csrf](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) | Cookie write request defenses | 2026-10-28; no integration executed |
| owasp-upload / security | [owasp-upload](https://cheatsheetseries.owasp.org/cheatsheets/File_Upload_Cheat_Sheet.html) | Upload trust boundaries | 2026-10-28; no integration executed |
| owasp-csp / security | [owasp-csp](https://cheatsheetseries.owasp.org/cheatsheets/Content_Security_Policy_Cheat_Sheet.html) | Compatible CSP rollout | 2026-10-28; no integration executed |
| owasp-asvs / security | [owasp-asvs](https://owasp.org/www-project-application-security-verification-standard/) | Risk-based security requirements | Discovery only; no integration executed |
| owasp-session / security | [owasp-session](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html) | Sessions/cookies/revocation | Discovery only; no integration executed |
| nist-incidents / recovery | [nist-incidents](https://csrc.nist.gov/pubs/sp/800/61/r3/final) | Incident response reference | 2026-10-28; no integration executed |
| playwright / testing | [playwright](https://playwright.dev/docs/test-configuration) · [changes](https://playwright.dev/docs/release-notes) | Browser configuration, supported runtimes and test setup | 2026-10-28; no integration executed |
| lighthouse / testing | [lighthouse](https://developer.chrome.com/docs/lighthouse/overview) | Lab quality audit setup/limits | 2026-10-28; no integration executed |
| wcag / accessibility | [wcag](https://www.w3.org/TR/WCAG22/) | Published accessibility standard/errata | 2026-10-28; no integration executed |
| wai / accessibility | [wai](https://www.w3.org/WAI/tutorials/) | Practical semantic/forms/image guidance | 2026-10-28; no integration executed |
| vitals / performance | [vitals](https://web.dev/articles/vitals) | Current field metrics and thresholds | 2026-10-28; no integration executed |
| google-schema / seo | [google-schema](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) | Structured data policies/verification | 2026-10-28; no integration executed |
| google-product / seo | [google-product](https://developers.google.com/search/docs/appearance/structured-data/product) | Product rich-result rules | 2026-10-28; no integration executed |
| google-event / seo | [google-event](https://developers.google.com/search/docs/appearance/structured-data/event) | Event fields/status/timezone rules | 2026-10-28; no integration executed |
| google-org / seo | [google-org](https://developers.google.com/search/docs/appearance/structured-data/organization) | Organization facts | 2026-10-28; no integration executed |
| google-noindex / seo | [google-noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing) | Noindex versus robots/auth | 2026-10-28; no integration executed |
| bing / seo | [bing](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a) | Bing official indexing tools | Discovery only; no integration executed |
| resend-docs / email | [resend-docs](https://resend.com/docs/send-with-nodejs) · [agent index](https://resend.com/docs/llms.txt) | Backend send, keys and verified domain | 2026-10-28; no integration executed |
| resend-price / costs | [resend-price](https://resend.com/pricing) | Daily/monthly email quotas | 2026-10-28; no integration executed |
| stripe-fulfillment / payments | [stripe-fulfillment](https://docs.stripe.com/checkout/fulfillment) | Signed events/idempotent verified payment fulfillment | 2026-10-28; no integration executed |
| stripe-webhooks / payments | [stripe-webhooks](https://docs.stripe.com/webhooks) | Signature verification and event handling | 2026-10-28; no integration executed |
| stripe-price / costs | [stripe-price](https://stripe.com/pricing) | Country/payment/add-on fee review | Discovery only; no integration executed |
| stripe-sandbox / payments | [stripe-sandbox](https://docs.stripe.com/sandboxes) | Isolated payment testing | Discovery only; no integration executed |
| calendar / calendar | [calendar](https://developers.google.com/workspace/calendar/api/guides/overview) | OAuth/scopes/quotas/event model | Discovery only; no integration executed |
| decap / cms | [decap](https://decapcms.org/docs/) | Git-backed CMS authentication/publishing | Discovery only; no integration executed |
| sanity / cms | [sanity](https://www.sanity.io/docs) | Managed CMS schema/roles/export | Discovery only; no integration executed |
| directus / cms | [directus](https://directus.io/docs/) | CMS backend, licensing and hosting requirements | Discovery only; no integration executed |
| cloudflare-analytics / analytics | [cloudflare-analytics](https://developers.cloudflare.com/web-analytics/) | Privacy-conscious aggregate analytics | Discovery only; no integration executed |
| zap / testing | [zap](https://www.zaproxy.org/docs/docker/baseline-scan/) | Optional passive scan scope/controls | 2026-10-28; no integration executed |
| openapi / api | [openapi](https://spec.openapis.org/oas/latest.html) | Contract syntax/validation | Discovery only; no integration executed |

## Retrieval limitations found during creation

- Astro root llms.txt returned 404; link to the current official Build with AI page rather than persisting an assumed endpoint. Use the current page's advertised index/MCP mechanism.
- Cloudflare Workers, Next.js and Supabase agent indexes were retrieved. Resend's documentation page advertises its docs/llms.txt index; fetch it when using that module.
- Supabase Markdown changelog retrieval failed due to tool content-type handling; its HTML changelog was reviewed instead.
- Bing's endpoint returned a JavaScript shell. The official URL remains a discovery link; indexing setup/UI was not verified.
- A guessed OWASP incident-response URL returned 404 and was replaced with NIST's actual incident-response publication. Never invent a cheat-sheet path from a title.
- Network/tool restrictions can prevent live URL checks. Mark unavailable content as unverified and use an official alternate source, rather than silently declaring the integration verified.

Source checking is not a scheduled service. The [source-review script](../scripts/sources.py) can report stale/discovery entries locally; optional live HTTP checks only report reachability and cannot prove instruction freshness. Review breaking changes/advisories and installed versions before applying a template.
