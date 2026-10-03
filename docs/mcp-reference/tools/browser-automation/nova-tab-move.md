# `nova.tab_move`

> **Reorders a tab position within the browser tab strip by index.**

* **Capability Bundle:** `browser_automation`
* **Security Tier:** Tier 2 (Tab Strip Management)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.tab_move` repositions an open tab within the visual tab strip.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Calling agent's ID for attribution in logs. |
| `insertAfter` | `boolean` | No | true places the moved tab to the right of targetTabId, false to its left. |
| `targetId` | `string` | **Yes** | Browser tab ID to move, or 'active'. |
| `targetTabId` | `string` | **Yes** | Browser tab ID to move it next to (must be a different tab in the same sandbox). 'active' is accepted. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_tab_move",
  "arguments": {
    "targetId": "tab-2",
    "newIndex": 0
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Moved tab-2 to index 0."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-2",
    "index": 0
  }
}
```

---

## 4. Operational Best Practices

* **Tab Strip Hygiene:** Pin or move critical monitoring tabs to the front of the strip.

---

## 5. Related Tools

* [`nova.tab_pin`](nova-tab-pin.md)
* [`nova.tabs`](nova-tabs.md)
