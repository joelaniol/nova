# `nova.auto_reload_get`

> **Reads the native auto-reload configuration and countdown timer for the target tab.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.auto_reload_get` inspects the native periodic-reload coordinator for a tab, returning its mode (`running`, `paused`, `off`), the configured interval in seconds, and the absolute UTC timestamp of the next scheduled reload.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | Yes | — | — | Required stable sandbox ID or browser-tab ID from nova.tabs. Active aliases are not accepted. |
| `agentId` | `string` | No | `"default"` | — | Optional agent identity. Reads may observe an unclaimed target but must match any existing claim. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
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
      "text": "Auto-Reload running for tab-1 (revision 2)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "lastReasonCode": null,
    "targetId": "tab-1",
    "targetExists": true,
    "featureEnabled": true,
    "mode": "running",
    "intervalSeconds": 60,
    "revision": 2,
    "previousRevision": 1,
    "nextRunAtUtc": "2026-10-03T12:01:00Z",
    "lastOutcome": "scheduled",
    "configuredBy": "agent",
    "boundUrl": "https://example.com/dashboard"
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
