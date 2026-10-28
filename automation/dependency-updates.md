# Dependency updates

Optional automated PR creation complements required security maintenance. Use [Dependabot template](../templates/github/dependabot.yml) only for actual manifests/paths. This blueprint already enables pip and GitHub Actions updates for itself; npm is for generated websites only.

1. Enable available dependency graph/security alerts in repository settings. Review account/plan entitlements and install minimal app permissions.
2. Set weekly update cadence and a small open-PR limit. Check active workflow SHA pins and inactive template pins manually; update source verification dates with actual review.
3. Triage security alerts by exploitability/exposure and affected deployed version. Read official release notes/advisories, inspect lockfile/install scripts and record accepted risks with owner/deadline.
4. Run relevant type/lint/build/unit/integration/negative authorization tests and hosted-preview smoke after updates. Major/auth/database/runtime changes need careful migration/rollback review. Never auto-merge simply because dependency installation succeeded.
5. Production deploy uses the same approval/checklist flow as features. Do not run unattended `audit fix --force` or supply production credentials to package scripts.

Free-tier limits: update PR checks consume runner/build minutes and storage; group routine updates only where review remains meaningful. Troubleshooting: incorrect ecosystem/directory yields no updates; missing manifest/lockfile must be fixed rather than adding empty package scaffolds.

Verification: a real PR updates only expected packages, checks pass, source/tool pins are valid and deployed behavior is verified after authorized release. See [dependency security](../security/dependency-security.md) and [official Dependabot options](https://docs.github.com/en/code-security/reference/supply-chain-security/dependabot-options-reference).
