# Build a Custom Nova Integration

This page is for developers building their own agent runner or MCP client. To connect an existing AI program, use the [connection guide](README.md).

## Choose a connection

| Connection | Use it when | Your client handles |
|---|---|---|
| Nova's stdio bridge | Your MCP client can start a local executable | MCP initialization, discovery and tool calls; the bridge locates Nova and supplies its token |
| Direct Streamable HTTP | Your client needs a direct HTTP connection | Authentication, MCP session headers, initialization and reconnecting |

Get the current connection details from Nova's **Settings → AI & agents → Connection & setup → Set up** wizard. Use **Connect another program** for a custom client. For stdio, start the runner command supplied by Nova rather than the main browser executable.

Nova must be installed. The standard bridge can start it when needed. Direct HTTP clients need Nova running and agent access enabled.

## Client compatibility

**Documentation checked: 2026-10-07.** These are observations of client behavior, not a guarantee for every version or runner. Structured-result observations below were made on **2026-10-04**; name compatibility reflects Nova's current client connection contracts. “Not checked” does not mean unsupported.

| Client | `structuredContent` reaches the model | Nova names containing `.` | Bridge option |
|---|---|---|---|
| Antigravity | No; the model receives text blocks | Needs underscore names, such as `nova_tabs` | `--antigravity-tool-names` enables name translation **and** structured-result mirroring |
| Claude Code | Yes; when present, the model receives the structured result | Supported by the standard Nova connection | No compatibility switch needed |
| Codex CLI | Yes; the model receives structured results and text | Supported by the standard Nova connection | No compatibility switch needed |
| Claude Desktop / Cowork | Not checked in these observations | Not checked in these observations | Use the wizard's standard entry; diagnose actual client behavior |
| Cursor and other/custom runners | Not checked in these observations | Not checked in these observations | Test both features before choosing a switch |

Some clients accept a structured MCP result but do not pass its `structuredContent` to the model. If your agent sees only a summary such as “Use structuredContent.tabs” without the actual tab data, add **`--mirror-structured-content`** to the Nova bridge arguments and restart the client. Do not work around missing results by querying Nova with `curl` or reading its profile files.

For a JSON-based client that supports dotted names but needs the data copied into text, the connection can look like this:

```json
{
  "mcpServers": {
    "nova": {
      "command": "C:\\Users\\YourName\\AppData\\Local\\nova-cognitive\\Nova\\bin\\NovaBrowser.McpProxy.exe",
      "args": ["--mirror-structured-content"]
    }
  }
}
```

`YourName` is an example username. Use the actual command path supplied by Nova's wizard. Older installations may use `AppData\Local\NovaBrowser\bin`. In JSON, `\\` represents one Windows path backslash. Keep other settings and server entries; this is only the Nova connection. The bridge handles Nova's local authentication, so no access token appears in this entry.

If you launch the bridge directly from your runner, the equivalent command is:

```powershell
& "C:\Users\YourName\AppData\Local\nova-cognitive\Nova\bin\NovaBrowser.McpProxy.exe" --mirror-structured-content
```

This starts a **stdio MCP server**: your runner must communicate through its standard input and output. It is not an interactive task command. Use the actual path from Nova's wizard.

If your client also requires names without dots, use `--antigravity-tool-names` instead. That mode also mirrors structured data. For example, discovery exposes `nova_tabs` where Nova's reference says `nova.tabs`; use the discovered name rather than rewriting names yourself. See the [complete Antigravity entry](google-antigravity.md#which-file-changes-and-what-should-it-look-like).

Verify that the model can see actual result fields and call the discovered tool names. A server listed as connected is not sufficient to establish either capability. These options repair the client connection; tool-specific result projections remain the agent's responsibility.

## Build against the actual contracts

1. Use a maintained MCP client implementation and follow the documentation for the version you install: the official [Python SDK](https://github.com/modelcontextprotocol/python-sdk) or [TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk), for example.
2. Initialize the MCP connection using that client's supported transport.
3. Give your agent access to [Nova's current instructions](../mcp-reference/tools/app-shell-and-ui/nova-get-instructions.md) and [tool discovery](../mcp-reference/tools/app-shell-and-ui/nova-tools-bundle.md).
4. Use the tool names and input schemas returned by discovery. Follow Nova's instructions for page inspection, tab ownership and verification.
5. Pass tool results and errors through your agent runner. Preserve the content and structured data your client receives; use the installed SDK's own result types.
6. Check the outcome in Nova. A successful connection proves the transport works; it does not prove the task succeeded.

The [protocol and transport reference](../mcp-reference/protocol-and-transport.md) describes Nova's handshake, authentication and result envelopes. The [tool catalog](../mcp-reference/tool-catalog.md) links each tool's contract. SDK code should be written and tested against the versions and schemas your integration actually uses.

## Results and permissions

Your runner and agent decide how to use task results. Output projection parameters belong to individual tool schemas; they are not a user-facing integration setting.

Keep Nova's access key out of source code, shared documents and logs. Tool execution remains subject to Nova's settings and permissions. Your agent runner must also apply the user's authorization for actions.

## Troubleshooting

Use [Connection diagnostics](../troubleshooting/agent-connection-issues.md) for transport problems and [Agent behavior](../troubleshooting/agent-behavior.md) for task failures. For repeated project work, see [optional onboarding](../getting-started/advanced-onboarding.md).
