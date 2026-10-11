# Session Recordings & Time-Travel Debugging

> [!NOTE]
> Nova AI Workspace includes a forensic **Session Recording** engine designed for developers, QA testers, and AI agents. It captures high-fidelity event streams within browser tabs—including network traffic, console output, JavaScript exceptions, user/agent clicks, and DOM snapshots—allowing you to diagnose complex failures post-mortem without re-running destructive actions.

---

## 1. What Is Session Recording?

When an automated workflow fails, a web application throws an unexpected error, or a form submission silently breaks, traditional logs rarely explain *why*. Session Recording acts like a tamper-resistant black box flight recorder for web browsing:

* **Complete Event Streams:** Captures network request headers and bodies, DevTools console messages, unhandled promise rejections, window resizing, navigation history, and DOM mutations.
* **Correlated Interactions:** Maps exact physical and simulated clicks, keyboard inputs, and scrolls directly to the resulting network responses and DOM state changes.
* **Capture-Time Secret Redaction:** Passwords, authentication headers (`Authorization: Bearer ...`), API keys, and DPAPI-stored credentials are automatically masked *before* writing to disk.
* **Encrypted Storage:** Recordings are written as line-by-line **AES-256-GCM** encrypted streams (`.jsonl`), with data encryption keys (DEK) protected by the Windows Data Protection API (DPAPI).

```
+-----------------------------------------------------------------------------------+
|  [A: Work] [Tab 1: Checkout (REC)] [+]                                   [_][O][X]|
+-----------------------------------------------------------------------------------+
|  [<-] [->] [Reload] | https://app.example.com/checkout  [REC Active] | [Menu]     |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  Active Recording: rec-9b41a82f                                                  |
|  Status: Recording (00:02:14 elapsed, 142 events, 3.4 MB)                        |
|                                                                                   |
|  Captured Streams:                                                                |
|  * [x] Network requests (38 captured, authorization masked)                      |
|  * [x] Console output & runtime errors (2 errors detected)                        |
|  * [x] User and Agent interactions (14 clicks, 2 form fills)                      |
|  * [x] DOM snapshots (4 automatic keyframe captures)                             |
|                                                                                   |
|  Actions: [ Pause ]  [ Snapshot DOM Now ]  [ Stop & Save ]  [ Export .novarec ]   |
+-----------------------------------------------------------------------------------+
```

---

## 2. Starting & Stopping Recordings

### Starting a Recording
1. **From the Main Menu:** Select **Menu → Tools → Start session recording**.
2. **From the Tab Context Menu:** Right-click any active tab and select **Record tab activity**.
3. **Agent-Initiated:** Autonomous AI agents can start recordings programmatically before executing sensitive or multi-step operations using [`nova.session_record_start`](../../mcp-reference/tools/session-recording/nova-session-record-start.md).

### Live Visual Indicators
* **Tab Strip Indicator:** An active recording tab displays a distinct red recording badge `(REC)` directly beside its favicon.
* **URL Bar Badge:** The status section of the address bar shows an active **Recording** chip. Clicking this badge opens the quick-control flyout to view live event counts, trigger an immediate DOM snapshot, or stop the recording.

### Stopping a Recording
* Click the recording chip in the URL bar and select **Stop & Save**, or select **Menu → Tools → Stop session recording**.
* The recording session is sealed, its encryption keys are committed, and its manifest is indexed in the local session database.

---

## 3. Investigating Failures Post-Mortem

Once a session is recorded, you and your AI agents can inspect it without mutating the live webpage or re-submitting transactions:

### 1. Correlating Interactions with Network Failures
* Review the chronological timeline of actions. For example, locate the exact timestamp when the `#submit-order` button was clicked.
* Inspect the outgoing `POST /api/v1/orders` request immediately following that click. Inspect response status codes (e.g. `500 Internal Server Error`), payload sizes, and server error bodies.

### 2. Identifying Silent JavaScript Errors
* Filter the event stream for `errors.jsonl` and `console.jsonl`.
* Inspect client-side exceptions (such as `Uncaught TypeError: Cannot read properties of undefined`) that prevented UI updates even when network requests succeeded.

### 3. Reviewing DOM Snapshots
* Nova automatically captures a complete DOM snapshot immediately before and after significant interactions.
* Inspect DOM snapshots to see whether form fields had CSS validation error classes (`.is-invalid`), whether hidden modal dialogs were obscuring buttons, or whether disabled attributes were present.

---

## 4. Privacy, Security & Quota Controls

Session recordings capture extensive data. Nova provides comprehensive privacy protections configurable in **Menu → Settings → Session recording**:

* **Master Switch:** Enable or disable session recording globally. When disabled, all recording attempts (including agent MCP calls) are blocked.
* **Toolbar Indicator:** Toggle whether the recording indicator is visible in the window chrome.
* **Storage Quota:** Configure the maximum disk space allocated for recordings (e.g. `1024 MB`). When the quota is reached, oldest recordings are automatically pruned.
* **Auto-Purge Retention:** Automatically purge recordings older than a specified number of days (e.g. `7 days`).
* **Concurrent Recordings Limit:** Prevent performance degradation by limiting how many tabs can record simultaneously (default: `2`).
* **Permission Classes:** Selectively enable or disable specific event streams:
  * *Network CDP:* Network headers and payloads.
  * *Console & Errors:* Developer console and runtime crashes.
  * *Interactions:* Clicks, scrolls, and key presses.
  * *DOM Snapshots:* Full-page structural snapshots.

---

## 5. Exporting & Sharing Recordings

* **Export Archive:** In the recording manager, select **Export recording** to package the encrypted session into a portable `.novarec` archive.
* **Sanitized Audit Export:** Export a redacted JSON summary containing timing, request URLs, and error messages for bug reports without embedding confidential session state.

---

## 6. AI Agent Integration

AI coding agents leverage session recording as a primary tool for self-verification and debugging:

* [`nova.session_record_start`](../../mcp-reference/tools/session-recording/nova-session-record-start.md): Begins recording a target tab with custom permission classes.
* [`nova.session_record_query`](../../mcp-reference/tools/session-recording/nova-session-record-query.md): Queries captured events with filtering by timestamp, event type, and status code.
* [`nova.session_record_interactions`](../../mcp-reference/tools/session-recording/nova-session-record-interactions.md): Lists user and agent clicks, inputs, and element targets.
* [`nova.session_record_dom_snapshot`](../../mcp-reference/tools/session-recording/nova-session-record-dom-snapshot.md): Retrieves complete serialized DOM keyframes.
* [`nova.session_record_stop`](../../mcp-reference/tools/session-recording/nova-session-record-stop.md): Finalizes the recording session.

---

## Related Documentation

* **[Core Features: Session Recording](../../core-features/session-recording/README.md)** — In-depth architectural details, encryption mechanics, and stream formats.
* **[Tools Overview](README.md)** — Other workspace utilities including Transcription and Scheduled Tasks.
* **[Agent Awareness Gates](../../core-features/agent-awareness-gates-aag/README.md)** — Safety boundaries for agent-initiated operations.
