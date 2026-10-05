# WebView2 and Other Child Processes

**Browser runtime executable:** `msedgewebview2.exe`, supplied by Microsoft.

Nova uses WebView2 to render websites and some embedded app surfaces. Its Chromium-based runtime uses multiple processes for browser, renderer, GPU and utility work. Several entries in Task Manager are expected; their count is not a one-to-one count of Nova tabs or sandboxes.

## Why It Is Separate

WebView2 provides the browser engine and its own process boundaries. Nova's sandbox profiles separate website sessions, but they do not each create an independent operating-system virtual machine. Terminating WebView2 processes can disrupt pages or other apps using that runtime.

## Shells, CLIs and Custom Programs

Terminal and scheduled work can launch PowerShell, agent CLIs and user-selected programs. For example, an agent CLI may itself use a runtime such as Node.js. Those processes belong to the selected workload; their names and lifetimes depend on the program and executor.

The process list can therefore include both Nova's own helpers and third-party runtime or task processes. Use the process path and parent relationship when identifying which workload an entry belongs to.

## What the Runtime Provides

WebView2 supplies website rendering, JavaScript execution, DOM access and browser networking. Nova uses its browser and developer-protocol interfaces to navigate pages, inspect content, capture evidence and dispatch supported interactions. Some embedded Nova surfaces also use WebView2, so a runtime process is not necessarily a normal website tab.

| Runtime role | Work it supports |
| :--- | :--- |
| Browser | Coordinates the browser runtime and its contexts. |
| Renderer | Processes page content and JavaScript. |
| GPU | Supports graphics and compositing. |
| Utility | Supports browser services such as network work. |

Chromium decides how to allocate these processes. Pages, embedded surfaces and profile environments can affect the process layout; neither a fixed process count nor one renderer per tab is a reliable inventory rule.

## Profiles and Process Isolation

Nova's profiles separate website data such as cookies and local storage. A private or sandbox tab uses its corresponding profile environment. This is a website-session boundary, while WebView2's subprocesses are browser-engine execution boundaries.

Those concepts should not be read as separate virtual machines or separate Windows users. Ending a runtime subprocess can interrupt more than the single visible page you had in mind. Other applications can also use `msedgewebview2.exe`; inspect its path and parent relationship before attributing it to Nova.

## Understanding Other Entries

Windows console infrastructure, such as a console-host process, can also accompany ConPTY sessions. A terminal shell may launch a compiler, development server or agent CLI. A scheduled task may launch its configured executor. Those programs can create their own child processes, with names and lifetimes determined by the workload. A running Node.js process, for example, is not enough to identify which agent or server is using it.

For an unfamiliar process, first identify its executable path, parent and the feature active at the time. Then use the relevant component page: native device work belongs with Outrider, consoles with TerminalRunner, and an agent's stdio MCP connection with McpProxy. Process count alone cannot establish a leak or a duplicate installation.

## Learn More

* [Sandbox isolation](../core-features/sandbox-isolation.md)
* [TerminalRunner](terminal-runner.md)
* [Scheduled tasks](../core-features/scheduled-tasks.md)
* [All components](README.md)
