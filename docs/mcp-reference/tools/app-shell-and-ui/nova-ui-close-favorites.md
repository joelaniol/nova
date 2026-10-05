# `nova.ui_close_favorites`

> **Closes the favorites panel if one is open.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_close_favorites` closes any open favorites panel: the one opened with `nova.ui_open_favorites`, a bookmark bar folder panel or "Search favorites..." from the main menu that the user opened. It reports whether something was open.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_close_favorites",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Favorites panel closed."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "closed"
  }
}
```

`status` is `closed` when a panel was open and `not_open` when there was nothing to close.

---

## 4. Related Tools

* [`nova.ui_open_favorites`](nova-ui-open-favorites.md)
