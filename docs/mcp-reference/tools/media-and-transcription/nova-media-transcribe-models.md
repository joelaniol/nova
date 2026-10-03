# `nova.media_transcribe_models`

Lists known Whisper speech models, installation statuses, and machine CPU/AVX2 capabilities.

---

## 1. Overview

`nova.media_transcribe_models` queries Nova's local speech model catalog. It details installed GGML models (e.g. `ggml-base.bin`, `ggml-small.bin`), sizes, supported languages, and reports hardware acceleration capabilities (AVX2, AVX512, NEON) on the host machine.

* **Capability Bundle:** `system_tools`
* **Security Tier:** Tier 1 (Read-Only Model Catalog)
* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| *(none)* | — | — | — | No parameters accepted. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_transcribe_models",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Machine has AVX2 support. 1 Whisper model installed: ggml-base.bin (142 MB)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "avx2Supported": true,
    "installedModels": [
      {
        "modelId": "ggml-base",
        "fileName": "ggml-base.bin",
        "sizeBytes": 147951456,
        "isInstalled": true,
        "default": true
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Hardware Check:** Verify `avx2Supported` to confirm optimal local CPU transcription performance.
* **Install Missing Models:** Use [`nova.media_transcribe_model_install`](nova-media-transcribe-model-install.md) if required models are not yet installed.

---

## 5. Related Tools

* [`nova.media_transcribe_model_install`](nova-media-transcribe-model-install.md)
* [`nova.media_transcribe_start`](nova-media-transcribe-start.md)
