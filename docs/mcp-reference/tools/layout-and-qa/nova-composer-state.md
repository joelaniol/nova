# `nova.composer_state`

> **Reads what is currently sitting in a chat composer: its text, its attachments, and whether the send control looks ready.**

* **Core Feature Guide:** [Visual Evidence & Layout QA](../../../research/evidence-verification-mode-evm/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.composer_state` is a read-only answer to "what is currently in the composer, and can it be sent?" — it never types, clicks, or sends. It resolves the composer with the same resolver `nova.guarded_send_message` uses (cache, then heuristics), so a state read and the send that follows it agree on which input, send button, and container they mean; pass `selector` to name the input explicitly instead.

It reports three things:
* **Text:** the composer's current value (`value`, trimmed length via `empty`, raw `chars`).
* **Attachments:** a tri-state `status` — `detected` (files on a file input, or a vendor "chip" matched in the composer container), `none_detected` (the container was searched and nothing was found — not proof there are none, vendor markup differs), or `unknown` (no container to search). Files on a file input are hard evidence (name + size); DOM chips are indications only.
* **Send readiness:** `status` of `ready`, `not_ready`, or `unknown` — `unknown` is the normal empty state on chat surfaces where the send button only appears once text exists.

A page without a resolvable composer answers `ok: false` with a `reasonCode` (`composer.not_found`, `composer.send_not_found`, `composer.ambiguous`, or `composer.input_not_found`) instead of an error — a missing composer is a legitimate answer, not a failure.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `selector` | `string` | No | — | ≤ 10000 characters | Optional CSS selector for the composer input. Omit to let Nova resolve the composer (cache, then heuristics). |
| `frameId` | `string` | No | — | — | Optional same-origin frame ID from nova.perceive(deep=true).structuredContent.frames[]. |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.composer_state",
  "arguments": {
    "targetId": "tab-1",
    "selector": ".ProseMirror"
  }
}
```

### JSON-RPC Response (composer found)
```json
{
  "content": [
    {
      "type": "text",
      "text": "{\"ok\":true,\"found\":true,\"url\":\"https://chat.example.com/\",\"inputSelector\":\".ProseMirror\",\"containerSelector\":\"form\",\"text\":{\"value\":\"Draft reply\",\"chars\":11,\"empty\":false},\"attachments\":{\"status\":\"none_detected\",\"fileInputs\":[],\"chips\":[],\"searchScope\":\"form\"},\"send\":{\"status\":\"ready\",\"selector\":\"button[data-testid=send-button]\",\"detail\":{\"disabled\":false,\"visible\":true,\"tag\":\"button\"}}}"
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "ok": true,
    "status": "ok",
    "reasonCode": null,
    "stage": "read",
    "retryable": null,
    "composer": {
      "inputSelector": ".ProseMirror",
      "sendSelector": "button[data-testid=send-button]",
      "containerSelector": "form",
      "resolutionSource": "caller",
      "pairConfidence": null,
      "frameId": null
    },
    "state": { "...": "the probe object shown above as text" },
    "pageUrl": "https://chat.example.com/",
    "toolName": "nova.composer_state"
  }
}
```

### JSON-RPC Response (no composer on this page)
```json
{
  "structuredContent": {
    "targetId": "tab-1",
    "ok": false,
    "status": "not_found",
    "reasonCode": "composer.not_found",
    "stage": "read",
    "retryable": false,
    "composer": null,
    "state": null,
    "pageUrl": "https://example.com/",
    "toolName": "nova.composer_state"
  }
}
```

---

## 4. Operational Best Practices

* **Pre-send sanity check:** Read the composer before [`nova.guarded_send_message`](../guarded-actions/nova-guarded-send-message.md) to confirm the text and attachments are what you expect, and that `send.status` is `ready`.
* **Attachment caution:** Treat `attachments.status: "none_detected"` as "nothing found by the known selectors", not as proof the composer holds no files — vendor markup varies.

---

## 5. Related Tools

* [`nova.guarded_send_message`](../guarded-actions/nova-guarded-send-message.md) — Sends through the same composer resolver this tool reads.
* [`nova.type_selector`](../browser-automation/nova-type-selector.md)
* [`nova.measure_elements`](nova-measure-elements.md)
