# `nova.hardware_diagnostics_start`

Initiates in-page hardware diagnostic loop for camera, microphone, or audio speaker output.

---

## 1. Overview

`nova.hardware_diagnostics_start` starts an isolated hardware diagnostic probe inside the target page. It verifies device permissions, captures live audio levels, measures peak decibels, and renders diagnostic canvases for camera input.

* **Capability Bundle:** `system_tools`
* **Security Tier:** Tier 2 (Hardware Diagnostics)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`kind`** | `string` | Yes | `null` | Diagnostic channel to start. |
| **`targetId`** | `string` | No | `"active"` | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.hardware_diagnostics_start",
  "arguments": {
    "kind": "microphone",
    "targetId": "tab-1"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Started microphone hardware diagnostics on tab-1."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "kind": "microphone",
    "active": true
  }
}
```

---

## 4. Operational Best Practices

* **Permission Verification:** Test whether media devices are physically connected and accessible before running voice or video workflows.
* **Stop Diagnostics:** Always call [`nova.hardware_diagnostics_stop`](nova-hardware-diagnostics-stop.md) when testing is complete to free hardware devices.

---

## 5. Related Tools

* [`nova.hardware_diagnostics_state`](nova-hardware-diagnostics-state.md)
* [`nova.hardware_diagnostics_stop`](nova-hardware-diagnostics-stop.md)
