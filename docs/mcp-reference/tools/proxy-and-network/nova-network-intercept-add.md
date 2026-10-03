# `nova.network_intercept_add`

Deposits a CDP network interception rule to mock responses, inject delays, modify headers, or fail requests.

---

## 1. Overview

`nova.network_intercept_add` intercepts live network requests matching a URL pattern on the target tab. Nova answers matching requests immediately from this rule without waiting for LLM turns, ensuring page JavaScript never hangs. Rules expire automatically by TTL, hit count, or tab closure.

* **Capability Bundle:** `proxy_management`
* **Security Tier:** Tier 2 (Network Interception)
* **Core Architecture Guide:** [Proxy Routing & Stealth Network Engine](../../../core-features/proxy-and-network.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`urlPattern`** | `string` | Yes | `none` | URL pattern wildcard or exact match (e.g. `"*api/v1/users*"`). |
| **`action`** | `string` | No | `"respondWith"` | Action: `"respondWith"`, `"fail"`, `"delay"`, `"modifyRequest"`, `"modifyResponse"`, or `"allow"`. |
| **`status`** | `integer` | No | `200` | HTTP response status code when `action: "respondWith"` (e.g. `200`, `404`, `500`). |
| **`body`** | `string` | No | `null` | Mock response body text or JSON string. |
| **`contentType`** | `string` | No | `"application/json"` | Response `Content-Type` header. |
| **`delayMs`** | `integer` | No | `0` | Delay in ms before fulfilling the request. |
| **`maxHits`** | `integer` | No | `null` | Maximum number of times this rule matches before auto-expiring. |
| **`ttlMs`** | `integer` | No | `60000` | Time-to-live in ms (max 300,000). Rule auto-purges after expiration. |
| **`methods`** | `array of strings` | No | `all` | Filter by HTTP methods (e.g. `["GET", "POST"]`). |
| **`targetId`** | `string` | No | `"active"` | Tab target ID from `nova.tabs`. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

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
      "text": "Interception rule 'rule-8f12a4b0' armed on tab-1 (*api/checkout/payment* -> respondWith 500)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "ruleId": "rule-8f12a4b0",
    "targetId": "tab-1",
    "urlPattern": "*api/checkout/payment*",
    "action": "respondWith",
    "status": 500,
    "maxHits": 1,
    "ttlMs": 30000
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
