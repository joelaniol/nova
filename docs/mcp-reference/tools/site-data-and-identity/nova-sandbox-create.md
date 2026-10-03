# `nova.sandbox_create`

Creates a new isolated sandbox profile with dedicated storage, cookies, and cache.

---

## 1. Overview

`nova.sandbox_create` provisions a new isolated browser profile container. Each sandbox maintains its own distinct CoreWebView2 profile directory, pristine cookie jar, and isolated localStorage, preventing cross-profile tracking and account collisions.

* **Capability Bundle:** `site_data_management`
* **Security Tier:** Tier 2 (Sandbox Provisioning)
* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`accountLabel`** | `string` | No | `null` | Account label for routing disambiguation (e.g. 'Work', 'Personal'). |
| **`aliases`** | `array` | No | `null` | Alternative names for the sandbox (used in resolve_sandbox matching). |
| **`color`** | `string` | No | `null` | Hex color (e.g. '#34d399'). Auto-assigned from palette if omitted. |
| **`name`** | `string` | No | `null` | Display name. Auto-generated if omitted (e.g. 'Sandbox C'). |
| **`preferredFor`** | `array` | No | `null` | Intent keys this sandbox prefers (e.g. 'email.compose', 'chat.ask'). |
| **`purpose`** | `string` | No | `null` | Purpose hint for intent-based routing (e.g. 'email', 'chat', 'project', 'code', 'docs'). |
| **`startUrl`** | `string` | No | `null` | Default URL to open when the sandbox has no remembered last URL. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.sandbox_create",
  "arguments": {
    "name": "Client Staging",
    "purpose": "Testing client portal logins",
    "color": "#107C41",
    "startUrl": "https://staging.example.com"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Created sandbox 'Client Staging' (id: sb-c819a)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "sandboxId": "sb-c819a",
    "name": "Client Staging",
    "color": "#107C41",
    "purpose": "Testing client portal logins"
  }
}
```

---

## 4. Operational Best Practices

* **Account Multi-Tenancy:** Create dedicated sandboxes for separate accounts (e.g. Personal vs Work vs Admin) on the same web application.
* **Visual Indicators:** Assign distinct colors to sandboxes to help human operators visually differentiate tab strips in the WinUI host.

---

## 5. Related Tools

* [`nova.sandbox_update`](nova-sandbox-update.md)
* [`nova.sandbox_delete`](nova-sandbox-delete.md)
* [`nova.sandbox_context`](nova-sandbox-context.md)
