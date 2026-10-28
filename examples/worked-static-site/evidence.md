# Local verification evidence

Executed 2026-10-28 with Python 3.12.14 on Linux. This record describes local artifacts and loopback HTTP, not a cloud deployment. Source is included in this release; GitHub CI reruns the same tests for the published commit.

| Check | Command / method | Observed result |
| --- | --- | --- |
| Build | `python examples/worked-static-site/build.py` | Four files: index.html, visit/index.html, 404.html and assets/site.css |
| Repeatability and publication boundary | WorkedExampleTests.test_repeatable_artifact_and_no_unexpected_files | Repeated builds match byte-for-byte; unexpected files cause refusal without deletion |
| Escaping and route constraints | WorkedExampleTests.test_content_is_escaped_and_unapproved_routes_rejected | Synthetic script markup escaped; unapproved route rejected |
| Representative HTML structure | WorkedExampleTests.test_html_landmarks_metadata_and_local_navigation | One main/h1/title, navigation, skip target, noindex, no scripts, links resolve to known output |
| Actual local HTTP | WorkedExampleTests.test_actual_loopback_http_routes_and_not_found | Home, Visit and CSS return 200 with expected content; unknown route returns 404 |
| Full repository suite | `python -m unittest discover -s tests -v` | 18 tests passed: 14 safety/parser tests and 4 worked-example tests |

Not executed: browser rendering, keyboard/screen-reader review, Lighthouse, a full accessibility/security audit, host-specific custom 404 routing, TLS/security headers, hosted preview or production deployment. These remain unverified, not passed. Python's development HTTP server is not suitable for production.

The generated dist folder is not tracked; reconstruct it with the build command. No cloud resources, credentials, real organization, customer data or external service was used.
