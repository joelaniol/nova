# Session Tracing & DOM Event Recording

Network HAR capture, user interaction timelines, DOM change snapshots, and replay verification.

* **Capability Bundle(s):** `session_recording`
* **Core Architecture Guide:** [Core Features: session-recording.md](../../../core-features/session-recording.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## Tool Inventory (14 Tools)

| Tool Name | Status | Description |
| :--- | :---: | :--- |
| **[`nova.session_record_dom_snapshot`](nova-session-record-dom-snapshot.md)** | Documented | Return a stored DOM snapshot blob by snapshotId. |
| **[`nova.session_record_events`](nova-session-record-events.md)** | Documented | Decrypt and return a generic stream from a recording (console, errors, lifecycle, indexedDB). |
| **[`nova.session_record_export`](nova-session-record-export.md)** | Documented | Decode a finalised recording to plaintext files on disk and return their paths. |
| **[`nova.session_record_extend`](nova-session-record-extend.md)** | Documented | Extend a recording's TTL by additionalMs. |
| **[`nova.session_record_get_entry`](nova-session-record-get-entry.md)** | Documented | Return the full event timeline for a single requestId in a recording. |
| **[`nova.session_record_interactions`](nova-session-record-interactions.md)** | Documented | Read the interaction timeline from a finalised session recording. |
| **[`nova.session_record_purge`](nova-session-record-purge.md)** | Documented | Delete finalised recordings older than the given threshold (whole dirs). |
| **[`nova.session_record_query`](nova-session-record-query.md)** | Documented | Query a finalised session recording for network entries matching a filter. |
| **[`nova.session_record_snapshot_dom`](nova-session-record-snapshot-dom.md)** | Documented | Trigger a fresh DOM snapshot on the live recording bound to a tab. |
| **[`nova.session_record_start`](nova-session-record-start.md)** | Documented | Start a session recording on a browser tab. |
| **[`nova.session_record_status`](nova-session-record-status.md)** | Documented | Return the current state, expiry timestamp, granted permission classes, and capture-waves for a recording. |
| **[`nova.session_record_stop`](nova-session-record-stop.md)** | Documented | Stop an active session recording and finalize its artifacts. |
| **[`nova.session_reset_screenshot_budget`](nova-session-reset-screenshot-budget.md)** | Documented | Reset the aag.screenshot_budget counters for the current MCP session only. |
| **[`nova.traces_list`](nova-traces-list.md)** | Documented | List recent operation traces for debugging. |

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
