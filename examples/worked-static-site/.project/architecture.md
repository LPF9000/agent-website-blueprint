# Architecture

Synthetic content.json → standard-library build.py → dist/index.html, dist/visit/index.html, dist/404.html and dist/assets/site.css. There is no runtime application, database, identity or network integration.

Only dist is served by a loopback-bound development server. Build output contains no source, project records, reports or fixtures. The example never reads environment secrets. HTML escaping handles the content boundary; input paths are a fixed explicit route allowlist.

Local tests build into a temporary directory and start an ephemeral loopback HTTP server. They verify routing, content/landmarks/noindex, escaped input and artifact scope. They do not establish browser layout quality, TLS, production headers or host-specific error handling.
