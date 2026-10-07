# `nova.hardware_diagnostics_start`

Initiates in-page hardware diagnostic loop for camera, microphone, or audio speaker output.

---

## 1. Overview

`nova.hardware_diagnostics_start` starts an isolated hardware diagnostic probe inside the target page: a camera preview, a live microphone level/peak meter, or a speaker test tone, depending on `kind`.

Camera and microphone diagnostics drive the page over CDP, which carries no user gesture. If the origin does not already hold an Allow for that device (a stored permission or an active session grant), the browser's own gesture requirement blocks the request and the call fails — this is a deliberate guard, not a transient error, and retrying will not help. The speaker test needs no capture permission and is unaffected.

* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `kind` | `string` | Yes | — | `video`, `microphone`, `speaker` | Diagnostic channel to start. |

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "Hardware diagnostics started (microphone)."
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "ok": true,
    "status": "ok",
    "reasonCode": null,
    "reason": null,
    "kind": "microphone",
    "command": "start_mic",
    "diagnostics": {
      "ok": true,
      "action": "start_mic",
      "videoRunning": false,
      "microphoneRunning": true,
      "speakerRunning": false,
      "micLevel": 0,
      "micPeak": 0
    }
  }
}
```

---

## 4. Operational Best Practices

* **Permission Verification:** Test whether media devices are physically connected and accessible before running voice or video workflows — but only after the origin already holds an Allow for that device; otherwise expect the gesture-required failure described above.
* **Stop Diagnostics:** Always call [`nova.hardware_diagnostics_stop`](nova-hardware-diagnostics-stop.md) when testing is complete to free hardware devices.

---

## 5. Related Tools

* [`nova.hardware_diagnostics_state`](nova-hardware-diagnostics-state.md)
* [`nova.hardware_diagnostics_stop`](nova-hardware-diagnostics-stop.md)
