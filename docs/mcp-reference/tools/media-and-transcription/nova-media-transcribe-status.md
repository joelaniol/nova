# `nova.media_transcribe_status`

Reports progress, elapsed percentage, and recognized text segments of an active transcription.

---

## 1. Overview

`nova.media_transcribe_status` inspects a running or completed transcription job. It reports the job's stage (`converting`/`loading_model`/`recognizing`), seconds of audio covered so far, a progress ratio once the audio length is known, and — with `includeText: true` — the recognized segments and full text with timestamps.

* **Core Architecture Guide:** [Media Intelligence & Speech Transcription](../../../core-features/media-intelligence/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `jobId` | `string` | Yes | — | — | Job ID returned by nova.media_transcribe_start. |
| `includeText` | `boolean` | No | `false` | — | Include the segments and the full text in the response. Off by default because a long transcript crowds out everything else; the file at transcriptPath holds the same content. |

The tool also accepts the optional `_meta` object for call metadata, such as `_meta.intent` (a short reason for the call).

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.media_transcribe_status",
  "arguments": {
    "jobId": "job-tx-1092",
    "includeText": true
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Transcription tr_a1b2c3d4e5f6 completed: 1 segment(s), 24.3s of audio, written to C:\\Users\\<user>\\AppData\\Local\\nova-cognitive\\Nova\\Exports\\Transcripts\\tr_a1b2c3d4e5f6.txt."
    }
  ],
  "structuredContent": {
    "jobId": "tr_a1b2c3d4e5f6",
    "state": "completed",
    "model": "ggml-base-q5_1",
    "device": "cpu",
    "audioPath": "downloads/captured-stream.wav",
    "stage": "recognizing",
    "stageProgress": 1,
    "segmentCount": 1,
    "coveredSeconds": 24.3,
    "audioSeconds": 24.3,
    "audioSecondsMeasured": true,
    "progressRatio": 1,
    "budgetMs": 60000,
    "budgetModelLoadMs": 10000,
    "budgetRecognitionMs": 50000,
    "budgetStallMs": 15000,
    "elapsedMs": 4210,
    "truncated": false,
    "transcriptPath": "C:\\Users\\<user>\\AppData\\Local\\nova-cognitive\\Nova\\Exports\\Transcripts\\tr_a1b2c3d4e5f6.txt",
    "accuracyNote": "Machine transcript from model 'ggml-base-q5_1'. Do not take numbers, amounts, proper nouns or technical terms as verified, and treat a passage that does not add up as a transcription error rather than an odd statement.",
    "segments": [
      { "start": 0, "end": 24.3, "text": "Hello, this is a test recording confirming that speech to text works completely offline." }
    ],
    "text": "Hello, this is a test recording confirming that speech to text works completely offline."
  }
}
```

`segments`/`text` are only present when `includeText: true`. While `state` is `queued` or `running`, the response also carries `suggestedPollMs` (2000). `reasonCode`/`message` appear only on a `failed` job.

---

## 4. Operational Best Practices

* **Incremental Polling:** Set `includeText: false` while polling to save tokens until `state` is `completed`, then request `includeText: true` to receive the final transcript. Always read `accuracyNote` alongside any text — it is a machine transcript, not a verified one.

---

## 5. Related Tools

* [`nova.media_transcribe_start`](nova-media-transcribe-start.md)
* [`nova.media_transcribe_stop`](nova-media-transcribe-stop.md)
