# Building Custom Agents (Python & Node.js)

This guide shows developers how to connect custom AI agents, automated test harnesses, and backend services directly to **Nova AI Workspace** using Python, TypeScript/Node.js, or raw JSON-RPC 2.0.

---

## 1. Choosing a Transport

Nova supports three distinct communication transports:

| Transport | Best For | Security & Performance |
| :--- | :--- | :--- |
| **Stdio Proxy (`NovaBrowser.McpProxy.exe`)** | Official Python & TypeScript MCP SDKs | Standard subprocess pipe, cross-platform SDK compatibility |
| **Direct Windows Named Pipe (`\\.\pipe\nova-mcp`)** | Native Windows applications, low-latency loops | Zero TCP overhead, kernel-enforced `CurrentUserOnly` ACL |
| **Streamable HTTP JSON-RPC (`http://127.0.0.1:port/mcp`)** | Web services, local Docker containers | Local loopback, authenticated via rotating Bearer token |

---

## 2. Python Integration (Official MCP SDK)

Using the official `mcp` Python package (`pip install mcp`):

```python
import asyncio
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def run_nova_agent():
    # Configure the Stdio Proxy connection to Nova's Named Pipe
    server_params = StdioServerParameters(
        command="C:\\Program Files\\Nova\\NovaBrowser.McpProxy.exe",
        args=["--pipe", "nova-mcp"],
        env=None
    )

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
            target_id = tab_result.content[0].text
            print(f"Opened tab: {target_id}")

            # 4. Extract page content
            dom = await session.call_tool("nova.read_text_structured", {
                "targetId": target_id,
                "selector": "h1, p"
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
  const transport = new StdioClientTransport({
    command: "C:\\Program Files\\Nova\\NovaBrowser.McpProxy.exe",
    args: ["--pipe", "nova-mcp"]
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

## 4. Direct Named Pipe Client (Low Latency)

For applications requiring ultra-low latency without launching child processes, connect directly to `\\.\pipe\nova-mcp`:

### Node.js Native Socket Example:
```typescript
import net from "net";

const client = net.connect("\\\\.\\pipe\\nova-mcp", () => {
  console.log("Connected directly to Nova Named Pipe!");

  const request = JSON.stringify({
    jsonrpc: "2.0",
    id: 1,
    method: "tools/call",
    params: {
      name: "nova.tabs",
      arguments: { outputDetail: "minimal" }
    }
  }) + "\n";

  client.write(request);
});

client.on("data", (data) => {
  console.log("Nova Response:", data.toString());
  client.end();
});
```

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
