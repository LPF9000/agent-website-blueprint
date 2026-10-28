# Releases and maintenance

Releases package a reviewed snapshot of the blueprint. A version does not certify any generated website or vendor integration. The project is independently maintained; no vendor endorsement or response SLA is implied.

## Versioning

Use `0.x.y` while the instruction system is evolving. Increment the patch for corrections and compatible additions; increment the minor for substantial workflow/template changes that require consumer review. Document breaking changes and migration instructions explicitly even before 1.0. Do not move an already published version tag to different content.

The changelog records changes in Git. A GitHub release attaches a named version to an exact commit and includes tested scope, known limitations and migration notes. Earlier changelog entries may predate the first published release. Only claim a release exists after it is visible in GitHub.

## Release procedure

1. Review the diff and current official references for changed instructions. Preserve privacy and generic examples; never include another project's names, domains, data or identifiers.
2. Run documentation/configuration validation and relevant tests; inspect hosted CI for the exact intended commit. For examples, name local versus hosted verification separately.
3. Update changelog and validation evidence. State what was added, what ran and what did not. Check links and required files.
4. Publish a tag/release for that reviewed commit. Use plain release notes without promotional claims. No deployment, external promotion or notification integration is required.
5. Consumers compare their pinned baseline with new release notes, retain their own project changes and revalidate selected integrations. Do not copy a release over a working website wholesale.

## Current verification boundary

Documentation/tooling and the small static walkthrough have local automated checks. GitHub CI reruns those checks; it does not provision a hosted preview, perform a full accessibility/security audit, or validate payments/Auth/database flows. Consult [validation report](validation-report.md), [roadmap](../ROADMAP.md) and [changelog](../CHANGELOG.md).

Official reference: [GitHub release management](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository), reviewed 2026-10-28. Available UI/API operations must be discovered rather than assumed.
