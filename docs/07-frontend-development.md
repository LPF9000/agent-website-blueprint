# Frontend development

## Purpose

Build a readable, responsive and accessible interface with minimal client JavaScript.

## When needed

Every website; application framework and styling choices depend on requirements.

## Prerequisites

Requirements, content model, wireframe/style direction, selected supported Node/tool versions and acceptance journeys.

## Recommended implementation

Astro + TypeScript for content sites. Use semantic HTML and CSS first, hydrating interactive components only where needed. Tailwind is optional; follow its current framework integration rather than old plugin instructions.

## Setup

1. Inspect existing files and scaffold only in the approved empty website folder. From its parent, `npm create astro@latest` opens Astro’s documented setup; choose the intended directory, review prompts, and record the resulting versions and lockfile. A latest initializer is used once; subsequent installs use the lockfile.
2. Select strict TypeScript options appropriate to the framework. Define public layouts, navigation, main landmark, heading hierarchy, footer and a real 404 page.
3. Model content with Markdown/collections or typed JSON. Build page templates, descriptive URLs and reusable accessible form/input/button components. Include loading, empty, validation-error and failure states for dynamic features.
4. Add responsive styles using content-driven breakpoints. Limit third-party scripts/fonts; self-host assets when practical and licensed.
5. Add only justified interactivity. If Next.js is selected, distinguish server/client modules, server-only secrets, cache boundaries and runtime compatibility. Follow current provider/framework guidance.
6. Add framework-specific type checking and lint scripts; an Astro build alone does not prove full type correctness. Run dev, type checks and production build, then test built output on hosted preview.

## Security considerations

Use framework escaping; sanitize untrusted rich HTML with a maintained sanitizer. Avoid injecting raw HTML and inline event handlers. Public-prefixed env vars are bundled for everyone. Never cache personalized HTML in shared caches.

## Free-tier limitations

Frontend tooling is generally open source, but SSR compute, hosted fonts, images, analytics and paid component libraries can cost money. Begin with local CSS and optimized static assets.

## Verification

Run declared check/lint/build commands, inspect the generated artifact, navigate all routes, use keyboard and mobile viewport, check 404 behavior and confirm no server secret in client assets. Record visual/manual checks separately from automated results.

## Troubleshooting

Hydration mismatch: compare server/client inputs and time-dependent values. Missing styles: follow current Tailwind integration and content detection. Blank deep route: inspect static versus SPA routing rather than returning index.html for every 404.

## Official documentation

[Astro installation](https://docs.astro.build/en/install-and-setup/) · [Astro TypeScript](https://docs.astro.build/en/guides/typescript/) · [Next.js docs](https://nextjs.org/docs) · [Tailwind installation](https://tailwindcss.com/docs/installation) · [TypeScript handbook](https://www.typescriptlang.org/docs/handbook/intro.html)

External guidance reviewed: 2026-10-28 where listed in the [source register](sources.md). Source review is not a live integration test. Recheck current versions, advisories and pricing using the [freshness protocol](source-freshness.md) before implementation.
