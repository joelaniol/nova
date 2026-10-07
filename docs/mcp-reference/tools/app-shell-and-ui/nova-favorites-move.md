# `nova.favorites_move`

> **Moves a bookmark favorite into a different folder or to the root collection.**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.favorites_move` moves an existing favorite into another bookmark folder or back to the top level. Address the favorite by its stable `id` (preferred, from `nova.favorites_list`) or by `url` (first match). Omitting `folderId` or passing `null` moves it to the top level. An unknown favorite returns `moved: false` ("Favorite not found.").

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `id` | `string` | No | — | — | Stable favorite id (from nova.favorites_list). Targets exactly one entry. Preferred over url. |
| `url` | `string` | No | — | — | URL of the favorite to move (first match). Used when id is omitted. |
| `folderId` | `string` | No | — | — | Target folder id. Null or omitted = root. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_favorites_move",
  "arguments": {
    "id": "8d0c4b6e2f1a4c7e9b3d5a1f6e2c8b40",
    "folderId": "3f2a9c1e7b4d4e0f9a6b2c8d1e5f7a90"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Favorite moved."
    }
  ],
  "structuredContent": {
    "moved": true,
    "id": "8d0c4b6e2f1a4c7e9b3d5a1f6e2c8b40",
    "folderId": "3f2a9c1e7b4d4e0f9a6b2c8d1e5f7a90"
  }
}
```

When the call uses `url` instead of `id`, `structuredContent` carries `url` in place of `id`.

---

## 4. Operational Best Practices

* **Move to Root:** Pass `folderId: null` (or omit it) to move a favorite to the top level.
* **Prefer the id:** `url` moves only the first match; use `id` when the same URL is saved in several folders.

---

## 5. Related Tools

* [`nova.favorites_list`](nova-favorites-list.md)
* [`nova.bookmarks_folders_list`](nova-bookmarks-folders-list.md)
