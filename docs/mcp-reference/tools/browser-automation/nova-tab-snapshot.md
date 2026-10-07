# `nova.tab_snapshot`

> **Reads URL, title, load state and optional text from up to 8 tabs in one call.**

* **Core Feature Guide:** [Input Dispatch & Shadow DOM Traversal](../../../core-features/humanized-input-engine/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.tab_snapshot` reads URL, title and `readyState` (plus an optional text snippet) from up to 8 tabs in one read-only call, without claiming them. Useful for price comparison, multi-source research and data consolidation. A tab that cannot be read gets `ok: false` with an `error` entry; the other tabs still return. An unknown target ID fails the whole call.

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
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_tab_snapshot",
  "arguments": {
    "targetIds": [
      "tab-1",
      "tab-2"
    ],
    "includeText": true,
    "maxCharsPerTab": 200
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "[{\"targetId\":\"tab-1\",\"ok\":true,\"url\":\"https://shop-a.example.com/item/42\",\"title\":\"Item 42 - Shop A\",\"readyState\":\"complete\",\"textSnippet\":\"Item 42\\nPrice: 19.99 EUR\\nIn stock\",\"textTruncated\":false,\"textChars\":33},{\"targetId\":\"tab-2\",\"ok\":true,\"url\":\"https://shop-b.example.com/p/42\",\"title\":\"Item 42 - Shop B\",\"readyState\":\"complete\",\"textSnippet\":\"Item 42\\nPrice: 18.49 EUR\\nShips in 3 days\",\"textTruncated\":false,\"textChars\":40}]"
    }
  ],
  "structuredContent": {
    "tabCount": 2,
    "includeText": true,
    "tabs": [
      {
        "targetId": "tab-1",
        "ok": true,
        "url": "https://shop-a.example.com/item/42",
        "title": "Item 42 - Shop A",
        "readyState": "complete",
        "textSnippet": "Item 42\nPrice: 19.99 EUR\nIn stock",
        "textTruncated": false,
        "textChars": 33
      },
      {
        "targetId": "tab-2",
        "ok": true,
        "url": "https://shop-b.example.com/p/42",
        "title": "Item 42 - Shop B",
        "readyState": "complete",
        "textSnippet": "Item 42\nPrice: 18.49 EUR\nShips in 3 days",
        "textTruncated": false,
        "textChars": 40
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Batch Reads:** Read several tabs in one call instead of claiming and reading them one after another.
* **Text Budget:** Keep `includeText` off when URL and title are enough; with text on, `maxCharsPerTab` caps each snippet and `textTruncated` shows whether it was cut.

---

## 5. Related Tools

* [`nova.tab_transfer`](nova-tab-transfer.md)
