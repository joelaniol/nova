# `nova.fingerprint_set_sandbox`

Sets or clears the per-sandbox fingerprint protection override.

---

## 1. Overview

`nova.fingerprint_set_sandbox` assigns a persistent fingerprint protection override to a specific sandbox profile. Pass `level: null` to revert to global defaults.

* **Capability Bundle:** `site_data_management`
* **Security Tier:** Tier 2 (Sandbox Configuration)
* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`level`** | `string,null` | Yes | `null` | Override level, or null to clear the override. |
| **`sandboxId`** | `string` | Yes | `null` | Sandbox letter id (e.g. 'A'). Must exist. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.fingerprint_set_sandbox",
  "arguments": {
    "sandboxId": "sb-research",
    "level": "Strict"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Set fingerprint protection override on sandbox sb-research to Strict."
    }
  ],
  "structuredContent": {
    "ok": true,
    "sandboxId": "sb-research",
    "overrideLevel": "Strict"
  }
}
```

---

## 4. Operational Best Practices

* **Stealth Sandboxes:** Create dedicated research sandboxes with `Strict` protection while keeping primary workspaces on `Balanced`.

---

## 5. Related Tools

* [`nova.fingerprint_get`](nova-fingerprint-get.md)
* [`nova.fingerprint_set_tab`](nova-fingerprint-set-tab.md)
