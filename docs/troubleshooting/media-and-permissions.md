# Microphone, Camera & Media Permissions Troubleshooting

This guide resolves hardware detection failures, microphone level issues, WebRTC connection errors, and permission blocks across Nova AI Workspace and connected AI agents.

---

## Quick Symptom Checker

| Symptom / Error Code | Root Cause | Primary Resolution |
| :--- | :--- | :--- |
| `diagnostics.user_gesture_required` | Agent attempted to start camera/microphone diagnostics over CDP without a user gesture. | **Expected behavior.** Nova deliberately blocks automated camera/microphone activation without a physical user gesture. Use the speaker test (`kind="speaker"`) or test interactively in Settings. |
| `permission_denied` (`NotAllowedError`) | The site is blocked in Permission Center, or the user denied access in the prompt dialog. | Inspect Site Info (lock/slider icon in address bar) and set Camera/Microphone to **Allow**, or check `nova.media_permission_get`. |
| `device_not_found` (`NotFoundError`) | The selected microphone or webcam is unplugged, powered off, or disabled in Windows. | Check physical USB/Bluetooth connection, run Windows Sound Settings, or inspect `nova.media_device_preferences_list`. |
| `device_busy` (`NotReadableError`) | Another Windows application holds an exclusive lock on the camera or microphone. | Close external conferencing software (Zoom, Teams, OBS), or call `nova.media_stop_all` if an adjacent Nova tab is streaming. |
| `insecure_context` | WebRTC media capture was requested from an unencrypted plain HTTP origin. | WebRTC APIs strictly require a **Secure Context**. Access the site via `https://` or `localhost`. |
| Microphone level meter shows 0% in test dialog | Input volume is muted in Windows, or wrong microphone endpoint selected. | Open **Settings → Media & permissions → Test hardware**, verify device selection, and check Windows microphone input volume. |
| Webcam activity LED stays on after closing meeting | Active media stream remained open in a background tab. | Call `nova.media_stop_all` or click **Menu → Emergency stop** (<kbd>Ctrl</kbd>+<kbd>Alt</kbd>+<kbd>Esc</kbd>) to force-close all streams. |

---

## 1. Automated Diagnostics & The User Gesture Guard (`diagnostics.user_gesture_required`)

### Symptom
An AI agent attempts to run hardware diagnostics using `nova.hardware_diagnostics_start`:
```json
{
  "name": "nova.hardware_diagnostics_start",
  "arguments": {
    "kind": "microphone"
  }
}
```
The call fails with structured reason code `diagnostics.user_gesture_required`:
> *"Nova blocks camera and microphone access that no user gesture asked for, and this tool drives the page over CDP - so it has no gesture to show."*

### Why This Happens (Security Invariant)
To protect user privacy and prevent rogue scripts or prompt injections from silently recording room audio, Nova enforces `NonUserInitiatedHardDenyRule`. WebRTC media capture requires an interactive user gesture (e.g. mouse click or keystroke). Because CDP automation runs out-of-band without an interactive human gesture, camera and microphone access are blocked.

### Resolution:
1. **Speaker Testing:** The speaker diagnostic test does not record audio and requires no permissions. Call:
   ```json
   {
     "name": "nova.hardware_diagnostics_start",
     "arguments": {
       "kind": "speaker"
     }
   }
   ```
2. **Interactive Microphone & Camera Testing:** Operators can test microphone and camera hardware directly inside Nova's desktop interface via **Settings → Media & permissions → Test hardware**.

---

## 2. Testing Audio & Video in Nova's Hardware Test Dialog

When a microphone or webcam is not working properly, use Nova's native diagnostic suite:

1. Click **Menu → Settings → Media & permissions**.
2. Click **Test hardware** to open the `HardwareTestDialog`.

### 2.1 Testing the Microphone
* Select your physical microphone from the dropdown (or leave set to **System default**).
* Click **Start**. Speak into your microphone.
* **Expected Activity:** The green level bar moves in real-time, showing percentage activity and a peak indicator (e.g. `Level: 45% (peak: 72%)`).
* **If Level Stays at 0%:**
  1. Check if the physical mute switch on your headset or microphone is engaged.
  2. Open **Windows Settings → System → Sound → Input**, and verify the **Input volume** slider is at 80–100%.
  3. Ensure Windows microphone privacy allows desktop apps: **Windows Settings → Privacy & Security → Microphone → Let desktop apps access your microphone = ON**.

### 2.2 Testing the Speaker
* Select your output headphones or speakers.
* Click **Play Tone**.
* **Expected Activity:** Nova plays a pure 440 Hz test tone in a continuous loop until stopped, verifying audio routing and low latency.

### 2.3 Testing the Camera
* Select your webcam from the dropdown.
* Click **Start**.
* **Expected Activity:** The live video preview appears inside the dialog border, displaying current resolution and frame rate.

---

## 3. Resolving Permission Denials & Inspecting the Reason Stack

When a website cannot access the camera or microphone, use `nova.media_permission_get` to inspect the 8-stage evaluation chain:

```json
{
  "name": "nova.media_permission_get",
  "arguments": {
    "axis": "microphone",
    "origin": "https://teams.microsoft.com"
  }
}
```

### Evaluating the `reasonStack`:
* **`automation_hard_deny`:** The tab is operating in an automated crawler context. Crawlers are permanently blocked from camera and microphone access.
* **`non_user_initiated_hard_deny`:** The site requested capture before the user clicked or interacted with the page. Ensure the user clicks an interactive "Join Meeting" button.
* **`os_privacy:microphone=block`:** The Windows operating system privacy switch is turned OFF. Enable microphone access in Windows Settings.
* **`site_grant:blocked`:** Access was previously blocked by the user. Click the lock/slider icon in Nova's address bar to open Site Info, change the permission to **Allow**, and reload the tab.
* **`session_grant:none`:** An ephemeral grant was not found. If needed, clear all temporary session grants via `nova.media_permissions_clear_session_grants`.

---

## 4. Hardware Configuration Drift (`nova.media_device_preferences_list`)

When external USB webcams or Bluetooth headsets are disconnected, web applications can fail unpredictably because they attempt to open an absent device ID.

### Auditing Device Drift:
Query stored device bindings against currently connected hardware:
```json
{
  "name": "nova.media_device_preferences_list"
}
```
* If a stored preference indicates that the bound device is missing, update the preference in **Settings → Media & permissions** or reset the device preference to `__nova.system_default__`.

---

## 5. Device In Use by Another Application (`device_busy`)

Windows webcams and certain professional audio interfaces do not support multi-client sharing. If an external application holds an exclusive DirectShow or MediaFoundation handle:
1. Nova reports error code `device_busy` (`NotReadableError` / `TrackStartError`).
2. Close external desktop software that might be holding the camera (e.g. Zoom, Microsoft Teams desktop, OBS Studio, or Windows Camera app).
3. If an adjacent tab inside Nova is holding the stream, call:
   ```json
   {
     "name": "nova.media_stop_all"
   }
   ```
   This immediately terminates all active audio and video streams across all Nova sandboxes and tabs.

---

## 6. Secure Context Requirement (`insecure_context`)

The W3C WebRTC specification mandates that `navigator.mediaDevices.getUserMedia` is only available within a **Secure Context**:
* **Permitted:** `https://example.com`, `https://localhost:3000`, `http://127.0.0.1:8080`.
* **Forbidden:** `http://192.168.1.100`, `http://dev-server.internal`.
* Web applications hosted over plain HTTP will fail immediately with `insecure_context`. Configure SSL/TLS certificates or access local services via `localhost`.

---

## Related Documentation

* **[Hardware Device Routing & Real-Time Diagnostics](../core-features/media-intelligence/devices-and-permissions/hardware-routing-and-diagnostics/README.md)** — Architectural specification of ConPTY, WebRTC diagnostics, and AudioGraph VU meters.
* **[Permission Hierarchy & The Reason Stack](../core-features/media-intelligence/devices-and-permissions/permission-hierarchy-and-reason-stack/README.md)** — The 8-stage permission resolver and provenance logging.
* **[Governance, Kill-Switches & Device Audits](../core-features/media-intelligence/devices-and-permissions/governance-killswitch-and-audit/README.md)** — Salted device ID hashing and emergency stream revocation.
* **[MCP Hardware Diagnostics Start Reference](../mcp-reference/tools/media-and-transcription/nova-hardware-diagnostics-start.md)** — Tool parameter definitions.
