# `nova.fingerprint_set_global`

Sets the global browser fingerprint protection level across all sandboxes.

---

## 1. Overview

`nova.fingerprint_set_global` configures baseline fingerprint protection (`Off`, `Balanced`, `Strict`) across all sandboxes and tabs that do not specify overrides. Persisted in `settings.json`.

* **Capability Bundle:** `site_data_management`
* **Security Tier:** Tier 2 (Global Privacy Configuration)
* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`level`** | `string` | Yes | `null` | New global protection level. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.fingerprint_set_global",
  "arguments": {
    "level": "Balanced"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Set global fingerprint protection level to Balanced."
    }
  ],
  "structuredContent": {
    "ok": true,
    "globalLevel": "Balanced"
  }
}
```

---

## 4. Operational Best Practices

* **Balanced Recommended:** `Balanced` provides Canvas, AudioContext, and WebGL noise without breaking complex web applications.

---

## 5. Related Tools

* [`nova.fingerprint_get`](nova-fingerprint-get.md)
* [`nova.fingerprint_set_sandbox`](nova-fingerprint-set-sandbox.md)
