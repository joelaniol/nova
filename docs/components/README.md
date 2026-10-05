# Components and Processes

Nova uses several processes with different lifetimes. Seeing more than one Nova-related entry in Task Manager is therefore expected. This guide explains what each process does and why it is separate.

| Process | Purpose | When to expect it |
| :--- | :--- | :--- |
| [`NovaAIWorkspace.exe`](nova-ai-workspace.md) | The main app, tabs, settings and agent tool server. | While Nova is open. |
| [`NovaBrowser.Outrider.exe`](outrider.md) | Supervised native hardware probes and local speech work. | When a feature needs native work; helper sessions or one-shot jobs. |
| [`NovaBrowser.McpProxy.exe`](mcp-proxy.md) | Connects an agent's standard-input/output MCP transport to Nova. | While a configured agent client is connected through the proxy. |
| [`NovaBrowser.TerminalRunner.exe`](terminal-runner.md) | Hosts pseudo consoles separately from the browser. | While terminal sessions need it; it can outlive the Nova window. |
| [`NovaBrowser.ReplayValidator.exe`](replay-validator.md) | Checks recording manifests and inventories artifacts; current replay coverage is limited. | When explicitly invoked for recording diagnostics or validation. |
| [`msedgewebview2.exe`](webview2-and-child-processes.md) | Microsoft's Chromium-based browser runtime. | While Nova's WebViews are active; multiple subprocesses are normal. |

Shells and agent CLIs such as PowerShell, Claude Code or Codex can appear underneath terminal or scheduled work. They are the selected programs, not additional Nova helper binaries.

## Why Separate Processes?

The boundaries solve different problems: Outrider contains native failures; TerminalRunner keeps console lifetimes independent; McpProxy adapts the connection transport; ReplayValidator inspects recordings outside the interactive app. WebView2 supplies the browser engine's own multiprocess architecture.

The MCP proxy is not a web-traffic proxy, and TerminalRunner is not Outrider. Closing a helper can interrupt the feature it serves. In particular, closing TerminalRunner ends its hosted terminals, even if the Nova window is already closed.

These names describe expected components, not proof that an arbitrary file with the same name is genuine. The main executable ships at the installation root, McpProxy under `tools/`, and the other Nova helpers alongside the app; Outrider also has an isolated copy under `outrider/`. WebView2 comes from Microsoft's runtime installation.

## Learn More

* [Core features](../core-features/README.md) — The capabilities these components support.
* [Agent integration](../integration/README.md) — Connecting an agent client.
* [Diagnostics](../troubleshooting/diagnostics.md) — Investigating a runtime problem.
* [Component inventory](components.json) — Executable names and their documentation pages.
