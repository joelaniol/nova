# `nova.identity_set`

Configures and persists a new browser identity profile (preset + version/custom UA).

---

## 1. Overview

`nova.identity_set` persists a new browser persona into `settings.json`. It configures the browser to emulate specific User-Agent strings, platform navigator properties, and client hints across future WebView instantiations.

* **Capability Bundle:** `site_data_management`
* **Security Tier:** Tier 2 (Identity Configuration)
* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| **`customUserAgent`** | `string,null` | No | `null` | Custom user-agent string. Required when preset='custom'. Set to null or an empty string to clear a stored custom user-agent. Max 1024 characters. Control characters are stripped automatically. |
| **`preset`** | `string` | No | `null` | Browser identity preset. 'default' = native WebView2/Edge UA. 'chrome'/'firefox'/'safari' = spoofed UA for that browser. 'custom' = free-form UA string (requires customUserAgent). |
| **`version`** | `string` | No | `null` | Version string for chrome/firefox/safari presets. 'latest' or omit for the newest available version. Ignored for 'default' and 'custom' presets. Use nova.identity_presets to see valid version strings. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.identity_set",
  "arguments": {
    "preset": "ChromeWindows",
    "version": "128.0.0.0"
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Persisted browser identity: ChromeWindows (v128.0.0.0)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "preset": "ChromeWindows",
    "version": "128.0.0.0",
    "effectiveUserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/128.0.0.0"
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
