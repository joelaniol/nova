# `nova.tls_inspect`

Inspects the TLS certificate and server configuration of one host in depth: full chain, names, purpose, validation level, protocol and cipher support, HSTS and Certificate Transparency subdomains.

---

## 1. Overview

`nova.tls_inspect` answers the questions a certificate dialog cannot: which names a certificate really covers, whether the server sends a complete chain, what each certificate may be used for, and what the server accepts on the wire — the view that scanners such as Shodan, SSL Labs or testssl give, from inside Nova.

* **Target:** either `url` (`https://host[:port]` or bare `host[:port]`; implicit-TLS ports such as `993` work) or `targetId` (the connection a tab uses, read without network traffic of its own: the certificate path Chromium verified, what the browser negotiated in `browserConnection`, and whether a certificate warning was overridden). One host per call, never ranges.
* **`checks`:**
  * `certificate` (default) — every certificate in delivery order with subject/issuer, validity and days left, subjectAltNames, key usage and extended key usage (`validForServerAuth`), DV/OV/IV/EV, key type and size, SHA-256 and SPKI pins, OCSP/CRL/CA-issuer URLs, must-staple, embedded SCTs, a stapled OCSP answer, host coverage per RFC 6125 for the host and every `checkHosts` entry, and an offline chain check that also catches a missing intermediate or wrong order.
  * `server` — SSLv3 to TLS 1.3 support, every accepted cipher suite per version in the server's order, server- or client-preferred order, key-exchange groups (including post-quantum hybrids), ALPN, secure renegotiation, extended master secret, session tickets, OCSP stapling and SNI behaviour. Bounded to 150 handshakes and 90 seconds; parts not reached are listed in `missing`.
  * `http` — HSTS policy, `Server` header, and whether plain http redirects to https.
  * `ct_subdomains` — every name ever certified under the domain, from public Certificate Transparency logs. **This sends the domain name to crt.sh**, a third-party service.
* **`findings[]`** grades what was measured (`critical`, `high`, `medium`, `info`). There is deliberately no overall score.
* **Network route:** every connection takes the same proxy route as the browser and never falls back to a direct connection when the proxy fails.

* **Core Architecture Guide:** [Proxy Routing & Network Engine](../../../core-features/proxy-and-network/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `url` | `string` | No | — | — | Server to inspect: 'https://host[:port]' or bare 'host[:port]' (port defaults to 443). Implicit-TLS services work as host:port, e.g. 'mail.example.com:993'. Other schemes are rejected. Pass exactly one of url or targetId. |
| `targetId` | `string` | No | — | — | Inspect the connection a tab is using (from nova.tabs), without network traffic of its own: the certificate path Chromium verified for the page (certificate.chainKind='verified_by_chromium'), what the browser negotiated (browserConnection: protocol, key-exchange group, cipher) and whether a certificate warning was overridden. For the chain exactly as the server delivers it, use url. Pass exactly one of url or targetId. |
| `checks` | `array` of `string` | No | — | — | Parts to run. certificate = chain and certificate details (default); server = protocol/cipher/group/extension scan; http = HSTS and redirect; ct_subdomains = names from Certificate Transparency logs via crt.sh. |
| `checkHosts` | `array` of `string` | No | — | — | Up to 50 additional host names to test against the certificate (e.g. subdomains); each reports covered and the matching subjectAltName. |
| `ctDomain` | `string` | No | — | — | Domain for ct_subdomains. Default: the registrable domain of the host (shop.example.co.uk -> example.co.uk). |
| `maxCtEntries` | `integer` | No | `200` | 1–2000 | Most CT names to return (1-2000, default 200); currently valid names come first, hasMore says whether more exist. |
| `includePem` | `boolean` | No | `false` | — | Also return every chain certificate as PEM. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.tls_inspect",
  "arguments": {
    "url": "shop.example.com",
    "checks": ["certificate", "server"],
    "checkHosts": ["www.example.com", "api.example.com"]
  }
}
```

### Result (abridged)
```json
{
  "ok": true,
  "target": { "host": "shop.example.com", "port": 443 },
  "route": "direct",
  "certificate": {
    "source": "handshake",
    "chainKind": "delivered",
    "deliveryOrderKnown": true,
    "chain": [
      {
        "position": 0,
        "subject": "CN=shop.example.com",
        "daysRemaining": 54,
        "subjectAltNames": { "dns": ["shop.example.com", "*.example.com"], "ip": [], "email": [], "uri": [], "wildcardCount": 1 },
        "usage": { "extendedKeyUsage": ["serverAuth"], "validForServerAuth": true },
        "validationType": "DV",
        "publicKey": { "algorithm": "EC", "bits": 256, "curve": "P-256", "description": "EC P-256" }
      }
    ],
    "hostChecks": [
      { "host": "shop.example.com", "covered": true, "matchedBy": "dns:shop.example.com" },
      { "host": "www.example.com", "covered": true, "matchedBy": "dns:*.example.com" },
      { "host": "api.example.com", "covered": true, "matchedBy": "dns:*.example.com" }
    ],
    "validation": { "trustedByWindows": true, "deliveredChainComplete": true, "deliveredOrderCorrect": true }
  },
  "server": {
    "protocols": [
      { "protocol": "TLSv1.3", "supported": true },
      { "protocol": "TLSv1.2", "supported": true },
      { "protocol": "TLSv1.1", "supported": false }
    ],
    "cipherSuites": [
      { "protocol": "TLSv1.2", "order": "server", "suites": [{ "name": "TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384", "strength": "ok" }] }
    ],
    "handshakesUsed": 41,
    "complete": true
  },
  "findings": [
    { "severity": "info", "code": "cbc_suites", "message": "CBC-mode suites are accepted; current guidance prefers AEAD suites only." }
  ],
  "complete": true,
  "message": "Certificate 'shop.example.com' from E6, 54 days left, host covered, trusted. Findings: 1 info."
}
```

---

## 4. Operational Best Practices

* **Start with the default.** `checks=['certificate']` costs one or two handshakes; add `server` when the configuration itself is the question.
* **`url` shows the delivered chain, `targetId` the verified one.** `chainKind` tells which; a missing intermediate or a sent root is only reported for a delivered chain.
* **Read `complete` and `missing`.** A protocol with `supported: null` was not tested (budget or connection lost), which is not the same as unsupported.
* **Use `checkHosts` for subdomain questions.** It answers "does this certificate cover api.example.com?" per RFC 6125: a wildcard covers exactly one label, never a public suffix.
* **`ct_subdomains` asks a third party.** Use it when the subdomain inventory is what you need; the domain is sent to crt.sh.

---

## See Also

* [`nova.tabs`](../browser-automation/nova-tabs.md) - The `security` block shows whether a tab runs under an overridden certificate.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
