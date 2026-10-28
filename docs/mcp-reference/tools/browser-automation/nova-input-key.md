# `nova.input_key`

Dispatches a physical keyboard keypress (`keydown` followed by `keyup`) to the currently focused DOM element or active viewport.

* **Interaction Guide:** [Input Dispatch](../../../core-features/browser-interaction/input-dispatch/README.md)

---

## 1. Overview

`nova.input_key` simulates low-level physical keystrokes for control keys, navigation keys, and shortcuts that cannot be sent via standard text input (e.g. `Enter` to submit a form, `Escape` to dismiss a popover, `Tab` to navigate focus rings, or arrow keys to navigate autocomplete menus).

* **Hardware-Level Dispatch:** Uses direct CDP keyboard input events with correct virtual key codes and scan codes.
* **Focused Target:** Sends keys to whatever element currently has focus.

---

## 2. Key Capabilities & Features

### A. Supported Special Keys
The `key` parameter accepts standardized key names:
* **Submission / Action:** `Enter`, `Space`
* **Navigation:** `Tab`, `ArrowUp`, `ArrowDown`, `ArrowLeft`, `ArrowRight`, `Home`, `End`, `PageUp`, `PageDown`
* **Editing:** `Backspace`, `Delete`
* **Dismissal:** `Escape`
* **Function Keys:** `F1` through `F12`

### B. Form Submission & Autocomplete Selection
When navigating custom comboboxes or dropdown search bars (e.g. search bars with instant suggestions), agents combine typing with arrow keys and `Enter`:
1. `nova.type_selector` enters the query.
2. `nova.input_key` with `key: "ArrowDown"` highlights the desired item.
3. `nova.input_key` with `key: "Enter"` selects it.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `observe` | `object` | No | — | — | See what this action set off, in the same call: requests started by page JavaScript (fetch, XHR, WebSocket, sendBeacon) with method, url, status, ok and duration, whether the page navigated, and optionally the state of an element afterwards. Waits until no request is in flight and nothing new arrived for quietMs, at most waitMs. Pass {} for the defaults. Replaces network_read before and after the action plus dom_extract. Document navigations and images are not listed. |
| `observe.waitMs` | `integer` | No | `3000` | 0–15000 | Longest wait for the traffic to settle after the action. |
| `observe.quietMs` | `integer` | No | `500` | 100–5000 | How long nothing may be in flight or arrive before the traffic counts as settled. |
| `observe.urlContains` | `string` | No | — | ≤ 500 characters | List only requests whose URL contains this text (counts still cover all). |
| `observe.maxRequests` | `integer` | No | `20` | 1–100 | Most requests listed; requestsOmitted counts the rest. |
| `observe.texts` | `boolean` | No | `true` | — | List text that became visible after the action in newTexts: an error next to a field, a toast, a banner, a changed price. Entries inside an alert or live region carry alert:true. false skips the comparison. |
| `observe.maxTexts` | `integer` | No | `8` | 1–50 | Most new texts listed; newTextsOmitted counts the rest. |
| `observe.after` | `object` | No | — | — | Read an element once the traffic settled, like nova.dom_extract: {selector, properties}. |
| `key` | `string` | Yes | — | — | Key name: Enter, Tab, Escape, Backspace, Delete, ArrowUp, ArrowDown, ArrowLeft, ArrowRight, Home, End, PageUp, PageDown, F1-F24, Space. |

Capability bundles: `browser_automation`, `form_submission`.
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 4. Example Calls

### Submit Focused Form with Enter
```json
{
  "key": "Enter"
}
```

### Dismiss Active Dialog with Escape
```json
{
  "key": "Escape",
  "targetId": "tab-102"
}
```

### Navigate Focus Ring with Tab
```json
{
  "key": "Tab"
}
```

---

## 5. Operational Best Practices

* **Ensure Prior Focus:** `nova.input_key` dispatches raw keystroke events to the active element holding DOM focus. Before pressing keys like `Enter`, `Tab`, or arrows, ensure the target input or control is focused by first clicking it with [`nova.click_selector`](nova-click-selector.md) or typing into it with [`nova.type_selector`](nova-type-selector.md).
* **Modal and Popover Dismissal:** For accessible dialogs, tooltips, or dropdown menus, sending `Escape` via `nova.input_key` is often faster and less brittle than hunting for small close buttons in the DOM.
* **Observe Async Key Side-Effects:** Pass the `observe` block when pressing keys that initiate network requests (such as `Enter` submitting a query or arrow keys populating autosuggestions). Nova automatically waits for the resulting HTTP/fetch traffic to settle before returning.

---

## 6. Related Tools & Documentation

* [`nova.type_selector`](nova-type-selector.md) — For typing textual strings into inputs.
* [`nova.click_selector`](nova-click-selector.md) — For clicking interactive elements.
* [Agent Awareness Gates (AAG)](../../../core-features/agent-awareness-gates-aag/README.md) — Checks that warn or block `nova.input_key` and other input tools when the agent has not looked at the page since its last navigation.
