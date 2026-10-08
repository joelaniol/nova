# Site Data Management

Site Data Management covers the data websites keep in a browser profile: cookies, Web Storage and cached resources. Nova offers a human-facing Cookie Inspector and permission-controlled agent tools. The sections below separate inspecting data, changing individual entries and clearing broader categories.

## Start with one website

If a website keeps returning to an expired login, ask your agent:

> Inspect cookie metadata and storage keys for this website in my work sandbox. Explain the scope before deleting anything. Keep my other profiles intact.

For a manual inspection, enable **Settings → Tools → Cookie inspector → Show cookie inspector in URL bar**, then open the inspector from the address bar.

## Topics

| Topic | What it covers |
|---|---|
| [Cookies](cookies/README.md) | HttpOnly cookies, metadata versus values, cookie identity, creation, validation and deletion. |
| [Web Storage](web-storage/README.md) | Current-origin localStorage and sessionStorage, individual keys and the limits of storage inspection. |
| [Cache & Cleanup](cache-and-cleanup/README.md) | Disk cache, Cache Storage, service workers, IndexedDB and profile-wide browsing-data clearing. |
| [Cookie Inspector](cookie-inspector/README.md) | The address-bar panel, cookie editing, storage previews and the profile cleanup dialog. |
| [Permissions & Audit](permissions-and-audit/README.md) | Agent access decisions, session grants, sensitive values and audit records. |
| [Troubleshooting](troubleshooting/README.md) | Login loops, recreated data, stale content and targeted repair before broad cleanup. |

## Choose the scope first

| Operation | Scope |
|---|---|
| Cookie list, write or delete | The profile behind the target, narrowed by cookie filters or identity. |
| Cookie clear with a domain | That domain and its subdomains in the selected profile. |
| Cookie clear without a domain | All cookies in the selected profile. |
| Web Storage inspect, set or delete | The current target document's origin and selected storage type. |
| Cache and browsing-data clear | Selected categories across the target's profile. |

Ordinary browser tabs share their normal profile. Sandbox targets use their sandbox's profile; private-session targets use their private profile. Selecting one tab does not make a profile-wide clear affect only that tab. See [Sandbox Isolation](../sandbox-isolation/README.md).

## Related features

* [Network request replay](../network/network-interception/README.md#adopt-a-browser-session-with-a-redacted-preview) can explicitly adopt applicable cookies and mapped storage values through the same permission gate. It prepares a separate HTTP request; it is not another site-data tool.
* [Site permissions](../../user-guide/settings/site-permissions.md) control website rights such as camera or microphone access. Removing cookies is not a substitute for resetting those permissions.
* [Privacy](../privacy/README.md) covers fingerprint protection and secrets kept in Nova's vault.
* [Site Data & Identity tool reference](../../mcp-reference/tools/site-data-and-identity/README.md) contains the API contracts. The eight cookie, storage and cache tools belong to the `site_data_management` bundle.

[All core features](../README.md)
