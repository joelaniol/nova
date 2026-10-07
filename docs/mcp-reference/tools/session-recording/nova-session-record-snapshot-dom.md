# `nova.session_record_snapshot_dom`

Triggers a fresh encrypted DOM snapshot on an active live recording bound to a tab.

---

## 1. Overview

`nova.session_record_snapshot_dom` captures a complete DOM state snapshot while a recording is actively running. It serializes the live DOM hierarchy into an encrypted artifact inside the recording directory and indexes it with a unique `snapshotId`.

* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `recordingId` | `string` | No | — | — | Recording ID returned from session_record_start. Mutually exclusive with tabId — provide one or the other. |
| `tabId` | `string` | No | — | — | Browser tab ID. The active recording on that tab is used. Mutually exclusive with recordingId. |
| `selector` | `string` | No | — | — | Optional CSS selector. When omitted, captures document.activeElement (falling back to document.body). |
| `fullPage` | `boolean` | No | `false` | — | When true, capture document.documentElement instead of a single node. |

Capability bundle: `session_recording` (load it with `nova.tools_bundle(bundle='session_recording')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.session_record_snapshot_dom",
  "arguments": {
    "tabId": "tab-1",
    "fullPage": true
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Recording rec-9b21f04a: DOM snapshot snap-108a captured (70044 byte(s))."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "captured",
    "reasonCode": null,
    "recordingId": "rec-9b21f04a",
    "snapshotId": "snap-108a",
    "sizeBytes": 70044,
    "sha256": "8e4b7c129f...",
    "snapshotCount": 3,
    "maxSnapshots": 100,
    "quotaRemaining": 97
  }
}
```

A recording holds at most 100 DOM snapshots (`maxSnapshots`) by default; once `quotaRemaining` reaches 0 the call fails with a `cap_exceeded` reason instead of capturing.

---

## 4. Operational Best Practices

* **Milestone Snapshots:** Capture snapshots immediately before and after high-impact operations (e.g. form submission, dialog dismissal) to record visual DOM state changes.
* **Container Scoping:** Use `selector` to record dynamic popups, modals, or dropdown menus without capturing unnecessary parent page DOM.
* **Quota Awareness:** Watch `quotaRemaining` on noisy pages — clicks/submits also trigger automatic snapshots internally, so the 100-snapshot cap can be reached faster than the agent's own explicit calls would suggest.

---

## 5. Related Tools

* [`nova.session_record_dom_snapshot`](nova-session-record-dom-snapshot.md) — Retrieve and view stored snapshots.
* [`nova.session_record_start`](nova-session-record-start.md) — Start recording session.
