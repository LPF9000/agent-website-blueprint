# Dependencies and CI security

Keep dependency count small, use a supported runtime, pin reviewed versions and commit lockfiles. Explain a new package’s need, license and alternative before installation.

1. Install from official registries/vendor sources; inspect package identity, maintainer changes, install scripts and unexpected lockfile updates. Reproducible `npm ci` is preferred after lockfile review. Do not run package scripts with production credentials present.
2. Enable dependency graph/alerts and [Dependabot](../templates/github/dependabot.yml) for actual paths/ecosystems. Review security exposure and release notes; do not auto-merge major or identity/runtime changes.
3. Run `npm audit` for a website with a supported npm lockfile; triage dev/runtime/reachability and record reason for accepted findings. Do not use `npm audit fix --force` as unattended remediation. Python validator dependencies use the pinned requirements file; review advisories for them as well.
4. Pin third-party Actions to a reviewed full commit SHA (or adopt the provider's stronger documented dependency-lock mechanism where suitable). Verify the commit belongs to the real action repository. Keep token permissions minimal, checkout credentials nonpersistent and jobs time-bounded.
5. Never checkout untrusted PR code using privileged `pull_request_target` with secrets. PR validation does not need deployment credentials; production workflows require explicit environment authorization controls. Avoid arbitrary workflow input interpolation into shell scripts; pass data through validated environment/config fields.
6. Limit artifacts (for example seven days or less), exclude auth state/env/backups and avoid secret-bearing logs. Dependabot updates may need additional configuration for action references in inactive template directories; review those pins manually too.

After an update run relevant type/build/behavior tests, hosted-preview compatibility and rollback checks. Record the exact changed version and evidence. Alerts are signals, not proof that all code is safe.

Sources: [GitHub secure use](https://docs.github.com/en/actions/reference/security/secure-use), [Dependabot options](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference), [npm audit](https://docs.npmjs.com/cli/commands/npm-audit). Reviewed 2026-10-28; recheck advisories before updates.
