# Decisions

D001 — Use Python's standard library to render plain HTML/CSS for a two-page teaching fixture. It requires no frontend dependencies and makes the artifact easy to inspect. Astro remains the blueprint's default for growing content sites; an application framework is not needed to demonstrate these local acceptance checks.

D002 — Keep all content fictional and generate only an explicit file map. Escape content before inserting HTML. Source, planning and tests stay outside the served directory.

D003 — Local HTTP only. No cloud resources or website are published for this example. Python http.server is a development preview, not a production security baseline. Preserve noindex in the teaching fixture; a real production launch needs its own metadata/domain review and hosted verification.

Reference reviewed 2026-10-28: [Python http.server documentation](https://docs.python.org/3/library/http.server.html). No provider configuration was executed.
