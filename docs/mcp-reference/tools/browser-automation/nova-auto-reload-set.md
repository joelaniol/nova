# `nova.auto_reload_set`

> **Configures native periodic reloading for a tab with a specified interval in seconds.**

* **Security Tier:** Tier 2 (Navigation Control)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.auto_reload_set` starts or stops native browser tab refresh cycles. Useful for dashboard monitoring and live status tracking without writing custom setTimeout loops.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | Yes | — | — | Required stable sandbox ID or browser-tab ID from nova.tabs. The same agentId must already hold an explicit claim; active aliases and auto-claim are not accepted. |
| `mode` | `string` | Yes | — | `running`, `paused`, `off` | Desired state. running starts or resumes, paused preserves the interval without reloading, and off removes the session schedule. |
| `intervalSeconds` | `integer` | No | — | 30–86400 | Reload interval in seconds (30-86400). Required to create mode=running; optional when resuming an existing schedule; forbidden for paused/off. |
| `expectedRevision` | `integer` | Yes | — | 0–2147483647 | Optimistic-concurrency revision from nova.auto_reload_get (0-2147483647). Use 0 only when no schedule exists. |
| `clientRequestId` | `string` | Yes | — | 1–128 characters | Caller-generated idempotency key scoped to this agent and target. Retrying identical arguments is safe; reuse with different arguments for the same target conflicts. |
| `agentId` | `string` | No | `"default"` | — | Agent identity that already owns the explicit target claim. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_auto_reload_set",
  "arguments": {
    "targetId": "tab-1",
    "intervalSeconds": 120,
    "enabled": true
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Configured auto-reload for tab-1 every 120 seconds."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "enabled": true,
    "intervalSeconds": 120
  }
}
```

---

## 4. Operational Best Practices

* **Preserve Form Data:** Do not enable auto-reload on tabs containing unsubmitted forms.
* **Turn Off When Done:** Explicitly call with `enabled: false` upon workflow completion.

---

## 5. Related Tools

* [`nova.auto_reload_get`](nova-auto-reload-get.md)
* [`nova.reload`](nova-reload.md)
