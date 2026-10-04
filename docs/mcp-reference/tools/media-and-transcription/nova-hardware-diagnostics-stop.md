# `nova.hardware_diagnostics_stop`

Stops in-page hardware diagnostics and releases active camera, microphone, or speaker handles.

---

## 1. Overview

`nova.hardware_diagnostics_stop` halts ongoing hardware diagnostic loops and disposes of in-page media streams and WebAudio analyzers.

* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `kind` | `string` | No | `"all"` | `video`, `microphone`, `speaker`, `all` | Diagnostic channel to stop. |
| `reason` | `string` | No | — | — | Optional stop reason for diagnostics state tracking. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
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
      "text": "Hardware diagnostics stopped (microphone)."
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "ok": true,
    "status": "ok",
    "reasonCode": null,
    "kind": "microphone",
    "command": "stop_mic",
    "reason": "tool_stop",
    "diagnostics": { "ok": true, "action": "stop_mic", "reason": "tool_stop" }
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
