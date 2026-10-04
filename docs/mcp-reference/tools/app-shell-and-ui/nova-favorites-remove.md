# `nova.favorites_remove`

> **Removes a saved favorite by its id or URL.**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.favorites_remove` deletes a saved favorite. Pass the stable `id` from `nova.favorites_list` to remove exactly one entry, or `url` to remove the first favorite with that URL. An unknown favorite returns `removed: false` ("Favorite not found.").

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `id` | `string` | No | — | — | Stable favorite id (from nova.favorites_list). Targets exactly one entry. Preferred over url. |
| `url` | `string` | No | — | — | URL to remove (first match). Used when id is omitted. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_favorites_remove",
  "arguments": {
    "id": "8d0c4b6e2f1a4c7e9b3d5a1f6e2c8b40"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Favorite removed."
    }
  ],
  "structuredContent": {
    "removed": true,
    "id": "8d0c4b6e2f1a4c7e9b3d5a1f6e2c8b40"
  }
}
```

When the call uses `url` instead of `id`, `structuredContent` carries `url` in place of `id`.

---

## 4. Operational Best Practices

* **Verify ID:** Take the exact `id` from `nova.favorites_list` before deleting.

---

## 5. Related Tools

* [`nova.favorites_list`](nova-favorites-list.md)
* [`nova.favorites_add`](nova-favorites-add.md)
