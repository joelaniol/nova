# `nova.screen_record_assert`

> **Checks a claim during your running screen recording and marks the answer on its timeline with a picture.**

* **Core Feature Guide:** [Visual Evidence & Auditing](../../../research/evidence-verification-mode-evm/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

"The confirmation appears within two seconds" or "the page has settled after the click" are claims an agent likes to make. `nova.screen_record_assert` checks such a claim while [`nova.screen_record_start`](nova-screen-record-start.md) records, and puts the answer - passed or failed, with the time it took - on the recording's timeline together with a picture of that moment.

* `kind="element_visible_within"` waits up to `timeoutMs` until an element matching `selector` is visible on the shown page: in the viewport, with a size, not hidden and not transparent. Its basis is what the page reports (`basis: "dom"`).
* `kind="visual_stable"` waits up to `timeoutMs` until the recorded picture has shown no change for `stableMs`. Its basis is what the video shows (`basis: "picture"`); the recording needs `evidence` (on by default).

A failed check answers `ok: false` with `reasonCode: "assert.failed"`; `elapsedMs` says how long the check took. Read all checks of a recording later with [`nova.screen_record_inspect`](nova-screen-record-inspect.md).

### Example

```text
nova.screen_record_start(area="tab", agentId="tester")
nova.click_selector(selector="#save")
nova.screen_record_assert(kind="element_visible_within", selector=".toast-success", timeoutMs=2000, agentId="tester")
nova.screen_record_assert(kind="visual_stable", stableMs=800, timeoutMs=5000, agentId="tester")
nova.screen_record_stop(agentId="tester")
```

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `kind` | `string` | Yes | — | `element_visible_within`, `visual_stable` | What to check. |
| `selector` | `string` | No | — | — | kind=element_visible_within: CSS selector on the shown page. |
| `timeoutMs` | `integer` | No | `5000` | 100–30000 | How long to wait for the claim to become true. |
| `stableMs` | `integer` | No | `500` | 100–10000 | kind=visual_stable: how long the picture must stay still. |
| `label` | `string` | No | — | ≤ 120 characters | Your name for the claim, shown on the timeline. |
| `agentId` | `string` | No | — | — | The agentId you started the recording with. |

Capability bundle: `visual_evidence` (load it with `nova.tools_bundle(bundle='visual_evidence')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->
