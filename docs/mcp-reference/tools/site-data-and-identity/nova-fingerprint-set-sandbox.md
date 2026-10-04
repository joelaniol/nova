# `nova.fingerprint_set_sandbox`

Sets or clears the per-sandbox fingerprint protection override.

---

## 1. Overview

`nova.fingerprint_set_sandbox` assigns a persistent fingerprint protection override to a specific sandbox profile. Pass `level: null` to revert to global defaults.

* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `sandboxId` | `string` | Yes | — | — | Sandbox letter id (e.g. 'A'). Must exist. |
| `level` | `string or null` | Yes | — | `off`, `standard`, `strict`, `null` | Override level, or null to clear the override. |

Capability bundle: `fingerprint_protection` (load it with `nova.tools_bundle(bundle='fingerprint_protection')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.fingerprint_set_sandbox",
  "arguments": {
    "sandboxId": "A",
    "level": "strict"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Sandbox 'A' fingerprint override set to strict"
    }
  ],
  "structuredContent": {
    "sandboxId": "A",
    "sandboxOverride": "strict",
    "changed": true
  }
}
```

---

## 4. Operational Best Practices

* **Stealth Sandboxes:** Give dedicated research sandboxes a `strict` override while keeping primary workspaces on `standard` or the global default.

---

## 5. Related Tools

* [`nova.fingerprint_get`](nova-fingerprint-get.md)
* [`nova.fingerprint_set_tab`](nova-fingerprint-set-tab.md)
