# `nova.tab_snapshot`

> **Captures a full tab state snapshot including URL, scroll position, and form state.**

* **Capability Bundle:** `browser_automation`
* **Security Tier:** Tier 1 (Read-Only Session State)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.tab_snapshot` records active browsing state for session preservation or migration across sandboxes.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `includeOkFacts` | `boolean` | No | Reserved OK (Operational Knowledge) facts projection. Omit or pass false; current runtimes reject true instead of silently ignoring it. |
| `includeText` | `boolean` | No | If true, include a text snippet (innerText) for each tab. |
| `maxCharsPerTab` | `integer` | No | Maximum characters of text content per tab (only when includeText=true). |
| `targetIds` | `array` | **Yes** | Array of target IDs from nova.tabs. Supports sandbox and browser tab IDs. Max 8 targets per call. The singular targetId spelling used by every other tab tool is accepted and wrapped into a one-element batch. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_tab_snapshot",
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
      "text": "Snapshot captured for tab-1."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "url": "https://app.example.com/editor",
    "scroll": {
      "x": 0,
      "y": 450
    },
    "title": "Project Editor"
  }
}
```

---

## 4. Operational Best Practices

* **Session Checkpointing:** Take snapshots prior to navigating away to allow exact state restoration later.

---

## 5. Related Tools

* [`nova.tab_transfer`](nova-tab-transfer.md)
