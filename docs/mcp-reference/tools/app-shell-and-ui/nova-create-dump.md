# `nova.create_dump`

> **Writes a diagnostic dump of a browser tab (screenshot, DOM, page info, and in full mode MHTML and resources) to a folder on disk.**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.create_dump` captures a tab's state for offline debugging. Each call creates its own folder under `%LOCALAPPDATA%\nova-cognitive\Nova\Dumps\` (named `<UTC timestamp>_<target>_<short id>`) with an `index.html` overview and a `manifest.json` that lists every capture step and whether it succeeded. `mode: "fast"` stores only the screenshot and the DOM and skips network fetches; `mode: "full"` (the default) also stores MHTML, inline scripts and resources. Dump folders older than 180 days are removed automatically.

If the screenshot step fails, the dump is still written and the result reports `status: "degraded"` with a `reasonCode`.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `mode` | `string` | No | `"full"` | `full`, `fast` | Dump depth. 'full': screenshot + DOM + MHTML + inline scripts + resources. 'fast': screenshot + DOM only (no network fetches, much faster). |

Capability bundle: `page_read_debug` (load it with `nova.tools_bundle(bundle='page_read_debug')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_create_dump",
  "arguments": {
    "targetId": "tab-1",
    "mode": "fast"
  }
}
```

### JSON-RPC Response
The first text block names the dump folder; a second text block carries the contents of `manifest.json` when it could be read (omitted here).

```json
{
  "content": [
    {
      "type": "text",
      "text": "Dump created: C:\\Users\\you\\AppData\\Local\\nova-cognitive\\Nova\\Dumps\\20261002_141503_tab-1_9f3c2a1b"
    }
  ],
  "structuredContent": {
    "targetId": "tab-1",
    "mode": "fast",
    "artifactDir": "C:\\Users\\you\\AppData\\Local\\nova-cognitive\\Nova\\Dumps\\20261002_141503_tab-1_9f3c2a1b",
    "dumpDir": "C:\\Users\\you\\AppData\\Local\\nova-cognitive\\Nova\\Dumps\\20261002_141503_tab-1_9f3c2a1b",
    "status": "ok",
    "reasonCode": null,
    "degraded": false,
    "screenshotOk": true,
    "screenshotStatus": "ok",
    "screenshotReasonCode": null,
    "screenshotFile": "screenshot.png",
    "screenshotError": null
  }
}
```

---

## 4. Operational Best Practices

* **Post-Incident Analysis:** Create a dump when an agent hits an unrecoverable navigation or script error, before changing the page.
* **Use `fast` when time matters:** `full` fetches resources over the network and takes noticeably longer.
* **Privacy Check:** A dump contains the page as the logged-in user sees it. Review it before sharing it outside your machine.

---

## 5. Related Tools

* [`nova.capture_screenshot`](../visual-evidence/nova-capture-screenshot.md)
* [`nova.console_read`](../dom-and-reading/nova-console-read.md)
