# `nova.media_transcribe_model_install`

Downloads a Whisper speech model or adopts an existing local GGML model file.

---

## 1. Overview

`nova.media_transcribe_model_install` acquires a speech recognition model for local offline transcription. It can download official Whisper GGML models directly from HuggingFace/GitHub mirrors or adopt an existing model file from disk.

* **Capability Bundle:** `system_tools`
* **Security Tier:** Tier 2 (Model Management)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`modelId`** | `string` | No | `null` | Catalog id to download: 'base', 'small' (recommended) or 'large-v3-turbo'. Mutually exclusive with path. |
| **`path`** | `string` | No | `null` | Absolute path of a ggml .bin model file to adopt. Requires 'Allow local files'. Mutually exclusive with modelId. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_transcribe_model_install",
  "arguments": {
    "modelId": "ggml-base"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Whisper model 'ggml-base' installed successfully (142 MB)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "modelId": "ggml-base",
    "fileName": "ggml-base.bin",
    "status": "installed",
    "sizeBytes": 147951456
  }
}
```

---

## 4. Operational Best Practices

* **One-Time Setup:** Models are installed into `%LOCALAPPDATA%\NovaBrowser\Models` and survive application updates.
* **Offline Resilience:** Once downloaded, transcription runs 100% offline with zero external network requests.

---

## 5. Related Tools

* [`nova.media_transcribe_models`](nova-media-transcribe-models.md)
* [`nova.media_transcribe_model_remove`](nova-media-transcribe-model-remove.md)
