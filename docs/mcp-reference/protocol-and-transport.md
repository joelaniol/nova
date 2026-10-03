# Protocol, Framing & Transport Contract

This document specifies the wire-level communication standards, transport mechanisms, and error handling contracts used by **Nova AI Workspace**.

---

## 1. Supported Transports

Nova implements three distinct transport interfaces under the Model Context Protocol:

```
[Agent Client]
      |
      +---> Stdio Streams --------> [NovaBrowser.McpProxy.exe]
      |                                       |
      +---> Windows Named Pipe -------------> [Nova Named Pipe (\\.\pipe\nova-mcp)]
      |                                       |
      +---> Streamable HTTP / SSE ----------> [Nova HTTP Server (127.0.0.1:27183)]
                                              |
                                     [Nova Core Engine]
```

### A. Windows Named Pipe (`\\.\pipe\nova-mcp`)
* **Default internal IPC transport.**
* **Security:** Configured with `PipeOptions.CurrentUserOnly`. Windows kernel ACLs guarantee that only processes running in the identical Windows user token can open or read the pipe.
* **Framing:** Standard UTF-8 JSON-RPC 2.0 messages separated by newline (`\n`) characters.

### B. Stdio Proxy (`NovaBrowser.McpProxy.exe`)
* **Standard bridge for CLI and desktop clients** (Claude Code, Claude Desktop, OpenAI Codex).
* Reads JSON-RPC requests from standard input (`stdin`), relays them into Nova's Named Pipe, and writes responses to standard output (`stdout`).
* **Command-line Switches:**
  * `--pipe <name>`: Connects to a specific Named Pipe (default: `nova-mcp`).
  * `--mirror-structured-content`: Automatically serializes `structuredContent` into plain text `content[0].text` for clients that do not parse structured objects.

### C. Streamable HTTP JSON-RPC (`http://127.0.0.1:27183/mcp`)
* **Local HTTP Loopback** for web services, containerized tools, and custom scripts.
* **Binding:** Strictly bound to `127.0.0.1` (`IPAddress.Loopback`). It never listens on public interfaces (`0.0.0.0`).
* **Authentication:** Requires an HTTP header:
  ```http
  Authorization: Bearer <ROTATING_BEARER_TOKEN>
  ```
* Nova writes the active token to `.mcp.json` on workspace launch.

---

## 2. JSON-RPC 2.0 Wire Specification

### Request Message
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "nova.read_text_structured",
    "arguments": {
      "targetId": "tab-1",
      "selector": "h1.title"
    }
  }
}
```

### Success Response
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Nova AI Workspace Documentation"
      }
    ],
    "structuredContent": {
      "count": 1,
      "items": ["Nova AI Workspace Documentation"],
      "targetId": "tab-1"
    },
    "isError": false
  }
}
```

---

## 3. V3 Typing & Coercion Rules

Nova implements strict V3 protocol validation:

1. **Native JSON Types:** Numbers and booleans should be transmitted as native JSON scalars (`1000`, `true`).
2. **Coercion Fallback:** If an agent transmits a stringified integer (`"1000"`) or stringified boolean (`"true"`), Nova's argument parser automatically coerces it safely into the target primitive.
3. **Strict Rejection of Unknown Properties:** Passing undeclared properties to tools returns a `-32602` error containing an explicit `Allowed: [...]` list to enable immediate agent self-correction.
4. **Boundary Range Checking:** Numeric fields (`durationMs`, `timeoutMs`, `jitterPx`) enforce upper and lower bounds. Out-of-bounds arguments are rejected early at the MCP pipeline boundary rather than causing downstream failures.

---

## 4. Error Code Reference

Nova distinguishes protocol errors, validation errors, and operational gate failures:

| Code | Label | Meaning & Actionable Remedy |
| :--- | :--- | :--- |
| **`-32700`** | `ParseError` | Malformed JSON received on the wire. Check string escaping. |
| **`-32600`** | `InvalidRequest` | Message is missing `jsonrpc: "2.0"` or `method`. |
| **`-32601`** | `MethodNotFound` | The requested tool does not exist. Call `nova.tools_bundle` to discover tools. |
| **`-32602`** | `InvalidParams` | Argument failed schema validation or enum constraints. Inspect the `Allowed: [...]` hint. |
| **`-32002`** | `AagPreconditionFailed` | An Agent Awareness Gate blocked the action (e.g. element obscured or tab lease held). |
| **`-32004`** | `TargetNotFound` | The specified `targetId` does not exist or the tab was closed. |

### Structured Error Payload Example:
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32602,
    "message": "Invalid parameter 'outputDetail': received 'verbose'. Allowed: ['minimal', 'full']",
    "data": {
      "parameter": "outputDetail",
      "received": "verbose",
      "allowed": ["minimal", "full"]
    }
  }
}
```

---

## Next Steps

* Explore all available tools in the **[Tool Catalog](tool-catalog.md)**.
* Return to the **[MCP Reference Index](README.md)**.
