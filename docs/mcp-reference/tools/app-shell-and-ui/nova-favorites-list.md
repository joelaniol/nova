# `nova.favorites_list`

> **Lists saved browser favorites, optionally filtered by bookmark folder.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.favorites_list` returns stored bookmarks including IDs, URLs, titles, folder IDs, and creation timestamps.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_favorites_list",
  "arguments": {
    "folderId": "folder-101"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Found 3 favorites in folder-101."
    }
  ],
  "structuredContent": {
    "ok": true,
    "favorites": [
      {
        "favoriteId": "fav-5501",
        "title": "Example API",
        "url": "https://docs.example.com/api"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Index Browsing:** Query all bookmarks by passing `folderId: null`.

---

## 5. Related Tools

* [`nova.favorites_add`](nova-favorites-add.md)
* [`nova.favorites_open`](nova-favorites-open.md)
