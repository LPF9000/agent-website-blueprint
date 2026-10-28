# Environment templates

Copy only required names from root [.env.example](../../.env.example) into an ignored local file. All example values are empty. Do not commit a filled environment file, paste it into chat or print it during debugging.

| Value | Browser-safe? | Where |
| --- | --- | --- |
| Canonical public site URL | Yes | Public build variable |
| Supabase URL/publishable key | Yes, with correct RLS/grants | Astro PUBLIC_ or Next NEXT_PUBLIC_ only |
| Turnstile site key | Yes | Public widget configuration |
| Supabase secret, Stripe restricted key, webhook secret, Resend key, Turnstile secret | No | Runtime secret fields / ignored local server environment |
| Calendar refresh token / CMS preview token | No | Restricted encrypted server storage |
| Cloudflare deploy token | No | Scoped CI secret only if CI deployment is chosen |

Build variables and runtime variables are different. Build-time substitution may permanently embed a value in generated assets. A secret field in a dashboard does not prevent a frontend bundler exposing a public-prefixed value. Review output and source maps.

## Monitor config

Copy [monitor.json](monitor.json) into `automation/monitor.json` in your website repo. Set the exact owned canonical origin, `authorized: true` only after the owner authorizes GET probes, and explicit safe public endpoints. Do not add logout, export, webhook or state-changing routes. No credentials/query strings are supported. Reserved example.com is rejected until replaced.

`expected_headers` uses case-insensitive substring expectations, except an empty value means present/non-empty. The script checks presence/basic values, not full CSP correctness. `redirects` maps an exact same-origin absolute source URL to its expected same-origin destination; redirects are never automatically followed. Configure endpoints for both an intentional redirect and final page if needed. `contains` is a public non-sensitive response marker; empty bodies/status-only 200 can miss soft failures.

TLS validates host/chain and warns (fails) below `tls_min_days`. Set no more than 10 daily endpoints and 30 weekly paths, each explicitly reviewed and safe. `weekly_paths` are a bounded internal link-check allowlist; the script does not recursively discover or visit arbitrary links. Logs print only paths and outcome codes, never response bodies/headers/cookies. Canonical origin must be HTTPS/public; this script is not a hardened network sandbox and must not run with attacker-controlled config or on privileged self-hosted networks.

Use separate preview configs. Test failure/notifications harmlessly by changing an expected marker on preview. Production probes must remain read-only.
