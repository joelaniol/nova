# `nova.sandbox_create`

Creates a new isolated sandbox profile with dedicated storage, cookies, and cache.

---

## 1. Overview

`nova.sandbox_create` provisions a new isolated browser profile container. Each sandbox maintains its own distinct CoreWebView2 profile directory, pristine cookie jar, and isolated localStorage, preventing cross-profile tracking and account collisions. The new sandbox gets the next free single-letter id (e.g. `C`); at most 100 sandboxes can exist at once.

* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `name` | `string` | No | — | — | Display name. Auto-generated if omitted (e.g. 'Sandbox C'). |
| `color` | `string` | No | — | — | Hex color (e.g. '#34d399'). Auto-assigned from palette if omitted. |
| `startUrl` | `string` | No | — | — | Default URL to open when the sandbox has no remembered last URL. |
| `purpose` | `string` | No | — | — | Purpose hint for intent-based routing (e.g. 'email', 'chat', 'project', 'code', 'docs'). |
| `accountLabel` | `string` | No | — | — | Account label for routing disambiguation (e.g. 'Work', 'Personal'). |
| `aliases` | `array` of `string` | No | — | — | Alternative names for the sandbox (used in resolve_sandbox matching). |
| `preferredFor` | `array` of `string` | No | — | — | Intent keys this sandbox prefers (e.g. 'email.compose', 'chat.ask'). |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "Sandbox 'C' created."
    }
  ],
  "structuredContent": {
    "sandboxId": "C",
    "name": "Client Staging",
    "color": "#107C41",
    "status": "created"
  }
}
```

This response has no `ok` field; `purpose`, `startUrl`, `accountLabel`, `aliases`, and `preferredFor` are saved but not echoed back — read them with [`nova.sandbox_context`](nova-sandbox-context.md).

---

## 4. Operational Best Practices

* **Account Multi-Tenancy:** Create dedicated sandboxes for separate accounts (e.g. Personal vs Work vs Admin) on the same web application.
* **Visual Indicators:** Assign distinct colors to sandboxes to help human operators visually differentiate tab strips in the WinUI host.

---

## 5. Related Tools

* [`nova.sandbox_update`](nova-sandbox-update.md)
* [`nova.sandbox_delete`](nova-sandbox-delete.md)
* [`nova.sandbox_context`](nova-sandbox-context.md)
