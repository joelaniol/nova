# `nova.capture_app_screenshot`

> **Captures a screenshot of the entire Nova host application window including tabs and window chrome.**

* **Capability Bundle:** `visual_evidence`
* **Security Tier:** Tier 1 (Read-Only Capture)
* **Core Feature Guide:** [Visual Evidence & Auditing](../../../core-features/evm-and-visual-evidence.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.capture_app_screenshot` takes a picture of the outer WinUI shell, tab bar, terminal dock, and window frame for full application evidence.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization. Defaults to 'default'. A foreign active-target claim selects the fail-closed shell-redacted read-only path. |
| `format` | `string` | No | Image format override. Default jpeg (Tool-Intent-Profile). |
| `maxHeight` | `integer` | No | Legacy alias for screenshotMaxHeight. Max screenshot height in pixels. |
| `maxWidth` | `integer` | No | Legacy alias for screenshotMaxWidth. Max screenshot width in pixels. |
| `quality` | `integer` | No | JPEG quality 1-100. Ignored for png. Default 72 (Tool-Intent-Profile). |
| `responseMode` | `string` | No | Wire-mode for the screenshot. Default 'thumbnail+reference' (Tool-Intent-Profile): full image stored as resource (read via nova.read_screenshot_resource(uri=...) or MCP resources/read) plus a small inline thumbnail. 'auto' resolves to inline or thumbnail+reference based on projected vision-tokens and session-budget headroom. |
| `screenshotMaxHeight` | `integer` | No | Preferred screenshot height limit in pixels. Must match maxHeight if both are provided. |
| `screenshotMaxWidth` | `integer` | No | Preferred screenshot width limit in pixels. Must match maxWidth if both are provided. |
| `targetId` | `string` | No | Target ID from nova.tabs, or 'active' / 'activeBrowserTab'. Nova may activate and later best-effort restore a non-active target only on the full authorized path; a target observed as foreign-claimed while inactive fails with app_target_not_active without activation. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_capture_app_screenshot",
  "arguments": {
    "quality": 80
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Captured app window screenshot (1920x1080)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "width": 1920,
    "height": 1080,
    "uri": "nova://screenshot/app-snap-01"
  }
}
```

---

## 4. Operational Best Practices

* **Shell QA:** Use to verify native tab styling, window docking, and settings drawer overlays.

---

## 5. Related Tools

* [`nova.capture_screenshot`](nova-capture-screenshot.md)
* [`nova.read_screenshot_resource`](../app-shell-and-ui/nova-read-screenshot-resource.md)
