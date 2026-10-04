# `nova.tab_move`

> **Moves a tab next to another tab in the same sandbox's tab strip.**

* **Core Feature Guide:** [Input Dispatch & Shadow DOM Traversal](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.tab_move` repositions an open tab within the visual tab strip. The position is named by a neighbour, not an index: the tab lands directly after (`insertAfter: true`, default) or before `targetTabId`. Both tabs must be browser tabs in the same sandbox. `sandboxTabOrder` is the order read back after the move.

If the tab already sits there, `status` is `noop` with `reasonCode: "tab.move_unchanged"`. A move across the boundary between pinned and unpinned tabs is refused with `tab.move_pin_boundary`; tabs in different sandboxes with `tab.move_cross_sandbox`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | Yes | `"active"` | — | Browser tab ID to move, or 'active'. |
| `targetTabId` | `string` | Yes | — | — | Browser tab ID to move it next to (must be a different tab in the same sandbox). 'active' is accepted. |
| `insertAfter` | `boolean` | No | `true` | — | true places the moved tab to the right of targetTabId, false to its left. |
| `agentId` | `string` | No | — | — | Calling agent's ID for attribution in logs. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_tab_move",
  "arguments": {
    "targetId": "tab-3",
    "targetTabId": "tab-1",
    "insertAfter": false
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Moved tab 'tab-3' before 'tab-1'."
    }
  ],
  "structuredContent": {
    "requested": {
      "targetId": "tab-3",
      "targetTabId": "tab-1",
      "insertAfter": false
    },
    "targetId": "tab-3",
    "targetTabId": "tab-1",
    "ok": true,
    "status": "ok",
    "message": "Moved tab 'tab-3' before 'tab-1'.",
    "retryable": false,
    "moved": true,
    "outcome": "Moved",
    "sandboxTabOrder": [
      "tab-3",
      "tab-1",
      "tab-2"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Tab Strip Hygiene:** Pin or move critical monitoring tabs to the front of the strip; to move a tab to the front, name the current first tab as `targetTabId` with `insertAfter: false`.

---

## 5. Related Tools

* [`nova.tab_pin`](nova-tab-pin.md)
* [`nova.tabs`](nova-tabs.md)
