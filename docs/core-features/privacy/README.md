# Privacy

Nova has separate controls for browser fingerprints, network routing and stored website data. This overview brings them together while keeping each detailed guide in its own topic area.

## Fingerprint Protection & Browser Identity

| Topic | What it covers |
| :--- | :--- |
| [Fingerprint Protection & Browser Identity](fingerprint-and-identity/README.md) | Protection levels, global/sandbox/tab scope, browser identity presets and temporary emulation. |

## Related Privacy Controls

| Guide | What it covers | Where it is maintained |
| :--- | :--- | :--- |
| [Proxy Routing](../network/proxy/README.md) | Proxy profiles, authentication, shared browser routing and optional leak protection. | Network |
| [Multi-Sandbox Session Isolation](../sandbox-isolation/README.md) | Separate cookies and persistent website storage for different sessions. | Session isolation |
| [Site Data & Privacy Management](../site-data-management/README.md) | Inspecting or clearing cookies, storage and cache with an explicit scope. | Site data |
| [Private Browsing](../../user-guide/browser/private-browsing.md) | Using a private session and understanding what remains after it ends. | User Guide |

The proxy guide belongs to Network and is linked here because routing also matters for privacy. Both overviews lead to the same article; changing it updates the guidance reached from either topic.

## How the Controls Relate

A proxy changes the browser's network route, subject to its configuration and bypasses. Fingerprint protection changes supported device and rendering readouts; browser identity changes the user-agent and Client Hints. Session isolation separates website state. These controls answer different questions and can be used together.

For example, two sandboxes can have different logins while using the same shared proxy route. Changing the route does not clear cookies or change a browser identity. Fingerprint protection does not prevent an account, cookies or an IP address from linking visits, and none of these controls alone guarantees anonymity.

* [Privacy Policy](../../../PRIVACY.md) — Nova's data handling and the role of connected AI providers.
* [Network overview](../network/README.md) — Routing, request interception, replay and TLS diagnostics.

[All core features](../README.md)
