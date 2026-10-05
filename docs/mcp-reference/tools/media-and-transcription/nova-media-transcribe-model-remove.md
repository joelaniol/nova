# `nova.media_transcribe_model_remove`

Deletes an installed speech model file to reclaim disk space or prepare for re-download.

---

## 1. Overview

`nova.media_transcribe_model_remove` removes a GGML model file from local storage. Useful for freeing disk space or removing corrupted model downloads.

* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `fileName` | `string` | Yes | — | — | File name as reported by nova.media_transcribe_models, e.g. 'ggml-small-q5_1.bin'. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_transcribe_model_remove",
  "arguments": {
    "fileName": "ggml-large-v3-turbo-q5_0.bin"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Removed speech model 'ggml-large-v3-turbo-q5_0.bin'."
    }
  ],
  "structuredContent": {
    "removed": true,
    "fileName": "ggml-large-v3-turbo-q5_0.bin",
    "reasonCode": null,
    "modelsDirectory": "C:\\Users\\<user>\\AppData\\Local\\nova-cognitive\\Nova\\Models\\whisper"
  }
}
```

When no file by that name exists, the response is `{ "removed": false, "fileName": "...", "reasonCode": "not_found", "modelsDirectory": "..." }` rather than an error — this is also the result when a model file is removed twice.

---

## 4. Operational Best Practices

* **Damaged File Recovery:** If a model fails verification or crashes during initialization, remove it and re-install with `media_transcribe_model_install`.

---

## 5. Related Tools

* [`nova.media_transcribe_model_install`](nova-media-transcribe-model-install.md)
* [`nova.media_transcribe_models`](nova-media-transcribe-models.md)
