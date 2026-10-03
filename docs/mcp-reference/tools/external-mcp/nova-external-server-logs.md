# `nova.external_server_logs`

Reads recent stderr log lines captured from an external MCP server process.

---

## 1. Overview

`nova.external_server_logs` retrieves stderr diagnostic lines captured in Nova's circular buffer (up to 500 lines per server), enabling quick troubleshooting of crashes, missing dependencies, or bad arguments.

* **Capability Bundle:** `external_mcp`
* **Security Tier:** Tier 1 (Safe Diagnostics)
* **Core Architecture Guide:** [Plugins & External Extensions](../../../core-features/plugins.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`serverKey`** | `string` | Yes | `none` | 8-character hex server key. |
| **`lines`** | `integer` | No | `50` | Number of most recent lines to return (1 - 500). |
| **`_meta`** | `object` | No | `null` | Optional call metadata. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.external_server_logs",
  "arguments": {
    "serverKey": "a1b2c3d4",
    "lines": 10
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "2 log line(s) for server 'a1b2c3d4'."
    }
  ],
  "structuredContent": {
    "ok": true,
    "serverKey": "a1b2c3d4",
    "lineCount": 2,
    "lines": [
      {
        "ts": "2026-10-02T21:15:00.120Z",
        "text": "[postgres-mcp] Connecting to database..."
      },
      {
        "ts": "2026-10-02T21:15:00.340Z",
        "text": "[postgres-mcp] Ready on stdio."
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Diagnosing Startup Failure:** When `nova.external_server_start` fails or times out, immediately inspect `nova.external_server_logs` to read Node/Python tracebacks.

---

## See Also

* [`nova.external_server_start`](nova-external-server-start.md) - Start server.
* [External MCP Servers Category](README.md)
* [MCP Tool Catalog](../../tool-catalog.md)
