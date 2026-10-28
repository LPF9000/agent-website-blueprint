# Resume a website project

Continue this repository without relying on earlier chat history.

1. Read root and applicable nested AGENTS.md instructions.
2. Read `.project/requirements.md` and confirm the current goal and explicit exclusions.
3. Read `.project/roadmap.md`, then progress, handoff, decisions, architecture and deployment records. If missing, reconstruct from files/commits and label uncertain findings.
4. Inspect `git status --short`, branch and `git log -10 --oneline`; inspect relevant open PRs and failing checks using the available GitHub connector. Preserve user changes. Do not repeat an already merged feature.
5. Read relevant code, tests, config, migrations and lockfiles. Compare claimed statuses with actual implementation and evidence. Do not trust progress notes blindly.
6. Re-run only the relevant checks needed to establish present state. Check actual deployed version/hostname if a task claims production verification and read-only access is available. Otherwise mark it unverified.
7. Summarize genuinely complete tasks, discrepancies, blockers and the highest-priority incomplete milestone whose dependencies are satisfied. Continue useful work rather than stopping at a summary.
8. Consult current official documentation for changed integrations. Use discovered connector operations; inspect resources before mutation. Honor production/destructive/spending approval boundaries.
9. Implement, test and verify the next small increment. Update roadmap/progress and decisions/architecture/deployment when affected; write a fresh handoff before ending.

Use exact states from AGENTS.md. Record commands, date, commit, environment, results, skipped checks and next steps. Never expose secrets to make a handoff more detailed.

## Current-source retrieval gate

Before version-sensitive implementation, read [source freshness](../docs/source-freshness.md) and [official source register](../docs/sources.md); use [sources.json](../docs/sources.json) to find topic URLs, indexes and changelogs. Match documentation to installed versions, check current security advisories and limits, and record source/date/version plus actual verification in project decisions. A successful URL fetch is not a reviewed instruction, and a reviewed instruction is not a tested integration. Never assume dated guidance is current.
