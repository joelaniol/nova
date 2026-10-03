# `nova.wait_for_modal`

> **Blocks execution until a modal dialog or overlay appears or closes in the document.**

* **Capability Bundle:** `browser_automation`
* **Security Tier:** Tier 1 (Synchronization)
* **Core Feature Guide:** [Humanized Input & Navigation](../../../core-features/humanized-input-engine.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.wait_for_modal` polls the DOM for common modal patterns (`role="dialog"`, `.modal`, backdrop elements) and awaits settlement.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `timeoutMs` | `integer` | No | `10000` | 0–300000 | Max ms to wait before returning timeout. |
| `pollMs` | `integer` | No | `250` | 50–2000 | Polling interval in ms. |
| `maxResults` | `integer` | No | `10` | 1–50 | Maximum modals to collect per probe. |
| `visibleOnly` | `boolean` | No | `true` | — | If true, only consider visible modals/dialogs. |
| `deep` | `boolean` | No | `true` | — | If true, includes same-origin iframe + open shadow-root traversal. |
| `includeScreenshot` | `boolean` | No | `false` | — | If true and modal is found, include a screenshot in the response. |
| `screenshotMaxWidth` | `integer` | No | — | — | Max screenshot width in pixels. |
| `screenshotMaxHeight` | `integer` | No | — | — | Max screenshot height in pixels. |
| `screenshotFormat` | `string` | No | `"png"` | `png`, `jpeg`, `auto` | Screenshot format. Use 'auto' to fall back to the tool-intent default (e.g. jpeg q=72 for confirm-shots). |
| `screenshotQuality` | `integer` | No | `80` | 1–100 | JPEG quality (1-100). Only used when screenshotFormat is 'jpeg'. |
| `screenshotResponseMode` | `string` | No | — | `inline`, `reference`, `thumbnail+reference`, `auto` | Override default delivery mode for the screenshot. Default comes from the tool-intent profile (e.g. confirm-shots default 'thumbnail+reference' for token efficiency). Use 'inline' to force full image bytes, 'auto' to let the server pick based on projected token cost and session budget. |
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_wait_for_modal",
  "arguments": {
    "targetId": "tab-1",
    "mode": "appear",
    "timeoutMs": 5000
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Modal dialog appeared."
    }
  ],
  "structuredContent": {
    "ok": true,
    "modalFound": true,
    "selector": ".confirmation-modal"
  }
}
```

---

## 4. Operational Best Practices

* **Pre-Dismissal Check:** Use before calling `nova.dismiss_blockers` to ensure the modal has finished animating in.

---

## 5. Related Tools

* [`nova.dismiss_blockers`](nova-dismiss-blockers.md)
* [`nova.wait_for_selector`](nova-wait-for-selector.md)
