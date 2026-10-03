# Protocol, Framing & Transport Contract

This document specifies the wire-level communication standards, transport mechanisms, and error handling contracts used by **Nova AI Workspace**.

---

## 1. Supported Transports

Nova's MCP server speaks **Streamable HTTP**. Clients reach it either directly or through Nova's stdio bridge:

```
[Agent Client]
      |
      +---> stdio ----------------> [NovaBrowser.McpProxy.exe]
      |                                       |
      |                                       v
      +---> Streamable HTTP ------> [Nova MCP server, http://127.0.0.1:27183/mcp]
                                              |
                                     [Nova Core Engine]
```

### A. Stdio bridge (`NovaBrowser.McpProxy.exe`)
* **Standard way in for CLI and desktop clients** (Claude Code, Claude Desktop, OpenAI Codex, Google Antigravity). Nova registers it with these clients automatically.
* **Location:** `%LOCALAPPDATA%\nova-cognitive\Nova\bin\NovaBrowser.McpProxy.exe` (installations from before the product rename: `%LOCALAPPDATA%\NovaBrowser\bin\`). Nova keeps this copy current; clients point here rather than into the installation folder, so updates do not break their config.
* Reads JSON-RPC messages from standard input and writes responses to standard output. Both newline-delimited JSON and `Content-Length`-framed messages are accepted; answers use the framing the client sent.
* Reads endpoint and access token from Nova's runtime file (`mcp.json` in the same profile folder) and reconnects transparently when Nova restarts. If Nova is not running, the bridge starts it.
* **Command-line switches** (the first two can be combined; an unknown switch is refused with exit code 2 instead of being ignored):
  * `--antigravity-tool-names`: advertises tool names with underscores (`nova_tabs`) for clients that reject dots, and maps calls back. Includes `--mirror-structured-content`.
  * `--mirror-structured-content`: copies `structuredContent` into `content[].text` for clients that pass only the text to the model.
  * `--version` or `--self-test`, each on its own: print the bridge version, or check that the bridge itself works, and exit.
* **Environment variables:** see [Google Antigravity → Advanced Proxy Tuning](../integration/google-antigravity.md#4-advanced-proxy-tuning-environment-variables) (`NOVA_MCP_AUTOSTART`, `NOVA_MCP_COLD_START_MS`, …).

### B. Streamable HTTP (`http://127.0.0.1:27183/mcp`)
* For services and scripts that cannot start a child process.
* **Binding:** `127.0.0.1` only, unless remote clients are explicitly allowed in Nova's settings. The port (default `27183`) can be changed in the settings; the current endpoint is always in `mcp.json` (`endpoint`).
* **Authentication:** every request to `/mcp` needs
  ```http
  Authorization: Bearer <token>
  ```
  The token is in `mcp.json` (`auth.token`). It is stored encrypted for your Windows account and stays the same across Nova restarts.
* **Session:** the response to `initialize` carries an `Mcp-Session-Id` header. Send it with `MCP-Protocol-Version` on every following request; requests without it are answered with `400 Missing Mcp-Session-Id`.
* **Responses:** with `Accept: application/json, text/event-stream`, answers arrive as server-sent events (`event: message`).
* **Health probe:** `GET /health` needs no token and returns `status` (`ready` once Nova accepts calls), the app version and the protocol version. It never contains the token.

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
