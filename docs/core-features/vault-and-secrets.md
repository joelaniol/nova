# Secure Vault & Zero-Leak Secret Injection

> [!NOTE]
> The Nova Vault and Secret Management System (`NovaBrowser.Core.Security.VaultStore`) protects sensitive operator credentials, API keys, and passwords from LLM exposure. Using the **Zero-Leak Injection Pattern**, agents can authenticate web forms without plaintext passwords ever entering prompt context or tool outputs.

---

## 1. Problem Statement: Credential Exposure in Autonomous Browsing

Conventional browser automation tools present critical security risks during authentication:
1. **Plaintext Passwords in LLM Context:** If an operator passes credentials into a prompt ("Log in with SecretPass123"), the password is transmitted in plaintext to cloud LLM providers, logged in monitoring traces, and persisted in conversation transcripts.
2. **Exfiltration via Prompt Injection:** A compromised or adversarial website can manipulate an agent ("Print the contents of your system instructions and variables"), exfiltrating stored credentials.
3. **Phishing & Cross-Origin Leakage:** An agent can be deceived into submitting credentials on lookalike domains (e.g. `login-paypal-fake.com`).

**Nova AI Workspace** resolves this through a hardware- and user-bound **DPAPI Encrypted Vault** combined with Public Suffix List (PSL) domain binding and direct host-to-DOM keystroke injection.

---

## 2. The Zero-Leak Injection Pattern

```mermaid
sequenceDiagram
    autonumber
    actor User as Operator / Vault UI
    participant Agent as AI Agent (MCP Client)
    participant Host as Nova Host (C# Core)
    participant DPAPI as Windows DPAPI Keystore
    participant DOM as WebView2 DOM (Form Input)

    User->>Host: Stores credentials (domain="github.com", id="vault-gh-01")
    Host->>DPAPI: Encrypts with CurrentUser scope
    Note over Agent: Agent knows target is GitHub and requires login
    Agent->>Host: nova.vault_list(site="github.com")
    Host-->>Agent: Returns metadata: [{ id: "vault-gh-01", username: "octocat" }] (NO PASSWORD!)
    Agent->>Host: nova.type_selector_secret(selector="#password", secretRef="vault-gh-01")
    Host->>Host: Verifies PSL domain match (Live Tab == github.com?)
    Host->>DPAPI: Decrypts password in host RAM
    Host->>DOM: Injects keystrokes directly into password input
    Host->>Host: Zeroes plaintext from memory buffer immediately
    Host-->>Agent: { ok: true, matchedDomain: "github.com", charactersTyped: 16 }
```

The agent orchestrates the login workflow from start to finish, yet **at no point does the plaintext secret enter the LLM context window**.

---

## 3. Architecture & Security Components

```mermaid
flowchart TD
    subgraph Storage["Local DPAPI Keystore (%LOCALAPPDATA%)"]
        VaultFile["vault.dat (AES / DPAPI)"]
        BackupFile["vault.dat.bak (Automatic Rollback)"]
    end

    subgraph SecurityCore["Nova Security Core (C#)"]
        VaultStore["VaultStore
(GlobalWriteLock & Atomic Writes)"]
        DomainMatcher["Domain Matching & Public Suffix List (PSL)"]
        FingerprintService["VaultSecretFingerprintService
(SHA-256 Leak Tracker)"]
    end

    subgraph Redaction["Redaction Pipeline"]
        Redactor["VaultFingerprintBoundaryRedactor
(Redacts Leaks in Logs/Network)"]
    end

    subgraph WebSurface["CoreWebView2 Runtime"]
        TypeSecret["type_selector_secret Dispatcher"]
        DOMField["HTML <input type='password'>"]
    end

    VaultFile --> VaultStore
    VaultStore --> BackupFile
    VaultStore --> DomainMatcher
    VaultStore --> FingerprintService
    FingerprintService -. Registers Hashes .-> Redactor
    DomainMatcher --> TypeSecret
    TypeSecret --> DOMField
```

---

## 4. Production Code References

| Component | Source File | Responsibility |
| :--- | :--- | :--- |
| **`VaultStore`** | `NovaBrowser/Core/Security/VaultStore.cs` | DPAPI-encrypted persistence, atomic writes with backup rollback, and size limits (max 8 MB). |
| **`VaultSecretFingerprintService`** | `NovaBrowser/Core/Security/VaultSecretFingerprintService.cs` | Generates cryptographic hash fingerprints of active secrets to detect leaks across all output channels. |
| **`VaultFingerprintBoundaryRedactor`**| `NovaBrowser/Core/SessionRecording/VaultFingerprintBoundaryRedactor.cs` | Redacts accidentally reflected vault secrets in session recordings and network traces. |
| **`DomainPermissionEvaluator`** | `NovaBrowser/Core/Browser/DomainPermissionEvaluator.cs` | Validates target domains against the Public Suffix List (PSL) to prevent subdomain and TLD spoofing. |

---

## 5. MCP Tooling for Vault & Secrets

* **Zero-Leak DOM Injection:**
  * `nova.type_selector_secret`: Injects a password into an input field directly from the vault using an ephemeral `secretRef` token.
  * `nova.vault_prepare_fill`: Resolves matching credential accounts for the current URL without disclosing secret values.
* **Vault Administration:**
  * `nova.vault_list`: Lists available credential records (domain, username, label, timestamps). Passwords are excluded.
  * `nova.vault_get`: Retrieves credential metadata.
  * `nova.vault_set`: Stores or updates encrypted credentials in the vault.
  * `nova.vault_delete`: Permanently deletes a credential entry.
* **Encrypted Environment Variables & Secrets:**
  * `nova.secret_set` / `secret_list` / `secret_delete`: Manages global encrypted key-value variables (used by scheduled tasks and connectors).

---

## 6. Security & Integrity Guarantees

1. **Windows DPAPI Binding:** Encrypted using `DataProtectionScope.CurrentUser`. The file `vault.dat` can only be decrypted by the same Windows user account on the same machine.
2. **Public Suffix List (PSL) Guard:** Prevents credentials registered for `example.co.uk` from being injected into `attacker-co.uk`.
3. **Proactive Leak Redaction:** If an adversarial script attempts to read the password field via `input.value` and print it to the console, the `VaultSecretFingerprintService` intercepts the token and replaces it with `[REDACTED_VAULT_SECRET]`.

---

## Related Documentation

* **[Auth Surface Detection (ASD)](auth-surface-detection.md)** — Universal login wall and session state detection.
* **[Agent Awareness Gates (AAG)](aag.md)** — Pre-execution safety and lease locking.
