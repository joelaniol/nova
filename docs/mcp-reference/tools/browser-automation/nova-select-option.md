# `nova.select_option`

> **Selects an option in a standard HTML <select> dropdown by its value attribute or visible text.**

* **Core Feature Guide:** [Input Dispatch & Shadow DOM Traversal](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.select_option` targets standard HTML dropdown elements and dispatches appropriate change events.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `selector` | `string` | Yes | — | — | CSS selector for the native <select> element. Supports ' >>> ' combinator to pierce Shadow DOM boundaries. |
| `value` | `string` | No | — | — | Option value attribute to select. Preferred when the option value is stable. |
| `values` | `array` of `string` | No | — | — | Option value attributes to select for <select multiple>. Each item must be a string. Use this instead of value when selecting multiple options. |
| `text` | `string` | No | — | — | Visible option label to select when the value attribute is unknown. Whitespace is normalized before matching. |
| `texts` | `array` of `string` | No | — | — | Visible option labels to select for <select multiple>. Each item must be a string and is whitespace-normalized before matching. |
| `verify` | `boolean` | No | `true` | — | If true (default), verify that the final selected option or option set matches the requested selection. |
| `timeoutMs` | `integer` | No | `10000` | 0–300000 | Max ms to wait for the select element to become visible and ready. |
| `autoDismissBlockers` | `boolean` | No | `false` | — | If true, explicitly auto-dismiss overlays/modals blocking the target element before selecting. Default false: use overlayDetected plus cmp_apply/dismiss_blockers for consent banners. |
| `autoDismissMode` | `string` | No | `"conservative"` | `conservative`, `aggressive` | Blocker dismissal strategy. 'conservative': common banners only. 'aggressive': all overlay/fixed-position blockers. |
| `includeScreenshot` | `boolean` | No | `false` | — | If true, include a screenshot in the response after the selection attempt. Screenshot delivery is an optional sidecar: if capture fails, this result stays authoritative and structuredContent.screenshotStatus/screenshotReasonCode/screenshotRetryable/screenshotError describe the capture-only failure - do not repeat the action to get the image. |
| `screenshotMaxWidth` | `integer` | No | — | — | Max screenshot width in pixels. |
| `screenshotMaxHeight` | `integer` | No | — | — | Max screenshot height in pixels. |
| `screenshotFormat` | `string` | No | `"png"` | `png`, `jpeg`, `auto` | Screenshot format. Use 'auto' to fall back to the tool-intent default. |
| `screenshotQuality` | `integer` | No | `80` | 1–100 | JPEG quality (1-100). Only used when screenshotFormat is 'jpeg'. |

Capability bundles: `browser_automation`, `form_submission`.
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.select_option",
  "arguments": {
    "selector": "select#state",
    "value": "CA"
  }
}
```

### JSON-RPC Response (abbreviated)
```json
{
  "content": [
    {
      "type": "text",
      "text": "Selected option for 'select#state'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "selector": "select#state",
    "value": "CA",
    "verified": true
  }
}
```
The full payload also carries `targetId`, `stage`, the raw selection `result`, and screenshot-sidecar fields; this is a trimmed excerpt.

---

## 4. Operational Best Practices

* **Native Selects:** Fast and reliable for standard HTML forms.
* **Custom Widgets:** For ARIA or JavaScript-driven dropdowns, use `nova.choose_option` instead.

---

## 5. Related Tools

* [`nova.choose_option`](nova-choose-option.md)
