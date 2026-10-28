# Roadmap

| ID | Work | State | Depends on | Acceptance / verification |
| --- | --- | --- | --- | --- |
| W1 | Requirements and simplest architecture | Tested | None | Compare scope/decisions with the synthetic two-page journey |
| W2 | Static rendering and stylesheet | Tested | W1 | Build the explicit artifact map and inspect semantic metadata/navigation |
| W3 | Local verification | Tested | W2 | Automated artifact, escaping, HTML and loopback HTTP tests |
| W4 | Hosted preview | Not started | W3, separate owner request and provider setup | Verify deployed artifact, TLS, headers, noindex and actual error route |
| W5 | Production | Not started | W4, production requirements and authorization | Real content/domain approval, full applicable checklist and production smoke |

W4/W5 are outside this example's published verification claim. They are explicit next stages for a consumer, not requirements to create infrastructure merely to read the walkthrough.
