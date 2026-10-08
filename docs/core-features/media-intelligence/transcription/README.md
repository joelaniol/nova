# Speech Transcription

To transcribe a file yourself, open **Transcribe audio or video** from Nova's toolbar and drop in the file. The result can be saved as text or subtitles. An agent can start a local transcription job, inspect progress and retrieve timestamped segments through the tools below.

## Local recognition and models

Speech recognition runs on this computer; the audio is never uploaded. Only downloading a model needs the network.

* **Outrider process isolation:** whisper.cpp is native code, and a crash there must not take the browser down. Decoding and recognition run inside `NovaBrowser.Outrider.exe` ([Outrider Process Boundary](../../outrider-boundary/README.md)); Nova kills the helper on cancel, or when it stops reporting progress.
* **Processor requirement:** Recognition needs a CPU with AVX, AVX2 and FMA. Nova checks this before loading the native library; `nova.media_transcribe_models` reports the result. Recognition runs on the processor.
* **Input formats:** WAV, Ogg/Opus and WebM/MKV with Opus audio (what browsers record) are decoded directly. Everything else Windows itself can play — MP3, AAC/M4A, MP4/MOV video, WMA, FLAC and, with the Web Media Extensions installed, other WebM/MKV — is decoded through Windows Media Foundation. No ffmpeg is involved.
* **Completeness:** a transcript counts as complete when the whole file was decoded and the text reaches the last moment where something can be heard — silence at the end or in the middle is not missing text. Stretches with sound but no recognized text are listed in `uncoveredAudible` as a hint (music and noise produce them too).
* **Speech models:** Nova knows three models, each pinned to a size and SHA-256 checksum that is checked after download:

  | Model | File | Size | In the app |
  | :--- | :--- | :--- | :--- |
  | `base` | `ggml-base-q5_1.bin` | about 57 MB | Basic — included with Nova |
  | `small` | `ggml-small-q5_1.bin` | about 181 MB | Recommended |
  | `large-v3-turbo` | `ggml-large-v3-turbo-q5_0.bin` | about 547 MB | Most accurate, slower than real time |

  Models are downloaded from the upstream whisper.cpp repository on Hugging Face. A model file you already have can be added with "Use a file I already have…"; Nova cannot verify such a file. An explicit `model` argument requests a matching installed file. Otherwise Nova honors the installed model selected in Settings, with automatic selection as a fallback when that choice is unavailable.
* **Progress and cancellation:** Jobs report progress and recognized segments. Cancel when appropriate; a stopped job returns the segments recognized so far. A job that stalls can be ended even when it has not reached its overall time budget.
* **Language:** Pass an ISO code such as `de` or `en`; without it the language is detected, which can be less reliable on short clips. Specify a known language when appropriate.

### Transcription window

The toolbar button "Transcribe audio or video" opens a window where a file can be dropped in. The result can be saved as plain text (`.txt`) or as subtitles (`.srt`, `.vtt`). The button is shown with "Show transcription button in the toolbar" (Settings → Tools, Transcription card). Models are managed under Settings → AI & agents → "Speech to text".

## Read the result as evidence

A completed job reports decoding and transcript coverage. Inspect `uncoveredAudible` before relying on the transcript: sound without recognized words can be music, noise or missed speech. A partial result after cancellation is not a complete transcript. Review names, numbers and consequential quotations against the recording.

## MCP tools

| Tool | Purpose |
| :--- | :--- |
| [`nova.media_transcribe_start`](../../../mcp-reference/tools/media-and-transcription/nova-media-transcribe-start.md) | Starts recognition for a local audio or video file. |
| [`nova.media_transcribe_status`](../../../mcp-reference/tools/media-and-transcription/nova-media-transcribe-status.md) | Retrieves progress and recognized segments. |
| [`nova.media_transcribe_stop`](../../../mcp-reference/tools/media-and-transcription/nova-media-transcribe-stop.md) | Cancels the job and returns recognized segments so far. |
| [`nova.media_transcribe_models`](../../../mcp-reference/tools/media-and-transcription/nova-media-transcribe-models.md) | Lists models, install state and processor support. |
| [`nova.media_transcribe_model_install`](../../../mcp-reference/tools/media-and-transcription/nova-media-transcribe-model-install.md) | Downloads a model or adopts an existing file. |
| [`nova.media_transcribe_model_remove`](../../../mcp-reference/tools/media-and-transcription/nova-media-transcribe-model-remove.md) | Removes a model file. |
| [`nova.media_file_info`](../../../mcp-reference/tools/media-and-transcription/nova-media-file-info.md) | Probes container and stated duration without decoding. It does not report channels, bitrate or video dimensions. |

[Transcription user guide](../../../user-guide/tools/transcription.md) · [Media Intelligence overview](../README.md) · [All core features](../../README.md)
