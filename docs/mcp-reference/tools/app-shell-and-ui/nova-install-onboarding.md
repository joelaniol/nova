# `nova.install_onboarding`

> **Automatically injects Nova MCP server configurations and reference docs into the current agent workspace.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Workspace Onboarding)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.install_onboarding` writes reference files (`.nova/nova-mcp.md`) and updates project agent files with Nova conventions. Adheres strictly to permission boundaries.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `projectRoot` | `string` | Yes | — | — | Absolute path to the project root directory (worktree) where agent config files should be written. |
| `confirmNewLocation` | `boolean` | No | — | — | Set true to onboard a directory Nova has not onboarded before. Already-onboarded worktrees update without it. |
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_install_onboarding",
  "arguments": {
    "workspacePath": "E:\\Projects\\WebWorkflow"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Installed Nova onboarding reference docs in E:\\Projects\\WebWorkflow."
    }
  ],
  "structuredContent": {
    "ok": true,
    "filesWritten": [
      ".nova/nova-mcp.quick.md",
      ".nova/nova-mcp.md"
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Boundary Adherence:** Nova never modifies client permission files (`settings.local.json`); it only populates reference markdown files.
* **Idempotent:** Safe to run repeatedly; preserves existing project instructions.

---

## 5. Related Tools

* [`nova.get_onboarding`](nova-get-onboarding.md)
* [`nova.setup_status`](nova-setup-status.md)
