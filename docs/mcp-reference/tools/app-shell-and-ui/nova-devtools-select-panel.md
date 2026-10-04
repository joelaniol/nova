# `nova.devtools_select_panel`

> **Dispatches the keyboard shortcut for a DevTools panel (Console, Elements, Network, Sources, ...) in an already-open DevTools window.**

* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.devtools_select_panel` sends the panel's keyboard shortcut into an open DevTools window. The result distinguishes whether the shortcut was dispatched from whether the active panel selection was actually verified: without a panel readback, the call reports `ok: false` with `status: "shortcut_dispatched_unverified"` even when the shortcut went through, because Nova cannot confirm which panel ended up focused.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID or 'active'. |
| `panel` | `string` | Yes | — | `elements`, `console`, `sources`, `network`, `performance`, `memory`, `application`, `security`, `lighthouse`, `next`, `previous` | Canonical DevTools panel to activate. Use one of the enum values; alias spellings are not part of the discovery contract. |

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_devtools_select_panel",
  "arguments": {
    "targetId": "tab-1",
    "panel": "network"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "DevTools panel shortcut 'Ctrl+Shift+E' dispatched for tab-1; active panel selection is not verified."
    }
  ],
  "structuredContent": {
    "ok": false,
    "status": "shortcut_dispatched_unverified",
    "reasonCode": "devtools.panel_selection_unverified",
    "targetId": "tab-1",
    "panel": "network",
    "shortcut": "Ctrl+Shift+E",
    "shortcutDispatched": true,
    "selectionVerified": false,
    "openedDevTools": true
  }
}
```

---

## 4. Operational Best Practices

* **Treat `ok: false` as normal:** This tool dispatches a keyboard shortcut; it does not read back which panel ended up active. Check `shortcutDispatched` to confirm the input was sent.
* **Panel Selection:** Supported panels are `elements`, `console`, `sources`, `network`, `performance`, `memory`, `application`, `security`, `lighthouse`, plus `next`/`previous` to cycle.

---

## 5. Related Tools

* [`nova.devtools_open`](nova-devtools-open.md)
