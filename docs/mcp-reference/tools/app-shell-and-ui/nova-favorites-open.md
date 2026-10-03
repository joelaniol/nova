# `nova.favorites_open`

> **Navigates to a stored favorite bookmark in the current or a new browser tab.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Navigation)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.favorites_open` resolves a bookmark URL by its ID and performs navigation, avoiding manual URL copying.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `openInNewTab` | `boolean` | No | If true, open in a new browser tab instead of the current tab. |
| `url` | `string` | **Yes** | Saved favorite URL to open. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_favorites_open",
  "arguments": {
    "favoriteId": "fav-5501",
    "newTab": true
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Opened favorite fav-5501 in new tab tab-4."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-4",
    "url": "https://docs.example.com/api"
  }
}
```

---

## 4. Operational Best Practices

* **Parallel Browsing:** Use `newTab: true` to preserve current page context.

---

## 5. Related Tools

* [`nova.favorites_list`](nova-favorites-list.md)
* [`nova.navigate`](../browser-automation/nova-navigate.md)
