# `nova.media_transcribe_model_remove`

Deletes an installed speech model file to reclaim disk space or prepare for re-download.

---

## 1. Overview

`nova.media_transcribe_model_remove` removes a GGML model file from local storage. Useful for freeing disk space or removing corrupted model downloads.

* **Security Tier:** Tier 2 (Model Management)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `fileName` | `string` | Yes | — | — | File name as reported by nova.media_transcribe_models, e.g. 'ggml-small-q5_1.bin'. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
<!-- /generated:parameters -->

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
