# `nova.devtools_select_panel`

> **Focuses a specific panel within an open DevTools window (Console, Elements, Network, Sources).**

* **Security Tier:** Tier 2 (Developer Tooling)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.devtools_select_panel` navigates the DevTools interface to a designated tab panel to streamline visual inspections.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID or 'active'. |
| `panel` | `string` | Yes | — | `elements`, `console`, `sources`, `network`, `performance`, `memory`, `application`, `security`, `lighthouse`, `next`, `previous` | Canonical DevTools panel to activate. Use one of the enum values; alias spellings are not part of the discovery contract. |

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
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
      "text": "Selected Network panel in DevTools for tab-1."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "panel": "network"
  }
}
```

---

## 4. Operational Best Practices

* **Panel Selection:** Supported panels include `elements`, `console`, `network`, `sources`, and `application`.

---

## 5. Related Tools

* [`nova.devtools_open`](nova-devtools-open.md)
