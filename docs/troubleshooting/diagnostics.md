# Diagnostics & Log Analysis

This guide shows where **Nova AI Workspace** keeps its logs, crash dumps and data files, and how to read them.

---

## 1. Local Filesystem Locations

Nova keeps its data, logs and crash artifacts in one profile folder per Windows user:

* `%LOCALAPPDATA%\nova-cognitive\Nova\` on new installations.
* `%LOCALAPPDATA%\NovaBrowser\` on installations from version 1.0.0-alpha.17 or older. The setup of a newer version moves this folder to the new location; if the move is not possible, Nova keeps using the old folder.

The paths below are relative to that profile folder:

```
<profile folder>\
├── settings.json                        # Settings, sandbox list, proxy profiles
├── mcp.json                             # Current MCP address and access token, read by the bridge
├── bootstrap.log                        # Early startup failures, before the normal log is up
├── pks.db                               # Learned site knowledge (PKS)
├── CrawlStore\crawl.db                  # Crawler URL index
├── Logs\
│   ├── app-<date>_<time>-<pid>.log      # Main application log, one file per run
│   ├── crash-<date>_<time>-<pid>.log    # Crash reports from fatal errors
│   ├── novabrowser-mcp-stdio-proxy.log  # Bridge log: connection attempts and why they failed
│   ├── mcp\mcp-*.log                    # Agent transport log (MCP requests and responses)
│   ├── actions\actions-*.jsonl          # One line per agent tool call: tool, source, duration, result
│   └── Setup\*.log                      # One log per installation, update or repair
├── CrashDumps\                          # Windows minidumps (*.dmp) after a native crash
└── Dumps\                               # Diagnostic dumps created on request (nova.create_dump)
```

Many of these files and folders appear only after the feature was first used.

> [!TIP]
> In Nova, **Settings → Developer options → Logs** lists every log channel, and **Open log folder** opens the `Logs` folder in Explorer. Outside Nova, press `Win + R`, paste `%LOCALAPPDATA%\nova-cognitive\Nova` (or `%LOCALAPPDATA%\NovaBrowser`) and press Enter.

**Crash dumps.** By default Nova registers itself with Windows Error Reporting on startup, so that a native crash of `NovaAIWorkspace.exe` leaves a minidump in `CrashDumps\` (up to five are kept). A crash-dump setup for Nova's process that someone else made in Windows is left unchanged.

---

## 2. Inspecting Logs

### A. Application log (`Logs\app-*.log`)
Nova starts a new file on every run; the newest file belongs to the current run. It records startup, warnings, errors and host diagnostics.
* Follow the current log in PowerShell (use `NovaBrowser` instead of `nova-cognitive\Nova` on older installations):
  ```powershell
  Get-ChildItem "$env:LOCALAPPDATA\nova-cognitive\Nova\Logs\app-*.log" |
    Sort-Object LastWriteTime | Select-Object -Last 1 |
    Get-Content -Wait -Tail 50
  ```
* Each line carries its level in brackets. Search for `[ERR]` (errors) and `[WRN]` (warnings) first.

### B. Agent transport log (`Logs\mcp\mcp-*.log`)
Records the MCP requests and responses between agents and Nova. Nova writes it while **Enable agent debug log** is on (the default) in the settings.
* Agents can read it over MCP without touching the filesystem:
  ```json
  nova.mcp_transport_log({ "run": "current", "maxLines": 100 })
  ```
  `contains` searches for a substring; `run` selects the log of the current, the latest or the previous run.

### C. Bridge log (`Logs\novabrowser-mcp-stdio-proxy.log`)
Written by `NovaBrowser.McpProxy.exe`, the bridge your AI program starts. If an agent cannot reach Nova, this log shows each connection attempt and why it failed. See [Agent Connection Issues](agent-connection-issues.md).

---

## 3. Reading MCP Errors

Nova reports a failed tool call as a tool result with `isError: true`. The details sit in `structuredContent` (`ok: false`, `errorCode`, `message`, usually a `reasonCode` and repair hints), and the same data is repeated as a text block starting with `structuredContent:` for clients that show only text. Releases up to 1.0.0-alpha.17 return these fields as a JSON-RPC error instead (`error.code`, `error.data`).

| Code | Typical `reasonCode` | Cause | Resolution |
| :--- | :--- | :--- | :--- |
| **`-32602`** | `target.unknown` and others | Invalid parameters: a missing or unknown argument, a wrong type or enum value, an unknown `targetId`, or an unknown tool name (the message then suggests similar names). | Check the tool's schema with `nova.tools_bundle({ "toolName": "nova.xyz" })`; get fresh tab IDs with `nova.tabs({ "outputDetail": "minimal" })`. |
| **`-32040`** | `claim.owner_mismatch` | The tab is claimed by another agent. The message names the owner and the remaining lease time. | See [Resolving tab claims](sandbox-and-session-recovery.md#2-resolving-tab-claims-held-by-another-agent). |

### Example error result (shortened)
```json
{
  "content": [
    { "type": "text", "text": "Invalid params: unknown target 'tab-9'. …" },
    { "type": "text", "text": "structuredContent:\n{\"reasonCode\":\"target.unknown\", …}" }
  ],
  "structuredContent": {
    "reasonCode": "target.unknown",
    "requestedTargetId": "tab-9",
    "ok": false,
    "errorCode": -32602,
    "message": "Invalid params: unknown target 'tab-9'. …"
  },
  "isError": true
}
```

---

## 4. In-Page Browser Diagnostics

When debugging web pages, SPAs, or JavaScript errors inside a tab:

* **Read page console messages:**
  ```json
  nova.console_read({ "targetId": "active", "maxEntries": 50 })
  ```
* **Read network requests and status codes** (for example only failed requests):
  ```json
  nova.network_read({ "targetId": "active", "onlyFailed": true, "maxEntries": 50 })
  ```

---

## Next Steps

* Review [Agent Connection Issues](agent-connection-issues.md) for connection problems between your AI program and Nova.
* Learn how to recover tabs and sandboxes in [Sandbox & Session Recovery](sandbox-and-session-recovery.md).
