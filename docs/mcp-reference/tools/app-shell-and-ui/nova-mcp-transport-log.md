# `nova.mcp_transport_log`

> **Reads recent redacted entries from Nova's internal MCP JSON-RPC transport log.**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.mcp_transport_log` reads Nova's MCP transport log files (`mcp-<UTC timestamp>-<process id>.log` in the `Logs\mcp` folder of the Nova profile). Without `startLine` it returns the last `maxLines` lines (tail mode); with `startLine` it returns a line range; with `contains` it returns matching lines. Authorization headers, bearer tokens and token values are replaced with `<redacted>` before lines are returned.

A transport log file exists only while MCP debug logging with the transport channel is enabled. If no matching file exists, the result is `ok: false` with `status: "not_found"` and `reasonCode: "mcp_transport_log_not_found"`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `run` | `string` | No | `"current"` | `current`, `latest`, `previous` | Which MCP transport log file to read. current: file whose name ends with this Nova process ID and is not older than the current process start; latest: newest mcp-*.log; previous: second-newest mcp-*.log. |
| `startLine` | `integer` | No | — | ≥ 1 | Optional 1-based first line to return. Omit for tail mode. Example: startLine=501,maxLines=200 reads lines 501-700. |
| `maxLines` | `integer` | No | `100` | 1–500 | Maximum lines or search matches to return. Default: 100. Max: 500. Values outside the range are clamped by the runtime. |
| `contains` | `string` | No | — | — | Optional substring search. When set, Nova scans from startLine (or line 1) and returns up to maxLines matching line-numbered entries. |
| `caseSensitive` | `boolean` | No | `false` | — | Whether contains matching is case-sensitive. Default false. |

Capability bundle: `system_tools` (load it with `nova.tools_bundle(bundle='system_tools')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_mcp_transport_log",
  "arguments": {
    "run": "current",
    "maxLines": 50
  }
}
```

### JSON-RPC Response
Abridged example; `entries` and `lines` carry the returned lines.

```json
{
  "content": [
    {
      "type": "text",
      "text": "MCP transport log mcp-20261002_081500-12840.log (current process) from Logs/mcp: returned 50 lines 1151-1200. Path: C:\\Users\\you\\AppData\\Local\\nova-cognitive\\Nova\\Logs\\mcp\\mcp-20261002_081500-12840.log. Log file name stamps are UTC; Nova-emitted log line stamps use local time with offset."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "source": "Logs/mcp",
    "run": "current",
    "fileName": "mcp-20261002_081500-12840.log",
    "processId": 12840,
    "currentProcessId": 12840,
    "isCurrentProcess": true,
    "totalLines": 1200,
    "mode": "tail",
    "startLine": 1151,
    "endLine": 1200,
    "maxLines": 50,
    "returnedCount": 50,
    "hasMore": false,
    "hasEarlier": true,
    "nextStartLine": null,
    "entries": [
      { "lineNumber": 1151, "text": "2026-10-02 10:31:12.004 +02:00 ..." }
    ],
    "lines": ["2026-10-02 10:31:12.004 +02:00 ..."]
  }
}
```

---

## 4. Operational Best Practices

* **Protocol Debugging:** Check transport logs when an MCP client reports unexpected disconnects or rejected requests.
* **Paging:** Use `nextStartLine` with `startLine` to continue reading; `hasEarlier` tells you that a tail read skipped older lines.
* **Redacted Credentials:** Authorization headers, bearer tokens and `token` values are masked before output.

---

## 5. Related Tools

* [`nova.agent_activity_summary`](nova-agent-activity-summary.md)
