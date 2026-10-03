# Diagnostics & Log Analysis

This guide provides developers and system operators with the tools and filesystem locations necessary to diagnose, inspect, and resolve issues in **Nova AI Workspace**.

---

## 1. Local Filesystem Locations

Nova stores all runtime diagnostics, configuration, and crash artifacts in the local Windows user profile:

```
%LOCALAPPDATA%\NovaBrowser\
├── diagnostics.log             # Primary application and WebView2 lifecycle log
├── mcp-transport.log           # Raw MCP framing, pipe connections, and transport events
├── settings.json               # Sandbox definitions, user preferences, and proxy profiles
├── pks.db                      # Phenomenological Knowledge Store SQLite database
├── crawl.db                    # Autonomous crawler URL index database
└── CrashDumps/                 # Windows Error Reporting (WER) minidumps (*.dmp)
```

> [!TIP]
> To quickly open this directory in Windows Explorer, press `Win + R`, paste `%LOCALAPPDATA%\NovaBrowser`, and press Enter.

---

## 2. Inspecting Logs in Real Time

### A. Application Log (`diagnostics.log`)
Tracks host window initialization, WebView2 controller warmup, sandbox profile switching, and unhandled exceptions.
* In PowerShell:
  ```powershell
  Get-Content "$env:LOCALAPPDATA\NovaBrowser\diagnostics.log" -Wait -Tail 50
  ```
* Critical markers to search for:
  * `[ERR]`: Application-level error.
  * `Process failed`: A WebView2 renderer or GPU worker process crashed.
  * `CanWebViewTakeFocus`: Guard prevented a focus crash on uninitialized controls.

### B. MCP Transport Log (`mcp-transport.log`)
Records client connections, protocol handshakes, and transport frames.
* You can read this log programmatically via MCP without touching the filesystem:
  ```json
  nova.mcp_transport_log({ "lines": 100 })
  ```

---

## 3. Decoding MCP Error Envelopes

Nova implements strict V3 protocol typing and returns structured error envelopes:

| JSON-RPC Code | Nova Error Type | Cause | Resolution |
| :--- | :--- | :--- | :--- |
| **`-32601`** | `MethodNotFound` | The requested tool name does not exist in the active catalog. | Run `nova.tools_bundle(includeUnavailable=true)` to check the live tool catalog. |
| **`-32602`** | `InvalidParams` | Missing required argument, wrong type, or invalid enum value. | Query `nova.tools_bundle(toolName="nova.xyz")` to view the exact JSON Schema requirements. |
| **`-32002`** | `AagPreconditionFailed` | An Agent Awareness Gate blocked the action (e.g. element is obscured, button disabled, or tab lease held by another agent). | Inspect the `suggestion` field in the error data payload. |
| **`-32004`** | `TargetNotFound` | The specified `targetId` does not exist or the tab was closed. | Call `nova.tabs(outputDetail="minimal")` to obtain fresh, valid tab IDs. |

### Example Structured Error Envelope:
```json
{
  "jsonrpc": "2.0",
  "id": 42,
  "error": {
    "code": -32002,
    "message": "Element is not clickable: covered by backdrop #modal-overlay",
    "data": {
      "errorCode": "aag.element_obscured",
      "selector": "button.submit",
      "obscuringSelector": "#modal-overlay",
      "suggestion": "Call nova.dismiss_blockers or wait for modal dismissal"
    }
  }
}
```

---

## 4. In-Page Browser Diagnostics

When debugging web pages, SPAs, or JavaScript execution errors inside a tab:

* **Read Page Console Messages:**
  ```json
  nova.console_read({ "targetId": "tab-1", "limit": 50 })
  ```
* **Read Network Traffic & Status Codes:**
  ```json
  nova.network_read({ "targetId": "tab-1", "limit": 50 })
  ```
* **Inspect Outrider Native Health:**
  ```json
  nova.hardware_diagnostics_state({})
  ```

---

## Next Steps

* Review [Agent Connection Issues](agent-connection-issues.md) for network and pipe problems.
* Learn how to recover hanging sessions in [Sandbox & Session Recovery](sandbox-and-session-recovery.md).
