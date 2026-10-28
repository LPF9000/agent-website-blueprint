# Deployment record

Environment: local development only. No account, project, host, DNS, secret or webhook settings exist for this fixture. Build: `python examples/worked-static-site/build.py`. Output: `examples/worked-static-site/dist/`. Local preview binds to 127.0.0.1; it is not production hosting.

The loopback tests prove local status/content behavior only. The supplied 404.html is an artifact; configuring a host to serve it with status 404 remains unverified. The development server's default 404 response is what the HTTP negative test observes.

Future hosted preview: follow the blueprint deployment guide, serve only dist, apply a tested static security-header policy, verify host-specific routes/error responses and retain noindex. No deployment should be inferred from the presence of these instructions. Rollback for a future host must be recorded when that host is selected.
