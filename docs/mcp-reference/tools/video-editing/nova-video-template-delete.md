# `nova.video_template_delete`

> **Deletes a saved template for nova.video_render.**

* **Core Feature Guide:** [Video Composition & Rendering](../../../core-features/media-intelligence/video-editing/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

Removes a template an agent saved with [`nova.video_template_save`](nova-video-template-save.md). Nova's own templates (names starting with `nova-`) cannot be deleted. A name that has no saved template answers `template.not_found`, so a deletion that did nothing is never reported as done.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `name` | `string` | Yes | — | — | The saved template's name. |
| `agentId` | `string` | No | — | — | Your agent identity. |

Capability bundle: `visual_evidence` (load it with `nova.tools_bundle(bundle='visual_evidence')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.video_template_delete",
  "arguments": {
    "name": "custom-showcase"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Template 'custom-showcase' deleted successfully."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "deleted",
    "name": "custom-showcase"
  }
}
```

---

## 4. Operational Best Practices

* **Built-in Protection:** Built-in templates starting with `nova-` (such as `nova-linkedin` and `nova-readme`) are immutable system fixtures and cannot be deleted. Attempting to delete a built-in template returns an error.
* **Pre-Deletion Check:** Call [`nova.video_template_list`](nova-video-template-list.md) beforehand to verify that the template exists and is not currently shared or required by other ongoing agent jobs.
* **Idempotency Awareness:** If the target template was already deleted or never existed, the tool returns `status: "error"` with `reasonCode: "template.not_found"`.

---

## 5. Related Tools

* [`nova.video_render`](nova-video-render.md) — Renders styled videos using templates.
* [`nova.video_template_list`](nova-video-template-list.md) — Lists available render templates and presets.
* [`nova.video_template_save`](nova-video-template-save.md) — Saves custom rendering presets.
