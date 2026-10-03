# `nova.tab_snapshot`

> **Captures a full tab state snapshot including URL, scroll position, and form state.**

* **Security Tier:** Tier 1 (Read-Only Session State)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.tab_snapshot` records active browsing state for session preservation or migration across sandboxes.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetIds` | `array` of `string` | Yes | — | 1–8 items | Array of target IDs from nova.tabs. Supports sandbox and browser tab IDs. Max 8 targets per call. The singular targetId spelling used by every other tab tool is accepted and wrapped into a one-element batch. |
| `includeText` | `boolean` | No | `false` | — | If true, include a text snippet (innerText) for each tab. |
| `maxCharsPerTab` | `integer` | No | `2000` | 100–50000 | Maximum characters of text content per tab (only when includeText=true). |
| `includeOkFacts` | `boolean` | No | `false` | — | Reserved OK (Operational Knowledge) facts projection. Omit or pass false; current runtimes reject true instead of silently ignoring it. |

Capability bundles: `browser_automation`, `page_read_debug`.
<!-- /generated:parameters -->

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
