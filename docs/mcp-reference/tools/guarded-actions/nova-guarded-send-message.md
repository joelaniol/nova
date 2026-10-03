# `nova.guarded_send_message`

High-level guarded macro for chat interfaces (ChatGPT, Claude.ai, Gemini, Slack, Teams): auto-discovers the composer, types text with read-back verification, resolves the send button, clicks it, and verifies delivery in a single atomic operation.

---

## 1. Overview

Sending a prompt or chat message in modern AI interfaces involves complex interactions: locating the contenteditable or textarea container, waiting for disabled send buttons to become active, handling focus state transitions, and verifying that the message was actually dispatched.

`nova.guarded_send_message` unifies this entire workflow into a **single guarded atomic action**:
1. **Composer Auto-Discovery:** Locates the chat input field (handling Shadow DOM and embedded iframes).
2. **Typing & Read-Back Verification:** Types the message text and reads it back from the DOM to assert complete transmission before clicking.
3. **Send-Button Resolution:** Automatically pairs the composer with its nearby send button, tolerating `disabled` buttons that activate only after typing.
4. **Closed-Loop Postcondition Verification:** Asserts that the composer cleared, the send button transitioned to a stop/streaming state, or the user's message bubble appeared in the transcript feed.

* **Capability Bundle:** `form_submission`, `guarded_actions`
* **Zero Selector Guessing:** When `selector` is omitted, Nova automatically locates both the composer input and the send button.
* **Closed-Loop Safety:** Injects an automated `transitionContract` ensuring messages are never submitted blindly or duplicated.
* **Blocker Clearance:** Can automatically clear cookie banners or dialogs obscuring the composer (`autoDismissBlockers: true`).

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`text`** | `string` | No | `null` | Text to type into the composer. Auto-chunked for long prompts. Alias: `message`. |
| **`selector`** | `string` | No | `null` | Optional explicit CSS selector for the send button. Auto-detected if omitted. |
| **`ctaRef`** | `integer`| No | `null` | Optional CTA handle reference (from `nova.perceive`). |
| **`targetId`** | `string` | No | `"active"` | Target tab ID from `nova.tabs`, or `"active"`. |
| **`autoDismissBlockers`**| `boolean`| No | `false` | Automatically dismiss modals or banners blocking the chat interface. |
| **`activateIfNeeded`** | `boolean` | No | `true` | Temporarily activate target tab before pointer dispatch. |
| **`timeoutMs`** | `integer` | No | `10000` | Max milliseconds to wait for element appearance (0–300,000 ms). |
| **`includeScreenshot`**| `boolean`| No | `false` | Capture visual evidence after message delivery. |
| **`agentId`** | `string` | No | `"default"` | Agent identity for claim lease verification. |

---

## 3. Example Calls

### Fully Automated Prompt Dispatch (Auto-Discovery)
```json
{
  "text": "Please summarize the key takeaways of the uploaded financial report in three bullet points."
}
```

### Explicit Selector with Blocker Clearance
```json
{
  "text": "Confirm order and proceed to invoice generation.",
  "selector": "button[data-testid='send-button']",
  "autoDismissBlockers": true
}
```

---

## 4. Return Value Structure

```json
{
  "ok": true,
  "actionDispatched": true,
  "verified": true,
  "targetId": "tab-101",
  "effectiveSelector": "button[data-testid='send-button']",
  "composerResolution": {
    "inputType": "contenteditable",
    "textLength": 84,
    "readbackVerified": true
  },
  "verifyState": "verified",
  "retryAdvice": "do_not_retry"
}
```

---

## 5. Common Errors & Troubleshooting

| Reason Code | Cause | Corrective Action |
| :--- | :--- | :--- |
| `action.no_input_field_found` | No visible chat composer textarea or contenteditable found. | Check if the chat page is finished loading using [`nova.wait_for_selector`](../browser-automation/nova-wait-for-selector.md). |
| `action.no_send_button_found` | Composer was found, but no send button could be paired with it. | Provide explicit `selector` for the send button. |
| `action.ambiguous_input_field` | Multiple input fields exist on page with equal pairing confidence. | Pass an explicit `selector` to identify the desired input. |

---

## 6. Related Tools & Documentation

* [`nova.click_selector`](../browser-automation/nova-click-selector.md) — Low-level single-element click execution.
* [`nova.type_selector`](../browser-automation/nova-type-selector.md) — Low-level text input typing.
* [`nova.guarded_submit_form`](nova-guarded-submit-form.md) — Guarded form submissions.
* [Agent Awareness Gates (AAG)](../../../core-features/aag.md) — Pre-action and post-action verification contracts.
