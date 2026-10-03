# `nova.permission_prompt`

> **Raises an interactive permission dialog asking the Nova human operator to approve a high-risk action.**

* **Security Tier:** Tier 2 (Interactive Authorization Gate)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.permission_prompt` displays an explicit authorization prompt in the Nova UI. The calling agent is blocked until the operator accepts or rejects the action.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `schemaVersion` | `integer` | No | — | 1–1 | Optional request schema version. Current supported value is 1. |
| `tool_name` | `string` | Yes | — | — | The name of the tool that requires approval (e.g. 'Bash', 'Write'). |
| `description` | `string` | Yes | — | — | Human-readable description of what the tool will do (e.g. "Run 'npm test'"). |
| `risk_level` | `string` | No | — | `low`, `medium`, `high` | Estimated risk level of the action. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_permission_prompt",
  "arguments": {
    "action": "delete_production_database",
    "reason": "User requested reset of staging test data."
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Operator approved the action."
    }
  ],
  "structuredContent": {
    "ok": true,
    "approved": true,
    "operatorComment": "Confirmed staging only."
  }
}
```

---

## 4. Operational Best Practices

* **Clear Justification:** Provide an unambiguous `reason` string to give the human operator complete context.
* **Timeout Handling:** Handle potential operator rejection or dismissal gracefully.

---

## 5. Related Tools

* [`nova.ui_permission_prompt_resolve`](nova-ui-permission-prompt-resolve.md)
