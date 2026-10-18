# `nova.video_template_save`

> **Saves a set of render values under a name of your own, for nova.video_render.**

* **Core Feature Guide:** [Visual Evidence & Auditing](../../../research/evidence-verification-mode-evm/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

Keep a look you will use again. `values` takes the render values `aspect`, `width`, `fps`, `format` (gif, webm or mp4), `idle`, `keys`, `zoom`, `endHoldMs` and `style`; each one is checked against the same names and ranges as [`nova.video_render`](nova-video-render.md), and anything else is refused. Saving under the same name again replaces the template and counts its version up.

`description` says what the template is for, `notes` how to record for it - both for whoever uses it later. Names starting with `nova-` belong to Nova's own templates; to change one, save a copy under another name. Saved templates stay until [`nova.video_template_delete`](nova-video-template-delete.md) removes them - Nova never deletes one by itself.

### Example

```text
nova.video_template_save(name="diary-clip", description="LinkedIn diary clips", values={"aspect": "4:5", "width": 1080, "fps": 30, "format": "mp4", "idle": "auto", "style": {"textAlign": "center"}})
nova.video_render(template="diary-clip")
```

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `name` | `string` | Yes | — | — | 2..48 characters: a-z, 0-9, '-'. |
| `description` | `string` | No | — | ≤ 200 characters | What the template is for, in one line (e.g. 'LinkedIn diary clips, German captions'). |
| `notes` | `string` | No | — | ≤ 1000 characters | How to record for it, for whoever uses it later. |
| `values` | `object` | Yes | — | — | Export values: aspect, width, fps, format (gif\|webm\|mp4), idle ('auto'), keys, zoom ('auto'), endHoldMs, style {...} (the style values of nova.video_render). |
| `agentId` | `string` | No | — | — | Your agent identity. |

Capability bundle: `visual_evidence` (load it with `nova.tools_bundle(bundle='visual_evidence')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->
