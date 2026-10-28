# Incident response runbook

Choose an incident lead and backup before launch; record private contact details outside public Git. Use this for credential leaks, unauthorized access, data exposure, malicious deployments and availability incidents. Do not promise a response SLA without an owner.

## First response

1. Record UTC time, impacted hostname/version, symptoms and reporter. Preserve redacted logs/evidence with access controls; avoid public issue disclosure and do not erase evidence while investigating.
2. Contain: revoke/rotate leaked credentials immediately; restrict compromised endpoints/access; disable affected integration or revert to a known-good deployment where safe. Production containment must be performed by an authorized operator. Removing a file from Git does not revoke a token.
3. Determine scope: affected users/data/time window, source/deploy account access, sessions, database/storage policies, backups and external webhook/integration abuse. Distinguish confirmed exposure from unknowns.
4. Eradicate: fix the underlying defect, remove unauthorized access, repair policy/dependency/configuration and invalidate affected sessions/keys as appropriate. Review logs for misuse and provider billing/abuse impact.
5. Recover: use a clean reviewed artifact, compatible migrations or rehearsed data recovery; restore integrity/permissions, purge leaked caches where relevant and run safe acceptance/security tests before reopening traffic.
6. Communicate through the designated owner/private channels. Involve privacy/legal/security specialists for notification duties and timelines where required; do not invent jurisdictional requirements or publicly post personal data.
7. Monitor closely, document root cause and impact, add regression tests, assign remediation owners/dates and revise threat model, roadmap, deployment and handoff.

## Evidence and recovery checklist

Credential IDs/scopes and revocation time (never values); trusted commit/provider version; redacted affected object/user counts; backup age/restore evidence; negative access tests; notification decisions; remaining uncertainty. Keep incident details in restricted storage if public project records would expose victims or exploitable information.

## Exercise

On isolated preview simulate a bad release or fake leaked test key. Verify the operator can locate versions, revoke the test credential, restore known-good behavior and contact the correct owner. Record recovery time and gaps. Never practice by exposing a real production secret.

Sources: [NIST incident response](https://csrc.nist.gov/pubs/sp/800/61/r3/final), [GitHub secret scanning guidance](https://docs.github.com/en/code-security/secret-scanning/introduction/about-secret-scanning), [SECURITY](../SECURITY.md). Links are discovery starting points; verify current provider procedures before use.
