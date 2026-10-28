# Project-state templates

Copy these into each website repository's `.project/` directory **before implementation**. Replace instructional text with actual decisions, keeping unknowns explicit. All records are tracked, non-secret engineering notes.

| Template | Destination |
| --- | --- |
| [Requirements](requirements-template.md) | `.project/requirements.md` |
| [Roadmap](roadmap-template.md) | `.project/roadmap.md` |
| [Progress](progress-template.md) | `.project/progress.md` |
| [Decision log](decision-log-template.md) | `.project/decisions.md` |
| [Architecture](architecture-template.md) | `.project/architecture.md` |
| [Deployment](deployment-template.md) | `.project/deployment.md` |
| [Handoff](handoff-template.md) | `.project/handoff.md` |
| [ADR](adr-template.md) | `.project/adr/NNNN-short-title.md` for major decisions |

Update triggers and evidence levels are defined in [AGENTS.md](../AGENTS.md). Do not publish private user data in these files even when the source repository is private.

## Operational cross-check

Additional optional evidence records: [environment matrix](environment-matrix-template.md) and [release evidence](release-evidence-template.md). Link them from `.project/deployment.md` or keep equivalent sections there; no new state file is mandatory.
