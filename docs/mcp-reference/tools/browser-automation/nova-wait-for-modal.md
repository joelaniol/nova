# `nova.wait_for_modal`

> **Waits until a modal dialog or overlay appears in the document and returns it.**

* **Core Feature Guide:** [Surface Explorer](../../../core-features/crawler-and-discovery/surface-explorer/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.wait_for_modal` polls the page every `pollMs` until at least one dialog or overlay is present (`role="dialog"`, `aria-modal="true"`, `<dialog>`, or class names containing modal, overlay or popup), then returns the detected elements with title, text, selector and buttons. It waits for a dialog to appear; it does not wait for one to close. The response example below is an excerpt; each modal entry also carries `scope` and `rect`, and the probe a `meta` block.

If no dialog appears within `timeoutMs`, the call returns `ok: false` with `reasonCode: "wait_for_modal.timeout"` and the last probe in `lastProbe`.

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

Capability bundle: `browser_automation` (load it with `nova.tools_bundle(bundle='browser_automation')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_wait_for_modal",
  "arguments": {
    "targetId": "tab-1",
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
      "text": "Modal detected after 640ms."
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "ok": true,
    "changed": true,
    "warnings": [],
    "waitedMs": 640,
    "deep": true,
    "visibleOnly": true,
    "maxResults": 10,
    "result": {
      "ok": true,
      "mode": "modals_wait_probe",
      "count": 1,
      "modals": [
        {
          "type": "dialog",
          "title": "Confirm deletion",
          "text": "Delete this item? This cannot be undone.",
          "role": "dialog",
          "visible": true,
          "selector": "#confirm-dialog",
          "buttons": [
            {
              "label": "Cancel",
              "tag": "button",
              "visible": true,
              "selector": "#confirm-dialog > button:nth-of-type(1)"
            },
            {
              "label": "Delete",
              "tag": "button",
              "visible": true,
              "selector": "#confirm-dialog > button:nth-of-type(2)"
            }
          ]
        }
      ]
    }
  }
}
```

---

## 4. Operational Best Practices

* **Pre-Dismissal Check:** Use before calling `nova.dismiss_blockers` to make sure the dialog is present.
* **Button Selectors:** The returned button selectors can be passed straight to `nova.click_selector`.

---

## 5. Related Tools

* [`nova.dismiss_blockers`](nova-dismiss-blockers.md)
* [`nova.wait_for_selector`](nova-wait-for-selector.md)
