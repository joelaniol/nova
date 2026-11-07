# Microphone, Camera, Media Permissions & Barcode Troubleshooting

This guide resolves hardware detection failures, microphone level issues, WebRTC connection errors, permission blocks, and barcode or QR code synthesis failures across Nova AI Workspace and connected AI agents.

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
| `invalid_check_digit` | EAN-13, EAN-8, or UPC-A barcode check digit fails the GS1 Modulo-10 checksum algorithm. | Verify the original product number. Omit the check digit to let Nova calculate it, or fix the final digit to match the required checksum. |
| `contrast_too_low` / `inverted_colors` | QR code modules are lighter than background or contrast ratio is below 4.5:1. | Darken modules (`foreground`), lighten `background`, or ensure all stops in `gradientTo` satisfy WCAG 4.5:1 contrast. |
| `logo_no_room` / `logo_needs_ecc_h` | Logo plate collides with structural patterns or error correction is not set to `H`. | Omit `errorCorrection` (Nova auto-selects `H`), shorten content (under 58 characters for Version < 7), or drop the logo. |
| `print_module_too_small` | Specified `printWidthMm` results in individual module size $< 0.25$ mm. | Increase `printWidthMm`, shorten the encoded string, or use `style: "classic"`. |
| `scan_validation_failed` / `write_failed` | In-memory read-back assertion failed before saving to disk. | The code could not be decoded. Use `style: "classic"`, increase module size (`width`), or improve color contrast. |
| `barcode_generate.output_exists` | The file specified in `outputPath` already exists on disk. | Choose a new destination file path or leave `outputPath` omitted to save into `Exports/Codes/`. |

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

## 7. Barcodes & QR Codes Troubleshooting

Nova enforces strict mathematical check-digit integrity, accessibility contrast thresholds, and decode-before-write invariants. When a code cannot be generated or read, use these resolutions:

### 7.1 Check Digit Verification Failures (`invalid_check_digit`)
* **Symptom:** Generating an EAN-13, EAN-8, or UPC-A barcode fails with:
  > *"The check digit of 4006381333930 is 0, but these digits need 1. Nova does not correct it; check the number."*
* **Root Cause:** Nova enforces the GS1 Modulo-10 checksum algorithm. Quietly "repairing" an invalid digit risks labeling the wrong physical product or corrupting inventory databases.
* **Resolution:**
  1. Inspect the source product number to verify the digits.
  2. If you are minting a new barcode and do not know the check digit, pass the number **without the final digit** (e.g. 12 digits for EAN-13, 7 digits for EAN-8, 11 digits for UPC-A). Nova will automatically compute and append the correct check digit.

### 7.2 Styling & Contrast Rejections (`contrast_too_low`, `inverted_colors`)
* **Symptom:** QR code generation fails with `contrast_too_low` or `inverted_colors`.
* **Root Cause:**
  * `inverted_colors`: Module luminance is higher than background luminance (light modules on a dark background). Standard phone cameras fail to scan inverted codes reliably.
  * `contrast_too_low`: Relative luminance contrast between modules and background is below **`4.5:1`** (WCAG 2.x standard). When using `gradientTo`, Nova checks 4 intermediate color steps along the gradient path; if any step drops below 4.5:1, the design is rejected.
* **Resolution:**
  1. Ensure the background is white (`#FFFFFF`) or very light, and modules are dark (e.g. `#000000`, deep blue, dark charcoal).
  2. If using gradients (`gradientTo`), ensure both start and end colors maintain $\ge 4.5:1$ contrast against the background.
  3. If your brand palette requires a dark background, place the QR code on a light plate with generous quiet-zone margins.

### 7.3 Logo Embedding & Alignment Pattern Collisions (`logo_no_room`, `logo_needs_ecc_h`)
* **Symptom:** Generating a QR code with `logoPath` fails with `logo_no_room` or `logo_needs_ecc_h`.
* **Root Cause:**
  * `logo_needs_ecc_h`: A logo covers data modules and strictly requires Error Correction Level `H` (30% recovery capacity). Passing `errorCorrection: "M"` or `"L"` with a logo is rejected.
  * `logo_no_room`: The central logo plate (limited to 28% width share) touches structural patterns. In QR Version 7 and higher symbols (character counts exceeding ~58 characters), an alignment pattern sits in the exact center of the matrix, preventing center logo placement.
  * `logo_not_allowed`: SEPA GiroCodes (`data.kind: "epc"`) strictly forbid logos under EPC banking standards.
* **Resolution:**
  1. Omit the `errorCorrection` parameter when using a logo; Nova will automatically promote the code to Level `H`.
  2. Shorten the encoded URL or text (e.g. using a vanity shortlink) so the matrix stays below Version 7.
  3. If the payload cannot be shortened, omit the logo to allow standard module placement.

### 7.4 Physical Print Sizing Floor (`print_module_too_small`)
* **Symptom:** Generation fails with `print_module_too_small`.
* **Root Cause:** The requested `printWidthMm` divided by the symbol module count yields individual modules smaller than **`0.25 mm`**. Standard mobile camera sensors cannot resolve modules below this physical size.
* **Resolution:**
  1. Increase `printWidthMm` to allocate more physical space for the printed asset.
  2. Shorten the payload to reduce total module count (e.g. switch from `vcard` to `mecard`).
  3. Aim for a module size of at least $0.35\text{ mm}$ for optimal outdoor and handheld scanning.

### 7.5 Read-Back Assertion & Safe Write Guards (`scan_validation_failed`, `write_failed`, `output_exists`)
* **Symptom:** Generation fails with `scan_validation_failed` or `barcode_generate.output_exists`.
* **Root Cause:**
  * `scan_validation_failed`: In-memory decode-before-write assertion failed. Even though parameters were mathematically valid, the rendered raster image could not be decoded by Nova's strict decoder (e.g. due to aggressive dot rounding or subtle anti-aliasing).
  * `barcode_generate.output_exists`: The file specified in `outputPath` already exists. Nova guarantees never to overwrite existing files.
* **Resolution:**
  1. For `scan_validation_failed`, switch to `style: "classic"`, increase `width` to give dots more pixels (at least 4 pixels per module), or increase color contrast.
  2. For `output_exists`, specify an unused output filename or leave `outputPath` omitted to let Nova generate a unique timestamped file in `Exports/Codes/`.

### 7.6 Decoding Failures from Photos or Scans (`foundCount: 0`)
* **Symptom:** `nova.barcode_decode` returns `foundCount: 0` on an image known to contain a barcode.
* **Root Cause:** The barcode occupies too few pixels in a high-resolution photo, the edges are blurred by motion, or the code is surrounded by complex background patterns.
* **Resolution:**
  1. Use `nova.image_transform` to tightly crop the image around the barcode area (`crop: { x: ..., y: ..., width: ..., height: ... }`).
  2. Restrict symbologies via `formats: ["qr"]` or `formats: ["ean13"]` to enable targeted decoding heuristics.
  3. Ensure the source image has adequate lighting and resolution (at least 200–300 DPI for printed documents).

---

## Related Documentation

* **[Barcode, QR Code & Data Chart Synthesis Architecture](../core-features/media-intelligence/barcodes-and-charts/README.md)** — Symbologies, structured payloads, and camera stress tests.
* **[Hardware Device Routing & Real-Time Diagnostics](../core-features/media-intelligence/devices-and-permissions/hardware-routing-and-diagnostics/README.md)** — Architectural specification of ConPTY, WebRTC diagnostics, and AudioGraph VU meters.
* **[Permission Hierarchy & The Reason Stack](../core-features/media-intelligence/devices-and-permissions/permission-hierarchy-and-reason-stack/README.md)** — The 8-stage permission resolver and provenance logging.
* **[Governance, Kill-Switches & Device Audits](../core-features/media-intelligence/devices-and-permissions/governance-killswitch-and-audit/README.md)** — Salted device ID hashing and emergency stream revocation.
* **[MCP Barcode Generate Reference](../mcp-reference/tools/files-and-documents/nova-barcode-generate.md)** — Tool parameter definitions.
* **[MCP Barcode Decode Reference](../mcp-reference/tools/files-and-documents/nova-barcode-decode.md)** — Extraction parameters and security invariants.
* **[MCP Hardware Diagnostics Start Reference](../mcp-reference/tools/media-and-transcription/nova-hardware-diagnostics-start.md)** — Tool parameter definitions.
