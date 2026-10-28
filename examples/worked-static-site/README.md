# Worked example: a small static information site

This fictional two-page example demonstrates requirements, an architecture decision, implementation, local verification and handoff. It uses plain HTML/CSS rendered with Python's standard library, so it needs no Node packages or cloud account. It is a teaching fixture inside the blueprint, not a hosted documentation website.

## 1. Read the request and plan

The fictional request is: “Show what our walking-notes group does and how a visitor would find visit information. We do not need accounts, forms, payments or a database.”

Review [.project/requirements.md](.project/requirements.md), [decisions](.project/decisions.md) and [roadmap](.project/roadmap.md). The plan intentionally chooses the smallest sufficient implementation. These are actual example records, not a claimed transcript of a user/agent conversation.

## 2. Inspect the implementation

[content.json](content.json) contains synthetic text. [build.py](build.py) escapes content and writes four explicit HTML/CSS files. There are no remote fonts/scripts, personal details, real venue information or secret values. Only the generated dist folder is suitable for serving; source, tests and project records remain outside it.

## 3. Build and verify

From the repository root, using Python 3.11+:

```sh
python examples/worked-static-site/build.py
python -m unittest discover -s tests -v
```

The first command prints the four-file artifact manifest. The second runs the blueprint safety/parser tests and the worked-example tests. See [evidence](evidence.md) for executed scope and limits.

To inspect the output yourself:

```sh
python -m http.server 8000 --bind 127.0.0.1 --directory examples/worked-static-site/dist
```

Open `http://127.0.0.1:8000/` locally, follow Visit, then stop the server with Ctrl+C. This server is for development only. It does not apply the production security baseline or host-specific custom error behavior. Generated dist is ignored by Git and regenerated; never publish the repository root.

## 4. Read the result honestly

Local checks cover reproducible output, file boundaries, text escaping, representative semantic/metadata structure, navigation and HTTP 200/404 behavior. They do not prove visual accessibility, browser rendering, HTTPS, production headers, a hosted preview or a deployed site. The supplied 404.html is checked as an artifact; the development server uses its own error response.

[Deployment](.project/deployment.md), [progress](.project/progress.md) and [handoff](.project/handoff.md) keep that distinction explicit. Hosted preview and production remain Not started. For an actual release, follow [deployment](../../docs/19-deployment.md) and [production checklist](../../docs/24-production-checklist.md); re-evaluate content, noindex and domain metadata first.
