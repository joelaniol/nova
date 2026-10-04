# `nova.permission_prompt`

> **Asks the Nova operator to approve or deny an action that an agent wants to run.**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.permission_prompt` is the approval hook for agent clients such as Claude Code: the client calls it with the name of the tool it wants to run and a description, and Nova shows an approval request to the operator. The call returns when the operator decides or the configured approval timeout expires; a timeout counts as not approved. Low-risk requests can be covered by a persistent grant the operator saved earlier; medium- and high-risk requests are asked every time.

`behavior` is `allow` or `deny`. On a denial or timeout, `updatedInput` carries guidance for the agent: continue without the action, or (after a timeout) ask the operator to confirm and retry.

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
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_permission_prompt",
  "arguments": {
    "tool_name": "Bash",
    "description": "Run 'npm test'",
    "risk_level": "low"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Permission allowed for: Bash"
    }
  ],
  "structuredContent": {
    "schemaVersion": 1,
    "behavior": "allow",
    "reasonCode": null,
    "updatedInput": null
  }
}
```

---

## 4. Operational Best Practices

* **Clear Description:** Write `description` so the operator can decide without further context (what runs, on which files or hosts).
* **Honest risk level:** Only `low` requests can be satisfied by a saved persistent grant.
* **Respect a denial:** On `deny`, do not retry the same action through another tool; follow `updatedInput`.

---

## 5. Related Tools

* [`nova.ui_permission_prompt_resolve`](nova-ui-permission-prompt-resolve.md)
