# `nova.fingerprint_get`

Reads the active browser fingerprint protection level (global, sandbox, or tab override).

---

## 1. Overview

`nova.fingerprint_get` inspects the anti-fingerprinting configuration applied to the browser, returning the global level (`off`, `standard`, `strict`; default `off`), per-sandbox overrides, and per-tab ephemeral overrides. Precedence for the effective level is per-tab, then per-sandbox, then global.

* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `sandboxId` | `string` | No | — | — | Sandbox letter id (e.g. 'A', 'B'). When provided, the response includes that sandbox's override. |
| `tabId` | `string` | No | — | — | Browser tab id (8-char hex). When provided, the response includes that tab's ephemeral override. |

Capability bundle: `fingerprint_protection` (load it with `nova.tools_bundle(bundle='fingerprint_protection')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.fingerprint_get",
  "arguments": {
    "tabId": "tab-1"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Fingerprint protection: effective=strict, source=sandbox, global=standard, sandbox=strict, tab=(none)"
    }
  ],
  "structuredContent": {
    "globalLevel": "standard",
    "sandboxOverride": "strict",
    "tabOverride": null,
    "effectiveLevel": "strict",
    "effectiveSource": "sandbox",
    "techniques": ["canvas", "audio", "font", "webgl", "hardware", "screen"],
    "allLevels": ["off", "standard", "strict"],
    "activeTabOverrides": {}
  }
}
```

This response has no `ok` field. `techniques` lists the protections active at the effective level; the exact set depends on the level.

---

## 4. Operational Best Practices

* **Stealth Auditing:** Verify effective fingerprinting levels before navigating to bot-protected surfaces.

---

## 5. Related Tools

* [`nova.fingerprint_set_global`](nova-fingerprint-set-global.md)
* [`nova.fingerprint_set_sandbox`](nova-fingerprint-set-sandbox.md)
* [`nova.fingerprint_set_tab`](nova-fingerprint-set-tab.md)
