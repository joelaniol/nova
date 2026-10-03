# `nova.session_record_dom_snapshot`

Retrieves and decrypts a previously stored DOM snapshot HTML payload by snapshot ID.

---

## 1. Overview

`nova.session_record_dom_snapshot` retrieves the serialized HTML payload of a DOM snapshot stored during a session recording. It decrypts the chunk from disk and returns the clean HTML string or raw base64 bytes for time-travel DOM analysis.

* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Session Recording & Time-Travel Debugging](../../../core-features/session-recording.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `recordingId` | `string` | Yes | — | — | Recording ID. |
| `snapshotId` | `string` | Yes | — | — | Snapshot ID returned in the dom-snapshots.jsonl index. |
| `asText` | `boolean` | No | `true` | — | Decode the HTML payload as UTF-8 text. Set false to receive raw base64 bytes (e.g. for binary tooling). |

Capability bundle: `session_recording` (load it with `nova.tools_bundle(bundle='session_recording')`).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.session_record_dom_snapshot",
  "arguments": {
    "recordingId": "rec-9b21f04a",
    "snapshotId": "snap-108a",
    "asText": true
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Decrypted DOM snapshot snap-108a (68 KB HTML)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "snapshotId": "snap-108a",
    "recordingId": "rec-9b21f04a",
    "html": "<!DOCTYPE html><html><head><title>Checkout</title></head><body>...</body></html>"
  }
}
```

---

## 4. Operational Best Practices

* **Time-Travel Verification:** Compare snapshots from before and after an action to verify that elements appeared or disappeared as expected.
* **Offline Inspection:** Once decrypted, analyze DOM elements using standard string parsing or CSS selector evaluation without live browser connections.

---

## 5. Related Tools

* [`nova.session_record_snapshot_dom`](nova-session-record-snapshot-dom.md) — Capture live snapshots.
* [`nova.read_dom`](../dom-and-reading/nova-read-dom.md) — Read active live tab DOM.
