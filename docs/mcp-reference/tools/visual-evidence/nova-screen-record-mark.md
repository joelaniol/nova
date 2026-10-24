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
| `selector` | `string` | No | — | — | Where this moment's proof is on the shown page (e.g. the table row you checked): Nova measures the element now and keeps its place on the timeline in video pixels (box), for effects that point at it. Not found = the mark is refused (video.element_not_found); nothing is guessed. |
| `rect` | `object` | No | — | — | Instead of selector: the place in CSS pixels of the shown page. |
| `rect.x` | `number` | Yes | — | — | — |
| `rect.y` | `number` | Yes | — | — | — |
| `rect.width` | `number` | Yes | — | — | — |
| `rect.height` | `number` | Yes | — | — | — |
| `check` | `object` | No | — | — | A check this moment shows - Nova compares the two values itself and returns its verdict (ok, reason); only its ok=true may become a tick in a clip. Numbers compare as numbers: spaces and thousands separators ignored, decimal comma or point; a single separator followed by exactly three digits ('17,098', '9.984') is ambiguous without a locale and fails with reason number_ambiguous. Your own ok can only take the tick away (checkMismatch when Nova disagrees). |
| `check.item` | `string` | Yes | — | ≤ 120 characters | What is checked, e.g. 'Russia'. |
| `check.expected` | `string` | Yes | — | ≤ 120 characters | The source value exactly as shown, e.g. '17,098,246'. |
| `check.actual` | `string` | Yes | — | ≤ 120 characters | The value under test exactly as shown, e.g. '17.098.246'. |
| `check.unit` | `string` | No | — | ≤ 20 characters | A unit to strip from both ends, e.g. 'km²'. |
| `check.tolerance` | `number` | No | `0` | 0–0.1 | Relative tolerance: 0.001 = ±0.1 %. 0 = equal. |
| `check.expectedLocale` | `string` | No | — | `de`, `en` | How expected is formatted: 'de' (1.234,5) or 'en' (1,234.5). |
| `check.actualLocale` | `string` | No | — | `de`, `en` | How actual is formatted. |
| `check.ok` | `boolean` | No | — | — | Your own verdict (optional); it never overrides Nova's. |
| `caption` | `string` | No | — | ≤ 80 characters | The clip's text for this moment, two to five words ('Source: Wikipedia'); nova.video_render(captionsFromMarks=true) shows it. Without caption a short label (up to 40 characters) serves. |
| `agentId` | `string` | No | — | — | The agentId you started the recording with. |

Capability bundle: `visual_evidence` (load it with `nova.tools_bundle(bundle='visual_evidence')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->
