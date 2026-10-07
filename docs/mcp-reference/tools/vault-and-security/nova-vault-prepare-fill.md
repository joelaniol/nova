# `nova.vault_prepare_fill`

Prepares stored credentials from the secure Vault for automated form-filling, returning an ephemeral, origin-bound, and single-use `SecretRef` token instead of the raw password string.

---

## 1. Overview

LLM-driven browser automation poses a severe credential security risk: if an agent reads a plaintext password to fill a web login form, that secret is exposed in LLM context logs, API provider telemetry, and prompt histories.

`nova.vault_prepare_fill` solves this by issuing an ephemeral **`SecretRef`** handle. The agent receives only an opaque token (a random hex string), which is cryptographically bound to the target tab's origin and expires automatically. The agent then passes this token to [`nova.type_selector_secret`](nova-type-selector-secret.md) to type the password directly into the browser without ever knowing the underlying plaintext.

* **Zero Plaintext Exposure:** Passwords never touch the LLM conversation context or prompt logs.
* **Site Check:** A token is only issued when the tab already shows the entry's site (same host or a subdomain of it); otherwise the call is refused with `vault.site_mismatch`.
* **Host Binding:** The token is bound to the tab's host (e.g. `github.com`); redemption on any other host is rejected.
* **Single-Use & Time-Bounded:** Tokens expire after 120 minutes and can only be redeemed once.

---

## 2. Security Architecture

```mermaid
sequenceDiagram
    participant Agent as Autonomous Agent
    participant MCP as Nova MCP Host
    participant Vault as DPAPI Encrypted Vault
    participant DOM as Browser DOM / WebView2

    Agent->>MCP: nova.vault_prepare_fill(site="github.com", targetId="tab-1")
    MCP->>Vault: Match origin & retrieve credentials
    Vault-->>MCP: Plaintext secret (in-memory only)
    MCP->>MCP: Mint single-use SecretRef (boundOrigin=github.com, ttl=120m)
    MCP-->>Agent: { username: "octocat", passwordRef: "<token>" }
    Note over Agent: Agent holds opaque token<br/>Password never exposed in context!
    Agent->>MCP: nova.type_selector_secret(selector="#password", secretRef="<token>")
    MCP->>MCP: Validate origin, expiry, and single-use lock
    MCP->>DOM: Set the field value via its native setter and dispatch input/change
    DOM-->>MCP: Success
    MCP-->>Agent: { ok: true, actionDispatched: true }
```

---

## 3. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | No | — | — | Tab ID or 'active'. The SecretRef will be bound to this tab's origin. |
| `site` | `string` | Yes | — | — | Site to match in the vault (e.g. 'github.com'). |
| `username` | `string` | No | — | — | Optional: specific username to match. |

**`_meta.intent` is required.** Pass a short reason for the call, e.g. `"_meta": { "intent": "why this call is needed" }`; calls without it are rejected.

Capability bundle: `vault_auth` (load it with `nova.tools_bundle(bundle='vault_auth')`).
Tool category: `high_impact` (highest risk class; Nova's agent permission settings can ask before it runs).
<!-- /generated:parameters -->

---

## 4. Example Calls

### Request Fill Token for Single-Account Site
```json
{
  "_meta": { "intent": "Logging into GitHub to create staging repository" },
  "site": "github.com",
  "targetId": "tab-101"
}
```

### Request Fill Token for Specific User Account
```json
{
  "_meta": { "intent": "Admin login for system maintenance" },
  "site": "aws.amazon.com",
  "username": "infra-admin@example.com",
  "targetId": "tab-102"
}
```

---

## 5. Return Value Structure

```json
{
  "found": true,
  "entryId": "a1b2c3d4",
  "site": "github.com",
  "username": "octocat",
  "passwordRef": "A819B02FE4918237C1894D2FF009988",
  "expiresAt": "2026-10-02T21:55:00Z",
  "boundOrigin": "github.com"
}
```

The token is single-use and bound to `boundOrigin`; both facts are enforced by `nova.type_selector_secret`, not re-stated as separate response fields.

---

## 6. Common Errors & Troubleshooting

| reasonCode / Message | Cause | Corrective Action |
| :--- | :--- | :--- |
| `found: false` ("No vault entry found for '...'.") | No saved credentials match the specified site. | Verify the site, or check stored entries with [`nova.vault_list`](nova-vault-list.md). |
| `ambiguous: true` ("Multiple accounts for '...' (N). Specify username.") | Multiple credentials exist for the site and no `username` was specified. | Inspect the returned `accounts` and supply `username` in the call. |
| `vault.site_mismatch` | The target tab is not already showing the entry's site (same host or a subdomain of it). | Navigate the tab to the entry's site first, then retry. |

---

## 7. Related Tools & Documentation

* [`nova.type_selector_secret`](nova-type-selector-secret.md) — Redeem the `SecretRef` to type the password.
* [`nova.vault_list`](nova-vault-list.md) — List available credential sites and usernames.
* [`nova.vault_get`](nova-vault-get.md) — Inspect site credential metadata without passwords.
* [Vault & Secret Management](../../../core-features/vault-and-secrets/README.md) — Architectural overview of DPAPI-encrypted credential management.
