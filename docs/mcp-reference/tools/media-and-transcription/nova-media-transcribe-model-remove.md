# `nova.media_transcribe_model_remove`

Deletes an installed speech model file to reclaim disk space or prepare for re-download.

---

## 1. Overview

`nova.media_transcribe_model_remove` removes a GGML model file from local storage. Useful for freeing disk space or removing corrupted model downloads.

* **Capability Bundle:** `system_tools`
* **Security Tier:** Tier 2 (Model Management)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`fileName`** | `string` | Yes | `null` | File name as reported by nova.media_transcribe_models, e.g. 'ggml-small-q5_1.bin'. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_transcribe_model_remove",
  "arguments": {
    "fileName": "ggml-large-v3.bin"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Deleted speech model file ggml-large-v3.bin."
    }
  ],
  "structuredContent": {
    "ok": true,
    "fileName": "ggml-large-v3.bin",
    "status": "removed"
  }
}
```

---

## 4. Operational Best Practices

* **Damaged File Recovery:** If a model fails verification or crashes during initialization, remove it and re-install with `media_transcribe_model_install`.

---

## 5. Related Tools

* [`nova.media_transcribe_model_install`](nova-media-transcribe-model-install.md)
* [`nova.media_transcribe_models`](nova-media-transcribe-models.md)
