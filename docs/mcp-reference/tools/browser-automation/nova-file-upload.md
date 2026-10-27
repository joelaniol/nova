# `nova.file_upload`

Attaches one or more local files directly to an HTML `<input type="file">` element via Chrome DevTools Protocol (CDP), bypassing native OS file picker dialogs.

---

## 1. Overview

Traditional browser automation fails when clicking an `<input type="file">` because it triggers a modal Windows File Open dialog that freezes DOM execution. `nova.file_upload` bypasses the native dialog entirely by assigning file handles directly via CDP (`DOM.setFileInputFiles`).

* **Native Dialog Bypass:** No OS file picker is opened; execution never hangs on Win32 modal loops.
* **Batch Uploads:** Supports attaching multiple files in a single invocation via `filePaths`.
* **Iframe Support:** Can target file inputs inside embedded cross-frame components (e.g. job application wizards) via `frameId`.
* **Privacy & Path Redaction:** Successful responses sanitize and redact local system paths, returning abstract file descriptors (`fileName`, `fileSizeBytes`, `uploadId`).

---

## 2. Key Capabilities & Features

### A. Auto-Detection of File Inputs (`selector: "input[type=file]"`)
If no selector is provided, Nova automatically locates the first enabled file input on the page. Many drag-and-drop uploaders forward their visible drop zone to a hidden `<input type="file">` element; Nova attaches to that hidden input directly.

### B. Multi-File Selection
When the underlying input includes the `multiple` attribute, agents can provide multiple paths:
```json
{
  "selector": "input[name='attachments']",
  "filePaths": [
    "C:/workspace/reports/q3_summary.pdf",
    "C:/workspace/reports/data_table.csv"
  ]
}
```

### C. Iframe Targeting (`frameId`)
If the upload widget resides within an embedded iframe (e.g. recruitment widgets, payment document verifications):
1. Obtain the `frameId` from [`nova.perceive`](../dom-and-reading/nova-perceive.md).
2. Pass `frameId` to `nova.file_upload`. The selector is resolved inside that frame's isolated DOM context.

### D. Optional PDF Previews (`previewPdf: true`)
When uploading documents, passing `previewPdf: true` renders page 1 of each attached PDF as a compact JPEG preview in the tool result, allowing visual verification before form submission.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `filePaths` | `array` of `string` | No | — | ≥ 1 items | Preferred array of absolute local file paths to upload in one call. Use this even for new single-file callers. |
| `filePath` | `string` | No | — | — | Legacy alias for a single absolute local file path. Prefer filePaths for new callers. If both filePaths and filePath are provided, filePaths must contain exactly one matching entry. |
| `selector` | `string` | No | `"input[type=file]"` | — | CSS selector for the file input. Default: auto-detect first input[type=file]. |
| `frameId` | `string` | No | — | — | Optional frame ID (from perceive frames[]). When set, the selector is resolved inside that iframe's isolated world and the file is set on the element there. Omit for top-document uploads. A frame of another site (perceive opaqueFrames[].frameId) works too, unless the user turned off 'Let agents click and type in embedded content from other websites' (on by default); then the call is refused with reasonCode frame.cross_origin_interaction_off. |
| `previewPdf` | `boolean` | No | `false` | — | If true, page 1 of each uploaded PDF (up to 3) comes back as an image content item (JPEG, at most 900 px wide), so you can see what you attached before sending - e.g. leftover page CSS in a PDF made with nova.save_pdf. structuredContent.pdfPreviews[] lists index, fileName, pageCount and a reason when a PDF could not be rendered (damaged, password-protected). The upload itself never fails because of the preview. Costs one image per PDF, hence off by default. |
| `observe` | `object` | No | — | — | See what this action set off, in the same call: requests started by page JavaScript (fetch, XHR, WebSocket, sendBeacon) with method, url, status, ok and duration, whether the page navigated, and optionally the state of an element afterwards. Waits until no request is in flight and nothing new arrived for quietMs, at most waitMs. Pass {} for the defaults. Replaces network_read before and after the action plus dom_extract. Document navigations and images are not listed. |
| `observe.waitMs` | `integer` | No | `3000` | 0–15000 | Longest wait for the traffic to settle after the action. |
| `observe.quietMs` | `integer` | No | `500` | 100–5000 | How long nothing may be in flight or arrive before the traffic counts as settled. |
| `observe.urlContains` | `string` | No | — | ≤ 500 characters | List only requests whose URL contains this text (counts still cover all). |
| `observe.maxRequests` | `integer` | No | `20` | 1–100 | Most requests listed; requestsOmitted counts the rest. |
| `observe.texts` | `boolean` | No | `true` | — | List text that became visible after the action in newTexts: an error next to a field, a toast, a banner, a changed price. Entries inside an alert or live region carry alert:true. false skips the comparison. |
| `observe.maxTexts` | `integer` | No | `8` | 1–50 | Most new texts listed; newTextsOmitted counts the rest. |
| `observe.after` | `object` | No | — | — | Read an element once the traffic settled, like nova.dom_extract: {selector, properties}. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 4. Example Calls

### Standard Single File Upload
```json
{
  "selector": "#resume-upload-input",
  "filePaths": ["C:/Users/user/Documents/candidate_cv.pdf"]
}
```

### Drag-and-Drop Dropzone Auto-Detection
```json
{
  "filePaths": ["C:/workspace/images/product_hero.png"]
}
```

### Upload Inside an Embedded Iframe
```json
{
  "frameId": "frame-sub-8891",
  "selector": "input[type='file']",
  "filePaths": ["C:/data/export.xlsx"]
}
```

---

## 5. Return Value Structure

Nova validates file existence, size, and element `accept` filters before completing the upload. To preserve local privacy, raw filesystem directory structures are omitted from output:

```json
{
  "success": true,
  "targetId": "tab-102",
  "selector": "#resume-upload-input",
  "fileNames": ["candidate_cv.pdf"],
  "fileCount": 1,
  "uploadedFiles": [
    {
      "uploadId": "upl-4019",
      "index": 0,
      "fileName": "candidate_cv.pdf",
      "fileSizeBytes": 245800
    }
  ]
}
```
The response also includes `fileName` (single-file case), `uploadedFile`, `frameId`, `nodeId`, and `pdfPreviews` (when `previewPdf: true`); this is a trimmed excerpt. There is no `mimeType` field.

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `File not found: ...` | Local file does not exist at the specified path. | Verify the file path before invoking upload. |
| `Invalid params: selector '...' must match an <input type="file"> element.` | The resolved selector matches a `div`, `button`, or text input rather than `<input type="file">`. | Inspect the dropzone DOM with `nova.read_dom` to find the associated hidden `<input type="file">`. |
| `Invalid params: selector '...' does not allow multiple files. Choose an input with the multiple attribute or upload one file.` | Multiple paths were passed to an input lacking the `multiple` attribute. | Upload files individually, or target an input that declares `multiple`. |

---

## 7. Related Tools & Documentation

* [`nova.click_selector`](nova-click-selector.md) — Click submit buttons after attaching files.
* [`nova.perceive`](../dom-and-reading/nova-perceive.md) — Identify iframes and file upload widgets on the page.
* [Native Dialog Handling](../../../core-features/native-dialogs-and-prompts/README.md) — Understanding how Nova handles file open/save dialogs.
