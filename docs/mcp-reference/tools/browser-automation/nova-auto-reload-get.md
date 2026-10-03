# `nova.auto_reload_get`

> **Reads the native auto-reload configuration and countdown timer for the target tab.**

* **Security Tier:** Tier 1 (Read-Only State)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.auto_reload_get` inspects whether native periodic tab reloading is enabled, returning the configured reload interval in seconds and the remaining time until the next reload trigger.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | Yes | — | — | Required stable sandbox ID or browser-tab ID from nova.tabs. Active aliases are not accepted. |
| `agentId` | `string` | No | `"default"` | — | Optional agent identity. Reads may observe an unclaimed target but must match any existing claim. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_auto_reload_get",
  "arguments": {
    "targetId": "tab-1"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Auto-reload enabled: interval 60s, next reload in 34s."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "enabled": true,
    "intervalSeconds": 60,
    "remainingSeconds": 34
  }
}
```

---

## 4. Operational Best Practices

* **Monitoring Feeds:** Check auto-reload intervals before long polling loops to prevent unexpected reload disruption.

---

## 5. Related Tools

* [`nova.auto_reload_set`](nova-auto-reload-set.md)
* [`nova.reload`](nova-reload.md)
