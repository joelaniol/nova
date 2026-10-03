# `nova.favorites_move`

> **Moves a bookmark favorite into a different folder or to the root collection.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Bookmark Management)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.favorites_move` reassigns the `folderId` parent of an existing bookmark favorite.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `id` | `string` | No | — | — | Stable favorite id (from nova.favorites_list). Targets exactly one entry. Preferred over url. |
| `url` | `string` | No | — | — | URL of the favorite to move (first match). Used when id is omitted. |
| `folderId` | `string` | No | — | — | Target folder id. Null or omitted = root. |
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_favorites_move",
  "arguments": {
    "favoriteId": "fav-5501",
    "folderId": "folder-102"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Moved favorite fav-5501 to folder-102."
    }
  ],
  "structuredContent": {
    "ok": true,
    "favoriteId": "fav-5501",
    "folderId": "folder-102"
  }
}
```

---

## 4. Operational Best Practices

* **Move to Root:** Pass `folderId: null` to move a bookmark to top-level.

---

## 5. Related Tools

* [`nova.favorites_list`](nova-favorites-list.md)
* [`nova.bookmarks_folders_list`](nova-bookmarks-folders-list.md)
