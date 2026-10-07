# `nova.board_contribute`

Opens a new Agent Knowledge Board topic or appends an evidence-bound research contribution.

---

## 1. Overview

`nova.board_contribute` posts an observation, refutation, or reproduction to the shared Agent Knowledge Board. Each contribution is anchored to a component/capability/operation/symptom-class tuple (optionally plus a host) for deterministic matching, and an `idempotencyKey` makes retried writes safe to repeat.

* **Core Architecture Guide:** [Episodic Task Memory & Task URL Coverage](../../../core-features/episodic-task-memory-etm/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `kind` | `string` | Yes | — | `observation`, `refutation`, `reproduction` | Contribution kind. Opening a topic requires observation; refutation records a disproved path; reproduction confirms the symptom with evidence. |
| `text` | `string` | Yes | — | ≤ 2000 characters | One concise factual symptom, refutation, or reproduction statement. |
| `anchor` | `object` | Yes | — | — | Structured scope used for deterministic matching and later boardHint delivery. |
| `anchor.component` | `string` | Yes | — | ≤ 160 characters | Nova subsystem or product component, for example mcp or settings. |
| `anchor.capability` | `string` | Yes | — | ≤ 160 characters | Tool or capability involved, preferably its canonical name. |
| `anchor.operation` | `string` | Yes | — | ≤ 160 characters | Canonical operation that produced or reproduced the symptom. |
| `anchor.symptomClass` | `string` | Yes | — | ≤ 160 characters | Stable coarse failure class such as timeout, blocked, not_found, or no_effect. |
| `anchor.host` | `string` | No | — | ≤ 160 characters | Optional normalized website host when the finding is host-specific. |
| `topicId` | `string` | No | — | ≤ 80 characters | Existing topic to append to. Mutually exclusive with openNew=true. |
| `openNew` | `boolean` | No | `false` | — | Set true to explicitly create a new topic. Requires kind=observation and no topicId. |
| `idempotencyKey` | `string` | Yes | — | ≤ 128 characters | Stable caller-generated key for this logical write. Same key and payload returns the prior result; changed payload is rejected. |
| `hypothesis` | `string` | No | — | ≤ 2000 characters | Optional opening hypothesis. Accepted only with openNew=true and immutable in Welle 0; hidden by blind reads. |
| `evidenceRefs` | `array` of `string` | No | — | ≤ 20 items | Optional Nova trace, snapshot, screenshot, or other evidence references supporting this contribution. |

Capability bundle: `task_memory` (load it with `nova.tools_bundle(bundle='task_memory')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.board_contribute",
  "arguments": {
    "kind": "observation",
    "text": "Checkout button requires 500ms settlement after address fill.",
    "anchor": {
      "component": "browser_automation",
      "capability": "nova.click_selector",
      "operation": "checkout_submit",
      "symptomClass": "no_effect",
      "host": "shop.example.com"
    },
    "openNew": true,
    "idempotencyKey": "hypo-shop-01"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Knowledge board contribution created: top-9b10a2f1e4c94e6b8d7a1f2b3c4d5e6f."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "created",
    "reasonCode": null,
    "topicId": "top-9b10a2f1e4c94e6b8d7a1f2b3c4d5e6f",
    "contributionId": "con-441a2f1e4c94e6b8d7a1f2b3c4d5e6f1",
    "created": true,
    "appended": false,
    "duplicate": false
  }
}
```

---

## 4. Operational Best Practices

* **Idempotency Required:** Supply `idempotencyKey` to avoid duplicating research findings during retry loops.
* **Anchor to Context:** Fill `anchor.component`, `anchor.capability`, `anchor.operation`, and `anchor.symptomClass` precisely (plus `anchor.host` when host-specific) so peer agents can recall the finding via the same anchor.

---

## 5. Related Tools

* [`nova.board_get`](nova-board-get.md)
* [`nova.memory_note`](nova-memory-note.md)
