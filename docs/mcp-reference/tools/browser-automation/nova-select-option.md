# `nova.select_option`

> **Selects an option in a standard HTML <select> dropdown by its value attribute.**

* **Capability Bundle:** `browser_automation`
* **Security Tier:** Tier 2 (DOM Input)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.select_option` targets standard HTML dropdown elements and dispatches appropriate change events.

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `autoDismissBlockers` | `boolean` | No | If true, explicitly auto-dismiss overlays/modals blocking the target element before selecting. Default false: use overlayDetected plus cmp_apply/dismiss_blockers for consent banners. |
| `autoDismissMode` | `string` | No | Blocker dismissal strategy. 'conservative': common banners only. 'aggressive': all overlay/fixed-position blockers. |
| `includeScreenshot` | `boolean` | No | If true, include a screenshot in the response after the selection attempt. Screenshot delivery is an optional sidecar: if capture fails, this result stays authoritative and structuredContent.screenshotStatus/screenshotReasonCode/screenshotRetryable/screenshotError describe the capture-only failure - do not repeat the action to get the image. |
| `screenshotFormat` | `string` | No | Screenshot format. Use 'auto' to fall back to the tool-intent default. |
| `screenshotMaxHeight` | `integer` | No | Max screenshot height in pixels. |
| `screenshotMaxWidth` | `integer` | No | Max screenshot width in pixels. |
| `screenshotQuality` | `integer` | No | JPEG quality (1-100). Only used when screenshotFormat is 'jpeg'. |
| `selector` | `string` | **Yes** | CSS selector for the native <select> element. Supports ' >>> ' combinator to pierce Shadow DOM boundaries. |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `text` | `string` | No | Visible option label to select when the value attribute is unknown. Whitespace is normalized before matching. |
| `texts` | `array` | No | Visible option labels to select for <select multiple>. Each item must be a string and is whitespace-normalized before matching. |
| `timeoutMs` | `integer` | No | Max ms to wait for the select element to become visible and ready. |
| `value` | `string` | No | Option value attribute to select. Preferred when the option value is stable. |
| `values` | `array` | No | Option value attributes to select for <select multiple>. Each item must be a string. Use this instead of value when selecting multiple options. |
| `verify` | `boolean` | No | If true (default), verify that the final selected option or option set matches the requested selection. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_select_option",
  "arguments": {
    "selector": "select#state",
    "value": "CA"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Selected value 'CA' in select#state."
    }
  ],
  "structuredContent": {
    "ok": true,
    "selector": "select#state",
    "selectedValue": "CA"
  }
}
```

---

## 4. Operational Best Practices

* **Native Selects:** Fast and reliable for standard HTML forms.
* **Custom Widgets:** For ARIA or JavaScript-driven dropdowns, use `nova.choose_option` instead.

---

## 5. Related Tools

* [`nova.choose_option`](nova-choose-option.md)
