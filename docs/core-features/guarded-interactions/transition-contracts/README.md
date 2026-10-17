# Closed-Loop Transition Contracts & Idempotency Safeguards

> [!NOTE]
> Every guarded interaction in Nova AI Workspace is evaluated through a **Transition Contract**. Transition contracts shift the responsibility of verifying UI mutations from conversational LLM memory into deterministic protocol assertions. They define explicit preconditions, atomic commit points, success criteria, explicit failure traps, and non-idempotent retry policies.

---

## 1. Anatomy of a Transition Contract

A `transitionContract` is a structured JSON specification that defines the expected lifecycle of a state-changing web action:

```json
{
  "actionKind": "submit_form",
  "retryPolicy": "non_idempotent",
  "ambiguityPolicy": "signal",
  "stabilityWindowMs": 3000,
  "stabilityMs": 500,
  "preconditions": {
    "all": [
      { "factKey": "form.fields.valid", "operator": "eq", "expected": true }
    ]
  },
  "postconditions": {
    "success": {
      "any": [
        { "factKey": "url.changed", "operator": "eq", "expected": true },
        { "factKey": "form.successIndicator.visible", "operator": "eq", "expected": true }
      ]
    },
    "forbidden": {
      "any": [
        { "factKey": "auth.authError", "operator": "eq", "expected": true }
      ]
    },
    "ambiguous": {
      "any": [
        { "factKey": "auth.mfaChallenge", "operator": "eq", "expected": true }
      ]
    }
  }
}
```

### Core Configuration Fields:

| Field | Type | Default | Description |
| :--- | :--- | :--- | :--- |
| `actionKind` | `string` | `"custom"` | Interaction classification: `send_message`, `submit_form`, `select_option`, `dismiss_overlay`, or `custom`. |
| `retryPolicy` | `string` | `"non_idempotent"` | `non_idempotent`: cautious retry advice; `idempotent`: safe to re-dispatch; `no_retry`: suppresses retry advice. |
| `ambiguityPolicy` | `string` | `"signal"` | Action taken when indeterminate: `signal` (reports indeterminate), `retry_once` (one safe retry), `abort`. |
| `stabilityWindowMs`| `integer` | `3000` | Maximum observation window to wait for postconditions to stabilize. |
| `stabilityMs` | `integer` | `500` | Duration for which a success condition must remain true before passing (prevents transient glitches). |

---

## 2. Fact Assertion Syntax & Operators

Every condition inside `preconditions` and `postconditions` is an array of assertion objects:

```json
{
  "factKey": "dom.element.count",
  "operator": "gte",
  "expected": 1,
  "frameId": "frame-main-content"
}
```

### Supported Operators:

| Operator | Semantics | Example |
| :--- | :--- | :--- |
| `eq` | Strict equality ($==$) | `{ "factKey": "auth.loggedIn", "operator": "eq", "expected": true }` |
| `not_eq` / `neq` | Inequality (!=) | `{ "factKey": "selectedModel.label", "operator": "not_eq", "expected": "GPT-4" }` |
| `exists` | Fact key is present and non-null | `{ "factKey": "composer.send_button.stopped", "operator": "exists" }` |
| `not_exists` | Fact key is absent or null | `{ "factKey": "overlay.blockingDiv", "operator": "not_exists" }` |
| `contains` | Substring or array membership | `{ "factKey": "page.url", "operator": "contains", "expected": "/dashboard" }` |
| `gt` / `gte` | Greater than ($\gt$, $\ge$) | `{ "factKey": "cart.itemCount", "operator": "gt", "expected": 0 }` |
| `lt` / `lte` | Less than ($\lt$, $\le$) | `{ "factKey": "form.errorCount", "operator": "lte", "expected": 0 }` |

---

## 3. Additive Contract Merging

When calling a high-level guarded tool like `nova.guarded_send_message` or `nova.guarded_submit_form`, callers do not need to construct an entire contract from scratch. Nova provides built-in macro templates for each action.

If an agent needs to add custom verification rules (such as verifying that a specific order number rendered after checkout), it passes an optional `transitionContract` argument.

Nova merges the caller's contract **additively** via its contract merger:

```
┌─────────────────────────────────┐       ┌─────────────────────────────────┐
│     Built-in Macro Template     │       │     Agent-Supplied Extension    │
│  - Pre: form.fields.valid == 1  │   +   │  - Post: dom.text contains      │
│  - Post: url.changed == true    │       │          "Order Confirmed"      │
│  - Retry: non_idempotent        │       │                                 │
└────────────────┬────────────────┘       └────────────────┬────────────────┘
                 │                                         │
                 └────────────────────┬────────────────────┘
                                      ▼
                        ┌───────────────────────────┐
                        │   Merged Closed-Loop Plan │
                        │  - Pre: form.fields.valid │
                        │  - Post: url.changed OR   │
                        │    "Order Confirmed" text │
                        │  - Retry: non_idempotent  │
                        └───────────────────────────┘
```

### Security & Invariant Pinning:
* **Pinned Array Paths:** On `nova.guarded_send_message`, built-in send preconditions and success assertions are pinned. Caller extensions cannot remove built-in assertions; they are merged into the execution plan additively.
* **Non-Idempotent Preservation:** High-impact tools enforce `retryPolicy: "non_idempotent"`. Even if a caller attempts to supply `retryPolicy: "idempotent"` to a chat message send, Nova overrides it to ensure non-idempotent protection remains active.

---

## 4. Stability Windows & Debounce Holds

Web interfaces frequently undergo transient DOM animations immediately after a click:
* A submit button briefly shows a loading spinner, then restores its previous label if an API request fails.
* A modal starts closing via a CSS fade-out animation, but is reopened by an error banner.

If an automation tool checks postconditions immediately (at millisecond 10), it may capture a temporary CSS class and declare success prematurely.

Nova enforces two temporal guards:
1. **`stabilityWindowMs` (Observation Window):** The maximum time Nova will observe the page waiting for postconditions to resolve (default: 3,000ms).
2. **`stabilityMs` (Hold Window):** Once a success condition is met, it must remain true continuously for `stabilityMs` (default: 500ms) without triggering any forbidden postconditions. If the state flashes or reverts during the hold window, verification is withheld.

---

## Related Documentation

* [Guarded Interactions Overview](../README.md)
* [Autonomous Chat Engine & Reply Watch](../chat-macro/README.md)
* [Transactional Form Submissions & Auth Gates](../form-submission/README.md)
* [Closed-Loop System (CLS) Architecture](../../closed-loop-system-cls/README.md)
* [Tool Catalog: Guarded Actions & Blocker Clearance](../../../mcp-reference/tools/guarded-actions/README.md)
