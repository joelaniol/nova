# `nova.media_transcribe_models`

Lists known Whisper speech models, installation statuses, and machine CPU/AVX2 capabilities.

---

## 1. Overview

`nova.media_transcribe_models` queries Nova's local speech model catalog. It lists every known ggml model (bundled, installed, available to download, user-supplied, or damaged) with size and tier, reports whether the CPU supports the AVX2/FMA instructions transcription requires, whether local file access is enabled (audio is read from disk, so this gates every run too), which model a run would use right now, and GPU information. Transcription itself always runs on CPU today — the GPU block is detection only (`inUse` is always `false`).

* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
      "text": "1 of 3 speech model(s) ready. A run right now would use: ggml-base-q5_1."
    }
  ],
  "structuredContent": {
    "modelsDirectory": "C:\\Users\\<user>\\AppData\\Local\\nova-cognitive\\Nova\\Models\\whisper",
    "cpuSupported": true,
    "localFileAccessEnabled": true,
    "chosenModelId": null,
    "effectiveModel": "ggml-base-q5_1",
    "graphics": {
      "accelerationUsable": true,
      "adapterName": "Example GPU",
      "videoMemory": "8 GB",
      "vulkanLoaderPresent": true,
      "reasonCode": null,
      "restartRequired": false,
      "inUse": false
    },
    "models": [
      { "id": "base", "fileName": "ggml-base-q5_1.bin", "state": "bundled", "size": "57 MB", "sizeBytes": 59707625, "tier": "baseline", "path": "C:\\Users\\<user>\\AppData\\Local\\nova-cognitive\\Nova\\Models\\whisper\\ggml-base-q5_1.bin" },
      { "id": "small", "fileName": "ggml-small-q5_1.bin", "state": "available", "size": "181 MB", "sizeBytes": 190085487, "tier": "recommended", "path": null },
      { "id": "large-v3-turbo", "fileName": "ggml-large-v3-turbo-q5_0.bin", "state": "available", "size": "547 MB", "sizeBytes": 574041195, "tier": "highaccuracy", "path": null }
    ]
  }
}
```

If the CPU lacks AVX2/FMA, `cpuSupported` is `false` and no model can run. If `localFileAccessEnabled` is `false`, every model shows as present but [`nova.media_transcribe_start`](nova-media-transcribe-start.md) still refuses, because audio is read from local disk.

---

## 4. Operational Best Practices

* **Hardware Check:** Verify `cpuSupported` to confirm local transcription can run at all on this machine; `graphics.inUse` is always `false` today, so GPU presence does not change performance yet.
* **Install Missing Models:** Use [`nova.media_transcribe_model_install`](nova-media-transcribe-model-install.md) if a wanted model is not `installed`/`bundled` yet.

---

## 5. Related Tools

* [`nova.media_transcribe_model_install`](nova-media-transcribe-model-install.md)
* [`nova.media_transcribe_start`](nova-media-transcribe-start.md)
