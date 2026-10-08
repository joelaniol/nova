# Browser Interaction

Nova separates finding the current element, delivering browser input and performing drag gestures. These guides explain the interaction paths and their boundaries.

| Topic | What it covers |
| :--- | :--- |
| [Input Dispatch](input-dispatch/README.md) | Browser mouse and keyboard input, text insertion, focus and scrolling. |
| [Selectors & Shadow DOM](selectors-and-shadow-dom/README.md) | Element-based actions, open shadow-root traversal and target visibility. |
| [Drag & Drop](drag-and-drop/README.md) | Browser-input drag, synthetic humanized drag and the HTML5 drag polyfill. |

## Choose the Interaction Path

A selector identifies the element to act on; the input path determines how the action reaches the page. The two can be combined. Coordinates refer to the page viewport, so layout changes can move the target.

“Humanized” describes one drag movement profile. Other input tools have their own delivery paths; the term does not establish trusted events or successful application outcomes.

After dispatch, verify the expected result through a [CLS transition contract](../closed-loop-system-cls/README.md) or appropriate [visual evidence](../../research/evidence-verification-mode-evm/README.md).

## Related Areas

* [Browser Navigation & Automation Tool Group](../../mcp-reference/tools/browser-automation/README.md) — Navigation, history, reload and tab-management tools alongside interaction tools.
* [Tabs & Windows User Guide](../../user-guide/browser/tabs-and-windows.md) — User-facing browsing guidance.
* [Surface Explorer](../crawler-and-discovery/surface-explorer/README.md) — Discovering and inspecting interactive page states.
* [Native Dialogs & UI Prompts](../native-dialogs-and-prompts/README.md) — Dialogs outside the page.

[All core features](../README.md)
