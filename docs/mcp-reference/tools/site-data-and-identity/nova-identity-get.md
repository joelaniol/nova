# `nova.identity_get`

Reads the active browser identity profile, spoofed User-Agent, and client hints.

---

## 1. Overview

`nova.identity_get` returns the current browser persona configuration: active preset (`ChromeWindows`, `EdgeWindows`, `SafariMac`), version strings, custom User-Agent, and Sec-CH-UA client hint headers.

* **Capability Bundle:** `site_data_management`
* **Security Tier:** Tier 1 (Read-Only)
* **Core Architecture Guide:** [Sandbox Isolation & Container Security](../../../core-features/sandbox-isolation.md)

---

## 2. Parameter Reference

| Parameter | Type | Required | Default | Description |
| :--- | :--- | :---: | :---: | :--- |
| *(none)* | — | — | — | No parameters accepted. |

---

## 3. Protocol Examples

### JSON-RPC Request
```json
{
  "name": "nova.identity_get",
  "arguments": {}
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Current browser identity: ChromeWindows (v128.0.0.0)."
    }
  ],
  "structuredContent": {
    "ok": true,
    "preset": "ChromeWindows",
    "version": "128.0.0.0",
    "effectiveUserAgent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36"
  }
}
```

---

## 4. Operational Best Practices

* **Client Hint Consistency:** Nova automatically keeps `Sec-CH-UA` and `Sec-CH-UA-Platform` client hints synchronized with the chosen User-Agent.

---

## 5. Related Tools

* [`nova.identity_presets`](nova-identity-presets.md)
* [`nova.identity_set`](nova-identity-set.md)
