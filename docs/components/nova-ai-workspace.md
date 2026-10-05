# Nova AI Workspace — Main Process

**Executable:** `NovaAIWorkspace.exe`.

This is the application you open: its window, tabs, settings, browser profiles and built-in MCP tool server. Agents ask this server to perceive pages, dispatch actions and inspect outcomes. Web content itself runs through [WebView2](webview2-and-child-processes.md).

The product name is Nova AI Workspace, or Nova. Helper executable names retain the `NovaBrowser` prefix; it does not mean they are another browser installation. Older installations may still leave an older main-process name visible.

## Why the Helpers Exist

Nova delegates particular workloads instead of putting every operation in the interactive app: native probes go to [Outrider](outrider.md), consoles to [TerminalRunner](terminal-runner.md), and agent transport adaptation to [McpProxy](mcp-proxy.md). Each boundary has its own purpose and lifetime.

Quitting Nova stops its in-app scheduler and interactive tool server. Keeping Nova running in the background leaves the application alive. Hosted terminal processes can remain in TerminalRunner; that does not mean scheduled tasks continue being dispatched after the main process exits.

## What the Main Process Owns

| Area | Responsibility |
| :--- | :--- |
| Workspace | Windows, tabs, navigation, settings and the visible controls for agent activity. |
| Website profiles | Selecting the ordinary, private or sandbox profile used by a WebView. |
| Agent tools | Publishing capabilities, receiving MCP calls and coordinating actions with Nova's policy and permission checks. |
| Knowledge and evidence | Coordinating learning, stored knowledge, task experience and recordings through the relevant subsystems. |
| Background automation | Dispatching scheduled tasks while the application process is running. |
| Helper coordination | Starting native jobs and connecting console or transport helpers to the features that need them. |

These responsibilities do not mean every operation runs on the UI thread. They identify the application that coordinates the work. The browser engine, native probes and console programs have their own process boundaries.

## A Typical Agent Workflow

An agent connects to Nova, discovers a capability and asks to inspect a tab. Nova resolves the target and its profile, obtains page information through WebView2 and returns a result. For an action, Nova applies the relevant prerequisites and permissions before dispatch. The agent then inspects the resulting state; a successful transport response alone does not establish that the intended website outcome occurred.

An action involving a console or native device can cross another boundary. Nova remains the coordinator: the helper does not become an independent agent or inherit authority to approve other actions.

## Window Visibility and Application Lifetime

**Keep running in the background** hides Nova in the Windows notification area while its process remains alive. Scheduled tasks can still be dispatched in this mode. **Quit Nova** ends the application; the in-app scheduler and MCP server then stop. A hidden window is therefore different from an exited process.

TerminalRunner may still host a shell after Nova exits. Conversely, a running MCP proxy may attempt to start Nova when a client needs it. Seeing either helper does not establish that the main app is currently ready to accept tools.

## Learn More

* [Workspace layout](../user-guide/workspace-layout.md)
* [Scheduled tasks](../core-features/scheduled-tasks.md)
* [All components](README.md)
