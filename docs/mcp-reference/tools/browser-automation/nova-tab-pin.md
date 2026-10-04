# `nova.tab_pin`

> **Pins or unpins a tab in the browser tab bar to prevent accidental closure.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.tab_pin` changes the pinned state of a tab, shrinking its tab strip footprint and protecting it against accidental bulk closure.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | Yes | `"active"` | — | Browser tab ID to pin or unpin, or 'active'. |
| `pinned` | `boolean` | Yes | — | — | true pins the tab, false unpins it. Required - there is no toggle and no default. |
| `agentId` | `string` | No | — | — | Calling agent's ID for attribution in logs. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.tab_pin",
  "arguments": {
    "targetId": "tab-1",
    "pinned": true
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Tab 'tab-1' is now pinned."
    }
  ],
  "structuredContent": {
    "requested": { "targetId": "tab-1", "pinned": true },
    "targetId": "tab-1",
    "ok": true,
    "status": "ok",
    "message": "Tab 'tab-1' is now pinned.",
    "changed": true,
    "pinned": true,
    "outcome": "Changed",
    "sandboxTabOrder": ["tab-1", "tab-2"]
  }
}
```
A repeated call with the same `pinned` value is not an error: it returns `status: "noop"`, `reasonCode: "tab.pin_unchanged"`, `changed: false`, and the already-current `pinned` state.

---

## 4. Operational Best Practices

* **Workflow Anchors:** Pin primary dashboard or reference tabs during complex multi-tab research.

---

## 5. Related Tools

* [`nova.tab_move`](nova-tab-move.md)
* [`nova.tab_close`](nova-tab-close.md)
