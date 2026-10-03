# `nova.tab_pin`

> **Pins or unpins a tab in the browser tab bar to prevent accidental closure.**

* **Capability Bundle:** `browser_automation`
* **Security Tier:** Tier 2 (Tab Strip Management)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.tab_pin` changes the pinned state of a tab, shrinking its tab strip footprint and protecting it against accidental bulk closure.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Calling agent's ID for attribution in logs. |
| `pinned` | `boolean` | **Yes** | true pins the tab, false unpins it. Required - there is no toggle and no default. |
| `targetId` | `string` | **Yes** | Browser tab ID to pin or unpin, or 'active'. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_tab_pin",
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
      "text": "Pinned tab-1."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "isPinned": true
  }
}
```

---

## 4. Operational Best Practices

* **Workflow Anchors:** Pin primary dashboard or reference tabs during complex multi-tab research.

---

## 5. Related Tools

* [`nova.tab_move`](nova-tab-move.md)
* [`nova.tab_close`](nova-tab-close.md)
