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
3. **Strict Rejection of Unknown Properties:** Passing undeclared properties to tools returns a `-32602` error that names what the tool accepts, so the agent can correct the call. A wrong enum value is reported as `<name> must be one of <a> | <b> (received '<value>')`.
4. **Boundary Range Checking:** Numeric fields (`durationMs`, `timeoutMs`, `jitterPx`) enforce upper and lower bounds. Out-of-bounds arguments are rejected early at the MCP pipeline boundary rather than causing downstream failures.

---

## 4. Error Code Reference

**A failed tool call is a tool result, not a JSON-RPC error.** For `tools/call`, Nova answers with
`isError: true`. `structuredContent` carries `ok: false`, the numeric `errorCode`, a `message` and,
in most cases, a `reasonCode` plus hints; the same data is repeated as a text block, because many
clients show the model only the text. Branch on `reasonCode` where it is present.

Other methods (`initialize`, `tools/list`, …) and malformed requests get a plain JSON-RPC `error`.

| Code | Meaning | What to do |
| :--- | :--- | :--- |
| **`-32700`** | The request is not valid JSON. | Check string escaping. |
| **`-32600`** | Not a valid JSON-RPC request. | Send `jsonrpc: "2.0"` and a `method`. |
| **`-32601`** | Unknown JSON-RPC method. | Use the MCP methods (`tools/list`, `tools/call`, …). |
| **`-32602`** | Invalid parameters: wrong type, unknown property, wrong enum value, out-of-range number, an unknown tool name (the message lists close matches) or an unknown `targetId`. | Read the message; it names what is accepted. Discover tools with `nova.tools_bundle`. |
| **`-32040`** | The tab is claimed by another agent (`claim.owner_mismatch`). | Use the `agentId` the message names, wait for the claim to expire, or reclaim with a `reclaimReason`. |
| **`-32044`** | Too many tabs claimed at once. | Release or close tabs you no longer need. |
| **`-32035`** | Blocked by a policy. | Not retryable as is; the message says which policy. |
| **`-32034`** / **`-32033`** / **`-32029`** | The action needs the user's approval / the approval is unavailable or expired / the user denied it. | Wait for the user, ask again, or stop. |
| **`-32031`** / **`-32030`** | An autonomy or bootstrap gate stopped the call. | Follow the hint in the message (often: call the named tool first). |
| **`-32005`** | The feature is switched off in Nova's settings. | Ask the user to enable it; `nova.tools_bundle(includeUnavailable=true)` names the setting. |
| **`-32004`** | Not found, e.g. no element matched the selector. | Check the selector or wait for the page. |
| **`-32003`** | A precondition failed (page not ready, URL mismatch, …). | Wait or navigate, then retry. |
| **`-32002`** | A resource is not available (the tab's web view is not initialized, a plugin does not exist, …). | Activate or reload the tab, or check the id. |
| **`-32001`** / **`-32000`** | Other blocked or application-level failures. | Read the message and `reasonCode`. |

### Example: a wrong enum value

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "isError": true,
    "content": [
      { "type": "text", "text": "Invalid params: outputDetail must be one of minimal | summary | full (received 'verbose')." }
    ],
    "structuredContent": {
      "ok": false,
      "errorCode": -32602,
      "message": "Invalid params: outputDetail must be one of minimal | summary | full (received 'verbose')."
    }
  }
}
```

The example is shortened: Nova also appends the `structuredContent` as a second text block.

---

## Next Steps

* Explore all available tools in the **[Tool Catalog](tool-catalog.md)**.
* Return to the **[MCP Reference Index](README.md)**.
