# Performance

## Purpose

Keep pages fast and stable without unnecessary infrastructure or expensive monitoring.

## When needed

Every website, with extra attention to image-heavy catalogs, client-heavy apps and slow mobile connections.

## Prerequisites

Representative pages, production-like content, agreed performance budget and a hosted preview.

## Recommended implementation

Static generation, small assets and minimal JavaScript first. Use Lighthouse for repeatable lab diagnosis and real-user field data where available. Core Web Vitals assess LCP, INP and CLS; measure rather than chasing a single score.

## Setup

1. Set a budget for page weight, client JavaScript, fonts/images and initial rendering. Establish baseline measurements for homepage and key detail/form pages on mobile throttling.
2. Resize/compress images, provide responsive sources and explicit dimensions; lazy-load below-the-fold media while prioritizing the actual LCP asset where appropriate. Use modern supported formats and alt text.
3. Remove unnecessary hydration, third-party tags and blocking requests. Subset/self-host fonts where licensing allows, limit variants and avoid excessive preloads.
4. Cache immutable fingerprinted assets with long lifetimes, HTML according to publishing needs, and never private/authenticated data in shared cache. Specify invalidation on publish. Do not add a service worker unless offline behavior is required and tested.
5. Optimize backend queries with indexes, bounded pagination and measured latency. Respect Worker CPU limits; avoid synchronous heavy tasks or speculative queues.
6. Run Lighthouse in a consistent environment, record several measurements rather than one noisy run, inspect network/render/layout causes, and test actual preview runtime. After launch review field metrics when enough traffic exists.

## Security considerations

Performance changes must not remove validation/authorization or cache personalized responses publicly. Avoid sending full URLs with sensitive query parameters to analytics. Compression/cache policy should not disclose secrets.

## Free-tier limitations

Image transformation, analytics history and SSR compute can have separate quotas/fees. Built-in static optimization and browser audits usually avoid a paid performance service.

## Verification

Compare before/after under the same profile; inspect image dimensions, requests, transferred bytes and main-thread work. Field good thresholds commonly use LCP ≤2.5s, INP ≤200ms and CLS ≤0.1 at the 75th percentile; recheck current definitions. Lab tests cannot establish field compliance.

## Troubleshooting

Noisy Lighthouse: repeat under controlled conditions and use medians. High CLS: reserve image/widget space and inspect fonts. Slow server: profile real queries and external calls before scaling hosting.

## Official documentation

[Core Web Vitals](https://web.dev/articles/vitals) · [Lighthouse](https://developer.chrome.com/docs/lighthouse/overview) · [Astro images](https://docs.astro.build/en/guides/images/) · [Workers limits](https://developers.cloudflare.com/workers/platform/limits/)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.
