# `nova.video_template_delete`

> **Deletes a saved template for nova.video_render.**

* **Core Feature Guide:** [Visual Evidence & Auditing](../../../research/evidence-verification-mode-evm/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

Removes a template an agent saved with [`nova.video_template_save`](nova-video-template-save.md). Nova's own templates (names starting with `nova-`) cannot be deleted. A name that has no saved template answers `template.not_found`, so a deletion that did nothing is never reported as done.

### Example

```text
nova.video_template_delete(name="diary-clip")
```

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

## 3. Related Tools

* [`nova.video_render`](nova-video-render.md) — Renders styled videos using templates
* [`nova.video_template_list`](nova-video-template-list.md) — Lists available render templates and presets
* [`nova.video_template_save`](nova-video-template-save.md) — Saves custom rendering presets
