# Passwords & Vault

> [!NOTE]
> Nova AI Workspace includes a built-in, local-only **Password Manager & Vault**. It securely stores web credentials, HTTP Basic/Digest authentication logins, and automation secrets. All credentials are encrypted using the **Windows Data Protection API (DPAPI)** and stored exclusively on your local disk in `%LOCALAPPDATA%\NovaBrowser\vault.db`—never uploaded to cloud servers or synced across the internet.

---

## 1. Overview & Security Architecture

Managing passwords in an AI-assisted browser requires higher security standards than traditional browsers. If an AI agent automates a website on your behalf, raw credentials must never leak into AI prompts or token contexts.

* **DPAPI Hardware/User Key Binding:** Passwords and secrets are encrypted with cryptographic keys bound to your Windows user logon session.
* **Biometric & PIN Protection:** Viewing or editing a saved password in the settings requires Windows Hello authentication (PIN, fingerprint, or facial recognition).
* **Agent-Safe Secret Injection:** AI coding agents can log in to websites using Nova's automated fill tools without ever seeing, reading, or transmitting the raw plaintext password.
* **Cross-Sandbox Isolation:** Credentials can be scoped globally or restricted to specific sandbox profiles, ensuring client accounts remain separated.

```
+-----------------------------------------------------------------------------------+
|  Settings > Identity & Security > Password Manager & Vault                        |
+-----------------------------------------------------------------------------------+
|  [X] Enable Password Vault                                                        |
|  [X] Offer to save passwords when logging into websites                          |
|  [X] Automatically offer saved logins on form fields                              |
|                                                                                   |
|  Search vault: [ github.com                             ] [ + Add Login ]         |
|                                                                                   |
|  +-----------------------------------------------------------------------------+  |
|  | github.com                                                                  |  |
|  | Username: developer@example.com                                             |  |
|  | Password: [ **************** ] [ Eye (Verify PIN) ] [ Copy ] [ Edit ] [Del] |  |
|  +-----------------------------------------------------------------------------+  |
|  | internal-portal.corp                                                        |  |
|  | Username: admin                                                             |  |
|  | Password: [ **************** ] [ Eye (Verify PIN) ] [ Copy ] [ Edit ] [Del] |  |
|  +-----------------------------------------------------------------------------+  |
|                                                                                   |
|  Backup & Portability:   [ Import Passwords (CSV) ]   [ Export Vault Backup ]     |
+-----------------------------------------------------------------------------------+
```

---

## 2. Managing Saved Logins in Settings

Open **Menu → Settings → Identity & security → Password manager & vault**:

### Global Settings
* **Enable Password Vault:** Master switch for credential storage and retrieval.
* **Offer to Save Passwords:** When enabled, Nova prompts to save newly entered credentials after form submission.
* **Autofill Credentials:** When enabled, focusing a login field displays a dropdown offer to fill saved accounts.

### Finding & Inspecting Entries
* **Filter Bar:** Type a domain name (e.g., `github.com`) or a username to instantly filter the list.
* **View Password:** Click the **Eye icon** next to the masked password. For security, Windows prompts for your **Windows Hello PIN, fingerprint, or Windows account password** before revealing the plaintext characters.
* **Copy Password:** Click **Copy** to place the password into your Windows clipboard. The action is logged to the local audit trail for security accountability.
* **Edit Entry:** Modify the URL, username, password, or associated notes.
* **Delete Entry:** Removes the credential permanently from `vault.db`.

---

## 3. Saving & Autofilling Logins While Browsing

### Saving Credentials
When you enter a new username and password on a webpage and submit the form, Nova detects the authentication event and displays a non-intrusive flyout beside the address bar:
* **Save:** Encrypts and adds the credential to the Vault.
* **Never for this site:** Adds the domain to an exception list so Nova will not prompt for it again.
* **Not now:** Dismisses the prompt for the current session without saving.

### Autofilling on Recognized Pages
When you navigate to a login page with saved credentials:
1. Click the username input field.
2. Nova displays an autofill suggestion chip showing the saved account name.
3. Click the suggestion to populate both the username and password fields instantly.
4. If multiple accounts exist for the same domain, select the desired profile from the list.

### Server Authentication Prompts (HTTP Basic / Digest)
For intranet portals, routers, or development servers that use native HTTP Basic or Digest authentication dialogs, Nova provides a dedicated credential prompt. Selecting **Remember this password** saves the login directly into the Vault, automatically providing it on subsequent visits. See [Certificates & Authentication](certificates-and-auth.md#sign-in-to-a-server).

---

## 4. Agent-Safe Secret Injection

A core innovation in Nova AI Workspace is **Agent-Safe Secret Injection**:

When an autonomous AI agent (such as Claude Code, Codex, or Antigravity) is instructed to perform tasks requiring authentication (e.g., *"Log in to our staging dashboard and download yesterday's telemetry report"*), traditional tools force you to share plaintext passwords with the agent.

Nova eliminates this risk:
1. The agent identifies the login form on the page using [`nova.ok_observe`](../../mcp-reference/tools/app-shell-and-ui/nova-ok-observe.md) or DOM tools.
2. The agent calls [`nova.vault_prepare_fill`](../../mcp-reference/tools/vault-and-security/nova-vault-prepare-fill.md) specifying the target domain.
3. Nova's host engine retrieves the credentials from DPAPI storage, verifies site origin matching, and injects the password directly into the browser DOM via [`nova.type_selector_secret`](../../mcp-reference/tools/vault-and-security/nova-type-selector-secret.md).
4. **The result:** The form is successfully filled and submitted, while the AI agent receives only a confirmation status (`{ "filled": true }`). The plaintext password never enters the agent's context window, prompt history, or remote logs.

---

## 5. Importing & Exporting Credentials

### Importing from Other Browsers & Password Managers
You can migrate passwords from Google Chrome, Microsoft Edge, Firefox, Bitwarden, or 1Password:
1. Export your passwords as a `.csv` file from your previous browser/manager.
2. In Nova, open **Settings → Password manager & vault** and click **Import passwords**.
3. Select the `.csv` file.
4. Choose conflict resolution:
   * **Skip existing entries (Recommended):** Keeps existing Nova entries and imports only new logins.
   * **Overwrite existing entries:** Replaces existing credentials with matching domains and usernames.
5. Nova parses and encrypts each entry into `vault.db`. Delete the unencrypted `.csv` file from your disk after import.

### Exporting Vault Backups
Click **Export vault backup** to save your credentials into a password-protected, encrypted backup file for migration to another Windows PC.

---

## Related Documentation

* **[Core Features: Password Vault & Secrets](../../core-features/privacy/vault-and-secrets/README.md)** — Cryptographic architecture, DPAPI key derivation, and threat model.
* **[Certificates, Authentication & Native Prompts](certificates-and-auth.md)** — HTTP server sign-in and client certificates.
* **[Sandboxes & Profiles](sandboxes-and-profiles.md)** — Isolating sessions and credentials across distinct profiles.
* **[Website & Agent Permissions](permissions.md)** — Managing origin security grants and review dialogs.
