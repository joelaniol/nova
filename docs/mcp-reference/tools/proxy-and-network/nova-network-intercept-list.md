# `nova.network_intercept_list`

Lists currently armed network interception rules with remaining hit budgets and expiration timers.

---

## 1. Overview

`nova.network_intercept_list` inspects which interception rules are currently active. Rules that have expired via TTL or hit budgets are automatically omitted.

* **Security Tier:** Tier 1 (Safe)
* **Core Architecture Guide:** [Proxy Routing & Stealth Network Engine](../../../core-features/proxy-and-network.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | — | — | Restrict to one tab. Omit to list every rule in the browser. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
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
      "text": "1 active network interception rule(s)."
    }
  ],
  "structuredContent": {
    "count": 1,
    "rules": [
      {
        "ruleId": "rule-8f12a4b0",
        "targetId": "tab-1",
        "urlPattern": "*api/checkout/payment*",
        "action": "respondWith",
        "status": 500,
        "hitsUsed": 0,
        "maxHits": 1,
        "expiresInMs": 24500
      }
    ]
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
