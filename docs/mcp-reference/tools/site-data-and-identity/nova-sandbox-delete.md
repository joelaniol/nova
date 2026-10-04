# `nova.sandbox_delete`

Permanently removes a sandbox profile and deletes its storage, cookies, and cache.

---

## 1. Overview

`nova.sandbox_delete` removes a sandbox profile's settings entry and its disk anchor, and schedules its browser data directory for cleanup; all tabs belonging to the sandbox are closed. At least one sandbox must always remain — the call is rejected if it would delete the last one.

* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `sandboxId` | `string` | Yes | — | — | Sandbox ID to delete (e.g. 'C'). |
| `confirm` | `boolean` | Yes | — | — | Safety confirmation. Must be true to proceed with deletion. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.sandbox_delete",
  "arguments": {
    "sandboxId": "C",
    "confirm": true
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Sandbox 'C' deleted."
    }
  ],
  "structuredContent": {
    "sandboxId": "C",
    "status": "deleted"
  }
}
```

This response has no `ok` field.

---

## 4. Operational Best Practices

* **Confirmation Required:** Requires explicit `confirm: true` to prevent accidental deletion of authenticated browser sessions.

---

## 5. Related Tools

* [`nova.sandbox_create`](nova-sandbox-create.md)
* [`nova.sandbox_context`](nova-sandbox-context.md)
