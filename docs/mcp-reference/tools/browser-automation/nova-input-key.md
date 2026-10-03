# `nova.input_key`

Dispatches a physical keyboard keypress (`keydown` followed by `keyup`) to the currently focused DOM element or active viewport.

---

## 1. Overview

`nova.input_key` simulates low-level physical keystrokes for control keys, navigation keys, and shortcuts that cannot be sent via standard text input (e.g. `Enter` to submit a form, `Escape` to dismiss a popover, `Tab` to navigate focus rings, or arrow keys to navigate autocomplete menus).

* **Capability Bundle:** `browser_automation`, `humanized_input`
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
| `key` | `string` | Yes | — | — | Key name: Enter, Tab, Escape, Backspace, Delete, ArrowUp, ArrowDown, ArrowLeft, ArrowRight, Home, End, PageUp, PageDown, F1-F12, Space. |
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

## 5. Related Tools & Documentation

* [`nova.type_selector`](nova-type-selector.md) ? For typing textual strings into inputs.
* [`nova.click_selector`](nova-click-selector.md) ? For clicking interactive elements.
* [Automated Actions Guide (AAG)](../../../core-features/aag.md) ? Overview of input automation and focus management.
