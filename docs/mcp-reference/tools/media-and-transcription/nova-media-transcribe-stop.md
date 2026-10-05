# `nova.media_transcribe_stop`

Stops an in-flight transcription job and returns recognized text segments up to the cancellation point.

---

## 1. Overview

`nova.media_transcribe_stop` cancels an active transcription job. It always returns with the recognized segments and text included (equivalent to `nova.media_transcribe_status` with `includeText: true`), keeping whatever was already recognized rather than discarding it.

* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `jobId` | `string` | Yes | — | — | Job ID returned by nova.media_transcribe_start. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_transcribe_stop",
  "arguments": {
    "jobId": "job-tx-1092"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Transcription tr_a1b2c3d4e5f6 was canceled after 3 segment(s); the partial transcript is kept."
    }
  ],
  "structuredContent": {
    "jobId": "tr_a1b2c3d4e5f6",
    "state": "canceled",
    "model": "ggml-base-q5_1",
    "device": "cpu",
    "audioPath": "downloads/captured-stream.wav",
    "stage": "recognizing",
    "stageProgress": 0.4,
    "segmentCount": 3,
    "coveredSeconds": 9.6,
    "audioSeconds": 24.3,
    "audioSecondsMeasured": true,
    "progressRatio": 0.395,
    "budgetMs": 60000,
    "budgetModelLoadMs": 10000,
    "budgetRecognitionMs": 50000,
    "budgetStallMs": 15000,
    "elapsedMs": 3100,
    "truncated": false,
    "transcriptPath": "C:\\Users\\<user>\\AppData\\Local\\nova-cognitive\\Nova\\Exports\\Transcripts\\tr_a1b2c3d4e5f6.txt",
    "accuracyNote": "Machine transcript from model 'ggml-base-q5_1'. Do not take numbers, amounts, proper nouns or technical terms as verified, and treat a passage that does not add up as a transcription error rather than an odd statement.",
    "segments": [
      { "start": 0, "end": 9.6, "text": "Hello, this is a test recording" }
    ],
    "text": "Hello, this is a test recording"
  }
}
```

---

## 4. Operational Best Practices

* **Partial Text Preservation:** Useful when a long recording is taking too long and partial early results are sufficient — the transcript written to `transcriptPath` also holds only the recognized part.

---

## 5. Related Tools

* [`nova.media_transcribe_start`](nova-media-transcribe-start.md)
* [`nova.media_transcribe_status`](nova-media-transcribe-status.md)
