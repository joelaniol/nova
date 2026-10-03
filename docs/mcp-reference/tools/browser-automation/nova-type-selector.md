# `nova.type_selector`

Focuses an input field or contenteditable element, clears existing text, and enters characters with realistic keystroke intervals and input events.

---

## 1. Overview

`nova.type_selector` handles keyboard input across textboxes, search inputs, textareas, and rich-text editors (`contenteditable`). Rather than injecting raw values directly into DOM properties (which often bypasses React/Vue `onChange` state synchronization), Nova generates authentic synthetic keyboard events (`keydown`, `keypress`, `input`, `keyup`).

* **Capability Bundle:** `browser_automation`, `form_submission`
* **Shadow-DOM Syntax:** Supports ` >>> ` combinator for encapsulated inputs.
* **Typing Modes:** Supports humanized intervals, fast typing, and clipboard paste injection.

---

## 2. Key Capabilities & Features

### A. Authentic Keystroke Dispatch
Frameworks like React 18, Angular, and Vue track input values using internal state proxies. Setting `input.value = "text"` often results in forms submitting empty strings. `nova.type_selector` dispatches the full keyboard event lifecycle, ensuring frameworks register every keystroke.

### B. Input Modes (`inputMode`)
* **`humanized` (Default):** Introduces slight, natural micro-delays (20–60ms) between keystrokes to prevent bot detection systems from flagging algorithmic typing.
* **`fast`:** Enters characters with minimal delay for high-throughput automated testing.
* **`paste`:** Emulates an atomic `Paste` event for entering long multiline text or code snippets instantly.

### C. Press Enter on Finish (`pressEnter: true`)
Search bars and command palettes frequently submit upon pressing the Enter key. Passing `pressEnter: true` dispatches the Enter keypress immediately after the final character without requiring a secondary tool call.

---

## 3. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`selector`** | `string` | **Yes** | — | CSS selector or CTA handle for the input element. Supports ` >>> `. |
| **`text`** | `string` | **Yes** | — | The text string to enter into the element. |
| **`targetId`** | `string` | No | `"active"` | Target tab ID. |
| **`clear`** | `boolean` | No | `true` | Selects and clears existing text before typing new content. |
| **`pressEnter`** | `boolean` | No | `false` | Dispatches an Enter key event after the last character. |
| **`inputMode`** | `string` | No | `"humanized"`| `"humanized"`, `"fast"`, or `"paste"`. |
| **`autoDismissBlockers`**| `boolean` | No | `false` | Automatically dismisses overlays obscuring the input field. |
| **`waitForNavigation`**| `boolean` | No | `false` | Wait for page navigation triggered by typing (e.g. Enter on search). |
| **`timeoutMs`** | `integer` | No | `5000` | Max milliseconds to wait for element to become editable. |

---

## 4. Example Calls

### Search Input with Immediate Enter Key
```json
{
  "name": "nova.type_selector",
  "arguments": {
    "targetId": "tab-1",
    "selector": "input[type='search']",
    "text": "wireless mechanical keyboard",
    "pressEnter": true,
    "waitForNavigation": true
  }
}
```

### Entering Comments into a Shadow-DOM Rich Text Area
```json
{
  "name": "nova.type_selector",
  "arguments": {
    "targetId": "tab-1",
    "selector": "comment-widget >>> textarea.editor",
    "text": "Great article! Thanks for the deep dive.",
    "clear": true,
    "inputMode": "humanized"
  }
}
```

---

## 5. Best Practices & Common Traps

* **Never Use for Passwords:** When entering sensitive credentials (passwords, 2FA tokens, API keys), **never** pass plaintext to `nova.type_selector`. Use [`nova.type_selector_secret`](../vault-and-security/nova-type-selector-secret.md) to keep secrets zero-leak and out of the LLM context.
* **Auto-Clear:** By default, `clear: true` selects existing text (`Ctrl+A` + `Backspace`) before typing. Pass `clear: false` only when appending text to an existing string.

---

## See Also

* [`nova.click_selector`](nova-click-selector.md) — Click buttons and links.
* [`nova.type_selector_secret`](../vault-and-security/nova-type-selector-secret.md) — Secure, zero-leak credential injection.
* [`nova.guarded_send_message`](nova-click-selector.md) — High-level chat message macro.
