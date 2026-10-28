# Static Cloudflare configuration

[wrangler.static.json](wrangler.static.json) is a **static-only** configuration example. Copy to the website root as `wrangler.json` after choosing Workers static assets. Set a unique authorized target name and current reviewed compatibility date; `dist` must be your real build output and include a 404.html to exercise the shown not-found mode. This blueprint contains no `dist` and is not itself deployable.

Install a reviewed Wrangler version locally and commit the lockfile. Validate configuration against that installed `node_modules/wrangler/config-schema.json`, inspect `npx wrangler --help`, build the site, then run local `npx wrangler dev`. A dry-run build/package check, where supported by the installed CLI help, does not create or verify a hosted deployment. Do not deploy before target/scope and authorization are established.

No database/storage bindings, Node compatibility flags, main script or secrets are needed for static-only assets. For an actual server framework use that framework's current generated configuration; do not merge this template blindly. Add Node compatibility only for runtime requirements and verify support.

Place adapted `_headers`/`_redirects` in the source public directory so the build includes them. Headers for generated Worker/SSR/API responses belong in response middleware, including errors/denials. Noindex preview policy must be environment-specific and verified at every preview hostname; never ship blanket production noindex accidentally.

Use a separate preview Worker/project or the product's current documented isolated preview settings. Record bindings, variables **names**, build/output commands, URLs, version and rollback in `.project/deployment.md`. Use dashboard/Git deployment only if selected; do not add redundant deployment CI.

Sources: [configuration](https://developers.cloudflare.com/workers/wrangler/configuration/), [static assets](https://developers.cloudflare.com/workers/static-assets/), [headers](https://developers.cloudflare.com/workers/static-assets/headers/), [previews](https://developers.cloudflare.com/workers/previews/). Fields reviewed 2026-10-28; JSON syntax validated, provider CLI/deploy not executed here.
