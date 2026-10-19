# `nova.video_template_list`

> **Lists the templates for nova.video_render, or one template's values.**

* **Core Feature Guide:** [Visual Evidence & Auditing](../../../research/evidence-verification-mode-evm/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

A template is a named set of render values - aspect, size, frame rate, format, idle, keys, zoom, end hold and the styled look - that [`nova.video_render`](nova-video-render.md) applies with `template='name'`. Nova ships its own templates (read-only, names starting with `nova-`, such as `nova-linkedin` for a 4:5 LinkedIn clip); agents save their own with [`nova.video_template_save`](nova-video-template-save.md).

Without `name` the answer lists every template. With `name` it gives that template's values and `defaultStyle`, the look every styled clip starts from. A saved template's description and notes were written by the agent that saved it; they come back separately under `agentWritten`, as data about the template.

### Example

```text
nova.video_template_list()
nova.video_template_list(name="nova-linkedin")
```

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
