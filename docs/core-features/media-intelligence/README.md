# Media Intelligence

Nova can transcribe local speech, display website images, read and export PDFs, inspect page playback, capture supported streams and manage media-device access. Choose the area that matches the task:

| Area | What it covers |
| :--- | :--- |
| [Speech Transcription](transcription/README.md) | Local speech recognition, models, progress, text and subtitle export. |
| [Image Viewer](image-viewer/README.md) | Magnifying a website image, zoom, original size, fit, navigator and save. |
| [PDF Reading & Export](pdf/README.md) | Extracting existing PDF text and exporting webpages as PDFs; no OCR. |
| [Media Capture](media-capture/README.md) | Saving supported MSE and Web Audio playback to track files. |
| [Media Playback Inspection](media-playback/README.md) | Playback state, position, volume and available pause diagnostics. |
| [Media Devices & Permissions](devices-and-permissions/README.md) | Camera, microphone, speaker, screen sharing, device preferences and activity. |

## How the areas relate

A captured audio file can become transcription input. A downloaded PDF can be read as text. An image viewer supports human inspection, while screenshot tools provide visual evidence to agents. Each operation has its own input and permissions; access to one does not authorize every other operation.

Transcription runs locally in [Nova Outrider](../outrider-boundary/README.md). Model downloads need a network connection. Camera, microphone and screen-sharing use is governed by website permissions and remains visible in Nova.

[Session Recording](../session-recording/README.md) records browser, network and interaction events for diagnostics. It is separate from recording media playback or using a microphone. [Research](../research/README.md) explains how factual and visual evidence can support conclusions.

## Related documentation

* [Media and transcription tool reference](../../mcp-reference/tools/media-and-transcription/README.md) — Full tool contracts and examples.
* [Visual evidence tool reference](../../mcp-reference/tools/visual-evidence/README.md) — PDF and screenshot operations.
* [Transcription user guide](../../user-guide/tools/transcription.md) — User-facing entry point.

[All core features](../README.md)
