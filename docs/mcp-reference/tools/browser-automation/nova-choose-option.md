# `nova.choose_option`

> **Selects an option from a custom UI or standard dropdown by visible text or index.**

* **Capability Bundle:** `browser_automation`
* **Security Tier:** Tier 2 (DOM Input)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.choose_option` selects a choice from both native `<select>` dropdowns and popular custom ARIA combobox widgets (e.g. React Select, Radix UI).

---

## 2. Parameter Reference

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `autoDismissBlockers` | `boolean` | No | If true, explicitly auto-dismiss overlays/modals blocking the target element before interaction. Default false: use overlayDetected plus cmp_apply/dismiss_blockers for consent banners. |
| `autoDismissMode` | `string` | No | Blocker dismissal strategy. 'conservative': common banners only. 'aggressive': all overlay/fixed-position blockers. |
| `includeScreenshot` | `boolean` | No | If true, include a screenshot in the response after the interaction attempt. Screenshot delivery is an optional sidecar: if capture fails, this result stays authoritative and structuredContent.screenshotStatus/screenshotReasonCode/screenshotRetryable/screenshotError describe the capture-only failure - do not repeat the action to get the image. |
| `screenshotFormat` | `string` | No | Screenshot format. Use 'auto' to fall back to the tool-intent default. |
| `screenshotMaxHeight` | `integer` | No | Max screenshot height in pixels. |
| `screenshotMaxWidth` | `integer` | No | Max screenshot width in pixels. |
| `screenshotQuality` | `integer` | No | JPEG quality (1-100). Only used when screenshotFormat is 'jpeg'. |
| `selector` | `string` | **Yes** | CSS selector for the choice control element. Can target the <select>, the combobox trigger, a listbox container, a radiogroup, or an individual radio. Supports ' >>> ' combinator to pierce Shadow DOM boundaries. |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `text` | `string` | No | Visible option label to select (single). Matched against textContent, aria-label, or associated label text. Whitespace is normalized before matching. |
| `texts` | `array` | No | Multiple option labels to select (for multi-select listboxes). Each matched against textContent or aria-label. Use when perceive reports selectionMode='multiple'. |
| `timeoutMs` | `integer` | No | Max ms to wait for the element to become visible and for popup interactions (combobox open/close). |
| `value` | `string` | No | Option value to select (single). Matched against option value attribute, data-value, or radio value. Preferred when the value is stable. |
| `values` | `array` | No | Multiple option values to select (for multi-select listboxes). Each matched against data-value or value attribute. Use when perceive reports selectionMode='multiple'. |
| `verify` | `boolean` | No | If true (default), verify that the final selection matches the requested option after interaction. |

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_choose_option",
  "arguments": {
    "selector": "#country-picker",
    "text": "Germany"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Selected option 'Germany' in #country-picker."
    }
  ],
  "structuredContent": {
    "ok": true,
    "selector": "#country-picker",
    "selectedText": "Germany",
    "value": "DE"
  }
}
```

---

## 4. Operational Best Practices

* **Custom Comboboxes:** Handles modern ARIA listboxes where options reside outside the trigger container.
* **Visible Text Match:** Matches visible label text case-insensitively.

---

## 5. Related Tools

* [`nova.select_option`](nova-select-option.md)
* [`nova.click_selector`](nova-click-selector.md)
