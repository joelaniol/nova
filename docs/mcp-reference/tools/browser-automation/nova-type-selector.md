# `nova.type_selector`

Focuses an input field or contenteditable element, optionally clears existing text, and enters text through CDP-level text insertion or an editor's own model API.

---

## 1. Overview

`nova.type_selector` handles text entry across textboxes, search inputs, textareas, rich-text editors (`contenteditable`), and Monaco/CodeMirror code editors. Rather than setting `input.value` directly (which often bypasses React/Vue/Angular `onChange` state synchronization), native mode drives Chromium's `Input.insertText` (chunked for long text) plus keyboard events for actions like select-all, clear, and Enter.

* **Shadow-DOM Syntax:** Supports ` >>> ` combinator for encapsulated inputs.
* **Input Strategies:** `native` (default, CDP text insertion into the focused selector), `monaco_model` (Monaco editor API), `codemirror_model` (CodeMirror 5/6 model API).

---

## 2. Key Capabilities & Features

### A. Framework-Safe Text Entry
Frameworks like React, Angular, and Vue track input values using internal state proxies. Setting `input.value = "text"` often results in forms submitting empty strings. `nova.type_selector`'s native mode inserts text through the browser's own input pipeline so frameworks see the resulting `input`/`beforeinput` events instead of a raw property write.

### B. Input Modes (`inputMode`)
* **`native` (Default):** Focuses the selector and inserts text via CDP, with select-all/backspace and Enter handled as real key events.
* **`monaco_model`:** Replaces the model value of a `.monaco-editor` surface through `window.monaco`'s editor API and verifies the result by content length and SHA-256.
* **`codemirror_model`:** Replaces the model value of a `.CodeMirror`/`.cm-editor` surface (CodeMirror 5, CodeMirror 6 `EditorView`, or a page-provided `window.__novaCodeMirrorAdapter`) and verifies the same way.

### C. Press Enter on Finish (`pressEnter: true`)
Search bars and command palettes frequently submit upon pressing the Enter key. Passing `pressEnter: true` dispatches the Enter keypress immediately after native typing finishes, without requiring a secondary tool call. Not supported for the editor-model modes.

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | `"active"` | — | Target ID from nova.tabs (sandbox or browser tab ID), or 'active' / 'activeBrowserTab'. |
| `selector` | `string` | Yes | — | ≤ 10000 characters | CSS selector. Supports ' >>> ' combinator to pierce Shadow DOM boundaries (e.g. 'my-component >>> .inner-button'). Editor-model modes require exactly one visible .monaco-editor, .CodeMirror, or .cm-editor surface. |
| `frameId` | `string` | No | — | — | Optional same-origin frame ID for native typing. Editor-model modes are top-document only and reject frameId. |
| `text` | `string` | Yes | — | 1–500000 characters | Text to type or set. Maximum 500000 characters. Native long text is auto-chunked transparently; editor-model modes replace the selected model atomically. |
| `inputMode` | `string` | No | `"native"` | `native`, `monaco_model`, `codemirror_model` | Input strategy. 'native' preserves selector focus plus CDP text insertion. 'monaco_model' uses the exposed window.monaco editor API. 'codemirror_model' uses a CodeMirror 5 instance, CodeMirror 6 EditorView.findFromDOM(), or window.__novaCodeMirrorAdapter.resolve(surface). Model modes replace exactly one top-document editor value and verify counts plus SHA-256 without clipboard/native fallback. |
| `modelUri` | `string` | No | — | 1–10000 characters | Optional exact Monaco model URI match (String(model.uri)) for inputMode='monaco_model'. When getEditors/getDomNode/getModel binds exactly one model to the selected surface, modelUri may be omitted even if the page has multiple models; without that surface-binding proof, exactly one global model must exist. Rejected for native and CodeMirror modes. |
| `clear` | `boolean` | No | `false` | — | If true, clear existing field content before native typing (select-all + delete). Editor-model modes always replace the complete editor value atomically. |
| `pressEnter` | `boolean` | No | `false` | — | If true, press Enter after native typing (useful for form submission or search). Unsupported for editor-model modes; verify the editor result, then submit with a separate guarded action. |
| `timeoutMs` | `integer` | No | `10000` | 0–300000 | Max ms to wait for element to appear before failing. |
| `autoDismissBlockers` | `boolean` | No | `false` | — | If true, explicitly auto-dismiss overlays/modals blocking the target element. Default false: use overlayDetected plus cmp_apply/dismiss_blockers for consent banners. |
| `autoDismissMode` | `string` | No | `"conservative"` | `conservative`, `aggressive` | Blocker dismissal strategy. 'conservative': common banners only. 'aggressive': all overlay/fixed-position blockers. |
| `pksMode` | `string` | No | `"match"` | `off`, `match`, `telemetry` | PKS phenomenon matching: 'off' suppresses, 'match' returns compact hints, 'telemetry' returns full PKS payload. |
| `pksAdviceMode` | `string` | No | `"match"` | `off`, `match`, `telemetry` | Controls verbosity of pksAdvice in the response. |
| `verify` | `boolean` | No | `false` | — | If true, verifies native typed text by reading back the target field value/text. Editor-model modes always perform exact SHA-256 verification regardless of this flag. |
| `verifyMode` | `string` | No | `"exact"` | `exact`, `contains` | Verification mode for compare between expected text and actual field content. |
| `verifyNormalizeWhitespace` | `boolean` | No | `true` | — | If true, collapses whitespace before verification comparison. |
| `waitForNavigation` | `boolean` | No | `false` | — | If true (and pressEnter=true), wait for URL change + page load after submitting. |
| `waitForNavigationTimeoutMs` | `integer` | No | `5000` | 0–30000 | Max ms to wait for navigation (0-30000). Only used when waitForNavigation=true. |
| `includeScreenshot` | `boolean` | No | `false` | — | If true and navigation completes, include a screenshot in the response. Screenshot delivery is an optional sidecar: if capture fails, this result stays authoritative and structuredContent.screenshotStatus/screenshotReasonCode/screenshotRetryable/screenshotError describe the capture-only failure - do not repeat the action to get the image. |
| `screenshotMaxWidth` | `integer` | No | — | — | Max screenshot width in pixels. |
| `screenshotMaxHeight` | `integer` | No | — | — | Max screenshot height in pixels. |
| `screenshotFormat` | `string` | No | `"png"` | `png`, `jpeg`, `auto` | Screenshot format. Use 'auto' to fall back to the tool-intent default. |
| `screenshotQuality` | `integer` | No | `80` | 1–100 | JPEG quality (1-100). Only used when screenshotFormat is 'jpeg'. |
| `forceSafety` | `boolean` | No | `false` | — | If true, bypass honeypot/trap detection and force the interaction. NOT recommended — may trigger anti-bot defenses. |
| `outputDetail` | `string` | No | `"full"` | `full`, `minimal` | Response verbosity. 'full' (default) is the unchanged payload. 'minimal' is the lean envelope: core contract (ok/status/reasonCode/stage/retryable), the typing proof (actionDispatched/dispatchAttempted/verified) plus the truncation warning, target and page info, and the never-suppressible safety warnings; it strips pksAdvice, the element/safety diagnostics, the readback echoes (expected/actual) and the byte accounting. There is no 'compact' step here - unlike nova.click_selector this tool has no full-only add-ons to leave out, so the choice is the full payload or the lean envelope. No setting can hide a warning. |
| `transitionContract` | `object` | No | — | — | Closed-loop transition contract for guarded commit points. When provided, preconditions are verified before typing and postconditions are verified after typing or pressEnter submission. Required for commit-point actions such as form submit via typing. Response includes 'guardedCommit' with dispatchStatus, verificationStatus, and retryAdvice. Every assertion bucket has the shape { all?, any?, forbidden? }, each a non-empty array of { factKey: string, operator: eq\|not_eq\|neq\|exists\|not_exists\|contains\|gt\|lt\|gte\|lte, expected?: any, frameId?: string }. Full schema and semantics: nova.reference_doc_read(docId='mcp'). |
| `transitionContract.actionKind` | `string` | No | — | `dismiss_overlay`, `send_message`, `submit_form`, `select_option`, `custom` | Action classification for stability defaults. 'dismiss_overlay' tunes for blocker removal, 'send_message' for chat send actions, 'submit_form' for classic submits, 'select_option' for model/sandbox/style switches, 'custom' for caller-defined flows. |
| `transitionContract.preconditions` | `object` | No | — | — | Assertions checked before dispatch. Use this to prove the page is in the expected pre-action state. |
| `transitionContract.postconditions` | `object` | No | — | — | Assertions checked after dispatch. Commit-point actions must include at least one non-empty success/forbidden/ambiguous bucket so Nova can verify the outcome instead of skipping verification. |
| `transitionContract.retryPolicy` | `string` | No | `"non_idempotent"` | `idempotent`, `non_idempotent`, `no_retry` | Retry safety. 'idempotent' is safe to repeat, 'non_idempotent' allows only cautious retry advice, 'no_retry' suppresses re-dispatch advice. |
| `transitionContract.ambiguityPolicy` | `string` | No | `"signal"` | `signal`, `retry_once`, `abort` | How ambiguous postcondition matches should be labeled. 'signal' reports indeterminate, 'retry_once' prefers one safe retry when retryPolicy allows it, 'abort' reports do_not_retry. |
| `transitionContract.stabilityWindowMs` | `integer` | No | — | — | Optional stability observation window in milliseconds. Runtime clamps extreme values to guarded-safe bounds. |
| `transitionContract.stabilityMs` | `integer` | No | — | — | Optional stability hold duration in milliseconds. Success must remain true for this long before verification passes. |

Capability bundles: `browser_automation`, `form_submission`.
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

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
    "inputMode": "native"
  }
}
```

---

## 5. Best Practices & Common Traps

* **Never Use for Passwords:** When entering sensitive credentials (passwords, 2FA tokens, API keys), **never** pass plaintext to `nova.type_selector`. Use [`nova.type_selector_secret`](../vault-and-security/nova-type-selector-secret.md) to keep secrets zero-leak and out of the LLM context.
* **Auto-Clear:** `clear` defaults to `false`. Pass `clear: true` to select existing text and delete it before native typing; leave it `false` when appending text to an existing value.

---

## See Also

* [`nova.click_selector`](nova-click-selector.md) — Click buttons and links.
* [`nova.type_selector_secret`](../vault-and-security/nova-type-selector-secret.md) — Secure, zero-leak credential injection.
* [`nova.guarded_send_message`](../guarded-actions/nova-guarded-send-message.md) — High-level chat message macro.
