# `nova.cookie_delete`

Deletes a specific cookie by cookieId or by name, domain, and path tuple.

---

## 1. Overview

`nova.cookie_delete` removes a single cookie from the target sandbox profile. It can target cookies using the stable `cookieId` returned by `nova.cookie_list` or an explicit `{name, domain, path}` tuple.

* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `targetId` | `string` | Yes | — | — | Tab or sandbox ID. Required. |
| `cookieId` | `string` | No | — | — | Deterministic cookie ID from cookie_list. Takes priority over name/domain/path if both are supplied. |
| `name` | `string` | No | — | — | Cookie name. Required if no cookieId. |
| `domain` | `string` | No | — | — | Cookie domain. Required if no cookieId. |
| `path` | `string` | No | `"/"` | — | Cookie path. Default: '/'. |
| `dryRun` | `boolean` | No | `false` | — | Preview deletion without executing. Returns matchCount. |

Capability bundle: `site_data_management` (load it with `nova.tools_bundle(bundle='site_data_management')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.cookie_delete",
  "arguments": {
    "targetId": "tab-1",
    "name": "user_pref",
    "domain": ".example.com",
    "path": "/"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Deleted 1 of 1 matching cookie(s) (sandbox:tab-1)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "deletedCount": 1,
    "matchCount": 1,
    "scope": {
      "profileId": "tab-1",
      "profileScope": "sandbox:tab-1",
      "isSharedProfile": false
    }
  }
}
```

---

## 4. Operational Best Practices

* **Exact Identity:** Cookies must match the exact domain and path under which they were registered.
* **Idempotent:** Deleting a cookie that no longer exists is not an error — `matchCount: 0` still returns `ok: true`.

---

## 5. Related Tools

* [`nova.cookie_clear`](nova-cookie-clear.md)
* [`nova.cookie_list`](nova-cookie-list.md)
