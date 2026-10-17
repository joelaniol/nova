# `nova.install_onboarding`

> **Writes Nova's reference files and a Nova block in the project's agent instruction file into a project directory.**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.install_onboarding` writes Nova's reference files into `.nova/` under `projectRoot` (the router `README.md`, one `tools/<area>.md` per tool area, the `guide/<topic>.md` guides and the generated connector schemas `tools/mail.md`, `tools/sftp.md`, `tools/ftp.md`; the 4.x files `nova-mcp.quick.md` and `nova-mcp.md` are removed) and adds or replaces a marked Nova block in the project's existing `CLAUDE.md`, `AGENTS.md` or `GEMINI.md`. If none of these exists, it creates all three — `CLAUDE.md` (Claude Code), `AGENTS.md` (Codex and other agents following that convention) and `GEMINI.md` (Gemini CLI, Antigravity) — each containing only that block, so whichever agent works in the project finds it. A project that already has one of them gets no additional files. Nova never writes agent permission files such as `.claude/settings.json`.

The tool is available only while agent self-onboarding is enabled in Nova's settings. A directory that Nova has not onboarded before needs `confirmNewLocation: true`; without it the call writes nothing and returns `status: "confirmation_required"` with the exact call to repeat.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `projectRoot` | `string` | Yes | — | — | Absolute path to the project root directory (worktree) where agent config files should be written. |
| `confirmNewLocation` | `boolean` | No | — | — | Set true to onboard a directory Nova has not onboarded before. Already-onboarded worktrees update without it. |

Capability bundles: `onboarding`, `system_tools`.
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_install_onboarding",
  "arguments": {
    "projectRoot": "C:\\Projects\\WebWorkflow",
    "confirmNewLocation": true
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Onboarding installed in C:\\Projects\\WebWorkflow (version 4.40.0)"
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "projectRoot": "C:\\Projects\\WebWorkflow",
    "version": "4.40.0",
    "filesWritten": [
      { "path": ".nova/README.md", "outcome": "created", "error": null },
      { "path": ".nova/tools/browser-automation.md", "outcome": "created", "error": null },
      { "path": ".nova/tools/mail.md", "outcome": "created", "error": null },
      { "path": ".nova/tools/sftp.md", "outcome": "created", "error": null },
      { "path": ".nova/tools/ftp.md", "outcome": "created", "error": null },
      { "path": "CLAUDE.md", "outcome": "markerreplaced", "error": null }
    ],
    "filesSkipped": [],
    "registered": true,
    "bootstrapNow": [
      "nova.get_instructions(taskKeywords=[...])",
      "nova.tools_bundle(bundle='browser_automation', includeUnavailable=true)"
    ]
  }
}
```

`outcome` is one of `created`, `updated`, `markerreplaced`, `unchanged`, `skipped` or `error`. Nova writes its block into `CLAUDE.md` (Claude Code), `AGENTS.md` (Codex, Cursor and other agents of that convention) and `GEMINI.md` (Gemini CLI, Antigravity): existing files are edited, missing ones are created, so every agent family finds the block. `AGENTS.md` is edited even when `CLAUDE.md` imports it, because the other `AGENTS.md` readers never open `CLAUDE.md`. `filesSkipped` lists each agent entry file Nova left out and why: `covered_by_import` (the root `CLAUDE.md` imports `.claude/CLAUDE.md`) or `same_agent_file_present` (no root `CLAUDE.md` is created next to an existing `.claude/CLAUDE.md`). `status` is `ok`, `partial` (some files written) or `error`.

---

## 4. Operational Best Practices

* **Boundary Adherence:** Nova never modifies agent permission files; it writes only the `.nova/` reference files and its marked block in the agent instruction file.
* **Idempotent:** Safe to run repeatedly. The Nova block is replaced between its markers, the rest of the instruction file is preserved, and an already current block reports `unchanged`.

---

## 5. Related Tools

* [`nova.get_onboarding`](nova-get-onboarding.md)
* [`nova.setup_status`](nova-setup-status.md)
