# `nova.fingerprint_set_tab`

Sets an ephemeral per-tab fingerprint protection override that expires on tab close.

---

## 1. Overview

`nova.fingerprint_set_tab` sets a temporary, in-memory fingerprint protection level for a single browser tab. The override does not touch disk settings and automatically disappears when the tab closes.

* **Capability Bundle:** `site_data_management`
* **Security Tier:** Tier 2 (Ephemeral Override)
* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `tabId` | `string` | Yes | — | — | Existing browser tab id (8-char hex). Sandbox ids are rejected. |
| `level` | `string or null` | Yes | — | `off`, `standard`, `strict`, `null` | Override level, or null to clear the override. |
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.fingerprint_set_tab",
  "arguments": {
    "tabId": "tab-1",
    "level": "Off"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Set ephemeral fingerprint protection on tab-1 to Off."
    }
  ],
  "structuredContent": {
    "ok": true,
    "tabId": "tab-1",
    "overrideLevel": "Off",
    "ephemeral": true
  }
}
```

---

## 4. Operational Best Practices

* **Compatibility Recovery:** Temporarily disable fingerprinting (`Off`) if a specialized legacy web application fails under Canvas or WebGL noise.

---

## 5. Related Tools

* [`nova.fingerprint_get`](nova-fingerprint-get.md)
* [`nova.fingerprint_set_sandbox`](nova-fingerprint-set-sandbox.md)
