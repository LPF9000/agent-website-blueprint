# Security policy

This blueprint has no deployed application or security response service. Only the current main branch receives documentation corrections; consumers must update and independently review generated websites.

Do not post a live vulnerability, token, private customer data or exploitable production URL in a public issue. Use GitHub's repository **Security → Advisories → Report a vulnerability** if private reporting is enabled. If that option is absent, ask in a public issue only for a private reporting channel, without exploit details. No private contact address or response SLA is promised.

Include affected file/commit, impact, redacted reproduction against a local or explicitly authorized preview, proposed mitigation and disclosure preferences. Never scan a third-party target without permission.

If a credential is exposed: revoke/rotate it first, contain misuse, preserve redacted evidence, audit access, then remediate history and caches as needed. Follow [incident response](security/incident-response.md). Do not wait for a maintainer reply to contain a leak in your own system.

The [security baseline](security/security-baseline.md) is an engineering starting point, not certification, legal advice, or a guarantee that generated code is safe.
