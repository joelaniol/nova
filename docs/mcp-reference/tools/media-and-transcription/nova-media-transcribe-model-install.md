# `nova.media_transcribe_model_install`

Downloads a Whisper speech model or adopts an existing local GGML model file.

---

## 1. Overview

`nova.media_transcribe_model_install` acquires a speech recognition model for local offline transcription. It can download one of the three catalog models (`base`, `small`, `large-v3-turbo`) from Hugging Face with a pinned checksum, or adopt an existing ggml `.bin` file from disk (unverified against any checksum).

* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `modelId` | `string` | No | — | — | Catalog id to download: 'base', 'small' (recommended) or 'large-v3-turbo'. Mutually exclusive with path. |
| `path` | `string` | No | — | — | Absolute path of a ggml .bin model file to adopt. Requires 'Allow local files'. Mutually exclusive with modelId. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_transcribe_model_install",
  "arguments": {
    "modelId": "small"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Speech model 'ggml-small-q5_1.bin' downloaded (181 MB)."
    }
  ],
  "structuredContent": {
    "action": "downloaded",
    "id": "small",
    "fileName": "ggml-small-q5_1.bin",
    "state": "installed",
    "size": "181 MB",
    "path": "C:\\Users\\<user>\\AppData\\Local\\nova-cognitive\\Nova\\Models\\whisper\\ggml-small-q5_1.bin",
    "verified": true
  }
}
```

A download that fails the pinned checksum, or an adopted file that is not a ggml model, is rejected with `reasonCode: "model_invalid"` rather than installed.

---

## 4. Operational Best Practices

* **One-Time Setup:** Models are installed into `%LOCALAPPDATA%\nova-cognitive\Nova\Models\whisper` and survive application updates. The `base` model ships with the installer and is already present without a download.
* **Offline Resilience:** Once downloaded, transcription runs 100% offline with zero external network requests.

---

## 5. Related Tools

* [`nova.media_transcribe_models`](nova-media-transcribe-models.md)
* [`nova.media_transcribe_model_remove`](nova-media-transcribe-model-remove.md)
