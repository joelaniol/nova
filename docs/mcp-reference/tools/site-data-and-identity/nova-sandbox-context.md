# `nova.sandbox_context`

Returns detailed identity, cookie jar bounds, and context metadata for a specific sandbox.

---

## 1. Overview

`nova.sandbox_context` returns raw profile metadata for a sandbox container: directory paths, assigned color tags, purpose declarations, preferred URL patterns, and active tab counts.

* **Capability Bundle:** `site_data_management`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`targetId`** | `string` | Yes | `null` | Sandbox target ID from nova.tabs (e.g. 'A', 'B'). |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.sandbox_context",
  "arguments": {
    "targetId": "sb-work-01"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Loaded context for sandbox sb-work-01: Work Profile (color: #0078D4)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "sandboxId": "sb-work-01",
    "name": "Work",
    "purpose": "Corporate SSO and Internal Tools",
    "color": "#0078D4",
    "openTabsCount": 3
  }
}
```

---

## 4. Operational Best Practices

* **Profile Verification:** Verify sandbox context before executing operations that require specific corporate credentials.

---

## 5. Related Tools

* [`nova.resolve_sandbox`](nova-resolve-sandbox.md)
* [`nova.sandbox_update`](nova-sandbox-update.md)
