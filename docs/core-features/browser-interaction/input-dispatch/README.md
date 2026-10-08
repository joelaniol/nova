# Input Dispatch

Nova delivers mouse, keyboard and text input through the browser's input pipeline. A known element can be resolved by a selector before dispatch; coordinate tools act at positions in the page viewport.

## A Concrete Example: Enter Text and Submit

An agent identifies the current text field, focuses it with `nova.type_selector`, inserts text and dispatches the appropriate key or click. Dispatch establishes that input was sent. It does not establish that a form was accepted or a record was saved; check the expected state afterward.

## How Input Is Delivered

| Tool | What Nova sends |
| :--- | :--- |
| `nova.input_click`, `nova.click_selector` | Through the DevTools input pipeline: a mouse move, a press, about 16 ms later the release. Events arrive as real browser input (`isTrusted: true`). |
| `nova.input_move` | One mouse-move event to the target position. |
| `nova.input_wheel` | One wheel event with `deltaX`/`deltaY`; Nova then checks whether something actually scrolled. |
| `nova.input_text` | Inserts the text into the focused element in one step (`Input.insertText`), not key by key. |
| `nova.type_selector` | Focuses the element (optionally clears it with select-all and delete), then inserts the text in chunks and waits for the page to render between chunks, so rich-text editors do not drop characters. Optional read-back verification. |
| `nova.input_key` | Key down and key up for one named key (Enter, Tab, Escape, arrows, F1–F12, ...). |
| `nova.input_shortcut` | A key combination such as `Ctrl+Shift+K` (modifiers Ctrl, Shift, Alt, Meta plus exactly one key). |

If the Nova window is minimized, Nova restores it before dispatching input, because a minimized window throttles input delivery.

## Choose the Target

* [Selectors & Shadow DOM](../selectors-and-shadow-dom/README.md) explains element resolution, supported open shadow roots and selection controls.
* Coordinate mouse input uses viewport positions. Layout changes or scrolling can move the target.
* `nova.input_wheel` dispatches a wheel event and checks whether scrolling occurred. The dedicated `nova.scroll_*` tools expose their own scrolling options in the [tool reference](../../../mcp-reference/tools/browser-automation/README.md).
* Drag gestures have separate browser-input and synthetic paths; see [Drag & Drop](../drag-and-drop/README.md).

## Related Documentation

* [Closed-Loop System (CLS)](../../closed-loop-system-cls/README.md) — Expected states and outcome verification.
* [Native Dialogs & UI Prompts](../../native-dialogs-and-prompts/README.md) — UI surfaces outside the page.
* [Browser Automation Tool Reference](../../../mcp-reference/tools/browser-automation/README.md) — Current parameters and protocol examples.

[Browser Interaction overview](../README.md) · [All core features](../../README.md)
