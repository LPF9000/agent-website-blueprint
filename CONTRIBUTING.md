# Contributing

Open a focused issue or PR explaining the user problem, intended behavior and scope. Do not submit credentials or personal records. Read [AGENTS.md](AGENTS.md) before editing.

1. Branch from current main; inspect existing changes and preserve them.
2. Keep optional infrastructure optional. Explain a new dependency and its free-tier/paid boundary.
3. For major guides include purpose, when needed, prerequisites, recommended implementation, ordered setup, security, limitations, verification, troubleshooting and official sources. Record verification dates; distinguish source review from execution.
4. Update cross-links, examples, source register and changelog when relevant. Do not claim compliance or production readiness based only on a tool score.
5. Run `python scripts/validate.py` and `python -m unittest discover -s tests -v` with the dependency in [scripts/requirements.txt](scripts/requirements.txt). Include results and skipped checks in the PR.
6. Review scripts for bounded requests, safe targets, read-only production behavior and secret-safe failures. Pin Actions by full commit SHA and keep permissions minimal.

PR description: problem; resulting behavior; affected modules; validation; unverified integrations; migration/rollback if relevant. Maintainers should review security changes and breaking guidance before merging. Use [SECURITY.md](SECURITY.md) for vulnerabilities.

## Small useful contributions

Use the documentation-problem form for an incorrect step, broken link or outdated source. Include the file/section, version/commit and redacted evidence. Use the improvement form for a concrete workflow change with acceptance criteria and dependency/cost impact. Issues do not need real website names or account/project identifiers.

The [roadmap](ROADMAP.md) identifies gaps without promising dates. Before extending example coverage, read the [worked-example evidence](examples/worked-static-site/evidence.md) and preserve its local-versus-hosted boundary. Follow the [release policy](docs/releases.md) for compatibility and verification notes. Use SECURITY.md for vulnerabilities; issue forms must not collect live exploit details.
