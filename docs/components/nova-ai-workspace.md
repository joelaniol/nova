# Nova AI Workspace — Main Process

**Executable:** `NovaAIWorkspace.exe`.

This is the application you open: its window, tabs, settings, browser profiles and built-in MCP tool server. Agents ask this server to perceive pages, dispatch actions and inspect outcomes. Web content itself runs through [WebView2](webview2-and-child-processes.md).

The product name is Nova AI Workspace, or Nova. Helper executable names retain the `NovaBrowser` prefix; it does not mean they are another browser installation. Older installations may still leave an older main-process name visible.

## Why the Helpers Exist

Nova delegates particular workloads instead of putting every operation in the interactive app: native probes go to [Outrider](outrider.md), consoles to [TerminalRunner](terminal-runner.md), and agent transport adaptation to [McpProxy](mcp-proxy.md). Each boundary has its own purpose and lifetime.

Closing Nova stops its in-app scheduler and interactive tool server. Hosted terminal processes can remain in TerminalRunner; that does not mean scheduled tasks continue being dispatched while Nova is closed.

## Learn More

* [Workspace layout](../user-guide/workspace-layout.md)
* [Scheduled tasks](../core-features/scheduled-tasks.md)
* [All components](README.md)
