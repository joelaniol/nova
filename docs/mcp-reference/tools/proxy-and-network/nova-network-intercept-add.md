# `nova.network_intercept_add`

Deposits a CDP network interception rule to mock responses, inject delays, modify headers, or fail requests.

---

## 1. Overview

`nova.network_intercept_add` intercepts live network requests matching a URL pattern on the target tab. Nova answers matching requests immediately from this rule without waiting for LLM turns, ensuring page JavaScript never hangs. Rules expire automatically by TTL, hit count, or tab closure.

* **Core Architecture Guide:** [Network Interception & Request Replay](../../../core-features/network/network-interception/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs, or 'active'. The rule lives and dies with this tab. |
| `urlPattern` | `string` | Yes | — | — | Glob the request URL must match, '*' and '?' allowed (e.g. 'https://example.com/api/*'). Required, and must carry at least 4 literal characters: a pattern that matches everything would take the whole page off the network instead of the request under test. |
| `methods` | `array` of `string` | No | — | — | Restrict to these HTTP methods (GET, POST, PUT, PATCH, DELETE, HEAD, OPTIONS). Omit to match any method. |
| `action` | `string` | No | `"fail"` | `fail`, `respondWith`, `modifyRequest`, `modifyResponse`, `delay` | fail = the request fails as if the network refused it. respondWith = Nova answers without reaching the network. modifyRequest = the outgoing request changes. modifyResponse = the real server response changes before the page receives it. delay = the request is held, then continues unchanged. |
| `errorReason` | `string` | No | `"Failed"` | `Failed`, `Aborted`, `TimedOut`, `AccessDenied`, `ConnectionClosed`, `ConnectionReset`, `ConnectionRefused`, `ConnectionAborted`, `InternetDisconnected`, `AddressUnreachable`, `BlockedByClient`, `BlockedByResponse`, `NameNotResolved` | How a fail rule fails. Pick the one the page would really see — a timeout and a refused connection often take different code paths. |
| `status` | `integer` | No | `200` | 100–599 | HTTP status for a respondWith rule. |
| `body` | `string` | No | — | — | Response body for a respondWith rule. Sent verbatim; max 200000 characters. |
| `contentType` | `string` | No | `"text/plain; charset=utf-8"` | — | Content-Type for a respondWith rule, unless headers already carries one. |
| `headers` | `object` | No | — | — | Extra response headers for a respondWith rule, as name/value pairs (max 20). |
| `requestHeaders` | `object` | No | — | — | modifyRequest: headers to set on the OUTGOING request, as name/value pairs (max 20). The page's own headers are kept; same-named entries are overridden. |
| `removeRequestHeaders` | `array` of `string` | No | — | — | modifyRequest: header names to strip from the outgoing request (max 20). Applied after requestHeaders. |
| `rewriteUrl` | `string` | No | — | — | modifyRequest: send the request to this absolute URL instead — useful for pointing one endpoint at a staging or mock host. |
| `setMethod` | `string` | No | — | `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS` | modifyRequest: replace the HTTP method of the outgoing request. |
| `setBody` | `string` | No | — | — | modifyRequest: replace the request body. An empty string clears it; whitespace is preserved. Stale Content-Length is removed. Max 200000 characters. |
| `responseHeaders` | `object` | No | — | — | modifyResponse: response headers to set after the real server answered (max 20). Existing same-named headers are replaced. |
| `removeResponseHeaders` | `array` of `string` | No | — | — | modifyResponse: response-header names to remove (max 20), for example Set-Cookie or Content-Security-Policy. |
| `setResponseStatus` | `integer` | No | — | 100–599 | modifyResponse: replace the real HTTP status before the page receives it. |
| `setResponseBody` | `string` | No | — | — | modifyResponse: replace the real response body as uncompressed text; max 200000 characters. Empty string clears it; omission preserves the original body without reading it into Nova. Original Content-Length, Content-Encoding and Transfer-Encoding are removed on replacement. HEAD and bodyless statuses never receive a payload. |
| `delayMs` | `integer` | No | `0` | 0–30000 | Hold the matching request this long before acting on it. Required for action='delay'; combinable with the other actions (e.g. a slow 500). Capped at 30 s, and the wait ends early when the rule is cleared or its tab closes. |
| `ttlMs` | `integer` | No | `120000` | 5000–900000 | How long the rule may live. Clamped to 15 minutes: a rule is an instrument, not a setting. |
| `maxHits` | `integer` | No | `20` | 1–1000 | How many requests the rule may answer before it removes itself. |
| `note` | `string` | No | — | — | Free text shown in the rule list and in Nova's own interception indicator, so a human can tell what this rule is for. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.network_intercept_add",
  "arguments": {
    "urlPattern": "*api/checkout/payment*",
    "action": "respondWith",
    "status": 500,
    "body": "{\"error\": \"Payment service temporarily unavailable\"}",
    "maxHits": 1,
    "ttlMs": 30000
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Rule ir_8f12a4b0 armed on tab-1: *api/checkout/payment* answered with HTTP 500. Expires in 30000 ms or after 1 hit(s), whichever comes first."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "ruleId": "ir_8f12a4b0",
    "rule": {
      "ruleId": "ir_8f12a4b0",
      "targetId": "tab-1",
      "urlPattern": "*api/checkout/payment*",
      "action": "respondWith",
      "summary": "*api/checkout/payment* answered with HTTP 500",
      "hits": 0,
      "maxHits": 1,
      "applied": 0,
      "failed": 0,
      "lastError": null,
      "expiresAtUtc": "2026-10-04T12:05:30.0000000Z",
      "remainingMs": 30000,
      "note": null
    },
    "reasonCode": null,
    "message": null,
    "guardrails": {
      "ttlMs": 30000,
      "maxHits": 1,
      "delayMs": 0,
      "maxDelayMs": 30000,
      "expiresAtUtc": "2026-10-04T12:05:30.0000000Z",
      "endsOnTabClose": true,
      "endsOnAppExit": true,
      "emergencyStop": "nova.network_intercept_clear"
    },
    "activeRuleCount": 1
  }
}
```

---

## 4. Operational Best Practices

* **Deterministic Fault Injection:** Excellent for QA: verify how UI components react when API endpoints return 500, empty collections, or take 8 seconds to answer.
* **Auto-Expiring Guards:** Always specify `maxHits` or short `ttlMs` so interception rules do not outlive your test step.
* **Emergency Stop:** Call `nova.network_intercept_clear()` without parameters to instantly disarm all interception rules across the entire browser.

---

## See Also

* [`nova.network_intercept_clear`](nova-network-intercept-clear.md) - Disarm interception rules.
* [`nova.network_intercept_list`](nova-network-intercept-list.md) - List active rules.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
