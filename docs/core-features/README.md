# Nova AI Workspace — Core Features

> [!NOTE]
> This hub lists the core-feature topics of **Nova AI Workspace** (`NovaAIWorkspace.exe`): what each one covers and which MCP tools belong to it. The tools are listed in full in the [tool catalog](../mcp-reference/tool-catalog.md).

---

## Overview

Nova AI Workspace is a Windows browser built on **.NET 8, WinUI 3 and Microsoft WebView2**. AI agents control it through the Model Context Protocol (MCP); Nova provides a [tool catalog](../mcp-reference/tools/README.md). The pages below explain the parts of Nova that sit behind those tools: how it reads and acts on pages, how it checks that an action worked, what it remembers between sessions, how it keeps logins apart, and what it can do outside the browser.

---

The [alpha status page](../../ALPHA.md) lists current limitations, including plugins being unavailable and connectors not yet recommended for terminal use.

## Core features by topic

### Seeing and acting on pages

| Page | What it covers | Main MCP tools |
| :--- | :--- | :--- |
| [Browser Interaction](browser-interaction/README.md) | How clicks, keys and drags reach the page; open Shadow DOM | `nova.input_click`, `nova.input_drag_humanized`, `nova.click_selector`, `nova.input_text` |
| [Native Dialogs & UI Prompts](native-dialogs-and-prompts/README.md) | Dialogs outside the web page | `nova.ui_inspect_native_dialog`, `nova.ui_confirm_native_dialog`, `nova.ui_*_prompt_resolve` |
| [Auth Surface Detection (ASD)](auth-surface-detection-asd/README.md) | Recognising login pages and checking a sign-in worked | `nova.guarded_login`, `nova.ok_observe` |
| [Crawler & Discovery](crawler-and-discovery/README.md) | Exploring whole sites instead of single pages | `nova.crawl_start`, `nova.site_urls`, `nova.explore_surface` |

### Verification and safety

| Page | What it covers | Main MCP tools |
| :--- | :--- | :--- |
| [Closed-Loop System (CLS)](closed-loop-system-cls/README.md) | Expected state, action, checked outcome | `nova.goal_register`, `nova.run_sequence`, `nova.phenomenon_apply` |
| [Agent Awareness Gates (AAG)](agent-awareness-gates-aag/README.md) | Checks that stop an agent from acting blind | `nova.guarded_*`, `nova.tab_claim`, `nova.task_instance_verify` |
| [Tool Observation Bus (TOB)](tool-observation-bus-tob/README.md) | What the agent really did, recorded on Nova's side | `nova.task_instance_verify`, `nova.task_instance_progress`, `nova.task_instance_get` |

### Agent interface

| Page | What it covers | Main MCP tools |
| :--- | :--- | :--- |
| [Agent-Native Affordances](agent-native-affordances/README.md) | Learned agent expectations, aliases and client naming compatibility | `nova.get_instructions`, `nova.tools_bundle` |

### Learning

| Page | What it covers | Main MCP tools |
| :--- | :--- | :--- |
| [Learning](learning/README.md) | Learning candidates, trusted playbooks, task memory, site knowledge and learned application | `nova.learn_*`, `nova.pks_*`, `nova.task_*`, `nova.memory_*`, `nova.ok_observe`, `nova.board_*` |

### Sessions, network and identity

| Page | What it covers | Main MCP tools |
| :--- | :--- | :--- |
| [Multi-Sandbox Session Isolation](sandbox-isolation/README.md) | Separate profiles with their own logins | `nova.sandbox_context`, `nova.resolve_sandbox`, `nova.sandbox_create` |
| [Site Data Management](site-data-management/README.md) | Cookies, Web Storage, cache cleanup, Cookie Inspector and agent permissions | `nova.cookie_list`, `nova.cookie_set`, `nova.storage_inspect`, `nova.cache_clear` |
| [Network](network/README.md) | Shared proxy, tab-scoped interception, replay and SSL/TLS diagnostics | `nova.proxy_switch`, `nova.proxy_status`, `nova.network_intercept_*`, `nova.tls_inspect` |
| [Privacy](privacy/README.md) | Fingerprint protection, browser identity, vault and secret delivery | `nova.fingerprint_*`, `nova.identity_*`, `nova.emulation_*`, `nova.vault_*`, `nova.secret_*`, `nova.type_selector_secret` |
| [Session Recording & Time-Travel Debugging](session-recording/README.md) | Recording a run to see later what happened | `nova.session_record_start`, `nova.session_record_query`, `nova.session_record_export` |

### Beyond the browser

| Page | What it covers | Main MCP tools |
| :--- | :--- | :--- |
| [Terminal Workspaces & ConPTY Integration](terminal-workspaces/README.md) | Terminals the agent can use | `nova.terminal_open`, `nova.terminal_run_command`, `nova.terminal_read` |
| [Scheduled Tasks & Background Automation Engine](scheduled-tasks/README.md) | Work that runs on its own | `nova.scheduled_task_create`, `nova.scheduled_task_runs`, `nova.scheduled_task_workspace_*` |
| [Connectors](connectors/README.md) | Mail, SSH, SFTP, FTP/FTPS and external MCP servers | `nova.connector_*`, `nova.mail_*`, `nova.ssh_run*`, `nova.sftp_*`, `nova.ftp_*`, `nova.external_*` |
| [Media Intelligence](media-intelligence/README.md) | Speech transcription, image viewing, PDFs, playback, capture and media devices | `nova.media_*`, `nova.read_pdf`, `nova.save_pdf`, `nova.hardware_diagnostics_*` |
| [Agent-Authored Plugins (AAP) & Jint JavaScript Runtime](plugins/README.md) | Reference only: unavailable during the public alpha | `nova.plugin_create`, `nova.plugin_test`, `nova.plugin_inspect` |

---

## Related Documentation

* **[Research](../research/README.md)** — EVM, visual evidence, research methods and empirical studies.

* **[Components & Processes](../components/README.md)** — Nova executables and process boundaries, including Outrider.

* **[Getting Started](../getting-started/README.md)** — Installation, system requirements and the first start.
* **[Agent Integration](../integration/README.md)** — Connecting Claude Code, Claude Desktop, Codex, Antigravity and your own agents.
* **[MCP Reference](../mcp-reference/README.md)** — Tool catalog, capability bundles and the protocol.
* **[Troubleshooting](../troubleshooting/README.md)** — Connection problems, logs and session recovery.
