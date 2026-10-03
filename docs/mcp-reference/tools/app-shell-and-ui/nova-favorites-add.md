# `nova.favorites_add`

> **Adds a URL to the browser favorites collection with optional title and target folder.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Bookmark Management)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.favorites_add` persists a URL as a bookmark. If title is omitted, the current page title is resolved automatically.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `url` | `string` | Yes | — | — | Absolute URL (http/https). If scheme is missing, https:// is assumed. |
| `title` | `string` | No | — | — | Optional custom title. |
| `folderId` | `string` | No | — | — | Optional bookmark folder id (see nova.bookmarks_folders_list). New favorites with null/omitted folderId land at root; existing favorites keep their current folder when folderId is null/omitted. Use nova.favorites_move to move to root explicitly. |
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_favorites_add",
  "arguments": {
    "url": "https://docs.example.com/api",
    "title": "Example API Reference",
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
      "text": "Added favorite 'Example API Reference' (fav-5501)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "favoriteId": "fav-5501",
    "url": "https://docs.example.com/api",
    "title": "Example API Reference",
    "folderId": "folder-101"
  }
}
```

---

## 4. Operational Best Practices

* **Deduplication:** Repeated calls with identical URLs update the existing favorite instead of duplicating.

---

## 5. Related Tools

* [`nova.favorites_list`](nova-favorites-list.md)
* [`nova.favorites_remove`](nova-favorites-remove.md)
* [`nova.favorites_open`](nova-favorites-open.md)
