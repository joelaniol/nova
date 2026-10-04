# `nova.ui_confirm_native_dialog`

> **Presses a button in the open dialog: by name in any dialog, including Nova's own, or the affirmative button of a Windows dialog.**

* **Core Feature Guide:** [Native Dialogs & UI Prompts](../../../core-features/native-dialogs-and-prompts.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.ui_confirm_native_dialog` presses a button in the dialog that is currently open.

* **With `button`:** it presses exactly the button with that label. This works in a Windows dialog Nova owns (file picker, print dialog) and in Nova's own dialogs, such as the connection setup guide or a confirmation in the settings. Take the names from [`nova.ui_inspect_native_dialog`](nova-ui-inspect-native-dialog.md); case, extra spaces and typographic apostrophes do not matter. If no button or more than one button matches, nothing is pressed and the answer lists `availableButtons`.
* **Without `button`:** it presses the confirm button (e.g. "Open" or "Save") of a Windows dialog, falling back to sending Enter if no confirm button is found through UI Automation. A Nova dialog has no single "confirm" — its buttons mean different things — so the call answers `reasonCode: "native_dialog.button_required"` with the dialog's buttons instead of guessing.

If no dialog is open, the call reports that instead of acting on anything.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `button` | `string` | No | — | — | Visible label of the button to press, e.g. 'Next' or 'Close'. Required for Nova's own dialogs; optional for native window dialogs, where it replaces the automatic choice of the affirmative button. |

Capability bundle: `app_shell_recovery` (load it with `nova.tools_bundle(bundle='app_shell_recovery')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_ui_confirm_native_dialog",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Native dialog confirm action dispatched and the dialog closed."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "reasonCode": null,
    "confirmed": true,
    "dialogStillOpen": false,
    "attemptedActions": ["foreground", "button_click"],
    "nativeDialogBefore": { "isOpen": true },
    "nativeDialogAfter": { "isOpen": false },
    "clickedButton": { "name": "Open" }
  }
}
```
Pressing a button in one of Nova's own dialogs (`"arguments": { "button": "Next" }`) answers with `pressedButton`, `dialogStillOpen`, and the dialog as read before and after the press (`inAppDialogBefore`/`inAppDialogAfter`: `title`, `texts`, `buttons`), so the next step of a multi-step dialog is visible without another call. A label that matches no button returns `ok: false` with `reasonCode: "native_dialog.button_not_found"`; a disabled button returns `"native_dialog.button_disabled"`.

`nativeDialogBefore`/`nativeDialogAfter` carry the same dialog snapshot shape as `nova.ui_inspect_native_dialog` (shown shortened above). If the click or the Enter-key fallback could not be dispatched, `ok` is `false`, `status` is `"apply_failed"`, and `reasonCode` is `"native_dialog.confirm_failed"`. If no native dialog was open to begin with, the call still returns `ok: true` with `status: "not_found"` and `confirmed: false` — it reports nothing happened rather than erroring.

---

## 4. Operational Best Practices

* **Pre-check State:** Call `nova.ui_inspect_native_dialog` first to confirm a dialog is actually open and to read its button names.
* **Prefer a name:** Pass `button` whenever you know what you want to press; the automatic choice only exists for Windows dialogs.

---

## 5. Related Tools

* [`nova.ui_dismiss_native_dialog`](nova-ui-dismiss-native-dialog.md)
* [`nova.ui_inspect_native_dialog`](nova-ui-inspect-native-dialog.md)
