# `nova.video_template_save`

> **Saves a set of render values under a name of your own, for nova.video_render.**

* **Core Feature Guide:** [Video Composition & Rendering](../../../core-features/media-intelligence/video-editing/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

Keep a look you will use again. `values` takes the render values `aspect`, `width`, `fps`, `format` (gif, webm or mp4), `idle`, `keys`, `zoom`, `endHoldMs` and `style`; each one is checked against the same names and ranges as [`nova.video_render`](nova-video-render.md), and anything else is refused. Saving under the same name again replaces the template and counts its version up.

`notes` explains how to record for it, for whoever uses it later. Names starting with `nova-` belong to Nova's own templates; to change one, save a copy under another name. Saved templates stay until [`nova.video_template_delete`](nova-video-template-delete.md) removes them - Nova never deletes one by itself.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `name` | `string` | Yes | — | — | 2..48 characters: a-z, 0-9, '-'. |
| `description` | `string` | No | — | ≤ 200 characters | What the template is for, in one line (e.g. 'LinkedIn diary clips, German captions'). |
| `notes` | `string` | No | — | ≤ 1000 characters | How to record for it, for whoever uses it later. |
| `values` | `object` | Yes | — | — | Render values: aspect, width, fps, format (gif\|webm\|mp4), idle ('auto'), keys, zoom ('auto'), endHoldMs, motion (standard\|short\|reduced), style {...} (the style values of nova.video_render). A call's own segments replace the template's idle. |
| `agentId` | `string` | No | — | — | Your agent identity. |

Capability bundle: `visual_evidence` (load it with `nova.tools_bundle(bundle='visual_evidence')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.video_template_save",
  "arguments": {
    "name": "custom-showcase",
    "notes": "Record in 1360x970 window. Use role='check' markers for value assertions.",
    "values": {
      "aspect": "4:5",
      "width": 1080,
      "fps": 30,
      "format": "mp4",
      "idle": "auto",
      "keys": true
    }
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Template 'custom-showcase' saved successfully (version 1)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "saved",
    "name": "custom-showcase",
    "version": 1,
    "values": {
      "aspect": "4:5",
      "width": 1080,
      "fps": 30,
      "format": "mp4",
      "idle": "auto",
      "keys": true
    }
  }
}
```

---

## 4. Operational Best Practices

* **Reserved Prefix:** Do not attempt to save templates prefixed with `nova-`. Those are reserved for built-in fixtures shipped with the application.
* **Strict Parameter Bounds:** All nested properties inside `values` are strictly validated against production limits: `width` (64–1920), `fps` (1–30), `format` (`gif`, `webm`, `mp4`), and `motion` (`standard`, `short`, `reduced`).
* **Version Tracking:** When re-saving an existing custom template name, Nova updates the definition in place and increments its internal `version` counter automatically.

---

## 5. Related Tools

* [`nova.video_render`](nova-video-render.md) — Renders styled videos using templates.
* [`nova.video_template_list`](nova-video-template-list.md) — Lists available render templates and presets.
* [`nova.video_template_delete`](nova-video-template-delete.md) — Deletes custom render presets.
