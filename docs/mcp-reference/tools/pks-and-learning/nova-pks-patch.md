# `nova.pks_patch`

> **Applies partial updates or selector refinements to an existing PKS phenomenon playbook.**

* **Core Feature Guide:** [Phenomenological Knowledge Store (PKS)](../../../core-features/phenomenological-knowledge-store-pks/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

`nova.pks_patch` updates whole sections of a phenomenon (`type`, `fingerprint`, `playbook`, `context`, `deprecated`) without touching the sections you omit. Within `playbook`, `policy`/`actions`/`verify`/`requiredCapabilities` are each replaced independently when provided — so fixing one drifted selector means resending that phenomenon's full `actions` array with the corrected selector, not a single-field edit. Like other PKS writes, the call is rejected unless `scope` matches a currently open tab or sandbox host.

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `scope` | `string` | Yes | — | — | Domain scope. |
| `phenomenonId` | `string` | Yes | — | — | Phenomenon ID to patch. |
| `patch` | `object` | Yes | — | — | Fields to merge. Only provided fields are updated. |
| `patch.type` | `string` | No | — | `consent_cmp`, `modal`, `paywall`, `login_wall`, `layout_shift`, `native_dialog`, `popover_open`, `custom` | Updated phenomenon type. |
| `patch.fingerprint` | `object` | No | — | — | Fingerprint signals to merge. When provided, the full fingerprint payload replaces the existing fingerprint. |
| `patch.playbook` | `object` | No | — | — | Playbook to merge. When provided, the full playbook payload replaces the existing playbook. |
| `patch.context` | `any` | No | — | — | Optional phenomenon-level context override. Set null to clear and fallback to domain context keys. |
| `patch.deprecated` | `boolean` | No | — | — | Set to false to reactivate a deprecated phenomenon. |

Capability bundle: `pks_learning` (load it with `nova.tools_bundle(bundle='pks_learning')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova_pks_patch",
  "arguments": {
    "scope": "example.com",
    "phenomenonId": "phenom-login",
    "patch": {
      "playbook": {
        "actions": [
          { "type": "click", "selector": "button[type=\"submit\"].btn-primary" }
        ]
      }
    }
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Phenomenon 'phenom-login' patched for example.com."
    }
  ],
  "structuredContent": {
    "patched": true,
    "scope": "example.com",
    "phenomenonId": "phenom-login"
  }
}
```

---

## 4. Operational Best Practices

* **Repairs Keep Telemetry:** Fix selector drift without resetting the phenomenon's accumulated health/attempt counters (unlike deprecate+recreate).

---

## 5. Related Tools

* [`nova.pks_upsert`](nova-pks-upsert.md)
* [`nova.revalidate`](nova-revalidate.md)
