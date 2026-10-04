# `nova.fingerprint_set_global`

Sets the global browser fingerprint protection level across all sandboxes.

---

## 1. Overview

`nova.fingerprint_set_global` configures baseline fingerprint protection (`off`, `standard`, `strict`) across all sandboxes and tabs that do not specify overrides. `standard` enables canvas and audio noise; `strict` adds font, WebGL, hardware, and screen protections on top.

* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `level` | `string` | Yes | — | `off`, `standard`, `strict` | New global protection level. |

Capability bundle: `fingerprint_protection` (load it with `nova.tools_bundle(bundle='fingerprint_protection')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.fingerprint_set_global",
  "arguments": {
    "level": "standard"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Global fingerprint protection set to standard"
    }
  ],
  "structuredContent": {
    "globalLevel": "standard",
    "changed": true
  }
}
```

---

## 4. Operational Best Practices

* **Standard Recommended:** `standard` enables canvas and AudioContext noise without the additional WebGL/hardware/screen protections that `strict` adds, which are more likely to affect complex web applications.

---

## 5. Related Tools

* [`nova.fingerprint_get`](nova-fingerprint-get.md)
* [`nova.fingerprint_set_sandbox`](nova-fingerprint-set-sandbox.md)
