# Privacy

Nova has separate controls for browser fingerprints, stored credentials, network routing and stored website data. This overview brings them together while keeping each detailed guide in its own topic area.

## Topics

| Topic | What it covers |
| :--- | :--- |
| [Fingerprint Protection & Browser Identity](fingerprint-and-identity/README.md) | Protection levels, global/sandbox/tab scope, browser identity presets and temporary emulation. |
| [Password Vault & Secret Injection](vault-and-secrets/README.md) | Saved-login metadata and SecretRef fills; scoped API keys and tokens for terminal sessions and scheduled tasks. |

## Related Privacy Controls

| Guide | What it covers | Where it is maintained |
| :--- | :--- | :--- |
| [Proxy Routing](../network/proxy/README.md) | Proxy profiles, authentication, shared browser routing and optional leak protection. | Network |
| [Multi-Sandbox Session Isolation](../sandbox-isolation/README.md) | Separate cookies and persistent website storage for different sessions. | Session isolation |
| [Site Data Management](../site-data-management/README.md) | Inspecting or clearing cookies, storage and cache with an explicit scope. | Site data |
| [Private Browsing](../../user-guide/browser/private-browsing.md) | Using a private session and understanding what remains after it ends. | User Guide |

The proxy guide belongs to Network and is linked here because routing also matters for privacy. Both overviews lead to the same article; changing it updates the guidance reached from either topic.

## How the Controls Relate

A proxy changes the browser's network route, subject to its configuration and bypasses. Fingerprint protection changes supported device and rendering readouts; browser identity changes the user-agent and Client Hints. Session isolation separates website state. The vault controls credential delivery, while the secret store supplies authorized programs with scoped secrets. These controls answer different questions and can be used together.

For example, two sandboxes can have different logins while using the same shared proxy route. Changing the route does not clear cookies or change a browser identity. Fingerprint protection does not prevent an account, cookies or an IP address from linking visits, and none of these controls alone guarantees anonymity.

A vault fill avoids returning the password through the vault and secret-fill responses, but the password still reaches the destination page. A program receiving a secret through an environment variable can print or transmit it. Trust in the receiving page or program remains a separate decision.

* [Passwords & Vault User Guide](../../user-guide/identity-and-security/passwords-and-vault.md) — Saved logins and related user-facing guidance.
* [Privacy Policy](../../../PRIVACY.md) — Nova's data handling and the role of connected AI providers.
* [Network overview](../network/README.md) — Routing, request interception, replay and TLS diagnostics.

[All core features](../README.md)
