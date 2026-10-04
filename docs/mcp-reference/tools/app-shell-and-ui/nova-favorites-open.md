# `nova.favorites_open`

> **Opens a saved favorite in the current or a new browser tab.**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.favorites_open` looks up a saved favorite by its URL and navigates to it. The URL must belong to a saved favorite; otherwise the tool returns `opened: false` ("Favorite not found.") and does not navigate. To open an arbitrary URL, use `nova.navigate`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `url` | `string` | Yes | — | — | Saved favorite URL to open. |
| `openInNewTab` | `boolean` | No | `false` | — | If true, open in a new browser tab instead of the current tab. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_favorites_open",
  "arguments": {
    "url": "https://docs.example.com/api",
    "openInNewTab": true
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Favorite opened."
    }
  ],
  "structuredContent": {
    "opened": true,
    "url": "https://docs.example.com/api",
    "openInNewTab": true
  }
}
```

---

## 4. Operational Best Practices

* **Parallel Browsing:** Use `openInNewTab: true` to preserve the current page.

---

## 5. Related Tools

* [`nova.favorites_list`](nova-favorites-list.md)
* [`nova.navigate`](../browser-automation/nova-navigate.md)
