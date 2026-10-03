# `nova.session_record_snapshot_dom`

Triggers a fresh encrypted DOM snapshot on an active live recording bound to a tab.

---

## 1. Overview

`nova.session_record_snapshot_dom` captures a complete DOM state snapshot while a recording is actively running. It serializes the live DOM hierarchy into an encrypted artifact inside the recording directory and indexes it with a unique `snapshotId`.

* **Capability Bundle:** `session_recording`
* **Security Tier:** Tier 2 (Live DOM Capture)
* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`tabId`** | `string` | No | `null` | Browser tab target ID. Active recording on this tab will be captured. |
| **`recordingId`** | `string` | No | `null` | Recording ID. Mutually exclusive with `tabId`. |
| **`fullPage`** | `boolean` | No | `false` | When true, captures entire `document.documentElement` instead of focused element. |
| **`selector`** | `string` | No | `null` | CSS selector scoping capture to a container (e.g. `"#modal-container"`). |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

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
      "text": "Captured DOM snapshot 'snap-108a' on recording rec-9b21f04a."
    }
  ],
  "structuredContent": {
    "ok": true,
    "snapshotId": "snap-108a",
    "recordingId": "rec-9b21f04a",
    "nodeCount": 1420,
    "characterLength": 68420,
    "capturedAtUtc": "2026-10-02T20:20:00Z"
  }
}
```

---

## 4. Operational Best Practices

* **Milestone Snapshots:** Capture snapshots immediately before and after high-impact operations (e.g. form submission, dialog dismissal) to record visual DOM state changes.
* **Container Scoping:** Use `selector` to record dynamic popups, modals, or dropdown menus without capturing unnecessary parent page DOM.

---

## 5. Related Tools

* [`nova.session_record_dom_snapshot`](nova-session-record-dom-snapshot.md) — Retrieve and view stored snapshots.
* [`nova.session_record_start`](nova-session-record-start.md) — Start recording session.
