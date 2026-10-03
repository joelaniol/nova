# `nova.devtools_select_panel`

> **Focuses a specific panel within an open DevTools window (Console, Elements, Network, Sources).**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Developer Tooling)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.devtools_select_panel` navigates the DevTools interface to a designated tab panel to streamline visual inspections.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `panel` | `string` | **Yes** | Canonical DevTools panel to activate. Use one of the enum values; alias spellings are not part of the discovery contract. |
| `targetId` | `string` | No | Target ID or 'active'. |

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
