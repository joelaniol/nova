# Nova AI Workspace — Core Features

> [!NOTE]
> This hub lists the 26 core-feature pages of **Nova AI Workspace** (`NovaAIWorkspace.exe`): what each one covers and which MCP tools belong to it. The tools are listed in full in the [tool catalog](../mcp-reference/tool-catalog.md).

---

## Overview

Nova AI Workspace is a Windows browser built on **.NET 8, WinUI 3 and Microsoft WebView2**. AI agents control it through the Model Context Protocol (MCP); Nova offers them over 400 tools ([current count](../mcp-reference/tools/README.md)). The pages below explain the parts of Nova that sit behind those tools: how it reads and acts on pages, how it checks that an action worked, what it remembers between sessions, how it keeps logins apart, and what it can do outside the browser.

---

## Core features by topic

### Seeing and acting on pages

| Page | What it covers | Main MCP tools |
| :--- | :--- | :--- |
| [Input dispatch](humanized-input-engine.md) | How clicks, keys and drags reach the page; open Shadow DOM | `nova.input_click`, `nova.input_drag_humanized`, `nova.click_selector`, `nova.input_text` |
| [Visual evidence (EVM)](evm-and-visual-evidence.md) | Screenshots as proof of what the page shows | `nova.capture_screenshot`, `nova.screenshot_diff`, `nova.screenshot_baseline` |
| [Native dialogs and prompts](native-dialogs-and-prompts.md) | Dialogs outside the web page | `nova.ui_inspect_native_dialog`, `nova.ui_confirm_native_dialog`, `nova.ui_*_prompt_resolve` |
| [Sign-in detection](auth-surface-detection.md) | Recognising login pages and checking a sign-in worked | `nova.guarded_login`, `nova.ok_observe` |
| [Crawler and discovery](crawler-and-discovery.md) | Exploring whole sites instead of single pages | `nova.crawl_start`, `nova.site_urls`, `nova.explore_surface` |

### Verification and safety

| Page | What it covers | Main MCP tools |
| :--- | :--- | :--- |
| [Closed-loop system](closed-loop-system.md) | Expected state, action, checked outcome | `nova.goal_register`, `nova.run_sequence`, `nova.phenomenon_apply` |
| [Agent awareness gates (AAG)](aag.md) | Checks that stop an agent from acting blind | `nova.guarded_*`, `nova.tab_claim`, `nova.task_instance_verify` |
| [Tool observation bus (TOB)](tob.md) | What the agent really did, recorded on Nova's side | `nova.task_instance_verify`, `nova.task_instance_progress`, `nova.task_instance_get` |
| [Vault and secrets](vault-and-secrets.md) | Saved-password delivery through references; scoped terminal secrets | `nova.vault_*`, `nova.type_selector_secret`, `nova.secret_*` |
| [Outrider boundary](outrider-boundary.md) | Risky Windows and hardware probes in a separate, killable process | `nova.permission_center_get`, `nova.media_transcribe_start` |

### Agent interface

| Page | What it covers | Main MCP tools |
| :--- | :--- | :--- |
| [Agent-native affordances](agent-native-affordances.md) | Learned agent expectations, aliases and client naming compatibility | `nova.get_instructions`, `nova.tools_bundle` |

### Memory and learning

| Page | What it covers | Main MCP tools |
| :--- | :--- | :--- |
| [PKS knowledge store](pks.md) | What Nova learns about how a site works | `nova.pks_get`, `nova.pks_match`, `nova.pks_upsert`, `nova.learn_promote` |
| [Operational knowledge](operational-knowledge.md) | Login state, plan and active model of a site, as signals agents report; domain notes | `nova.ok_observe`, `nova.ok_signal_schema`, `nova.domain_note` |
| [Task memory (ETM)](etm-and-task-memory.md) | Recurring tasks and their progress | `nova.task_match`, `nova.task_instance_create`, `nova.task_instance_complete` |
| [Learning pipeline (ALP)](learning-pipeline-alp.md) | How a lesson is checked before it is kept | `nova.learn_suggest`, `nova.learn_generate`, `nova.learn_promote` |
| [Browser memory and board](browser-memory-and-board.md) | Notes and preferences per site; an opt-in board for tool problems agents hit | `nova.memory_note`, `nova.memory_recall`, `nova.board_get`, `nova.board_contribute` |

### Sessions, network and identity

| Page | What it covers | Main MCP tools |
| :--- | :--- | :--- |
| [Sandbox isolation](sandbox-isolation.md) | Separate profiles with their own logins | `nova.sandbox_context`, `nova.resolve_sandbox`, `nova.sandbox_create` |
| [Site data](site-data-management.md) | Cookies, storage and cache | `nova.cookie_list`, `nova.cookie_set`, `nova.storage_inspect`, `nova.cache_clear` |
| [Proxy and network](proxy-and-network.md) | Shared browser proxy, tab-scoped interception and request replay | `nova.proxy_switch`, `nova.proxy_status`, `nova.network_intercept_*` |
| [Fingerprint and identity](fingerprint-and-identity.md) | Browser fingerprint protection | `nova.fingerprint_*`, `nova.identity_*`, `nova.emulation_*` |
| [Session recording](session-recording.md) | Recording a run to see later what happened | `nova.session_record_start`, `nova.session_record_query`, `nova.session_record_export` |

### Beyond the browser

| Page | What it covers | Main MCP tools |
| :--- | :--- | :--- |
| [Terminal workspaces](terminal-workspaces.md) | Terminals the agent can use | `nova.terminal_open`, `nova.terminal_run_command`, `nova.terminal_read` |
| [Scheduled tasks](scheduled-tasks.md) | Work that runs on its own | `nova.scheduled_task_create`, `nova.scheduled_task_runs`, `nova.scheduled_task_workspace_*` |
| [Connectors and protocols](connectors-and-protocols.md) | Mail, FTP and SFTP | `nova.connector_*`, `nova.mail_*`, `nova.sftp_*`, `nova.ftp_*` |
| [Media intelligence](media-intelligence.md) | Audio, video and transcription | `nova.media_transcribe_start`, `nova.media_capture_start`, `nova.media_activity_*` |
| [Plugins](plugins.md) | Small scripts an agent writes for a site | `nova.plugin_create`, `nova.plugin_test`, `nova.plugin_inspect` |

---

## Related Documentation

* **[Getting Started](../getting-started/README.md)** — Installation, system requirements and the first start.
* **[Agent Integration](../integration/README.md)** — Connecting Claude Code, Claude Desktop, Codex, Antigravity and your own agents.
* **[MCP Reference](../mcp-reference/README.md)** — Tool catalog, capability bundles and the protocol.
* **[Troubleshooting](../troubleshooting/README.md)** — Connection problems, logs and session recovery.
