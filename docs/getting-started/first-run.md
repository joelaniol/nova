# First Run & UI Tour

This page walks through what happens when you start **Nova AI Workspace** for the first time and introduces the parts of the window you will use most.

---

## 1. Activating Nova

Nova needs an activated license.

* **During setup:** the setup has an optional page **Activate Nova now (optional)** with your Nova account email address and license key. If you fill it in, Nova activates with it on its first start. Leave both fields empty to activate later in the app.
* **In the app:** without an activation, Nova starts with its sign-in window (**Sign in with your license**). Enter the email address and license key and click **Sign in**.
* **Alpha trial:** during the public alpha no registration is needed. **Get trial key** opens the GitHub page with the shared trial key; the setup page and the sign-in window are already filled with it. The key is also on [Alpha Trial License](trial-license.md).

---

## 2. The Setup Wizard for AI Programs

A few seconds after Nova starts, it opens its connection wizard if no AI program on this computer is connected to Nova yet and you have not finished the wizard before. If you ticked **Open the setup guide for AI programs on first start** in the setup, the wizard also opens when Nova starts from the setup's last page.

* **Easy setup (recommended):** Nova lists the AI programs it found (**Your AI programs**). Click **Connect** next to the one you want to use, then restart that program.
* **Connect another program:** for a program Nova cannot set up by itself, **Copy setup text** copies ready-made instructions to paste into that program; **Copy key** copies the access key.
* **Set up manually:** copy the connection details and add them to your AI program yourself.
* Nova never changes a configuration just because the wizard is open; every change is a button you press.

You can open the wizard again at any time: **Settings → AI & agents → Connection & setup → Set up**. Agents can open it with `nova.setup_wizard_open`. Details: [Settings & connection wizard](../user-guide/settings-and-connection-wizard.md).

---

## 3. Workspace Anatomy

### A. Tabs and address bar
Nova works like a Chromium browser: tabs, back, forward, reload and an address bar. Common shortcuts such as `Ctrl+L` (address bar), `Ctrl+R` / `F5` (reload), `Ctrl+W` (close tab), `Ctrl+Tab` (next tab) and `Ctrl+J` (downloads) work as in Chrome or Edge. Full list: [Keyboard shortcuts](../user-guide/keyboard-shortcuts.md).

### B. Sandboxes
* **What are sandboxes?** Separate browser profiles inside the same window. A new installation starts with **Sandbox A** and **Sandbox B**; you can add more (up to 100).
* **Isolation:** each sandbox has its own cookies, logins and site data, so you can be signed in to two accounts on the same site at the same time. Proxy and fingerprint protection can be set per sandbox.
* **Switching:** each sandbox appears as a pill; with many sandboxes, a search helps you find one.
* **For agents:** `nova.sandbox_context` describes a sandbox; `nova.resolve_sandbox` picks the right sandbox for a task.

More: [Sandboxes & profiles](../user-guide/sandboxes-and-profiles.md).

### C. Terminal dock
* Nova has a built-in terminal dock. Sessions currently run PowerShell, hosted in a separate helper process.
* Agents can open sessions, run commands and read output with `nova.terminal_open`, `nova.terminal_run_command` and `nova.terminal_read` while **Allow agents to control the terminal dock** is on.

More: [Terminal dock](../user-guide/terminal-dock.md).

### D. Downloads and browser prompts
* **Downloads:** `Ctrl+J` opens the downloads list. See [Downloads manager](../user-guide/downloads-manager.md).
* **Prompts:** when a site asks for an HTTP sign-in or a client certificate, Nova shows its own prompt. Agents can answer such prompts too, for example with `nova.ui_auth_prompt_resolve` or `nova.ui_client_certificate_prompt_resolve`. See [Native dialogs](../user-guide/native-dialogs-ui.md).

### E. Permission center
* **Settings → Site permissions → Permission center** sets the default behavior for camera, microphone, speaker, screen sharing and location: ask, allow or block.
* Decisions for single sites and temporary grants for the current session come on top of these defaults. Agents read and change the defaults with `nova.permission_center_get` and `nova.permission_center_set`.
* `nova.media_stop_all` stops every running camera, microphone and screen-sharing stream at once.

---

## Next Step

Now that you know the window, continue with the **[5-Minute Quickstart](quickstart.md)** to connect an AI agent and run your first automated task.
