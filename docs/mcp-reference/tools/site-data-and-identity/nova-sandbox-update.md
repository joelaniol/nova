# `nova.sandbox_update`

Updates configuration, display name, color tag, or purpose of an existing sandbox.

---

## 1. Overview

`nova.sandbox_update` modifies metadata for a sandbox profile. It can update display names, color tags, preferred routing keywords, or pause/resume background scheduling for the container.

* **Capability Bundle:** `site_data_management`
* **Security Tier:** Tier 2 (Sandbox Mutation)
* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`accountLabel`** | `string,null` | No | `null` | New account label. Pass null to clear. |
| **`aliases`** | `array,null` | No | `null` | New aliases. Pass null to clear. |
| **`color`** | `string` | No | `null` | New hex color (e.g. '#f472b6'). |
| **`isPaused`** | `boolean` | No | `null` | Pause (true) or unpause (false) the sandbox. |
| **`name`** | `string` | No | `null` | New display name. |
| **`preferredFor`** | `array,null` | No | `null` | New preferred intent keys. Pass null to clear. |
| **`purpose`** | `string,null` | No | `null` | New purpose hint. Pass null to clear. |
| **`sandboxId`** | `string` | Yes | `null` | Sandbox ID to update (e.g. 'A', 'B', 'C'). |
| **`startUrl`** | `string,null` | No | `null` | New default URL. Pass null to clear. |

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
