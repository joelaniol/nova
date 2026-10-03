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

| Parameter | Type | Required | Description |
| :--- | :---: | :---: | :--- |
| `_meta` | `object` | No | Optional MCP request metadata (e.g. _meta.intent). Accepted on every tool; annotations.intentRequired says when intent is expected. |
| `agentId` | `string` | No | Optional agent identity for claim authorization at the MCP entry point. Defaults to 'default'. |
| `deep` | `boolean` | No | If true, includes same-origin iframe + open shadow-root traversal. |
| `includeScreenshot` | `boolean` | No | If true and modal is found, include a screenshot in the response. |
| `maxResults` | `integer` | No | Maximum modals to collect per probe. |
| `pollMs` | `integer` | No | Polling interval in ms. |
| `screenshotFormat` | `string` | No | Screenshot format. Use 'auto' to fall back to the tool-intent default (e.g. jpeg q=72 for confirm-shots). |
| `screenshotMaxHeight` | `integer` | No | Max screenshot height in pixels. |
| `screenshotMaxWidth` | `integer` | No | Max screenshot width in pixels. |
| `screenshotQuality` | `integer` | No | JPEG quality (1-100). Only used when screenshotFormat is 'jpeg'. |
| `screenshotResponseMode` | `string` | No | Override default delivery mode for the screenshot. Default comes from the tool-intent profile (e.g. confirm-shots default 'thumbnail+reference' for token efficiency). Use 'inline' to force full image bytes, 'auto' to let the server pick based on projected token cost and session budget. |
| `targetId` | `string` | No | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `timeoutMs` | `integer` | No | Max ms to wait before returning timeout. |
| `visibleOnly` | `boolean` | No | If true, only consider visible modals/dialogs. |

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
