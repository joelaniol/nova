# `nova.choose_option`

> **Selects an option from a custom UI or standard dropdown by visible text or value.**

* **Core Feature Guide:** [Input Dispatch & Shadow DOM Traversal](../../../core-features/humanized-input-engine/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.choose_option` selects a choice from both native `<select>` dropdowns and popular custom ARIA combobox widgets (e.g. React Select, Radix UI).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `selector` | `string` | Yes | — | — | CSS selector for the choice control element. Can target the <select>, the combobox trigger, a listbox container, a radiogroup, or an individual radio. Supports ' >>> ' combinator to pierce Shadow DOM boundaries. |
| `value` | `string` | No | — | — | Option value to select (single). Matched against option value attribute, data-value, or radio value. Preferred when the value is stable. |
| `text` | `string` | No | — | — | Visible option label to select (single). Matched against textContent, aria-label, or associated label text. Whitespace is normalized before matching. |
| `values` | `array` of `string` | No | — | — | Multiple option values to select (for multi-select listboxes). Each matched against data-value or value attribute. Use when perceive reports selectionMode='multiple'. |
| `texts` | `array` of `string` | No | — | — | Multiple option labels to select (for multi-select listboxes). Each matched against textContent or aria-label. Use when perceive reports selectionMode='multiple'. |
| `verify` | `boolean` | No | `true` | — | If true (default), verify that the final selection matches the requested option after interaction. |
| `timeoutMs` | `integer` | No | `10000` | 0–300000 | Max ms to wait for the element to become visible and for popup interactions (combobox open/close). |
| `autoDismissBlockers` | `boolean` | No | `false` | — | If true, explicitly auto-dismiss overlays/modals blocking the target element before interaction. Default false: use overlayDetected plus cmp_apply/dismiss_blockers for consent banners. |
| `autoDismissMode` | `string` | No | `"conservative"` | `conservative`, `aggressive` | Blocker dismissal strategy. 'conservative': common banners only. 'aggressive': all overlay/fixed-position blockers. |
| `includeScreenshot` | `boolean` | No | `false` | — | If true, include a screenshot in the response after the interaction attempt. Screenshot delivery is an optional sidecar: if capture fails, this result stays authoritative and structuredContent.screenshotStatus/screenshotReasonCode/screenshotRetryable/screenshotError describe the capture-only failure - do not repeat the action to get the image. |
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
  "name": "nova.choose_option",
  "arguments": {
    "selector": "#country-picker",
    "text": "Germany"
  }
}
```

### JSON-RPC Response (abbreviated)
```json
{
  "content": [
    {
      "type": "text",
      "text": "Chose option for '#country-picker' (controlKind=\"select\")."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "selector": "#country-picker",
    "text": "Germany",
    "controlKind": "select",
    "result": {
      "selectedText": "Germany"
    }
  }
}
```
The full payload also carries `targetId`, `stage`, `pageTitle`/`pageUrl`, and screenshot-sidecar fields; this is a trimmed excerpt.

---

## 4. Operational Best Practices

* **Custom Comboboxes:** Handles modern ARIA listboxes where options reside outside the trigger container.
* **Visible Text Match:** Matches against `textContent`, `aria-label`, or associated label text, with whitespace normalized before comparison.

---

## 5. Related Tools

* [`nova.select_option`](nova-select-option.md)
* [`nova.click_selector`](nova-click-selector.md)
