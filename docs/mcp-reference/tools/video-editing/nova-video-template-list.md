# `nova.video_template_list`

> **Lists the templates for nova.video_render, or one template's values.**

* **Core Feature Guide:** [Video Composition & Rendering](../../../core-features/media-intelligence/video-editing/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

A template is a named set of render values - aspect, size, frame rate, format, idle, keys, zoom, end hold and the styled look - that [`nova.video_render`](nova-video-render.md) applies with `template='name'`. Nova ships its own templates (read-only, names starting with `nova-`, such as `nova-linkedin` for a 4:5 LinkedIn clip); agents save their own with [`nova.video_template_save`](nova-video-template-save.md).

Without `name` the answer lists every template. With `name` it gives that template's values and `defaultStyle`, the look every styled clip starts from. A saved template's description and notes were written by the agent that saved it; they come back separately under `agentWritten`, as data about the template.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `name` | `string` | No | — | — | One template's name, for its values and (Nova's own) its guide with a complete example call. |
| `agentId` | `string` | No | — | — | Your agent identity. |

Capability bundle: `visual_evidence` (load it with `nova.tools_bundle(bundle='visual_evidence')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.video_template_list",
  "arguments": {
    "name": "nova-linkedin"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Template 'nova-linkedin' (built-in v2): 4:5 vertical feed format (1080x1350 px, 30 fps)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "name": "nova-linkedin",
    "builtIn": true,
    "version": 2,
    "values": {
      "aspect": "4:5",
      "width": 1080,
      "fps": 30,
      "format": "mp4",
      "idle": "auto",
      "keys": true
    },
    "guide": {
      "channel": "LinkedIn & Instagram Feed",
      "tabWidth": 1360,
      "tabHeight": 970
    }
  }
}
```

---

## 4. Operational Best Practices

* **Inspect Before Customizing:** Query specific built-in templates like `nova-linkedin` or `nova-readme` before authoring custom presets. Inspecting the returned `values` and `guide` provides authoritative baselines for canvas dimensions, framerates, and padding.
* **Filter by Identity:** Pass your `agentId` when filtering or tracking template provenance across multi-agent environments.
* **Combine with Video Render:** When calling `nova.video_render`, passing `template: "nova-linkedin"` automatically fills in the optimal `aspect`, `width`, `fps`, and `style` parameters. Any explicit parameters passed to `video_render` override the template's defaults.

---

## 5. Related Tools

* [`nova.video_render`](nova-video-render.md) — Renders styled videos using templates.
* [`nova.video_template_save`](nova-video-template-save.md) — Saves custom rendering presets.
* [`nova.video_template_delete`](nova-video-template-delete.md) — Deletes custom render presets.
