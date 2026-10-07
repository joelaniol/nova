# `nova.sandbox_update`

Updates configuration, display name, color tag, or purpose of an existing sandbox.

---

## 1. Overview

`nova.sandbox_update` modifies metadata for a sandbox profile: display name, color tag, start URL, purpose/account/alias routing hints, and the `isPaused` flag. A paused sandbox is hidden from the tab strip and from agent-visible targets, but its profile data and settings are kept (pausing is not deletion).

* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation/README.md)

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
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.sandbox_update",
  "arguments": {
    "sandboxId": "C",
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
      "text": "Sandbox 'C' updated."
    }
  ],
  "structuredContent": {
    "sandboxId": "C",
    "name": "Client Staging V2",
    "status": "updated",
    "updatedFields": [
      "name",
      "color"
    ]
  }
}
```

This response has no `ok` field. Calling with no recognized fields set returns `status: "unchanged"` and an empty `updatedFields` instead of an error.

---

## 4. Operational Best Practices

* **Routing Hints:** Update `preferredFor` keywords so [`nova.resolve_sandbox`](nova-resolve-sandbox.md) accurately matches new workflow intents.

---

## 5. Related Tools

* [`nova.sandbox_context`](nova-sandbox-context.md)
* [`nova.sandbox_create`](nova-sandbox-create.md)
