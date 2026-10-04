# `nova.media_transcribe_start`

Transcribes local audio or video files into text entirely on-device using local Whisper.cpp.

---

## 1. Overview

`nova.media_transcribe_start` converts spoken audio from local files into structured text. Transcription runs locally inside the sandboxed Outrider process via whisper.cpp with SIMD acceleration. No audio ever leaves the user's computer.

* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `path` | `string` | Yes | — | — | Absolute path of the audio or video file to transcribe. |
| `language` | `string` | No | — | — | Spoken language as an ISO code, e.g. 'de' or 'en'. Omit to detect it, which costs roughly 18% more time and is less reliable on short clips. |
| `model` | `string` | No | — | — | Substring of the model file name to prefer, e.g. 'small'. Omit to use the most accurate model installed. |
| `waitMs` | `integer` | No | `0` | 0–30000 | Wait up to this many milliseconds for the job to finish before returning, so a short recording needs only this one call. On timeout the jobId is returned and the job keeps running. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_transcribe_start",
  "arguments": {
    "path": "downloads/captured-stream.wav",
    "model": "base"
  }
}
```

Language is omitted here to let Nova detect it — passing a code like `"de"` skips detection and is faster.

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Transcription tr_a1b2c3d4e5f6 is queued for the single run slot. Poll nova.media_transcribe_status."
    }
  ],
  "structuredContent": {
    "jobId": "tr_a1b2c3d4e5f6",
    "state": "queued",
    "model": "ggml-base-q5_1",
    "device": "cpu",
    "audioPath": "downloads/captured-stream.wav",
    "stage": null,
    "stageProgress": null,
    "segmentCount": 0,
    "coveredSeconds": 0,
    "audioSeconds": 24.3,
    "audioSecondsMeasured": true,
    "progressRatio": 0,
    "budgetMs": 60000,
    "budgetModelLoadMs": 10000,
    "budgetRecognitionMs": 50000,
    "budgetStallMs": 15000,
    "elapsedMs": 5,
    "truncated": false,
    "transcriptPath": null,
    "accuracyNote": "Machine transcript from model 'ggml-base-q5_1'. Do not take numbers, amounts, proper nouns or technical terms as verified, and treat a passage that does not add up as a transcription error rather than an odd statement.",
    "suggestedPollMs": 2000
  }
}
```

Only one transcription runs at a time; a second call while one is active comes back `queued` until the run slot frees up. Every field is read from the job's real state rather than defaulted — exact budget numbers depend on the audio length and model.

---

## 4. Operational Best Practices

* **Privacy Guarantees:** 100% on-device processing guarantees confidentiality for internal meetings, voicemails, and private recordings.
* **Asynchronous Processing:** Returns immediately with a `jobId`; use [`nova.media_transcribe_status`](nova-media-transcribe-status.md) to poll for transcribed text segments, at the interval in `suggestedPollMs`.

---

## 5. Related Tools

* [`nova.media_transcribe_status`](nova-media-transcribe-status.md)
* [`nova.media_transcribe_stop`](nova-media-transcribe-stop.md)
* [`nova.media_file_info`](nova-media-file-info.md)
