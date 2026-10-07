# `nova.network_intercept_clear`

Disarms network interception rules: by rule ID, by tab ID, or globally across the entire browser.

---

## 1. Overview

`nova.network_intercept_clear` removes active network interception rules. Called with no arguments, it acts as an emergency stop disarming every interception rule across all tabs.

* **Core Architecture Guide:** [Proxy Routing & Network Engine](../../../core-features/proxy-and-network/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | — | — | Clear only this tab's rules. |
| `ruleId` | `string` | No | — | — | Clear only this rule. Reports intercept_rule_not_found when it already ended on its own. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.network_intercept_clear",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Removed 2 interception rule(s) (all)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "scope": "all",
    "targetId": null,
    "ruleId": null,
    "removedCount": 2,
    "targetExists": true,
    "removed": [
      { "ruleId": "ir_8f12a4b0", "targetId": "tab-1", "urlPattern": "*api/checkout/payment*", "action": "respondWith", "summary": "*api/checkout/payment* answered with HTTP 500", "hits": 0, "maxHits": 1, "applied": 0, "failed": 0, "lastError": null, "expiresAtUtc": "2026-10-04T12:05:30.0000000Z", "remainingMs": 24500, "note": null }
    ],
    "reasonCode": null,
    "message": null,
    "anyActiveAnywhere": false
  }
}
```
The `removed` array is shortened here to one entry; a real response lists every rule that was taken down.

---

## 4. Operational Best Practices

* **Emergency Stop:** Run `nova.network_intercept_clear()` without arguments if automated tests fail unexpectedly to restore normal network traffic.

---

## See Also

* [`nova.network_intercept_add`](nova-network-intercept-add.md) - Add interception rule.
* [`nova.network_intercept_list`](nova-network-intercept-list.md) - List active rules.
* [Proxy Routing Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
