# `nova.network_intercept_list`

Lists currently armed network interception rules with remaining hit budgets and expiration timers.

---

## 1. Overview

`nova.network_intercept_list` inspects which interception rules are currently active. Rules that have expired via TTL or hit budgets are automatically omitted.

* **Core Architecture Guide:** [Network Interception & Request Replay](../../../core-features/network/network-interception/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | — | — | Restrict to one tab. Omit to list every rule in the browser. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.network_intercept_list",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "ir_8f12a4b0 [tab-1] *api/checkout/payment* answered with HTTP 500 — 0/1 hits, 24500 ms left"
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": null,
    "count": 1,
    "rules": [
      {
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
        "remainingMs": 24500,
        "note": null
      }
    ],
    "anyActiveAnywhere": true
  }
}
```

---

## 4. Operational Best Practices

* **Checking Rule Liveness:** If a rule is missing from this list, it has already expired cleanly.

---

## See Also

* [`nova.network_intercept_add`](nova-network-intercept-add.md) - Add new rule.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
