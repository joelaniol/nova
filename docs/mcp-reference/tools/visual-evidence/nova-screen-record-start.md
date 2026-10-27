# `nova.screen_record_start`

> **Starts a video of the Nova window, so your agent can show a feature or a bug as it happens.**

* **Core Feature Guide:** [Visual Evidence & Auditing](../../../research/evidence-verification-mode-evm/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

A screenshot shows one moment. Some things only make sense as a sequence: a menu opening, an animation, a loading state that flickers, an error that appears for half a second. `nova.screen_record_start` records the Nova window - tabs, address bar, the page and Nova's own dialogs - into an MP4 video.

The call returns only after the first frame is recorded (`firstFrameCaptured: true`), so the action your agent takes next is already in the video. Nova encodes with the H.264 encoder Windows provides, on the graphics card when one is available (`encoder`, `hardwareEncoder`). The video has a constant frame rate (`fps`) and is scaled down to fit `maxWidth` x `maxHeight` without stretching. One recording runs at a time.

**Quality.** `quality` trades picture quality against file size: `standard` keeps small interface text sharp, `low` halves the bitrate for long recordings, `high` doubles it for scrolling, animations or a video playing in a tab. The bitrate used is in the result (`bitrate`, bits per second). Still screens cost far less than the rate suggests.

**Pointer.** Your agent clicks and types through the page, not with the mouse. Its actions appear in the video as Nova's assist cursor, a ring that moves to each target and pulses on a click; `agentCursorShown` in the result says whether the user has it switched on. `includeCursor` (on by default) also draws the user's own mouse pointer; the result's `cursor` says whether it is in the video.

**Sound.** The video carries the sound of Nova's pages as AAC (`includeAudio`, on by default). Only Nova's own processes are heard - music, calls or notifications from other programs never end up in the file. While a page in Nova uses the microphone, for example during a call, the sound is silenced and the picture goes on: the other people's voices are not your agent's to record. The result's `audio` reports how loud the sound got (`peakDbfs`; `silent: true` when nothing audible played), how long it was silenced (`mutedMs`, `muteReasons`) and, if the file has no sound at all, why (`audioNote`). The level is what Nova plays after its own volume in the Windows mixer.

**Area.** `area` chooses what the video shows: `window` (default) the whole Nova window, `tab` only the page of the shown tab without the tab strip and address bar, `element` one element of that page (`selector`), `region` a rectangle of it (`region`, in the CSS pixels `nova.get_element_rect` reports). The area is measured once when the recording starts and is always cut to the visible page; it does not follow later scrolling, and an element that is not visible is refused (`video.element_not_found`, `video.area_not_visible`). The result's `crop` names the recorded rectangle in window pixels.

**File format.** `finalize` decides what the file becomes after the recording: `compatible` (default) is a classic MP4 for any player, editor or upload form; `fragmented` keeps the file as recorded, which plays in browsers and on Windows but not in every editor. Either way, a crash during the recording keeps what was recorded.

**Privacy.** Minimizing Nova means the user hid the window. While Nova is minimized nothing is recorded; if it stays minimized for a few seconds, the recording ends and keeps what was recorded before (`stoppedBy: "user_minimized"`). Nova never restores its window to keep recording. A recording does not start while the active tab is claimed by another agent (`reasonCode: "video.foreign_claim"`), because that tab's content would be in the video.

**Visible to the user.** While recording, a red light pulses on the tab in view, on the recording button in the toolbar and on Nova's taskbar button; it stays steady while the recording is paused, and never pulses when Windows animations are turned off. The user can stop the recording from the toolbar button at any time. The file is then finished and checked as usual, and the result says `stoppedBy: "user"` with `reasonCode: "video.user_stopped"`.

The recording ends by itself after `maxDurationSec`, at 2 GB, or when the Nova window closes. Stop it with [`nova.screen_record_stop`](nova-screen-record-stop.md), which returns the file together with a check that the video really shows what was recorded; [`nova.screen_record_status`](nova-screen-record-status.md) shows progress in between. Files go to Nova's Exports folder (`ScreenRecordings`) unless `saveDir` names another folder, which needs the user's "Allow local files" setting. Nothing is ever overwritten.

### Example

```text
nova.screen_record_start(fps=30, maxDurationSec=30, quality="high", fileName="settings-dropdown")
nova.click_selector(selector="#language-menu")
nova.screen_record_stop()
```

Common refusals: `video.already_recording`, `video.source_minimized`, `video.foreign_claim`, `video.start_timeout` (no frame within 10 seconds).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `fitTab` | `any` | No | — | — | Size Nova's window for the take so the tab is exactly this shape, measured after the resize: a template name ('nova-linkedin': 1360x970, 'nova-readme': 1280x720) or {width, height} in CSS pixels. A maximized window is restored first; a minimized Nova is refused untouched (video.source_minimized: the user hid it). nova.screen_record_stop puts size and state back and says so (windowRestored). Refused (video.window_fit_failed) when the screen is too small. |
| `fps` | `integer` | No | `30` | 1–60 | Frames per second of the video (constant; the last frame repeats when nothing changed). |
| `maxDurationSec` | `integer` | No | `60` | 1–1800 | The recording ends by itself after this many seconds of video. |
| `maxWidth` | `integer` | No | `1920` | 64–7680 | Largest video width in pixels; the window is scaled down to fit, never up, aspect ratio kept. |
| `maxHeight` | `integer` | No | `1080` | 64–7680 | Largest video height in pixels; the window is scaled down to fit, never up, aspect ratio kept. |
| `quality` | `string` | No | `"standard"` | `low`, `standard`, `high` | Picture quality versus file size. standard keeps small UI text sharp; low halves the bitrate for long recordings; high doubles it for scrolling, animations or video in a tab. The rate used is in the result (bitrate, bits per second). |
| `includeCursor` | `boolean` | No | `true` | — | Draw the user's mouse pointer into the video. Off hides only the user's pointer; your own actions stay visible through Nova's assist cursor. |
| `includeAudio` | `boolean` | No | `true` | — | Record the sound of Nova's pages (only Nova's own processes; other programs are never heard). While a page uses the microphone - a call or a voice recording - the sound is silenced and the picture goes on (audio.muteReasons audio.microphone_in_use): other people's voices are not yours to record. The result's audio says whether the file has sound and how loud it got (peakDbfs; silent=true when nothing audible played). |
| `area` | `string` | No | `"window"` | `window`, `tab`, `element`, `region` | What the video shows. window: all of Nova's window. tab: only the page of the shown tab, without Nova's tab strip and address bar (whatever covers the page, such as Nova's assist cursor or a dialog, is in it). element: one element of the shown page (selector). region: a rectangle of the shown page (region). The area is measured once at the start and does not follow later scrolling or resizing; it is always clipped to the visible page. The result's crop gives it in window pixels. |
| `actionVeil` | `string` | No | `"hidden"` | `hidden`, `subtle`, `normal` | How Nova shows that you control the tab while this recording runs. hidden (default): not at all, so the clip shows the page as it is. subtle: a thin frame and a small notice at the bottom right. normal: the page dimmed with a notice in the middle, as outside recordings. Only the look changes: the user's input stays blocked and a click still takes over. The stop result repeats the choice. |
| `purpose` | `string` | No | — | ≤ 160 characters | One line for the user: what this recording is for (e.g. 'README demo: stopping the agent'). Shown in Nova's approval dialog next to the file name, so the user knows what they agree to. |
| `selector` | `string` | No | — | — | With area=element: CSS selector of a visible element on the shown tab (refused with video.element_not_found or video.area_not_visible when it is missing or scrolled away). |
| `follow` | `boolean` | No | `false` | — | With area=element: the video follows the element when it moves or changes size (measured about ten times a second; the video frame keeps its size and the element is fitted in). While the element is gone or scrolled away the frames are black - never its surroundings. The result's follow says how often it moved and how many frames were black. |
| `region` | `object` | No | — | — | With area=region: rectangle in CSS pixels of the visible page (as nova.get_element_rect reports them). |
| `region.x` | `number` | Yes | — | — | Left coordinate of the region in CSS pixels. |
| `region.y` | `number` | Yes | — | — | Top coordinate of the region in CSS pixels. |
| `region.width` | `number` | Yes | — | — | Width of the region in CSS pixels. |
| `region.height` | `number` | Yes | — | — | Height of the region in CSS pixels. |
| `finalize` | `string` | No | `"compatible"` | `compatible`, `fragmented` | What the file becomes after the recording. compatible: a classic MP4 that every player, editor and upload form takes (the recording is rewritten after the stop, which costs a copy of the file). fragmented: kept as recorded - plays in browsers and Windows, but some editors refuse it. While recording the file is always fragmented, so a crash keeps what was recorded. |
| `saveDir` | `string` | No | — | — | Absolute folder for the video. Omit to use Nova's Exports folder; any other folder needs 'Allow local files'. |
| `fileName` | `string` | No | — | ≤ 80 characters | File name without extension; default recording-<UTC time>. A taken name gets -2, -3 ... |
| `privacy` | `string` | No | `"standard"` | `standard`, `strict` | standard: masks follow the page with about 0.1 s delay; a field that appears or moves can show for that long. strict: frames wait about 0.3 s until the masks for their moment are known; unknown or moving masks black out the page area, frames of other websites in the page are black. Use strict when the flow shows secrets (account data, payment) or another agent's content could appear. |
| `evidence` | `boolean` | No | `true` | — | Keep evidence beside the video in <name>.evidence: a timeline of your marks (nova.screen_record_mark), every MCP tool call (name, call id, phase; never arguments) and observed picture changes, lossless PNGs at marks and before/after each change, a contact sheet and manifest.json with the video's SHA-256. Read it with nova.screen_record_inspect. |
| `maskSelectors` | `array` of `string` | No | — | ≤ 20 items | CSS selectors of elements to black out in the video, in addition to password and payment fields (searched in the page and its same-origin frames; strict also in open shadow roots). An invalid selector refuses the start. |
| `allowedOrigins` | `array` of `string` | No | — | ≤ 20 items | Websites the recording may show, as origins (https://example.com). The start is refused when the shown page is elsewhere, and the recording pauses while it is (video.origin_not_allowed). Omit to allow any website. |
| `agentId` | `string` | No | — | — | Your agent identity; it owns the recording, so pass it to status, stop and export too. The recording is refused (video.foreign_claim) while the active tab is claimed by another agent. |

Capability bundle: `visual_evidence` (load it with `nova.tools_bundle(bundle='visual_evidence')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->
