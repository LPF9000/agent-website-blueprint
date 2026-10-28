# Monthly operational review

The [monthly workflow](workflows/monthly.yml) produces this **human checklist** in a run summary. It does not perform the reviews or send failure notifications for incomplete human work. Create a calendar/reminder task or existing issue process if you need due-date alerts; assign an owner and backup. No write permissions are required by the template.

| Review | Required evidence / action |
| --- | --- |
| Backup/recovery | Latest source/database/object backup age and protected location; isolated restore test at agreed cadence, row/object checks, achieved RPO/RTO and gaps |
| Access/permissions | GitHub/Cloudflare/Supabase/CMS/provider memberships, OAuth/app scopes, MFA/recovery owners; remove access through approved change process |
| Dependencies | Open advisory/update PR triage, unsupported runtimes and current release notes; tested preview upgrade plan |
| Secrets policy | Review exposure, unused credentials/scopes, owner and rotation requirements; rotate for compromise/provider policy, not needless monthly churn |
| Database/storage policies | Grants/RLS/view/function/bucket audit, A/B/admin negative tests after changes, retention/deletion and drift |
| Cost/usage | Current plan/quotas/alerts/spending behavior, preview duplication, traffic/storage/mail trends and approved limits |
| Domain/TLS | Registrar renewal date/auto-renew/payment owner, nameserver/DNSSEC state, certificate health/managed renewal and DNS ownership |
| Security/operations docs | Threat model, incident contacts, deployment/rollback, source freshness and schedule/notification health |

## Procedure

1. Copy workflow, enable `ENABLE_MONTHLY_REVIEW=true`, run manually and assign review date/owner in `.project/roadmap.md`. Check [automation setup](README.md).
2. Collect redacted evidence from actual dashboards/resources, using read-only inspection first. No raw dumps/tokens/personal data in Git.
3. Record reviewer/date/status/findings and next due date in progress. Open roadmap tasks with owners for gaps. Request required production/destructive/spending authorization before corrective actions.
4. Test recovery in isolation with real email/payments disabled. Use [backup guide](../docs/22-backup-and-recovery.md) and [incident response](../security/incident-response.md).
5. Mark the review complete only after evidence exists; a green reminder workflow is not a completed access review or restore test.

Limits: Free backup/log retention and permission features vary by provider; domain renewal and retained exports may cost money. Troubleshooting overdue reviews: escalate to the accountable owner, not an autonomous production cleanup bot.

Sources: [Supabase backups](https://supabase.com/docs/guides/platform/backups), [GitHub secure use](https://docs.github.com/en/actions/reference/security/secure-use), [Cloudflare DNS](https://developers.cloudflare.com/dns/), [pricing sources](../docs/23-cost-management.md). Recheck at review time.
