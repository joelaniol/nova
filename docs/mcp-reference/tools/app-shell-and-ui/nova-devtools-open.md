# `nova.devtools_open`

> **Opens the Chromium DevTools inspection window for a specified browser tab.**

* **Capability Bundle:** `app_shell_recovery, onboarding`
* **Security Tier:** Tier 2 (Developer Tooling)
* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.devtools_open` launches the native Chromium developer tools window docked or detached for interactive visual debugging by human operators.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID or 'active'. |
| `mode` | `string` | No | — | `docked`, `popout` | DevTools display mode override. 'popout': separate window, the mode WebView2 supports natively. 'docked': attached to the bottom of Nova's browser surface — it overlays the lower part of the page instead of shrinking it, so page content underneath stays covered. If omitted, Nova uses the Settings default (fresh default: popout). |
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_devtools_open",
  "arguments": {
    "targetId": "tab-1"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Opened Chromium DevTools for tab-1."
    }
  ],
  "structuredContent": {
    "ok": true,
    "targetId": "tab-1",
    "isOpen": true
  }
}
```

---

## 4. Operational Best Practices

* **Operator Assistance:** Open DevTools when requesting human operator triage on complex DOM bugs.
* **Automated Workflows:** Prefer `nova.cdp` or `nova.console_read` over opening visual DevTools in headless automation.

---

## 5. Related Tools

* [`nova.devtools_select_panel`](nova-devtools-select-panel.md)
* [`nova.cdp`](nova-cdp.md)
