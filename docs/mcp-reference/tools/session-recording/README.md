# Session Tracing & DOM Event Recording

Network HAR capture, user interaction timelines, DOM change snapshots, and replay verification.

* **Core Architecture Guide:** [Core Features: session-recording.md](../../../core-features/session-recording.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

<!-- generated:tool-list (from the tool pages in this folder; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
## Tool Inventory (14 Tools)

Capability bundles of these tools: `page_read_debug`, `session_recording`, `visual_evidence`.

| Tool | What it does |
| :--- | :--- |
| **[`nova.session_record_dom_snapshot`](nova-session-record-dom-snapshot.md)** | Retrieves and decrypts a previously stored DOM snapshot HTML payload by snapshot ID. |
| **[`nova.session_record_events`](nova-session-record-events.md)** | Decrypts and streams generic event logs (console, errors, lifecycle, IndexedDB) from a recording. |
| **[`nova.session_record_export`](nova-session-record-export.md)** | Decodes a finalized encrypted recording to plaintext files on disk for debugging or archival. |
| **[`nova.session_record_extend`](nova-session-record-extend.md)** | Extends an active recording’s time-to-live (TTL) to prevent premature expiration during long workflows. |
| **[`nova.session_record_get_entry`](nova-session-record-get-entry.md)** | Retrieves the complete event timeline, headers, and decoded payload for a single CDP request ID. |
| **[`nova.session_record_interactions`](nova-session-record-interactions.md)** | Reads the chronological interaction timeline (clicks, typing, form submits) from a recording. |
| **[`nova.session_record_purge`](nova-session-record-purge.md)** | Destructively deletes finalized session recordings older than a specified day threshold. |
| **[`nova.session_record_query`](nova-session-record-query.md)** | Queries the complete CDP network stream of a finalized recording with rich filters (URL regex, status, headers). |
| **[`nova.session_record_snapshot_dom`](nova-session-record-snapshot-dom.md)** | Triggers a fresh encrypted DOM snapshot on an active live recording bound to a tab. |
| **[`nova.session_record_start`](nova-session-record-start.md)** | Initiates encrypted background recording of CDP network, DOM mutations, console logs, and user interactions on a tab. |
| **[`nova.session_record_status`](nova-session-record-status.md)** | Returns the live state, start/expiry timestamps, tab/sandbox binding, and granted permission classes of a recording. |
| **[`nova.session_record_stop`](nova-session-record-stop.md)** | Stops an active session recording, flushes buffered events, and finalizes the encrypted artifact with a per-stream SHA-256 integrity manifest. |
| **[`nova.session_reset_screenshot_budget`](nova-session-reset-screenshot-budget.md)** | Resets the session screenshot budget counter to allow fresh visual captures. |
| **[`nova.traces_list`](nova-traces-list.md)** | Lists recent host operation traces with execution timing, phases, and outcome status for debugging. |
<!-- /generated:tool-list -->

---

## Related Documentation

* [MCP Protocol & Transport Specifications](../../protocol-and-transport.md)
* [Agent Integration Hub](../../../integration/README.md)
* [Core Features Hub](../../../core-features/README.md)
