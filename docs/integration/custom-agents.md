# Build a Custom Nova Integration

This page is for developers building their own agent runner or MCP client. To connect an existing AI program, use the [connection guide](README.md).

## Choose a connection

| Connection | Use it when | Your client handles |
|---|---|---|
| Nova's stdio bridge | Your MCP client can start a local executable | MCP initialization, discovery and tool calls; the bridge locates Nova and supplies its token |
| Direct Streamable HTTP | Your client needs a direct HTTP connection | Authentication, MCP session headers, initialization and reconnecting |

Get the current connection details from Nova's **Settings → AI & agents → Connection & setup → Set up** wizard. Use **Connect another program** for a custom client. For stdio, start the runner command supplied by Nova rather than the main browser executable.

Nova must be installed. The standard bridge can start it when needed. Direct HTTP clients need Nova running and agent access enabled.

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
