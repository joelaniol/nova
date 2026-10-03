# `nova.click_selector`

Executes a verified click on a DOM element matching a CSS selector or CTA handle, featuring deep Shadow-DOM piercing, backdrop dismissal, and postcondition verification.

---

## 1. Overview

`nova.click_selector` is the primary interaction tool for activating buttons, links, toggles, and interactive DOM nodes. Unlike naive browser clicks, Nova enforces **Pre-Click Visibility & Clickability Verification**, **Deep Shadow-DOM Piercing**, and **Postcondition Settlement** to eliminate silent click failures.

* **Capability Bundle:** `browser_automation`, `form_submission`
* **Shadow-DOM Syntax:** Uses ` >>> ` to pierce through open and closed shadow roots cleanly.
* **Pre-Check Safety:** Verifies element is not covered by modal backdrops or cookie banners.

---

## 2. Key Capabilities & Features

### A. Deep Shadow-DOM Piercing (` >>> `)
Standard CSS selectors fail when an element resides inside a Web Component or Shadow Root. Nova's selector engine supports the deep combinator ` >>> `:
```css
custom-checkout >>> payment-module >>> button.pay-now
```
Nova traverses shadow root boundaries recursively to locate the target node.

### B. Auto-Dismiss Blockers (`autoDismissBlockers: true`)
If a click cannot land because a cookie banner, modal backdrop, or promotional popover covers the element:
* When `autoDismissBlockers: true` is set, Nova automatically identifies the obscuring overlay, dismisses it, and retries the click seamlessly in a single step.

### C. Postcondition Verification (`verify`)
Prevents clicking and immediately declaring victory while the page is still mutating:
* `verify.absent`: Asserts that an element (e.g. the clicked modal or loading spinner) disappears from the DOM.
* `verify.present`: Asserts that the expected success message or resulting container appears.

### D. Multi-Match Strictness (`strict: true`)
If multiple elements match the selector and `strict: true` is passed, Nova fails-fast with `-32602` and reports the count and locations rather than clicking the wrong element arbitrarily.

---

## 3. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`selector`** | `string` | **Yes** | — | CSS selector or CTA handle. Supports ` >>> ` for shadow roots. |
| **`targetId`** | `string` | No | `"active"` | Target tab ID. |
| **`button`** | `string` | No | `"left"` | Mouse button: `"left"`, `"right"`, or `"middle"`. |
| **`clickCount`** | `integer` | No | `1` | `1` for single-click, `2` for double-click. |
| **`strict`** | `boolean` | No | `false` | When `true`, throws an error if more than one element matches. |
| **`autoDismissBlockers`**| `boolean` | No | `false` | Automatically dismiss overlay banners obscuring the element. |
| **`waitForNavigation`**| `boolean` | No | `false` | Wait for a document navigation triggered by the click. |
| **`verify`** | `object` | No | `null` | Postcondition assertion: `{ absent?: string, present?: string }`. |
| **`includeScreenshot`**| `boolean` | No | `false` | Capture visual evidence crop after click settles. |
| **`timeoutMs`** | `integer` | No | `5000` | Max milliseconds to wait for clickability (1,000–30,000 ms). |

---

## 4. Example Calls

### Standard Button Click with Verification
```json
{
  "name": "nova.click_selector",
  "arguments": {
    "targetId": "tab-1",
    "selector": "button#submit-order",
    "verify": {
      "present": ".order-confirmation-badge"
    },
    "timeoutMs": 10000
  }
}
```

### Shadow-DOM Click with Blocker Dismissal
```json
{
  "name": "nova.click_selector",
  "arguments": {
    "targetId": "tab-1",
    "selector": "app-root >>> user-profile >>> button.save-changes",
    "autoDismissBlockers": true,
    "strict": true
  }
}
```

---

## 5. Best Practices & Common Traps

* **The Shadow-DOM Trap:** If `document.querySelector` fails in regular browsers, check if the button is hosted inside a Web Component. Use `host >>> target` syntax.
* **Navigation Timeouts:** When clicking a link that opens a new tab (`target="_blank"`), the originating tab does not navigate. Inspect the response payload: Nova reports `newTabOpened: true` and `newTabIds: [...]` instead of timing out.

---

## See Also

* [`nova.type_selector`](nova-type-selector.md) — Type text into inputs.
* [`nova.scroll_smart`](nova-scroll-smart.md) — Bring off-screen elements into view.
* [`nova.dismiss_blockers`](nova-dismiss-blockers.md) — Standalone modal and banner dismissal.
* [Core Feature: Humanized Input Engine](../../../core-features/humanized-input-engine.md)
