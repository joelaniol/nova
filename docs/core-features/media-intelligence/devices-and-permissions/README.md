# Media Devices & Permissions

Camera, microphone, speaker routing and screen sharing are separate from playing an audio or video file. Review which website is requesting access, which device it will use and whether the permission is temporary or persistent.

## Control site access and device choice

Use Nova's site-information panel to review access for the current site. Permission tools can inspect global defaults and per-origin overrides, including a separate requesting origin for embedded content. Changing a stored permission does not prove that a device has started successfully.

**Allow once** grants are held in memory rather than stored as persistent site permissions. Temporary grants can expire or be cleared. Clearing session grants stops live tracks that depend on those grants; it does not erase every persistent permission.

Nova shows active camera, microphone and screen sharing in the tab and site-information icon. Device preferences record a site's preferred camera, microphone or speaker; a preference is not an access grant and does not guarantee that the device is currently available.

## Inspect current activity and stop tracks

| Tool | Purpose |
| :--- | :--- |
| [`nova.media_permissions_list`](../../../mcp-reference/tools/media-and-transcription/nova-media-permissions-list.md) | Lists global defaults and stored origin overrides. |
| [`nova.media_permission_get`](../../../mcp-reference/tools/media-and-transcription/nova-media-permission-get.md) | Reads effective and stored permissions for an origin. |
| [`nova.media_permission_set`](../../../mcp-reference/tools/media-and-transcription/nova-media-permission-set.md) | Sets or clears persistent or session permissions. |
| [`nova.media_device_preferences_list`](../../../mcp-reference/tools/media-and-transcription/nova-media-device-preferences-list.md) | Lists stored per-site preferred device IDs. |
| [`nova.media_activity_status`](../../../mcp-reference/tools/media-and-transcription/nova-media-activity-status.md) | Reports currently active camera, microphone and screen-sharing streams. |
| [`nova.media_permissions_clear_session_grants`](../../../mcp-reference/tools/media-and-transcription/nova-media-permissions-clear-session-grants.md) | Clears temporary grants and stops dependent tracks. |
| [`nova.media_stop_all`](../../../mcp-reference/tools/media-and-transcription/nova-media-stop-all.md) | Stops active tracks browser-wide or for a selected origin. |

Stopping tracks and revoking stored permission are different operations. Check activity after stopping and inspect stored permissions when future access should also change.

## Audit and diagnose

[`nova.media_activity_audit`](../../../mcp-reference/tools/media-and-transcription/nova-media-activity-audit.md), [`nova.media_permission_activity_list`](../../../mcp-reference/tools/media-and-transcription/nova-media-permission-activity-list.md) and [`nova.media_activity_delta`](../../../mcp-reference/tools/media-and-transcription/nova-media-activity-delta.md) expose recent permission decisions and audit information. The activity log is held in memory; it is not a permanent history of every past session.

The [`nova.hardware_diagnostics_start`](../../../mcp-reference/tools/media-and-transcription/nova-hardware-diagnostics-start.md), [`state`](../../../mcp-reference/tools/media-and-transcription/nova-hardware-diagnostics-state.md) and [`stop`](../../../mcp-reference/tools/media-and-transcription/nova-hardware-diagnostics-stop.md) tools test camera, microphone or speaker output inside a page. Diagnostics can use real hardware; select the intended kind and stop the test when finished.

The shared permission interface also includes geolocation. Location access is not an audio/video recording feature; see the [Permissions user guide](../../../user-guide/identity-and-security/permissions.md) for the broader distinction between website and agent permissions.

[Media Capture](../media-capture/README.md) · [Media Playback](../media-playback/README.md) · [Media Intelligence overview](../README.md) · [All core features](../../README.md)
