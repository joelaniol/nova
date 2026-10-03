# Media Intelligence & Whisper Speech-to-Text

In-browser audio/video recording, local OpenAI Whisper transcription, model management, and camera/mic permissions.

* **Capability Bundle(s):** `system_tools`
* **Core Architecture Guide:** [Core Features: media-intelligence.md](../../../core-features/media-intelligence.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (24 Tools)

| Tool Name | Status | Description |
| :--- | :---: | :--- |
| **[`nova.hardware_diagnostics_start`](nova-hardware-diagnostics-start.md)** | Documented | Start in-page hardware diagnostics for camera, microphone, or speaker on the target page. |
| **[`nova.hardware_diagnostics_state`](nova-hardware-diagnostics-state.md)** | Documented | Get current in-page hardware diagnostics state (running channels + microphone level/peak). |
| **[`nova.hardware_diagnostics_stop`](nova-hardware-diagnostics-stop.md)** | Documented | Stop in-page hardware diagnostics for a specific channel or all channels. |
| **[`nova.media_activity_audit`](nova-media-activity-audit.md)** | Documented | Audit-trail of stored per-site media permissions joined with the most recent activity-log decision. |
| **[`nova.media_activity_delta`](nova-media-activity-delta.md)** | Documented | Incremental read of the in-memory permission activity log. |
| **[`nova.media_activity_status`](nova-media-activity-status.md)** | Documented | O(1) snapshot of currently live media streams. |
| **[`nova.media_capture_start`](nova-media-capture-start.md)** | Documented | Start recording media playing in a tab (WebAudio, MSE streams, dynamic blobs). |
| **[`nova.media_capture_status`](nova-media-capture-status.md)** | Documented | Report progress of the streaming capture running on a tab: bytes written, elapsed time. |
| **[`nova.media_capture_stop`](nova-media-capture-stop.md)** | Documented | Stop the streaming capture on a tab, close files and return their paths. |
| **[`nova.media_device_preferences_list`](nova-media-device-preferences-list.md)** | Documented | List stored per-site device preferences (camera/microphone/speaker device IDs). |
| **[`nova.media_file_info`](nova-media-file-info.md)** | Documented | Probe media container metadata, duration, channels, and codecs from a local file without ffmpeg. |
| **[`nova.media_permission_activity_list`](nova-media-permission-activity-list.md)** | Documented | Read the in-memory audit trail of media permission decisions (camera/microphone/speaker/screen). |
| **[`nova.media_permission_get`](nova-media-permission-get.md)** | Documented | Read the stored per-origin override (if any) plus the effective decision for an origin. |
| **[`nova.media_permission_set`](nova-media-permission-set.md)** | Documented | Write or clear per-origin camera/microphone/speaker/screenCapture/geolocation permission. |
| **[`nova.media_permissions_clear_session_grants`](nova-media-permissions-clear-session-grants.md)** | Documented | Drop every in-memory session grant AND stop any live media tracks running under them. |
| **[`nova.media_permissions_list`](nova-media-permissions-list.md)** | Documented | List per-origin camera/microphone/speaker permission overrides plus current global defaults. |
| **[`nova.media_status`](nova-media-status.md)** | Documented | Get playback status of the primary `<video>` or `<audio>` element on the page. |
| **[`nova.media_stop_all`](nova-media-stop-all.md)** | Documented | Emergency stop for live camera/microphone/screen-sharing tracks browser-wide. |
| **[`nova.media_transcribe_model_install`](nova-media-transcribe-model-install.md)** | Documented | Obtain a speech model, either by downloading a known one (modelId) or adopting an existing file. |
| **[`nova.media_transcribe_model_remove`](nova-media-transcribe-model-remove.md)** | Documented | Delete an installed speech model file. |
| **[`nova.media_transcribe_models`](nova-media-transcribe-models.md)** | Documented | List the speech models Nova knows about and machine CPU/AVX2 capabilities. |
| **[`nova.media_transcribe_start`](nova-media-transcribe-start.md)** | Documented | Transcribe local audio or video files into text entirely on-device using local Whisper.cpp. |
| **[`nova.media_transcribe_status`](nova-media-transcribe-status.md)** | Documented | Report progress of a speech-to-text job: state, segments completed, recognized text. |
| **[`nova.media_transcribe_stop`](nova-media-transcribe-stop.md)** | Documented | Stop a running transcription and return what was recognized up to that point. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
