# Environment matrix

Copy into `.project/deployment.md` or a linked `.project/environments.md`. Record names/references and evidence only; never values, raw customer data or secret-bearing URLs. Updated: YYYY-MM-DD. Owner: assign.

| Configuration class | Local | Isolated preview | Production | How change takes effect | Evidence / intentional difference |
| --- | --- | --- | --- | --- | --- |
| Public build variables | Names + expected public host/mode | Separate project URL/mode | Approved production host/mode | Rebuild/redeploy; values embedded in client | Commit/artifact and observed destination, no key dumps |
| Runtime vars/secrets/bindings | Ignored local store | Restricted preview store/reference | Restricted production store/reference | Inspect actual instance, inheritance and redeploy/update rules | Provider version, configuration revision/time, safe behavior |
| Schema/migration/RLS/grants | Reviewed local migration set | Same reviewed migrations first | Same set after authorization | Explicit target-confirmed migration | History/policy comparisons, denied A/B operations |
| Auth templates/policies | Synthetic/test | Intended template parity, test delivery | Approved customer delivery | Allowlisted settings sync; keep secrets/URLs separate | Email verification/recovery and policy checks |
| SMTP/sender/redirects | Local/test destinations | Allowlisted test recipients/callbacks | Exact approved production destinations | Provider-specific | Tested safe delivery/callback; no recovery tokens |
| Payments/webhooks | Sandbox only | Isolated active receiver + paired secret reference | Live receiver + separate credential references | Update receiver/settings and verify actual delivery | Receiver owner, event subscription, pending delivery review |
| Data/fixtures | Synthetic | Namespaced synthetic data; document shared-project collisions | Customer data protected | No data copy or unapproved reset | Test owner, cleanup/retention and reset authorization |
| Access/CI identities | Selected local access | Scoped machine/user policy | Separate approved policies | Verified JWT/policy configuration | Identity type, permitted action, denial evidence |

List expected parity and deliberate differences. A dashboard save is not deployment evidence. Before changing a shared base setting identify existing previews, inheritance behavior and safe refresh/update steps. Before retiring preview resources inspect dependent webhooks, test identities and outstanding retries. Record approval and rollback for production-impacting changes.

Use [operational failure modes](../docs/25-operational-failure-modes.md) and [deployment template](deployment-template.md). This is a planning template, not verified environment state.
