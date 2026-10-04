# `nova.capture_app_screenshot`

> **Captures the Nova app window (tabs, topbar, WebView content) — or, if another agent holds the active tab's claim, a read-only redacted shell view with page content masked out.**

* **Core Feature Guide:** [Visual Evidence & Auditing](../../../core-features/evm-and-visual-evidence.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.capture_app_screenshot` takes a picture of the Nova app window — tabs, topbar, and the active WebView content — for app-chrome and orientation evidence. It is NOT the tool for reading page text (use [`nova.capture_screenshot`](nova-capture-screenshot.md) with a `selector`/`region` crop plus [`nova.search_text`](../dom-and-reading/nova-search-text.md) or `nova.eval` for that).

An unclaimed target, or one claimed by the calling agent, returns the full app UI. If another owner/session currently claims the active target, Nova instead attempts a read-only `status: "partial"` capture with `captureScope: "shell_redacted"`: tab titles, the URL, bookmarks, page content, and tab-bound overlays are masked out before the image is scaled, hashed, or stored. If Nova cannot prove the protected regions are stable, it fails closed with `reasonCode: "app_shell_redaction_unavailable"` rather than risk leaking the foreign tab's content. A target that is foreign-claimed while inactive is never activated by this call; it fails with `app_target_not_active`.

The capture also checks the WebView area for an all-dark/blank frame and reports `status: "degraded"` with a `webViewContentReasonCode` when the content looks unusable.

Nova's own dialogs, flyouts, menus and the address-bar suggestion list sit on a separate layer above the window. The capture draws every open one into the image and lists them in `openPopups`, topmost first: `kind` (`dialog`, `backdrop` for a dialog's dimming layer, or `popup`), `name` (dialog title or accessible name, when there is one), `element` (UI element type), the position in image pixels, and `rendered`. In a shell-redacted capture they are listed with `rendered: false` and not drawn, because a popup can show the foreign tab's content.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `agentId` | `string` | No | `"default"` | — | Optional agent identity for claim authorization. Defaults to 'default'. A foreign active-target claim selects the fail-closed shell-redacted read-only path. |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs, or 'active' / 'activeBrowserTab'. Nova may activate and later best-effort restore a non-active target only on the full authorized path; a target observed as foreign-claimed while inactive fails with app_target_not_active without activation. |
| `maxWidth` | `integer` | No | — | 1–10000 | Legacy alias for screenshotMaxWidth. Max screenshot width in pixels. |
| `maxHeight` | `integer` | No | — | 1–10000 | Legacy alias for screenshotMaxHeight. Max screenshot height in pixels. |
| `screenshotMaxWidth` | `integer` | No | — | 1–10000 | Preferred screenshot width limit in pixels. Must match maxWidth if both are provided. |
| `screenshotMaxHeight` | `integer` | No | — | 1–10000 | Preferred screenshot height limit in pixels. Must match maxHeight if both are provided. |
| `format` | `string` | No | — | `png`, `jpeg` | Image format override. Default jpeg (Tool-Intent-Profile). |
| `quality` | `integer` | No | — | 1–100 | JPEG quality 1-100. Ignored for png. Default 72 (Tool-Intent-Profile). |
| `responseMode` | `string` | No | — | `inline`, `reference`, `thumbnail+reference`, `auto` | Wire-mode for the screenshot. Default 'thumbnail+reference' (Tool-Intent-Profile): full image stored as resource (read via nova.read_screenshot_resource(uri=...) or MCP resources/read) plus a small inline thumbnail. 'auto' resolves to inline or thumbnail+reference based on projected vision-tokens and session-budget headroom. |

Capability bundles: `app_shell_recovery`, `page_read_debug`, `visual_evidence`.
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.capture_app_screenshot",
  "arguments": {
    "quality": 80
  }
}
```

### JSON-RPC Response (full capture)
```json
{
  "structuredContent": {
    "status": "ok",
    "degraded": false,
    "captureScope": "full",
    "redacted": false,
    "redactionReasonCode": null,
    "pageContentAvailable": true,
    "bytes": 184320,
    "pixelWidth": 1920,
    "pixelHeight": 1080,
    "scaled": false,
    "sourcePixelWidth": 1920,
    "sourcePixelHeight": 1080,
    "webViewOnly": false,
    "webViewContentOk": true,
    "openPopups": [
      { "kind": "dialog", "name": "Welcome to Nova", "element": "ContentDialog", "pixelX": 0, "pixelY": 0, "pixelWidth": 1920, "pixelHeight": 1080, "rendered": true },
      { "kind": "backdrop", "name": null, "element": "Rectangle", "pixelX": 0, "pixelY": 0, "pixelWidth": 1920, "pixelHeight": 1080, "rendered": true }
    ],
    "targetId": "tab-1",
    "resource": { "uri": "nova://screenshot/<id>", "mimeType": "image/jpeg", "size": 184320 },
    "filePath": "C:\\Users\\me\\AppData\\Local\\NovaBrowser\\Screenshots\\<id>.jpg"
  }
}
```

### JSON-RPC Response (foreign claim — shell-redacted)
```json
{
  "content": [
    { "type": "text", "text": "Partial app-shell screenshot: tab titles, URL, bookmarks, page content, and tab-bound overlays are redacted because another owner/session holds the active-tab claim." }
  ],
  "structuredContent": {
    "status": "partial",
    "captureScope": "shell_redacted",
    "redacted": true,
    "redactionReasonCode": null,
    "pageContentAvailable": false
  }
}
```

Fields shown above are a representative subset; the full response also carries `rasterizationScale`, `webViewPixelX/Y/Width/Height`, `captureFallbackUsed`/`captureFallbackReason`, `byteAccounting`, `tokens`, `deliveryMode`, `inlinePreview`/`evidenceImage`, `readabilityRisk`, and `evidenceGuidance` — the same telemetry shape as `nova.capture_screenshot`.

---

## 4. Operational Best Practices

* **Shell QA:** Use to verify native tab styling, window docking, and settings drawer overlays.
* **Dialogs:** When Nova shows one of its own dialogs, this is the tool that shows its text and buttons; check `openPopups` to know a dialog is open before acting on the page.
* **Foreign-claim awareness:** A `status: "partial"` / `captureScope: "shell_redacted"` result is not a bug — it means another agent/session holds the active tab's claim, and page content was intentionally masked. Wait for the claim to release, or capture from the owning session.

---

## 5. Related Tools

* [`nova.capture_screenshot`](nova-capture-screenshot.md)
* [`nova.read_screenshot_resource`](../app-shell-and-ui/nova-read-screenshot-resource.md)
