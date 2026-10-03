# `nova.sandbox_update`

Updates configuration, display name, color tag, or purpose of an existing sandbox.

---

## 1. Overview

`nova.sandbox_update` modifies metadata for a sandbox profile. It can update display names, color tags, preferred routing keywords, or pause/resume background scheduling for the container.

* **Security Tier:** Tier 2 (Sandbox Mutation)
* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `sandboxId` | `string` | Yes | — | — | Sandbox ID to update (e.g. 'A', 'B', 'C'). |
| `name` | `string` | No | — | — | New display name. |
| `color` | `string` | No | — | — | New hex color (e.g. '#f472b6'). |
| `startUrl` | `string or null` | No | — | — | New default URL. Pass null to clear. |
| `purpose` | `string or null` | No | — | — | New purpose hint. Pass null to clear. |
| `accountLabel` | `string or null` | No | — | — | New account label. Pass null to clear. |
| `aliases` | `array or null` | No | — | — | New aliases. Pass null to clear. |
| `preferredFor` | `array or null` | No | — | — | New preferred intent keys. Pass null to clear. |
| `isPaused` | `boolean` | No | — | — | Pause (true) or unpause (false) the sandbox. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.sandbox_update",
  "arguments": {
    "sandboxId": "sb-c819a",
    "name": "Client Staging V2",
    "color": "#008080"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Updated sandbox sb-c819a: name='Client Staging V2'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "sandboxId": "sb-c819a",
    "updatedFields": [
      "name",
      "color"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Routing Hints:** Update `preferredFor` keywords so [`nova.resolve_sandbox`](nova-resolve-sandbox.md) accurately matches new workflow intents.

---

## 5. Related Tools

* [`nova.sandbox_context`](nova-sandbox-context.md)
* [`nova.sandbox_create`](nova-sandbox-create.md)
