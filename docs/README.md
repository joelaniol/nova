# Nova AI Workspace Documentation

Every page of the documentation on one screen. Pick the row that matches what you want to do;
each section also has its own overview page.

Deutsch: [weiter unten](#dokumentation-auf-deutsch).

## Where to start

| I want to … | Go to |
|---|---|
| Install Nova and get it running | [Installation](getting-started/installation.md) → [First run](getting-started/first-run.md) |
| See an agent do something useful in five minutes | [Quickstart](getting-started/quickstart.md) |
| Connect my AI assistant (Claude, Codex, Antigravity, …) | [Agent integration](integration/README.md) |
| Fix an agent that is connected but behaves oddly | [MCP troubleshooting](mcp-troubleshooting/README.md) |
| Fix an agent that cannot connect at all | [Connection issues](troubleshooting/agent-connection-issues.md) |
| Look up a specific tool | [Tool catalog](mcp-reference/tool-catalog.md) |
| Understand how Nova works under the hood | [Core features](core-features/README.md) |
| Identify a Nova-related process in Task Manager | [Components and processes](components/README.md) |

## Getting started

[Overview](getting-started/README.md)

| Page | What it covers |
|---|---|
| [Installation](getting-started/installation.md) | System requirements and the setup on Windows |
| [First run](getting-started/first-run.md) | A tour of the window after the first launch |
| [Quickstart](getting-started/quickstart.md) | From a fresh start to the first verified agent action |

## User guide

[Overview](user-guide/README.md)

| Page | What it covers |
|---|---|
| [Workspace layout](user-guide/workspace-layout.md) | Tabs, address bar, panels and window chrome |
| [Sandboxes and profiles](user-guide/sandboxes-and-profiles.md) | Separate logins side by side in one window |
| [Settings and connection wizard](user-guide/settings-and-connection-wizard.md) | Settings panel and the setup for AI programs |
| [Terminal dock](user-guide/terminal-dock.md) | The built-in terminal next to the browser |
| [AI visualization and staying in control](user-guide/live-assist-and-spectator.md) | Seeing what the agent does, taking over a tab, emergency stop |
| [Downloads](user-guide/downloads-manager.md) | Download list and safety checks |
| [Native dialogs](user-guide/native-dialogs-ui.md) | File pickers, sign-in and permission prompts |
| [Keyboard shortcuts](user-guide/keyboard-shortcuts.md) | All shortcuts in one table |

## Agent integration

[Overview](integration/README.md)

| Page | What it covers |
|---|---|
| [Claude Code](integration/claude-code.md) | Connecting the Claude Code CLI |
| [Claude Desktop](integration/claude-desktop.md) | Connecting the Claude Desktop app |
| [OpenAI Codex](integration/openai-codex.md) | Connecting the Codex CLI |
| [Google Antigravity and Gemini CLI](integration/google-antigravity.md) | Connecting Antigravity and Gemini |
| [Codex and Antigravity notes](integration/codex-and-antigravity.md) | Pointer page to the two guides above |
| [Custom agents](integration/custom-agents.md) | Your own agent in Python, Node.js or raw JSON-RPC |

## MCP reference

[Overview](mcp-reference/README.md)

| Page | What it covers |
|---|---|
| [Tool catalog](mcp-reference/tool-catalog.md) | Every tool by area, each linked to its own page |
| [Protocol and transport](mcp-reference/protocol-and-transport.md) | Wire format, transports and error contract |

[One page per tool](mcp-reference/tools/README.md), grouped by area:

| Area | Tools |
|---|---|
| [App shell and UI](mcp-reference/tools/app-shell-and-ui/) | Window, settings, dialogs, favorites, discovery |
| [Browser automation](mcp-reference/tools/browser-automation/) | Tabs, navigation, clicking, typing, scrolling |
| [DOM and reading](mcp-reference/tools/dom-and-reading/) | Page text, DOM, tables, PDFs |
| [Visual evidence](mcp-reference/tools/visual-evidence/) | Screenshots and visual comparison |
| [Layout and QA](mcp-reference/tools/layout-and-qa/) | Overflow, layout metrics, accessibility checks |
| [Device emulation](mcp-reference/tools/device-emulation/) | Viewport, device, locale, media emulation |
| [Guarded actions](mcp-reference/tools/guarded-actions/) | Sign-in, sending and submitting with a safety check |
| [Downloads](mcp-reference/tools/downloads/) | Listing, waiting for and handling downloads |
| [Site data and identity](mcp-reference/tools/site-data-and-identity/) | Cookies, storage, fingerprint, identity |
| [Proxy and network](mcp-reference/tools/proxy-and-network/) | Proxies, network log, request interception |
| [Vault and security](mcp-reference/tools/vault-and-security/) | Stored logins and secrets |
| [Crawler and discovery](mcp-reference/tools/crawler-and-discovery/) | Crawling sites and mapping their pages |
| [PKS and learning](mcp-reference/tools/pks-and-learning/) | Learned site knowledge and its review |
| [Task memory](mcp-reference/tools/task-memory/) | Task profiles, progress and memory notes |
| [Scheduled tasks](mcp-reference/tools/scheduled-tasks/) | Jobs that run on a schedule |
| [Session recording](mcp-reference/tools/session-recording/) | Recording and replaying a session |
| [Media and transcription](mcp-reference/tools/media-and-transcription/) | Camera, microphone, capture, speech to text |
| [Notifications](mcp-reference/tools/notifications/) | Site notifications and their permissions |
| [Connectors and mail](mcp-reference/tools/connectors-and-mail/) | Mail, FTP and SFTP |
| [Terminal](mcp-reference/tools/terminal-ops/) | Opening and driving terminals |
| [External MCP servers](mcp-reference/tools/external-mcp/) | Other MCP servers run through Nova |
| [Plugins](mcp-reference/tools/plugins/) | Plugins an agent writes, tests and installs for a site |

## Components and processes

[Overview](components/README.md) — What each process does, when it runs and why it is separate.

| Component | Learn more |
|---|---|
| Main app | [Nova AI Workspace](components/nova-ai-workspace.md) |
| Native work | [Outrider](components/outrider.md) |
| Agent connection | [MCP Proxy](components/mcp-proxy.md) |
| Console host | [TerminalRunner](components/terminal-runner.md) |
| Recording diagnostics | [ReplayValidator](components/replay-validator.md) |
| Microsoft browser runtime and task programs | [WebView2 and child processes](components/webview2-and-child-processes.md) |

## Core features

[Overview](core-features/README.md)

[Agent-native affordances](core-features/agent-native-affordances.md) — Built with agents: familiar naming patterns, scoped aliases and client compatibility.

**Seeing and acting on pages**

| Page | What it covers |
|---|---|
| [Input dispatch](core-features/humanized-input-engine.md) | How clicks, keys and drags reach the page; open Shadow DOM |
| [Visual evidence (EVM)](core-features/evm-and-visual-evidence.md) | Screenshots as proof of what the page shows |
| [Native dialogs and prompts](core-features/native-dialogs-and-prompts.md) | Dialogs outside the web page |
| [Sign-in detection](core-features/auth-surface-detection.md) | Recognising login pages and checking a sign-in worked |
| [Crawler and discovery](core-features/crawler-and-discovery.md) | Exploring whole sites instead of single pages |

**Verification and safety**

| Page | What it covers |
|---|---|
| [Closed-loop system](core-features/closed-loop-system.md) | Expected state, action, checked outcome |
| [Agent awareness gates (AAG)](core-features/aag.md) | Checks that stop an agent from acting blind |
| [Tool observation bus (TOB)](core-features/tob.md) | What the agent really did, recorded on Nova's side |
| [Vault and secrets](core-features/vault-and-secrets.md) | Passwords filled in without the agent seeing them |
| [Outrider boundary](core-features/outrider-boundary.md) | Risky Windows and hardware probes in a separate, killable process |

**Memory and learning**

| Page | What it covers |
|---|---|
| [PKS knowledge store](core-features/pks.md) | What Nova learns about how a site works |
| [Operational knowledge](core-features/operational-knowledge.md) | Login state, plan and active model of a site, as signals agents report; domain notes |
| [Task memory (ETM)](core-features/etm-and-task-memory.md) | Recurring tasks and their progress |
| [Learning pipeline (ALP)](core-features/learning-pipeline-alp.md) | How a lesson is checked before it is kept |
| [Browser memory and board](core-features/browser-memory-and-board.md) | Notes and preferences per site; an opt-in board for tool problems agents hit |

**Sessions, network and identity**

| Page | What it covers |
|---|---|
| [Sandbox isolation](core-features/sandbox-isolation.md) | Separate profiles with their own logins |
| [Site data](core-features/site-data-management.md) | Cookies, storage and cache |
| [Proxy and network](core-features/proxy-and-network.md) | Proxies per sandbox and network routing |
| [Fingerprint and identity](core-features/fingerprint-and-identity.md) | Browser fingerprint protection |
| [Session recording](core-features/session-recording.md) | Recording a run to see later what happened |

**Beyond the browser**

| Page | What it covers |
|---|---|
| [Terminal workspaces](core-features/terminal-workspaces.md) | Terminals the agent can use |
| [Scheduled tasks](core-features/scheduled-tasks.md) | Work that runs on its own |
| [Connectors and protocols](core-features/connectors-and-protocols.md) | Mail, FTP and SFTP |
| [Media intelligence](core-features/media-intelligence.md) | Audio, video and transcription |
| [Plugins](core-features/plugins.md) | Small scripts an agent writes for a site |

## Troubleshooting

| Page | What it covers |
|---|---|
| [MCP troubleshooting](mcp-troubleshooting/README.md) | Agent is connected but does not use Nova properly |
| [Antigravity](mcp-troubleshooting/antigravity.md) | Known quirks of Google Antigravity and Gemini CLI |
| [Troubleshooting overview](troubleshooting/README.md) | Entry point for runtime problems |
| [Connection issues](troubleshooting/agent-connection-issues.md) | Agent cannot connect or find Nova |
| [Diagnostics](troubleshooting/diagnostics.md) | Logs and where to find them |
| [Sandbox and session recovery](troubleshooting/sandbox-and-session-recovery.md) | Hanging tabs, lost sessions, restoring sandboxes |

## More

- [Demo lab](../demos/README.md) — a page with eight cases where usual browser automation fails
- [Alpha notes](../ALPHA.md) · [Privacy](../PRIVACY.md) · [Acceptable use](../ACCEPTABLE-USE.md) · [Disclaimer](../DISCLAIMER.md) · [License](../LICENSE)

---

## Dokumentation auf Deutsch

Die Dokumentation ist überwiegend englisch. Eine deutsche Fassung gibt es bisher für die
[Installation](getting-started/installation.md#nova-ai-workspace-installieren), die
[MCP-Fehlerbehebung](mcp-troubleshooting/README.md) (im unteren Teil der Seite) und die
[Antigravity-Hinweise](mcp-troubleshooting/antigravity.md).

Schnelleinstieg: [Installation](getting-started/installation.md#nova-ai-workspace-installieren) →
[Erster Start](getting-started/first-run.md) (englisch) → [KI-Programm verbinden](integration/README.md)
(englisch). Alles Weitere steht in der Übersicht oben.
