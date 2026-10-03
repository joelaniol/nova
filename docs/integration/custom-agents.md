# Building Custom Agents (Python & Node.js)

This guide shows developers how to connect custom AI agents, automated test harnesses, and backend services directly to **Nova AI Workspace** using Python, TypeScript/Node.js, or raw JSON-RPC 2.0.

---

## 1. Choosing a Transport

Nova's MCP server speaks **Streamable HTTP** on the local machine. You can reach it in two ways:

| Transport | Best For | What you have to handle |
| :--- | :--- | :--- |
| **Stdio bridge (`NovaBrowser.McpProxy.exe`)** | Official Python & TypeScript MCP SDKs, anything that can start a program | Nothing: the bridge finds Nova, adds the token, survives Nova restarts and starts Nova if needed |
| **Streamable HTTP (`http://127.0.0.1:27183/mcp`)** | Services that cannot start a child process | Read endpoint and token from Nova's runtime file, send the `Mcp-Session-Id` header, re-read the file after a Nova restart |

**Where things are.** Nova keeps its files in `%LOCALAPPDATA%\nova-cognitive\Nova` (installations from before the product rename: `%LOCALAPPDATA%\NovaBrowser`). Inside it:

* `bin\NovaBrowser.McpProxy.exe` — the stdio bridge
* `mcp.json` — runtime file with the current `endpoint` and the access token (`auth.token`); it only exists while Nova has been started at least once

The server only listens on `127.0.0.1` unless you explicitly allow remote clients in Nova's settings, and every request needs the token.

---

## 2. Python Integration (Official MCP SDK)

Using the official `mcp` Python package (`pip install mcp`). The examples on this page are written for version 2.x of the package; version 1.x names the result field `structuredContent` instead of `structured_content`.

```python
import asyncio
import os
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

# Nova's stdio bridge; use %LOCALAPPDATA%\NovaBrowser on installations from before the rename
BRIDGE = os.path.expandvars(r"%LOCALAPPDATA%\nova-cognitive\Nova\bin\NovaBrowser.McpProxy.exe")

async def run_nova_agent():
    server_params = StdioServerParameters(command=BRIDGE, args=[])

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # 1. Initialize MCP session
            await session.initialize()

            # 2. Execute bootstrap handshake
            instructions = await session.call_tool("nova.get_instructions", {
                "taskKeywords": ["automation", "custom-agent"]
            })
            print("Session Hints:", instructions)

            # 3. Create a new tab and navigate
            tab_result = await session.call_tool("nova.tab_new", {
                "url": "https://example.com"
            })
            target_id = tab_result.structured_content["targetId"]
            print(f"Opened tab: {target_id}")

            # 4. Extract page content
            dom = await session.call_tool("nova.read_text", {
                "targetId": target_id,
                "selector": "body"
            })
            print("Extracted Content:", dom)

if __name__ == "__main__":
    asyncio.run(run_nova_agent())
```

---

## 3. TypeScript / Node.js Integration

Using the official `@modelcontextprotocol/sdk` package (`npm install @modelcontextprotocol/sdk`):

```typescript
import { Client } from "@modelcontextprotocol/sdk/client/index.js";
import { StdioClientTransport } from "@modelcontextprotocol/sdk/client/stdio.js";

async function main() {
  // Nova's stdio bridge; use %LOCALAPPDATA%\NovaBrowser on installations from before the rename
  const transport = new StdioClientTransport({
    command: `${process.env.LOCALAPPDATA}\\nova-cognitive\\Nova\\bin\\NovaBrowser.McpProxy.exe`,
    args: []
  });

  const client = new Client(
    { name: "custom-agent", version: "1.0.0" },
    { capabilities: {} }
  );

  await client.connect(transport);

  // 1. Handshake
  await client.callTool({
    name: "nova.get_instructions",
    arguments: { taskKeywords: ["node-agent"] }
  });

  // 2. Open tab and claim it
  const tabRes = await client.callTool({
    name: "nova.tab_new",
    arguments: { url: "https://example.com" }
  });

  console.log("Tab created successfully:", tabRes);
}

main().catch(console.error);
```

---

## 4. Direct HTTP Client (no child process)

If your agent cannot start a program, connect to Nova's Streamable HTTP endpoint directly. Read the endpoint and token from the runtime file each time you connect — both can change when Nova restarts.

### Python, official MCP SDK:
```python
import asyncio
import json
import os
import httpx2
from mcp import ClientSession
from mcp.client.streamable_http import streamable_http_client

# use %LOCALAPPDATA%\NovaBrowser on installations from before the rename
RUNTIME_FILE = os.path.expandvars(r"%LOCALAPPDATA%\nova-cognitive\Nova\mcp.json")

async def main():
    with open(RUNTIME_FILE, encoding="utf-8-sig") as f:
        runtime = json.load(f)
    http = httpx2.AsyncClient(
        headers={"Authorization": f"Bearer {runtime['auth']['token']}"},
        timeout=httpx2.Timeout(30, read=300),  # some Nova tools wait for pages; allow long reads
    )

    async with http, streamable_http_client(runtime["endpoint"], http_client=http) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tabs = await session.call_tool("nova.tabs", {"outputDetail": "minimal"})
            print(tabs.structured_content)

asyncio.run(main())
```

### Rules for a hand-written HTTP client
1. `POST` every JSON-RPC message to the `endpoint` from `mcp.json` with `Authorization: Bearer <auth.token>`, `Content-Type: application/json` and `Accept: application/json, text/event-stream`.
2. Start with `initialize`. The response carries an `Mcp-Session-Id` header; send it, together with `MCP-Protocol-Version`, on every following request. Without it Nova answers `400 Missing Mcp-Session-Id`.
3. Responses arrive as a server-sent event stream (`event: message` / `data: {...}`).
4. `401 Unauthorized` means the token is missing or outdated: read `mcp.json` again.
5. `GET /health` on the same host and port needs no token and tells you whether Nova is ready (`"status": "ready"`).

Keep the token out of logs and source code; anyone who has it can control your browser.

---

## 5. Error Handling Contract

Nova returns standard JSON-RPC 2.0 error envelopes with structured diagnosis fields:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "error": {
    "code": -32002,
    "message": "Tab is locked by another agent lease",
    "data": {
      "errorCode": "aag.lease_conflict",
      "targetId": "tab-1",
      "leaseRemainingMs": 142000,
      "suggestion": "Wait for lease expiry or request a distinct targetId via tab_new"
    }
  }
}
```

### Common Error Codes:
* **`-32602` (Invalid Params):** Missing mandatory argument or invalid enum value.
* **`-32002` (AAG Precondition Blocked):** Action blocked by Agent Awareness Gate (e.g. attempting to click an obscured element or violating tab lease).
* **`-32004` (Target Not Found):** Specified `targetId` does not exist or was closed.

---

## Next Steps

* Review the architectural principles in **[Core Features](../core-features/README.md)**.
* Learn about [Agent Awareness Gates (AAG)](../core-features/aag.md).
