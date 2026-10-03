# `nova.hardware_diagnostics_state`

Returns current live hardware diagnostic metrics including microphone audio levels and peak decibels.

---

## 1. Overview

`nova.hardware_diagnostics_state` polls live measurements from an active diagnostic channel on a tab. It reports running channels, real-time microphone input volume (0.0 - 1.0), and peak decibels.

* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |

Capability bundles: `browser_automation`, `page_read_debug`.
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
      "text": "Microphone diagnostics running: current level 0.42, peak 0.85."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "activeChannels": [
      "microphone"
    ],
    "micLevel": 0.42,
    "micPeak": 0.85
  }
}
```

---

## 4. Operational Best Practices

* **Silence Detection:** Check whether `micLevel` remains 0.0 to diagnose muted microphones or incorrect hardware input selections.

---

## 5. Related Tools

* [`nova.hardware_diagnostics_start`](nova-hardware-diagnostics-start.md)
* [`nova.hardware_diagnostics_stop`](nova-hardware-diagnostics-stop.md)
