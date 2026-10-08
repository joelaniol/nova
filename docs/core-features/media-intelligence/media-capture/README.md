# Media Capture

Media Capture saves supported audio or video played by a browser tab. For example, an agent can capture a voice message or a supported stream, finish the files and then pass the audio to [Speech Transcription](../transcription/README.md).

## What is captured

`nova.media_capture_start` installs a recorder in the tab and writes what the page plays to files:

* **Sources:** `mse` (Media Source Extensions — HLS/DASH streaming), `webaudio` (`decodeAudioData`, e.g. messenger voice messages) or `both` (default).
* **Output:** One file per track, with the extension taken from the media type (for example `.mp4`, `.m4a`, `.webm`, `.wav`). Without `saveDir`, files go to a `MediaCaptures` folder inside Nova's Exports folder; a custom `saveDir` requires "Allow local files".
* **Size limit:** 2 GB by default, up to 16 GB with `maxBytes`. Reaching the limit stops the capture from growing; playback continues.
* **Players that already started:** The recorder hooks in at page load. `reload=true` reloads the tab so a running player is captured from the beginning.

These recorders capture the page's supported playback path. They are different from camera, microphone and screen-sharing tracks, and from [Session Recording](../../session-recording/README.md), which records browser and network events for diagnostics. A capture is not a universal download mechanism for every player or protected stream.

## Start, inspect and finish

Start capture in the intended tab before playing the content. Inspect the capture's progress and bytes written. Stop capture to flush pending segments and obtain the resulting file paths; do not treat a still-growing file as a completed recording. Reloading can alter the current page, so choose it deliberately.

| Tool | Purpose |
| :--- | :--- |
| [`nova.media_capture_start`](../../../mcp-reference/tools/media-and-transcription/nova-media-capture-start.md) | Starts MSE, Web Audio or combined capture. |
| [`nova.media_capture_status`](../../../mcp-reference/tools/media-and-transcription/nova-media-capture-status.md) | Inspects current capture progress. |
| [`nova.media_capture_stop`](../../../mcp-reference/tools/media-and-transcription/nova-media-capture-stop.md) | Finishes capture and returns track-file paths. |

Capturing content does not supply rights to copy or redistribute it. Review the [Acceptable Use Policy](../../../../ACCEPTABLE-USE.md) and protect recordings that contain private information.

[Media Playback](../media-playback/README.md) · [Devices & Permissions](../devices-and-permissions/README.md) · [Media Intelligence overview](../README.md) · [All core features](../../README.md)
