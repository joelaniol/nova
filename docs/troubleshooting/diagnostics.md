# Diagnostics & Log Analysis

Use this when Nova fails to start, a connection keeps failing, or you need evidence for a report.

## Start with the visible problem

Note what you were doing, the time, the visible error and the AI program involved. If Nova is open:

1. Open **Menu → Settings → Developer options → Logs**.
2. Choose **Open log folder** to open the logs in Explorer.
3. Find the recent application or bridge log using the table below. Keep the original file; copy the relevant excerpt for review.

If Nova cannot open, press **Win + R**, enter `%LOCALAPPDATA%\nova-cognitive\Nova` and press Enter. If that folder does not exist, try `%LOCALAPPDATA%\NovaBrowser`. Check `bootstrap.log` and the `Logs` folder.

You can ask a connected agent:

> Investigate the Nova failure I just saw: [describe what happened and when]. Read the relevant logs, separate observed errors from possible causes, and explain the next step. Do not change my settings or delete profile data while investigating.

For reporting, ask the agent for Nova's bug-report instructions. Review excerpts and screenshots for personal data and secrets before sharing; see the [reporting policy](../../ALPHA.md#what-to-report) and the separate [security reporting route](../../SECURITY.md).

## 1. Local Filesystem Locations

Nova keeps its data, logs and crash artifacts in one profile folder per Windows user:

* `%LOCALAPPDATA%\nova-cognitive\Nova\` on new installations.
* `%LOCALAPPDATA%\NovaBrowser\` on installations from version 1.0.0-alpha.17 or older. The setup of a newer version moves this folder to the new location; if the move is not possible, Nova keeps using the old folder.

The paths below are relative to that profile folder:

```
<profile folder>\
├── settings.json                        # Settings, sandbox list, proxy profiles
├── mcp.json                             # Current MCP address and access token, read by the bridge
├── bootstrap.log                        # Early startup failures, before the normal log is up
├── pks.db                               # Learned site knowledge (PKS)
├── CrawlStore\crawl.db                  # Crawler URL index
├── Logs\
│   ├── app-<date>_<time>-<pid>.log      # Main application log, one file per run
│   ├── crash-<date>_<time>-<pid>.log    # Crash reports from fatal errors
│   ├── novabrowser-mcp-stdio-proxy.log  # Bridge log: connection attempts and why they failed
│   ├── mcp\mcp-*.log                    # Agent transport log (MCP requests and responses)
│   ├── actions\actions-*.jsonl          # One line per agent tool call: tool, source, duration, result
│   └── Setup\*.log                      # One log per installation, update or repair
├── CrashDumps\                          # Windows minidumps (*.dmp) after a native crash
└── Dumps\                               # Diagnostic dumps created on request (nova.create_dump)
```

Many of these files and folders appear only after the feature was first used.

> [!TIP]
> In Nova, **Settings → Developer options → Logs** lists every log channel, and **Open log folder** opens the `Logs` folder in Explorer. Outside Nova, press `Win + R`, paste `%LOCALAPPDATA%\nova-cognitive\Nova` (or `%LOCALAPPDATA%\NovaBrowser`) and press Enter.

**Crash dumps.** By default Nova registers itself with Windows Error Reporting on startup, so that a native crash of `NovaAIWorkspace.exe` leaves a minidump in `CrashDumps\` (up to five are kept). A crash-dump setup for Nova's process that someone else made in Windows is left unchanged.

---

## 2. Inspecting Logs

| Symptom | Look at |
|---|---|
| Nova does not open | `bootstrap.log`, then recent `Logs/app-*.log` and `Logs/crash-*.log` |
| AI program cannot connect | `Logs/novabrowser-mcp-stdio-proxy.log`; follow [Connection troubleshooting](agent-connection-issues.md) |
| A connected agent's call fails | Agent transport logs under `Logs/mcp/` and action records under `Logs/actions/` |
| Installation or update fails | `Logs/Setup/` |

The application starts a new log on each run. Select the file for the time of the failure; the newest file may belong to a later restart. `[ERR]` and `[WRN]` identify errors and warnings, but a nearby message is not automatically the cause.

Agent transport logging depends on **Enable agent debug log** in Nova's settings. A missing log can mean that channel was disabled or not used.

Do not share `mcp.json`: it contains the current access token. Crash dumps and logs can contain sensitive data too; only share them through the intended reporting route after review.

## 3. Reading MCP Errors

Copy the complete visible error to your agent and ask it to diagnose it. Invalid parameters usually require the agent to refresh the tool schema; a claimed tab requires an ownership or takeover decision. You should not have to construct tool calls or change agent IDs yourself.

For a reservation problem, follow [Resolving tab claims](sandbox-and-session-recovery.md#2-resolving-tab-claims-held-by-another-agent). Developers can use [Protocol errors](../mcp-reference/protocol-and-transport.md) for the result format and error codes.

## 4. In-Page Browser Diagnostics

For a page that fails while Nova is otherwise working, ask:

> Inspect this page's visible state, console errors and failed network requests using Nova. Explain the evidence before retrying or changing anything.

Tell the agent which tab or sandbox is affected. If the page shows a CAPTCHA or a human verification step, handle it yourself and then ask the agent to continue. See [Agent behavior](agent-behavior.md).

## Next Steps

- [Agent connection issues](agent-connection-issues.md)
- [Sandbox and session recovery](sandbox-and-session-recovery.md)
