# Domains, DNS and HTTPS

## Purpose

Connect a domain without breaking mail, existing services or TLS.

## When needed

Only when a custom domain is requested; a provider subdomain is sufficient for previews and low-cost launch.

## Prerequisites

Domain ownership/registrar access, existing DNS inventory/export, desired canonical hostname, current deployment and production approval.

## Recommended implementation

Use Cloudflare-managed TLS and product-specific custom domain setup. For proxied external origins use end-to-end validated TLS; do not choose Flexible TLS. Add HSTS gradually after HTTPS and all relevant subdomains are proven safe.

## Setup

1. Record registrar, renewal date/owner, current nameservers, DNSSEC state and all existing A/AAAA/CNAME/MX/TXT/CAA records. Identify mail and third-party verification dependencies.
2. If moving DNS to Cloudflare, add the zone, compare imported records with the inventory and follow registrar/Cloudflare DNSSEC migration guidance. Stale DS records can make the domain unresolvable. Do not change nameservers blindly.
3. Use the hosting product’s Custom Domains flow; follow its generated DNS instructions. Do not guess IPs or CNAME destinations. Apex Pages setup has zone/nameserver requirements; read that product’s guide.
4. Confirm certificate issuance, hostname coverage and HTTPS before redirecting traffic. Choose apex or www as canonical, configure an intentional redirect with path/query preservation, and test loops.
5. For an external origin behind Cloudflare select Full (strict) with a valid origin certificate. Document any direct-origin access restrictions.
6. Test and then enable a short HSTS lifetime; increase only after observing all impacted hosts. Add `includeSubDomains` or preload only with explicit review of every subdomain and long-term consequences.
7. Record DNS diff, TTL/propagation expectations, HTTPS checks, renewal owner and reversal procedure in deployment records.

## Security considerations

DNS changes are production-impacting. Never delete MX/TXT records because the website does not use them. Account/registrar MFA and recovery are essential. HSTS does not replace certificate renewal or TLS validation.

## Free-tier limitations

DNS/managed TLS may be available free, but the domain normally has an annual registration/renewal charge. Premium domains, advanced certificate features and some DNS/security features may cost extra.

## Verification

Check `dig YOUR_HOST` or `nslookup YOUR_HOST`, actual browser certificate, `curl -I https://YOUR_HOST/`, HTTP-to-HTTPS and canonical redirects. Verify mail-related DNS still matches inventory. Repeat from another resolver after propagation.

## Troubleshooting

NXDOMAIN: confirm delegation and spelling. SERVFAIL after migration: investigate DNSSEC DS records. Pending certificate: inspect CAA and product domain validation. Redirect loop: compare scheme at edge/origin and conflicting rules. Do not bypass TLS warnings.

## Official documentation

[DNS setup](https://developers.cloudflare.com/dns/zone-setups/full-setup/setup/) · [Pages custom domains](https://developers.cloudflare.com/pages/configuration/custom-domains/) · [Workers custom domains](https://developers.cloudflare.com/workers/configuration/routing/custom-domains/) · [Full strict TLS](https://developers.cloudflare.com/ssl/origin-configuration/ssl-modes/full-strict/) · [HSTS](https://developers.cloudflare.com/ssl/edge-certificates/additional-options/http-strict-transport-security/)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.
