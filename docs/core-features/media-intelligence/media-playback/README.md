# Media Playback Inspection

Use playback inspection when an audio or video element appears paused, stops unexpectedly or needs a position check. Ask your agent to inspect the current tab and report the element's playback state and available diagnostic evidence.

## What Nova reports

[`nova.media_status`](../../../mcp-reference/tools/media-and-transcription/nova-media-status.md) inspects the first video element on the page, or the first audio element when no video element is found. It reports:

* Playing, paused, ended and seeking state, current position and duration.
* Volume, mute state and playback rate.
* Readiness, network state and any error on the element.
* Page visibility and focus; when the in-page diagnostics script is present, a classified pause reason and recent events.
* Limited YouTube-specific ad detection when the relevant player element is present.

This is a snapshot of one media element, not an inventory of every player. The result does not distinguish audio from video as a media type and does not include buffered time ranges. Absence of an element or diagnostic trail does not prove that no other playback mechanism exists.

## Inspection, capture and device use

Playback state answers what the selected page element reports. [Media Capture](../media-capture/README.md) saves supported page playback to files. [Devices & Permissions](../devices-and-permissions/README.md) describes camera, microphone and screen-sharing activity. A playing video does not by itself mean the camera is active.

[Media Intelligence overview](../README.md) · [All core features](../../README.md)
