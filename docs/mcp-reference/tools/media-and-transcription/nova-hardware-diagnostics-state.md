# `nova.hardware_diagnostics_state`

Returns current live hardware diagnostic metrics including microphone audio levels and peak decibels.

---

## 1. Overview

`nova.hardware_diagnostics_state` polls live measurements from an active diagnostic channel on a tab. It reports whether video/microphone/speaker channels are currently running and a real-time microphone level on a 0-100 scale (`micLevel`, with `micPeak` decaying slowly from the highest level seen).

* **Core Architecture Guide:** [Media Devices & Permissions](../../../core-features/media-intelligence/devices-and-permissions/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |

Capability bundles: `browser_automation`, `page_read_debug`.
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.hardware_diagnostics_state",
  "arguments": {
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
      "text": "Hardware diagnostics state: video=False, mic=True, speaker=False, micLevel=0, micPeak=0."
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "ok": true,
    "status": "ok",
    "reasonCode": null,
    "videoRunning": false,
    "microphoneRunning": true,
    "speakerRunning": false,
    "micLevel": 0,
    "micPeak": 0,
    "diagnostics": { "ok": true, "action": "get_state" }
  }
}
```

---

## 4. Operational Best Practices

* **Silence Detection:** Check whether `micLevel` stays at 0 to diagnose muted microphones or incorrect hardware input selections.

---

## 5. Related Tools

* [`nova.hardware_diagnostics_start`](nova-hardware-diagnostics-start.md)
* [`nova.hardware_diagnostics_stop`](nova-hardware-diagnostics-stop.md)
