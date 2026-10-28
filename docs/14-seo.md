# Search engine optimization

## Purpose

Make public content understandable, discoverable and accurately represented. Metadata alone does not guarantee rankings or rich results.

## When needed

Every public, indexable site. Private/admin content must stay private, regardless of robots rules.

## Prerequisites

Canonical production hostname, real page/content inventory, publication rules and public route list.

## Recommended implementation

Create useful semantic content and crawlable internal links first. Generate route-aware metadata and sitemap from actual public canonical pages. Structured data must accurately describe visible content.

## Setup

1. Build semantic headings, landmarks, descriptive links and server/static rendered public content. Give each page a specific title and useful unique description.
2. Choose clean stable URLs, a canonical HTTPS hostname and route-specific absolute canonical URLs. Avoid pointing every page at the homepage. Maintain explicit redirects from changed URLs; preserve intent and avoid chains/loops.
3. Add Open Graph title/description/type/url/image and suitable social card tags. Use an accessible, correctly sized public image with absolute URL; inspect previews without disclosing private URLs.
4. Generate XML sitemap entries for public, indexable, successful canonical URLs only. Exclude admin/auth/search variants/drafts. Use honest last-modified dates. Publish robots.txt with intended crawl rules and absolute Sitemap location.
5. Add JSON-LD safely serialized from validated content: Organization for real organizational identity, Product for actual product details/offers, Event for real dates/timezone/location/status, and BreadcrumbList reflecting visible hierarchy. Do not invent reviews, prices, availability or business details to qualify for rich results. Follow each search engine feature policy.
6. Preview: protect sensitive previews with authentication and send `X-Robots-Tag: noindex, nofollow` on all preview responses, or equivalent supported page directives. Robots Disallow alone does not reliably remove a URL from an index; crawlers must be able to see noindex, unless authentication blocks access. Canonical tags alone do not prevent preview indexing.
7. Production: remove preview-only noindex from intended public routes, keep private pages out of indexes, and submit sitemap after proving ownership in Google Search Console and Bing Webmaster Tools. Verify DNS/HTML ownership without leaking credentials.
8. Optimize images, responsive layout, performance and internal links; write original useful content with clear authorship/update practices. Review indexing reports rather than expecting immediate rankings.

## Security considerations

robots.txt and noindex are not access controls and reveal paths publicly. Never include private file URLs, recovery tokens, personal information or preview credentials in sitemaps, canonical tags or structured data. Escape `<` in JSON-LD serialization to avoid script termination injection.

## Free-tier limitations

Search Console/Bing tools are generally free; crawler/API and external SEO tools have limits. Paid SEO software is not required. Hosting/build quotas still apply to generated pages and image transformations.

## Verification

Inspect rendered HTML and actual GET headers for home/detail/error/preview pages; verify titles, canonical, social images, sitemap XML and robots. Run Google Rich Results Test and Schema.org validator for relevant types; use Search Console URL inspection and Bing reports. Confirm private routes require auth and preview noindex is present. Automated scores do not guarantee indexing.

## Troubleshooting

No indexing: inspect noindex, authentication, robots rules, canonical targets, status codes and sitemap URL. Wrong social preview: verify absolute image accessibility/cache and metadata. Invalid Event/Product: compare visible facts and required fields with current official feature docs.

## Official documentation

[Search essentials](https://developers.google.com/search/docs/essentials) · [Structured data](https://developers.google.com/search/docs/appearance/structured-data/intro-structured-data) · [Product](https://developers.google.com/search/docs/appearance/structured-data/product) · [Event](https://developers.google.com/search/docs/appearance/structured-data/event) · [Organization](https://developers.google.com/search/docs/appearance/structured-data/organization) · [Noindex](https://developers.google.com/search/docs/crawling-indexing/block-indexing) · [Sitemaps](https://developers.google.com/search/docs/crawling-indexing/sitemaps/overview) · [Bing guidance](https://www.bing.com/webmasters/help/webmaster-guidelines-30fba23a)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.
