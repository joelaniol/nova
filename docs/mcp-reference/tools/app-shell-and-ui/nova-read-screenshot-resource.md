# `nova.read_screenshot_resource`

> **Reads a screenshot resource URI (`nova://screenshot/...`) returned by a capture tool and returns its image bytes as base64.**

* **Core Feature Guide:** [EVM & Visual Evidence](../../../core-features/evm-and-visual-evidence.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.read_screenshot_resource` resolves a `nova://screenshot/...` URI emitted by a capture tool (such as `nova.capture_screenshot`) and returns the backing image file's bytes, base64-encoded, along with its MIME type. The resource is only readable by the MCP session that created it and expires after a limited time; an expired, not-found, or inaccessible URI fails with a structured `reasonCode`. The response does not carry image width/height — read those from the capture tool's own result instead.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `uri` | `string` | Yes | — | — | Screenshot resource URI returned by capture tools, starting with nova://screenshot/.... Aliases accepted before validation: resourceUri, fullImageResourceUrl, url. |
| `maxBytes` | `integer` | No | `1048576` | 1024–50000000 | Maximum bytes of the full screenshot resource to return as base64. |

Capability bundles: `page_read_debug`, `visual_evidence`.
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_read_screenshot_resource",
  "arguments": {
    "uri": "nova://screenshot/ctx-7f2a/20261003_120000_a1b2c3d4.png"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "iVBORw0KGgoAAAANSUhEUgAA..."
    }
  ],
  "structuredContent": {
    "profileId": null,
    "source": "screenshot-resource",
    "frameId": null,
    "url": "nova://screenshot/ctx-7f2a/20261003_120000_a1b2c3d4.png",
    "resourceUri": "nova://screenshot/ctx-7f2a/20261003_120000_a1b2c3d4.png",
    "mimeType": "image/png",
    "ok": true,
    "status": null,
    "base64Encoded": true,
    "truncated": false,
    "chars": null,
    "bytes": 184320,
    "resourceText": null,
    "resourceBase64": "iVBORw0KGgoAAAANSUhEUgAA...",
    "filePath": "%LOCALAPPDATA%\\NovaBrowser\\mcp\\screenshots\\ctx-7f2a\\20261003_120000_a1b2c3d4.png",
    "expiresAt": "2026-10-03T12:05:00.0000000Z",
    "outputBudget": { "...": "..." }
  }
}
```

A not-found, expired, or inaccessible URI fails with error code -32002 and a `reasonCode` of `RESOURCE_EXPIRED_OR_NOT_FOUND`, `RESOURCE_ACCESS_DENIED`, or `RESOURCE_FILE_MISSING`.

---

## 4. Operational Best Practices

* **Visual Reasoning:** Use when feeding captured viewports into multimodal LLM vision APIs.

---

## 5. Related Tools

* [`nova.capture_screenshot`](../visual-evidence/nova-capture-screenshot.md)
* [`nova.tab_snapshot`](../browser-automation/nova-tab-snapshot.md)
