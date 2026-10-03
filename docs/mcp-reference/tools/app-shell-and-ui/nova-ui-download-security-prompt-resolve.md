# `nova.ui_download_security_prompt_resolve`

> **Resolves Nova's executable download security warning dialog (.exe, .msi, .ps1, .bat).**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Security Gate Resolution)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_download_security_prompt_resolve` allows or blocks potentially dangerous file downloads flagged by Windows SmartScreen heuristics.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `decision` | `string` | Yes | — | `keep`, `discard` | discard: do not write the file (safe, unblocks browsing). keep: write it to the downloads folder. |
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_download_security_prompt_resolve",
  "arguments": {
    "action": "allow_once"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Allowed executable download once."
    }
  ],
  "structuredContent": {
    "ok": true,
    "action": "allow_once",
    "downloadAllowed": true
  }
}
```

---

## 4. Operational Best Practices

* **Verified Hashes:** Only allow executable downloads from known, trusted sources with verified file hashes.

---

## 5. Related Tools

* [`nova.downloads_wait`](../downloads/nova-downloads-wait.md)
