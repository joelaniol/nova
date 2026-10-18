# `nova.ui_open_menu`

> **Opens one of Nova's own menus and lists its entries, so they can be pressed like a click.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_open_menu` opens a menu of Nova's window the way a click on it would:

| `menu` | Menu |
| :--- | :--- |
| `main` | The ⋯ menu (History, zoom, print, settings, ...) |
| `back` / `forward` | The active tab's history in that direction, with site icons; the back menu ends with *Show full history* |
| `reload` | Reload, hard reload, auto-reload |
| `tab` | The right-click menu of the tab given as `targetId` |

The answer lists the entries in `inAppMenu`. Press one with [`nova.ui_confirm_native_dialog(button='<entry>')`](nova-ui-confirm-native-dialog.md) — a submenu entry such as *History* opens its submenu. [`nova.ui_inspect_native_dialog`](nova-ui-inspect-native-dialog.md) reads what is open now, [`nova.ui_dismiss_native_dialog`](nova-ui-dismiss-native-dialog.md) closes it.

What a pressed entry does counts as the agent's action: a tab closed this way appears under *Recently closed* as closed by an agent.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `menu` | `string` | Yes | — | `main`, `back`, `forward`, `reload`, `tab` | Which menu: 'main', 'back', 'forward', 'reload' or 'tab' (needs targetId). |
| `targetId` | `string` | No | — | — | Browser tab id from nova.tabs whose tab menu to open. Only with menu='tab'. |

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_open_menu",
  "arguments": { "menu": "back" }
}
```

### JSON-RPC Response
```json
{
  "structuredContent": {
    "ok": true,
    "status": "opened",
    "menu": "back",
    "inAppMenu": {
      "kind": "menu",
      "buttons": [
        { "name": "Example Domain", "enabled": true, "role": "item" },
        { "name": "Show full history", "enabled": true, "role": "item" }
      ]
    },
    "pressWith": "nova.ui_confirm_native_dialog(button='<name>')",
    "closeWith": "nova.ui_dismiss_native_dialog"
  }
}
```

When there is nothing to show — a `back` menu on a tab without earlier pages — the answer is `ok: false`, `status: "not_opened"`, `reasonCode: "menu.nothing_to_show"`.

---

## 4. Related Tools

* [`nova.ui_confirm_native_dialog`](nova-ui-confirm-native-dialog.md)
* [`nova.ui_inspect_native_dialog`](nova-ui-inspect-native-dialog.md)
* [`nova.history_get`](../browser-automation/nova-history-get.md)
