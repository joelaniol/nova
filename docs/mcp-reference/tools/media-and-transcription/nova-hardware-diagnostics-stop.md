# `nova.hardware_diagnostics_stop`

Stops in-page hardware diagnostics and releases active camera, microphone, or speaker handles.

---

## 1. Overview

`nova.hardware_diagnostics_stop` halts ongoing hardware diagnostic loops and disposes of in-page media streams and WebAudio analyzers.

* **Capability Bundle:** `system_tools`
* **Security Tier:** Tier 2 (Diagnostics Lifecycle)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `kind` | `string` | No | `"all"` | `video`, `microphone`, `speaker`, `all` | Diagnostic channel to stop. |
| `reason` | `string` | No | — | — | Optional stop reason for diagnostics state tracking. |
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.hardware_diagnostics_stop",
  "arguments": {
    "targetId": "tab-1",
    "kind": "microphone"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Stopped microphone diagnostics on tab-1."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "stoppedChannels": [
      "microphone"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Clean Shutdown:** Stopping diagnostics ensures OS camera/mic privacy indicators turn off immediately.

---

## 5. Related Tools

* [`nova.hardware_diagnostics_start`](nova-hardware-diagnostics-start.md)
* [`nova.media_stop_all`](nova-media-stop-all.md)
