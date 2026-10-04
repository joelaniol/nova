# `nova.ui_download_security_prompt_resolve`

> **Answers Nova's "Keep this file?" question for a download that Windows can run (for example .exe, .msi, .bat, .ps1).**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

Before a file type that Windows can execute is written to disk, Nova replaces the WebView2 default handling with its own question "Keep this file?" (buttons **Keep** and **Discard**). The same blocklist decides which types Nova never opens automatically after download. `nova.ui_download_security_prompt_resolve` answers that question for the agent: `discard` does not write the file and unblocks browsing; `keep` writes it to the downloads folder and is recorded in Nova's log. Nova does not check what the file does.

If no question is open, the call returns `ok: false` with `reasonCode: "download_security.no_prompt_open"`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `decision` | `string` | Yes | — | `keep`, `discard` | discard: do not write the file (safe, unblocks browsing). keep: write it to the downloads folder. |

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_download_security_prompt_resolve",
  "arguments": {
    "decision": "discard"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Download security prompt resolved (discard, status=discarded)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "decision": "discard",
    "status": "discarded",
    "reasonCode": "none",
    "message": "The file was not written; browsing is unblocked.",
    "promptWasOpen": true,
    "fileName": "setup.exe",
    "extension": ".exe"
  }
}
```

With `decision: "keep"` the result reports `status: "kept"`.

---

## 4. Operational Best Practices

* **Keep only what the task needs:** Use `keep` when the download is the point of the task (a build artefact, an installer under test) and the source is known; otherwise `discard`.
* **Check the outcome:** After `keep`, confirm the finished download with `nova.downloads_wait`.

---

## 5. Related Tools

* [`nova.downloads_wait`](../downloads/nova-downloads-wait.md)
