# Password Vault & Secret Injection

> [!NOTE]
> The assistant password vault stores login credentials so that agents can fill password fields without ever receiving the password. Agents work with metadata (site, username) and a short-lived, single-use token; Nova itself puts the password into the page. A separate secret store holds API keys and tokens that Nova passes to terminal sessions and scheduled tasks as environment variables.

---

## 1. Problem Statement: Credential Exposure in Autonomous Browsing

Conventional browser automation exposes credentials during sign-in:
1. **Plaintext passwords in the model context:** If an operator writes a password into a prompt ("Log in with SecretPass123"), it is sent to the model provider and ends up in conversation transcripts and logs.
2. **Exfiltration via prompt injection:** A page can try to talk an agent into repeating values it has seen. A password the agent never received cannot be repeated.

Nova addresses the first point directly: no vault tool returns a password. The second is reduced to what the agent can see, which is metadata only.

---

## 2. The Fill Flow

```mermaid
sequenceDiagram
    autonumber
    actor User as Operator
    participant Agent as AI Agent (MCP client)
    participant Host as Nova
    participant DOM as Page in the tab

    User->>Host: Saves a login in the password vault
    Host->>Host: Encrypts the vault file with Windows DPAPI (current user)
    Agent->>Host: nova.vault_list(site) or nova.vault_get(site)
    Host-->>Agent: id, site, username - no password
    Agent->>Host: nova.vault_prepare_fill(site, username, targetId)
    Host-->>Agent: passwordRef token, bound to the tab's current host, valid 2 h, single use
    Agent->>Host: nova.type_selector_secret(selector, secretRef)
    Host->>Host: Redeems the token only if the tab is still on the bound host
    Host->>DOM: Sets the field value and fires input and change events
    Host-->>Agent: ok, selector, targetId - no password
```

At no point does a tool result contain the password. It exists in Nova's process memory and, once filled, in the page's password field.

---

## 3. What Agents Can and Cannot See

| Tool | Returns | Never returns |
| :--- | :--- | :--- |
| `nova.vault_list` | `id`, `site`, `username`, `createdBy`, `createdUtc` per entry; optional `site` filter (substring, case-insensitive) | password |
| `nova.vault_get` | entry metadata plus `passwordAvailable`, `passwordRedacted: true`, `retrievalMode: "secretref_required"` | password |
| `nova.vault_prepare_fill` | `entryId`, `site`, `username`, `passwordRef`, `expiresAt`, `boundOrigin` | password |
| `nova.type_selector_secret` | `ok`, `selector`, `targetId`, `actionDispatched`, an autofill popup warning if relevant | password |
| `nova.vault_set` / `nova.vault_delete` | action result | stored password (it is only written, never read back) |

---

## 4. The SecretRef Token

* **Issued by `nova.vault_prepare_fill`:** If the `site` matches several entries, the call returns the usernames and asks for `username` instead of issuing a token.
* **Bound to a host:** The token is bound to the host of the target tab at the moment it is issued. `nova.type_selector_secret` redeems it only while that tab is on the same host (exact, case-insensitive host comparison). On a mismatch nothing is typed and the same token can be retried on the right host.
* **Single use, 2 hours:** A redeemed token cannot be used again; an unused token expires after 2 hours. Both cases need a fresh `nova.vault_prepare_fill`.
* **In memory only:** Tokens are random 128-bit values held in memory and are gone after a Nova restart.

> [!IMPORTANT]
> `nova.vault_prepare_fill` only issues a token when the tab already shows the vault entry's site: the same host or a subdomain of it, by the same rule the autofill for you uses (never the reverse, never across shared-hosting domains such as `github.io`). Otherwise the call is refused with `vault.site_mismatch`. Open the real login page first, then prepare the fill.

---

## 5. Storage & Encryption

* **Vault file:** `vault.dat` in the Nova profile folder (`%LOCALAPPDATA%\nova-cognitive\Nova\`; installations upgraded from older versions may still use `%LOCALAPPDATA%\NovaBrowser\`).
* **Encryption:** The whole vault is serialized and encrypted with Windows DPAPI in the current-user scope. Only the same Windows user account can decrypt it; restoring a backup on another machine or under another user requires re-entering credentials.
* **Writes:** Each save writes to a temporary file and replaces `vault.dat` in one step, so an interrupted save leaves the previous file intact. A vault that exists but cannot be read is not treated as empty, so a failed read cannot overwrite it.
* **Limits:** at most 5,000 entries and 8 MB for the encrypted file. Via MCP, `site` is limited to 512 characters, `username` to 256 and `password` to 4,096.

---

## 6. User Controls

* **Settings > Passwords & autofill > "Enable assistant password vault":** turns the vault on or off. While it is off, every vault tool returns "Vault is disabled".
* **"Agent may use saved passwords"** (agent permissions): turns off `nova.vault_list`, `nova.vault_get`, `nova.vault_prepare_fill` and `nova.type_selector_secret` for agents. Per-domain agent rules can additionally disallow vault access on specific sites.
* Depending on the agent permission settings, Nova asks for confirmation before an agent stores or removes credentials ("The agent wants to store or update credentials in the vault.").

---

## 7. Redaction in Session Recordings

When a session recording is running, Nova keeps HMAC-SHA-256 fingerprints of the vault passwords (in six encodings: raw, URL-encoded upper and lower case, JSON-escaped, Base64, Base64url) under a random key that exists only in memory. Recorded HTTP bodies and WebSocket payloads that contain a vault password in one of these forms are stored with the value replaced by a `[redacted:vault-fingerprint:...]` marker, and the entry is flagged `vaultFingerprintMatched`. This applies to session recordings only; it does not filter console output or what a page itself does with a field's value.

---

## 8. Secret Store for Terminal & Tasks

`nova.secret_set`, `nova.secret_list` and `nova.secret_delete` manage API keys and tokens with the scopes `global`, `workspace` and `task`. Values are DPAPI-encrypted (current user), are never returned by any tool, and are injected as environment variables into terminal-workspace sessions and scheduled-task runs. A `global` secret reaches a terminal workspace only after the user has granted that workspace access.

---

## Related Documentation

* **[Auth Surface Detection (ASD)](auth-surface-detection.md)** — Detection of login walls and session state.
* **[Agent Awareness Gates (AAG)](aag.md)** — Pre-execution safety and lease locking.
