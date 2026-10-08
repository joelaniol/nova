# SSL/TLS Inspection & Debugging

Use TLS inspection to investigate a certificate warning, a missing certificate in a chain, host-name coverage or a server's accepted encryption protocols. Nova provides both inspection of an existing tab connection and active checks against a specified host.

## Choose the connection you need to examine

[`nova.tls_inspect`](../../../mcp-reference/tools/proxy-and-network/nova-tls-inspect.md) accepts exactly one of:

* **`targetId`** — Inspect what Chromium verified and negotiated for the current tab connection, including the verified certificate path and whether a certificate warning was overridden. This mode does not generate its own network probes.
* **`url`** — Inspect a specified host, with an optional port. Active probes can examine the certificate chain as delivered by the server and run the selected checks. Implicit-TLS services such as `mail.example.com:993` are supported.

These modes answer different questions: the browser's verified path can differ from the chain a server sends. Choose the mode before interpreting a missing intermediate or a connection-specific finding.

## Available checks

| Check | What it inspects |
| :--- | :--- |
| `certificate` | Chain, issuer, validity, covered host names, key and permitted purposes, fingerprints and validation information. This is the default check. |
| `server` | Supported SSL/TLS versions, cipher suites, key-exchange groups, ALPN and related TLS behavior. |
| `http` | HSTS, server header and HTTP-to-HTTPS redirect behavior. |
| `ct_subdomains` | Names recorded in public Certificate Transparency logs for the domain. **This sends the domain name to crt.sh, a third-party service.** |

`checkHosts` tests additional names against the certificate. `includePem` can include certificate material for closer examination. See the tool reference for exact parameters, result fields and limits.

## Interpret measured findings

Findings have severity levels rather than a single overall security score. Active server scans are bounded; parts not reached are reported in `missing`. Incomplete measurement is not proof that a protocol or feature is absent. Certificate Transparency names are historical certification evidence, not confirmation that each service is currently online.

Active connections use Nova's configured browser proxy route. They do not fall back to a direct route when the proxy fails. Read the selected target, route and missing checks alongside the findings.

## Inspection and certificate prompts

Inspection diagnoses the connection; it does not turn off certificate validation or approve an untrusted server. Nova's certificate and client-certificate prompts are separate decisions, described in the [Certificates & authentication user guide](../../../user-guide/identity-and-security/certificates-and-auth.md) and [Native Dialogs & UI Prompts](../../native-dialogs-and-prompts/README.md).

* [Proxy Routing](../proxy/README.md) — Shared browser route and proxy configuration.
* [Network Interception & Request Replay](../network-interception/README.md) — Request/response debugging and separate HTTP replay.

[Network overview](../README.md) · [All core features](../../README.md)
