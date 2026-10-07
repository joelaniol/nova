# `nova.identity_presets`

Lists available browser identity presets and selectable browser engine versions.

---

## 1. Overview

`nova.identity_presets` returns the catalog of browser identity presets (`default`, `chrome`, `firefox`, `safari`, `custom`), each with its display name, whether it supports selecting a specific version, the list of known versions, and the latest known version.

* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation/README.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
This tool takes no parameters.

Capability bundle: `identity_management` (load it with `nova.tools_bundle(bundle='identity_management')`).
Tool category: `safe` (lowest risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.identity_presets",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Available browser identity presets: 5"
    }
  ],
  "structuredContent": {
    "presets": [
      {
        "id": "default",
        "displayName": "Default (WebView2/Edge)",
        "supportsVersionSelection": false,
        "versions": [],
        "latestVersion": null
      },
      {
        "id": "chrome",
        "displayName": "Chrome",
        "supportsVersionSelection": true,
        "versions": ["150.0.4078.65", "147.0.7727.56", "146.0.7680.180", "..."],
        "latestVersion": "150.0.4078.65"
      },
      {
        "id": "firefox",
        "displayName": "Firefox",
        "supportsVersionSelection": true,
        "versions": ["149.0.2", "148.0.2", "147.0.4", "..."],
        "latestVersion": "149.0.2"
      },
      {
        "id": "safari",
        "displayName": "Safari",
        "supportsVersionSelection": true,
        "versions": ["26.4", "26.3", "26.2", "..."],
        "latestVersion": "26.4"
      },
      {
        "id": "custom",
        "displayName": "Custom (free-form UA)",
        "supportsVersionSelection": false,
        "versions": [],
        "latestVersion": null
      }
    ]
  }
}
```

The `versions` lists are shortened here; each Chrome/Firefox/Safari preset actually lists several recent known versions, newest first. This response has no `ok` field.

---

## 4. Operational Best Practices

* **Catalog Selection:** Use preset `id` values directly in [`nova.identity_set`](nova-identity-set.md). `custom` requires a non-empty `customUserAgent`.

---

## 5. Related Tools

* [`nova.identity_get`](nova-identity-get.md)
* [`nova.identity_set`](nova-identity-set.md)
