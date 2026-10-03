# `nova.file_upload`

Attaches one or more local files directly to an HTML `<input type="file">` element via Chrome DevTools Protocol (CDP), bypassing native OS file picker dialogs.

---

## 1. Overview

Traditional browser automation fails when clicking an `<input type="file">` because it triggers a modal Windows File Open dialog that freezes DOM execution. `nova.file_upload` bypasses the native dialog entirely by assigning file handles directly via CDP (`DOM.setFileInputFiles`).

* **Capability Bundle:** `browser_automation`, `form_submission`
* **Native Dialog Bypass:** No OS file picker is opened; execution never hangs on Win32 modal loops.
* **Batch Uploads:** Supports attaching multiple files in a single invocation via `filePaths`.
* **Iframe Support:** Can target file inputs inside embedded cross-frame components (e.g. job application wizards) via `frameId`.
* **Privacy & Path Redaction:** Successful responses sanitize and redact local system paths, returning abstract file descriptors (`fileName`, `fileSizeBytes`, `uploadId`).

---

## 2. Key Capabilities & Features

### A. Auto-Detection of File Inputs (`selector: "input[type=file]"`)
If no selector is provided, Nova automatically locates the first enabled file input on the page. For modern drag-and-drop file uploaders (like ChatGPT, GitHub, or Slack), the visible drag zone almost always forwards events to a hidden `<input type="file">` element; Nova attaches to that hidden input directly.

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
| `frameId` | `string` | No | — | — | Optional same-origin frame ID (from perceive frames[]). When set, the selector is resolved inside that iframe's isolated world and the file is set on the element there. Omit for top-document uploads. |
| `previewPdf` | `boolean` | No | `false` | — | If true, page 1 of each uploaded PDF (up to 3) comes back as an image content item (JPEG, at most 900 px wide), so you can see what you attached before sending - e.g. leftover page CSS in a PDF made with nova.save_pdf. structuredContent.pdfPreviews[] lists index, fileName, pageCount and a reason when a PDF could not be rendered (damaged, password-protected). The upload itself never fails because of the preview. Costs one image per PDF, hence off by default. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.
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
  "uploadedFiles": [
    {
      "uploadId": "upl-4019",
      "index": 0,
      "fileName": "candidate_cv.pdf",
      "fileSizeBytes": 245800,
      "mimeType": "application/pdf"
    }
  ],
  "selector": "#resume-upload-input",
  "targetId": "tab-102"
}
```

---

## 6. Common Errors & Troubleshooting

| Error Code / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `File not found: ...` | Local file does not exist at specified path. | Verify file path before invoking upload. |
| `Element is not a file input` | The resolved selector matches a `div`, `button`, or text input rather than `<input type="file">`. | Inspect the dropzone DOM with `nova.read_dom` to find the associated hidden `<input type="file">`. |
| `Element does not allow multiple files` | Multiple paths were passed to an input lacking the `multiple` attribute. | Upload files individually or inspect if another upload input exists. |

---

## 7. Related Tools & Documentation

* [`nova.click_selector`](nova-click-selector.md) — Click submit buttons after attaching files.
* [`nova.perceive`](../dom-and-reading/nova-perceive.md) — Identify iframes and file upload widgets on the page.
* [Native Dialog Handling](../../../core-features/native-dialogs-and-prompts.md) — Understanding how Nova handles file open/save dialogs.
