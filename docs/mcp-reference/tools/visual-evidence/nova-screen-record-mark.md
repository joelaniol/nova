# `nova.screen_record_mark`

> **Marks a moment of your running screen recording, with a lossless picture of it.**

* **Core Feature Guide:** [Visual Evidence & Auditing](../../../research/evidence-verification-mode-evm/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

A recording started with [`nova.screen_record_start`](nova-screen-record-start.md) keeps a timeline next to the video: every MCP tool call and every change Nova observed in the picture. `nova.screen_record_mark` adds the moments that matter for your claim - "clicked Save", "error banner visible" - so you and anyone checking your work can find them without watching the whole video.

The mark lands on the first video frame that can show what happened at that moment; pauses are taken into account. With `capture` (on by default) Nova also saves that frame as a PNG - sharper than any frame decoded from the video, and blacked out in the same places as the video.

Only the agent that started the recording can mark it. Read the result with [`nova.screen_record_inspect`](nova-screen-record-inspect.md).

### Example

```text
nova.screen_record_start(area="tab", agentId="tester")
nova.click_selector(selector="#save")
nova.screen_record_mark(label="clicked Save", agentId="tester")
nova.wait_for_selector(selector=".error")
nova.screen_record_mark(label="error banner visible", agentId="tester")
nova.screen_record_stop(agentId="tester")
```

Common refusals: `not_recording`, `video.not_owner`, `video.evidence_off` (the recording was started with `evidence=false`).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `label` | `string` | Yes | — | 1–200 characters | What this moment shows. |
| `capture` | `boolean` | No | `true` | — | Also save a PNG of the frame. |
| `agentId` | `string` | No | — | — | The agentId you started the recording with. |

Capability bundle: `visual_evidence` (load it with `nova.tools_bundle(bundle='visual_evidence')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->
