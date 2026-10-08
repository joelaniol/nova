# Selectors & Shadow DOM

Selector-based actions identify the current page element before Nova interacts with it. Open shadow roots require explicit traversal because an ordinary document-level CSS query cannot reach every visible web component.

## A Concrete Example: Save Inside a Web Component

An agent sees a Save button inside a custom dialog, but an ordinary CSS query cannot find it. If the components expose open shadow roots, a selector such as `my-custom-dialog >>> user-avatar >>> button.save-btn` follows those boundaries. Nova resolves the element and dispatches a browser-input click.

The click result establishes that input was dispatched. It does not establish that the application saved the record. A [CLS transition contract](../../closed-loop-system-cls/README.md) can check the expected confirmation or state change; a [visual capture](../../../research/evidence-verification-mode-evm/README.md) can show what the user sees afterward.

## Shadow DOM Traversal (` >>> `)

Selector-based tools (`nova.click_selector`, `nova.type_selector`, `nova.select_option`, `nova.guarded_*` and others) accept the ` >>> ` combinator. Each segment is a normal CSS selector; ` >>> ` steps into the shadow root of the element matched so far:

```css
/* The save button inside the shadow root of user-avatar, inside my-custom-dialog */
my-custom-dialog >>> user-avatar >>> button.save-btn
```

* **Open shadow roots only:** Nova follows `element.shadowRoot`, which pages can read for open shadow roots. Closed shadow roots are not reachable this way.
* **Effective opacity:** Nova computes an element's opacity multiplied by that of all its ancestors, across shadow hosts. A fully transparent element stays a valid click and upload target — the classic `<input type="file">` laid over a styled button — but element screenshots of it are refused, because the picture would show whatever lies behind it.

## Selector-Based Actions

* **Selector-based actions:**
  * `nova.click_selector`: Clicks the element matched by a CSS selector (with ` >>> ` support) or a CTA handle from `nova.perceive`; optional verification and blocker dismissal.
  * `nova.type_selector`: Types into the matched field; see [Input Dispatch](../input-dispatch/README.md) for focus and text insertion.
  * `nova.select_option`: Selects an option of a native `<select>` by value.
  * `nova.choose_option`: Selects an option of a custom or native dropdown by visible text or index.

Resolving a selector and delivering input are separate steps. See [Input Dispatch](../input-dispatch/README.md) for how clicks, keys and text reach the page. When an action is rejected or the page changes, inspect the current target rather than assuming a previously resolved element is still valid.

## Related Documentation

* [Drag & Drop](../drag-and-drop/README.md) — Gesture paths and HTML5 drag events.
* [Surface Explorer](../../crawler-and-discovery/surface-explorer/README.md) — Interactive controls and hidden page states.
* [DOM & Reading Tools](../../../mcp-reference/tools/dom-and-reading/README.md) — Page inspection and deep focus inspection.

[Browser Interaction overview](../README.md) · [All core features](../../README.md)
