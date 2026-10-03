# `nova.mcp_transport_log`

> **Reads recent redacted entries from Nova's internal MCP JSON-RPC transport log.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 1 (Read-Only Logging)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.mcp_transport_log` provides visibility into incoming client requests, parsed arguments, server response timings, and protocol parsing exceptions.

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
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_mcp_transport_log",
  "arguments": {
    "limit": 50
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Returned 50 log records from logs/mcp/mcp-server.log."
    }
  ],
  "structuredContent": {
    "ok": true,
    "recordsCount": 50,
    "logPath": "logs/mcp/mcp-server.log"
  }
}
```

---

## 4. Operational Best Practices

* **Protocol Debugging:** Check transport logs when an MCP client encounters unexpected JSON-RPC disconnects or schema rejections.
* **Redacted Credentials:** Auth tokens and passwords are automatically masked before output.

---

## 5. Related Tools

* [`nova.agent_activity_summary`](nova-agent-activity-summary.md)
