# `nova.emulation_clear_media`

Clears all emulated CSS media features, reverting to host system theme and display settings.

---

## 1. Overview

`nova.emulation_clear_media` resets all emulated media features (`colorScheme`, `reducedMotion`, `forcedColors`, `contrast`, `media`), returning the tab to real OS defaults.

* **Capability Bundle:** `device_emulation`
* **Security Tier:** Tier 2 (CSS Emulation Reset)
* **Core Architecture Guide:** [Fingerprint & Identity Systems](../../../core-features/fingerprint-and-identity.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`targetId`** | `string` | No | `"active"` | Target tab ID. |
| **`agentId`** | `string` | No | `"default"` | Optional agent identifier. |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.emulation_clear_media",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Emulated media features cleared."
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "cleared": true
  }
}
```

---

## 4. Operational Best Practices

* **State Cleanup:** Always clear emulated media after completing visual regression audits.

---

## See Also

* [`nova.emulation_set_media`](nova-emulation-set-media.md) - Set emulated CSS media.
* [Device Emulation Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
