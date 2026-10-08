# `nova.auto_reload_set`

> **Configures native periodic reloading for a tab with a specified interval in seconds.**

* **Related Tool Group:** [Browser Navigation & Automation](README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.auto_reload_set` starts, pauses or removes Nova's own reload schedule for one tab (`mode`: `running`, `paused`, `off`). The schedule lives only for the current session. Useful for dashboard monitoring and live status tracking without writing custom setTimeout loops.

The call needs an explicit claim on `targetId`, the current `expectedRevision` from `nova.auto_reload_get` (0 when no schedule exists) and a `clientRequestId`; retrying identical arguments is safe. A stale revision returns `status: "conflict"` with `reasonCode: "auto_reload.revision_conflict"`. If Auto-Reload is turned off in Nova's settings, the call returns `status: "blocked"` with `reasonCode: "auto_reload.feature_disabled"`.

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
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_auto_reload_set",
  "arguments": {
    "targetId": "tab-1",
    "mode": "running",
    "intervalSeconds": 120,
    "expectedRevision": 0,
    "clientRequestId": "dashboard-reload-1"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Auto-Reload created for tab-1 (revision 1)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "created",
    "changed": true,
    "previousRevision": 0,
    "clientRequestId": "dashboard-reload-1",
    "state": {
      "ok": true,
      "status": "updated",
      "targetId": "tab-1",
      "targetExists": true,
      "featureEnabled": true,
      "mode": "running",
      "intervalSeconds": 120,
      "revision": 1,
      "previousRevision": 0,
      "nextRunAtUtc": "2026-10-03T09:02:00.0000000+00:00",
      "lastOutcome": "scheduled",
      "configuredBy": "agent",
      "boundUrl": "https://status.example.com/"
    }
  }
}
```

---

## 4. Operational Best Practices

* **Preserve Form Data:** Do not enable auto-reload on tabs containing unsubmitted forms.
* **Turn Off When Done:** Call with `mode: "off"` (and the current revision) upon workflow completion.

---

## 5. Related Tools

* [`nova.auto_reload_get`](nova-auto-reload-get.md)
* [`nova.reload`](nova-reload.md)
