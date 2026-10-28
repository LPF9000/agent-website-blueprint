# Configuration and contract templates

Copy only the selected module into a generated website, then replace names and verify with the current official docs. These files do not provision resources or implement an application by themselves.

- [Environment/monitor configuration](environment/README.md): variable exposure, separate environments and bounded public health checks.
- [GitHub](github/README.md): Dependabot and Playwright examples; workflow templates are in [automation](../automation/README.md).
- [Cloudflare](cloudflare/README.md): static-asset deployment configuration without bindings or credentials.
- [Supabase](supabase/README.md): published-content SELECT-only SQL example; admin writes require separately designed authorization.
- [API contracts](api/README.md): products/events OpenAPI, statuses and permissions.
- [Security](security/README.md): static-only headers, preview indexing and review notes.

Recheck version-specific fields using [source freshness](../docs/source-freshness.md). JSON/YAML parsing is not provider deployment validation; see [validation report](../docs/validation-report.md).
