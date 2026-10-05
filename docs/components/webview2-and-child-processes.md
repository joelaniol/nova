# WebView2 and Other Child Processes

**Browser runtime executable:** `msedgewebview2.exe`, supplied by Microsoft.

Nova uses WebView2 to render websites and some embedded app surfaces. Its Chromium-based runtime uses multiple processes for browser, renderer, GPU and utility work. Several entries in Task Manager are expected; their count is not a one-to-one count of Nova tabs or sandboxes.

## Why It Is Separate

WebView2 provides the browser engine and its own process boundaries. Nova's sandbox profiles separate website sessions, but they do not each create an independent operating-system virtual machine. Terminating WebView2 processes can disrupt pages or other apps using that runtime.

## Shells, CLIs and Custom Programs

Terminal and scheduled work can launch PowerShell, agent CLIs and user-selected programs. For example, an agent CLI may itself use a runtime such as Node.js. Those processes belong to the selected workload; their names and lifetimes depend on the program and executor.

The process list can therefore include both Nova's own helpers and third-party runtime or task processes. Use the process path and parent relationship when identifying which workload an entry belongs to.

## Learn More

* [Sandbox isolation](../core-features/sandbox-isolation.md)
* [TerminalRunner](terminal-runner.md)
* [Scheduled tasks](../core-features/scheduled-tasks.md)
* [All components](README.md)
