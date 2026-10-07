# Nova AI Workspace Documentation

## I want to use Nova

**[Install Nova](getting-started/installation.md) → [Your first five minutes](getting-started/quickstart.md)**

Connect your AI program and watch it complete a short research task. Then choose [What's next?](getting-started/whats-next.md): everyday browsing, regular agent work or how Nova works. For any problem, start at [Troubleshooting](troubleshooting/README.md).

## I want to understand Nova

**[Architecture and processes](components/README.md) → [Core features](core-features/README.md) → [MCP reference](mcp-reference/README.md)**

Explore how Nova acts, verifies and learns; identify its helper processes; or look up a tool in the [catalog](mcp-reference/tool-catalog.md).

[Gemini code-review reliability](research/gemini/nova-code-review/README.md) — 552 findings separately counterchecked by another agent, outcome charts and a timeline alongside project growth.

## Complete reference

<details>
<summary>Browse all documentation sections and pages</summary>

## Getting started

[Overview](getting-started/README.md)

| Page | What it covers |
|---|---|
| [Installation](getting-started/installation.md) | System requirements and the setup on Windows |
| [Your first five minutes](getting-started/quickstart.md) | Launch, connect, restart your AI program, complete a task and stay in control |
| [What's next?](getting-started/whats-next.md) | Everyday browsing, optional onboarding, recurring workflows and architecture |
| [How the connection works](getting-started/mcp-setup.md) | Restarting, automatic reconnect and connection concepts |
| [Advanced onboarding](getting-started/advanced-onboarding.md) | Optional project references and explicit bootstrap |

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
| [Permissions](user-guide/permissions.md) | Website access, agent autonomy and client approvals |
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

[One troubleshooting hub](troubleshooting/README.md) covers installation, connection, agent behavior, browser sessions, diagnostics and client-specific quirks.

| Page | What it covers |
|---|---|
| [Connection issues](troubleshooting/agent-connection-issues.md) | Missing connections, local server and bridge checks |
| [Agent behavior](troubleshooting/agent-behavior.md) | Connected but not using tools, missing data or unchecked outcomes |
| [Antigravity compatibility](troubleshooting/antigravity.md) | Nova's client-compatible names and result handling |
| [Diagnostics](troubleshooting/diagnostics.md) | Logs and failure evidence |
| [Sandbox and session recovery](troubleshooting/sandbox-and-session-recovery.md) | Abandoned tabs, held claims and missing sandboxes |

## Research

[Overview](research/README.md)

| Page | What it covers |
|---|---|
| [BREACH](research/breach/README.md) | A method for structurally new concepts by breaking load-bearing assumptions |
| [The BREACH prompt](research/breach/prompt.md) | The meta-prompt that runs the method with a language model |

## Changelog & releases

[Overview](changelog/README.md)

| Version | Release date | Highlights |
|---|---|---|
| [1.0.0-alpha.18](changelog/v1.0.0-alpha.18.md) | 2026-10-07 | New product name & look, favorites panel, SQLite history, native permission dialogs, AI setup, expanded sandboxes, password vault, resumable transfers, local transcription |
| [1.0.0-alpha.17](changelog/v1.0.0-alpha.17.md) | 2026-09-10 | Targeted hotfix for blank context menu spellcheck rows, official slogan adoption ("Built for what's next."), UI blank label scanner |
| [1.0.0-alpha.16](changelog/v1.0.0-alpha.16.md) | 2026-09-10 | Background agent mode with notification area icon, taskbar integration & autostart fix, console read for agent devtools |
| [1.0.0-alpha.15](changelog/v1.0.0-alpha.15.md) | 2026-09-08 | Network request inspection & interception rules for agents, agent tab pinning & reordering, terminal settings & NO_COLOR chip, media file info, update & install repair |
| [1.0.0-alpha.14](changelog/v1.0.0-alpha.14.md) | 2026-09-04 | Local speech-to-text transcription engine (Whisper), browser-built and streaming media capture, PDF reading/saving, private tabs, loops in agent sequences |

## More

- [Interactive demo](../demos/README.md) — an experience loop with repeat visits, a changed page and checked outcomes, plus eight browser exercises ([German guide](../demos/README.de.md))
- [Alpha notes](../ALPHA.md) · [Privacy](../PRIVACY.md) · [Acceptable use](../ACCEPTABLE-USE.md) · [Disclaimer](../DISCLAIMER.md) · [License](../LICENSE)

</details>

## Dokumentation auf Deutsch

Der [Demo-Guide](../demos/README.de.md), die [Installation](getting-started/installation.md#nova-ai-workspace-installieren), die [Hilfe zum Agentenverhalten](troubleshooting/agent-behavior.md#deutsch-der-agent-ist-verbunden-arbeitet-aber-nicht-richtig) und die [Antigravity-Hinweise](troubleshooting/antigravity.md#google-antigravity-deutsch) sind auch auf Deutsch verfügbar. Die übrige Dokumentation ist überwiegend englisch.

Zum Einstieg: [Installieren](getting-started/installation.md#nova-ai-workspace-installieren) → [KI-Programm verbinden](integration/README.md) → [Erste Aufgabe](getting-started/quickstart.md).
