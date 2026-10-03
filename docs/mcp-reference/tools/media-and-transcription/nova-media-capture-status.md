# `nova.media_capture_status`

Reports progress, elapsed time, and bytes written for an active in-tab media capture.

---

## 1. Overview

`nova.media_capture_status` monitors an ongoing streaming capture, reporting elapsed recording time, bytes written per track, and buffer health.

* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID of the capturing tab, or 'active' / 'activeBrowserTab'. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_capture_status",
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
      "text": "Capture on tab-1: 15.2s elapsed (240 KB written)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "status": "recording",
    "elapsedSeconds": 15.2,
    "bytesWritten": 245760
  }
}
```

---

## 4. Operational Best Practices

* **Paced Polling:** Poll periodically to verify that audio chunks are actively arriving from the page.

---

## 5. Related Tools

* [`nova.media_capture_start`](nova-media-capture-start.md)
* [`nova.media_capture_stop`](nova-media-capture-stop.md)
