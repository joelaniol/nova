# Network

Nova's network controls cover browser routing and tab-scoped request debugging. Choose the area that matches your task:

| Area | What it covers |
| :--- | :--- |
| [Proxy Routing](proxy/README.md) | Proxy profiles, authentication, the shared browser route and optional leak protection. |
| [Network Interception & Request Replay](network-interception/README.md) | Temporary request/response rules in a tab and a separate HTTP request repeater. |
| [SSL/TLS Inspection & Debugging](tls-inspection/README.md) | Certificate chains, host coverage, protocols, ciphers, HSTS and Certificate Transparency. |

## How the Controls Relate

Proxy routing selects the shared browser's route to the network, subject to configured bypasses. Network interception temporarily changes matching requests or responses in one tab. Interception does not require a proxy profile.

Request replay sends a separate HTTP request outside the page, optionally adopting session material. It does not run through the page's tab-scoped interception rules. TLS inspection examines certificate and connection evidence; it does not approve a certificate warning or change interception rules.

Session recording preserves granted event streams for later investigation; it does not change the route, install interception rules or restore an earlier page state.

Session isolation, proxy routing and browser identity are separate controls. Two sandboxes can have different logins while still using the same proxy and outward-facing IP.

## Related Documentation

* [Session Recording & Time-Travel Debugging](../session-recording/README.md) — Captured network events together with console, page and interaction evidence.

* [Privacy](../privacy/README.md) — Fingerprint protection and related privacy controls.

* [Multi-Sandbox Session Isolation](../sandbox-isolation/README.md) — Separate browser profiles per sandbox.
* [Fingerprint Protection & Browser Identity](../privacy/fingerprint-and-identity/README.md) — Fingerprint protection and client hints.
* [Network Tool Reference](../../mcp-reference/tools/proxy-and-network/README.md) — Proxy, interception, replay and TLS inspection tools.

[All core features](../README.md)
