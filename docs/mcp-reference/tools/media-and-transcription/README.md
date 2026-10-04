# Media Intelligence & Whisper Speech-to-Text

In-browser audio/video recording, local OpenAI Whisper transcription, model management, and camera/mic permissions.

* **Core Architecture Guide:** [Core Features: media-intelligence.md](../../../core-features/media-intelligence.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

<!-- generated:tool-list (from the tool pages in this folder; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
## Tool Inventory (24 Tools)

Capability bundles of these tools: `browser_automation`, `page_read_debug`, `system_tools`.

| Tool | What it does |
| :--- | :--- |
| **[`nova.hardware_diagnostics_start`](nova-hardware-diagnostics-start.md)** | Initiates in-page hardware diagnostic loop for camera, microphone, or audio speaker output. |
| **[`nova.hardware_diagnostics_state`](nova-hardware-diagnostics-state.md)** | Returns current live hardware diagnostic metrics including microphone audio levels and peak decibels. |
| **[`nova.hardware_diagnostics_stop`](nova-hardware-diagnostics-stop.md)** | Stops in-page hardware diagnostics and releases active camera, microphone, or speaker handles. |
| **[`nova.media_activity_audit`](nova-media-activity-audit.md)** | Retrieves an audit trail of stored media permissions joined with recent decision records per origin. |
| **[`nova.media_activity_delta`](nova-media-activity-delta.md)** | Performs an incremental read of the in-memory media permission activity ring buffer. |
| **[`nova.media_activity_status`](nova-media-activity-status.md)** | Returns an O(1) instant snapshot of currently active camera, microphone, and screen-sharing streams. |
| **[`nova.media_capture_start`](nova-media-capture-start.md)** | Starts streaming capture of live audio/video playing in a tab (Media Source Extensions streams and WebAudio playback). |
| **[`nova.media_capture_status`](nova-media-capture-status.md)** | Reports progress, elapsed time, and bytes written for an active in-tab media capture. |
| **[`nova.media_capture_stop`](nova-media-capture-stop.md)** | Stops in-tab media capture, flushes pending segments, closes the per-track files, and returns their paths. |
| **[`nova.media_device_preferences_list`](nova-media-device-preferences-list.md)** | Lists stored per-site preferred device IDs (camera, microphone, speaker). |
| **[`nova.media_file_info`](nova-media-file-info.md)** | Identifies a local media file's container and duration from its header, without decoding it. |
| **[`nova.media_permission_activity_list`](nova-media-permission-activity-list.md)** | Reads recent entries from the in-memory ring buffer of camera, microphone, speaker, screen-share, and geolocation permission decisions. |
| **[`nova.media_permission_get`](nova-media-permission-get.md)** | Reads the effective and stored media permissions for a specific web origin. |
| **[`nova.media_permission_set`](nova-media-permission-set.md)** | Sets or clears persistent or session-based camera, mic, speaker, and geolocation permissions. |
| **[`nova.media_permissions_clear_session_grants`](nova-media-permissions-clear-session-grants.md)** | Drops all temporary session permissions and halts any live media tracks relying on them. |
| **[`nova.media_permissions_list`](nova-media-permissions-list.md)** | Lists all stored per-origin permission overrides along with global default policies. |
| **[`nova.media_status`](nova-media-status.md)** | Inspects the first `<video>` or `<audio>` element on a page: playback state, position, and why it may have stopped. |
| **[`nova.media_stop_all`](nova-media-stop-all.md)** | Emergency kill switch terminating all active camera, microphone, and screen-sharing tracks browser-wide. |
| **[`nova.media_transcribe_model_install`](nova-media-transcribe-model-install.md)** | Downloads a Whisper speech model or adopts an existing local GGML model file. |
| **[`nova.media_transcribe_model_remove`](nova-media-transcribe-model-remove.md)** | Deletes an installed speech model file to reclaim disk space or prepare for re-download. |
| **[`nova.media_transcribe_models`](nova-media-transcribe-models.md)** | Lists known Whisper speech models, installation statuses, and machine CPU/AVX2 capabilities. |
| **[`nova.media_transcribe_start`](nova-media-transcribe-start.md)** | Transcribes local audio or video files into text entirely on-device using local Whisper.cpp. |
| **[`nova.media_transcribe_status`](nova-media-transcribe-status.md)** | Reports progress, elapsed percentage, and recognized text segments of an active transcription. |
| **[`nova.media_transcribe_stop`](nova-media-transcribe-stop.md)** | Stops an in-flight transcription job and returns recognized text segments up to the cancellation point. |
<!-- /generated:tool-list -->

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
