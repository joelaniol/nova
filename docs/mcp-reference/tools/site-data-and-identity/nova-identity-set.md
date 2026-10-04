# `nova.identity_set`

Configures and persists a new browser identity profile (preset + version/custom UA).

---

## 1. Overview

`nova.identity_set` persists a new browser persona into `settings.json`. It configures the browser to emulate specific User-Agent strings, platform navigator properties, and client hints across future WebView instantiations.

* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `preset` | `string` | No | — | `default`, `chrome`, `firefox`, `safari`, `custom` | Browser identity preset. 'default' = native WebView2/Edge UA. 'chrome'/'firefox'/'safari' = spoofed UA for that browser. 'custom' = free-form UA string (requires customUserAgent). |
| `version` | `string` | No | — | — | Version string for chrome/firefox/safari presets. 'latest' or omit for the newest available version. Ignored for 'default' and 'custom' presets. Use nova.identity_presets to see valid version strings. |
| `customUserAgent` | `string or null` | No | — | — | Custom user-agent string. Required when preset='custom'. Set to null or an empty string to clear a stored custom user-agent. Max 1024 characters. Control characters are stripped automatically. |

Capability bundle: `identity_management` (load it with `nova.tools_bundle(bundle='identity_management')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.identity_set",
  "arguments": {
    "preset": "chrome",
    "version": "147.0.7727.56"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Browser identity changed to chrome (Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.7727.56 Safari/537.36)"
    }
  ],
  "structuredContent": {
    "preset": "chrome",
    "version": "147.0.7727.56",
    "customUserAgent": null,
    "effectiveUserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/147.0.7727.56 Safari/537.36",
    "changed": true
  }
}
```

---

## 4. Operational Best Practices

* **Restart Notice:** Identity changes apply to new tabs and newly initialized WebViews; existing active tabs may retain current session state until refreshed.

---

## 5. Related Tools

* [`nova.identity_get`](nova-identity-get.md)
* [`nova.identity_presets`](nova-identity-presets.md)
