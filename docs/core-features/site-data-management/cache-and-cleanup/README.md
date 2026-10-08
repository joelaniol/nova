# Cache & Cleanup

When a website serves stale resources, start with the cache category that matches the problem. Before clearing cookies or application storage, check which profile is selected and which other tabs use it. Clearing those categories can sign you out or remove saved website state.

## Browsing-data categories

`nova.cache_clear` accepts one or more `dataTypes`. Categories are combined and cleared across the selected target's browser profile.

| Category | What Nova requests the browser to clear |
|---|---|
| `diskCache` | Cached resource files. |
| `cacheStorage` | The Cache Storage category used by web applications. |
| `serviceWorkers` | The service-worker category. |
| `cookies` | All cookies in the selected profile. |
| `allDomStorage` | localStorage, sessionStorage and IndexedDB together. |
| `localStorage` | The same combined DOM-storage category as `allDomStorage`, despite the narrower name. |
| `history` | Browsing history and download history. This does not delete downloaded files. |
| `allSite` | The combined site-data category, including `AllDomStorage` and cookies, across the selected profile. |
| `allProfile` | Site data plus disk cache, browsing/download history, general autofill, browser password-autosave data and browser-profile settings. |

This operation does not offer a domain filter. For one domain's cookies use [cookie clearing](../cookies/README.md); for one current-origin storage key use [Web Storage deletion](../web-storage/README.md). Clearing Cache Storage or service workers is category-level cleanup, not inspection or editing of individual entries.

## `allSite` versus `allProfile`

`allSite` groups the browser's site-data categories. Its DOM-storage part is broader than individual Web Storage keys and also covers categories such as Cache Storage and file-system storage. The name does not mean "only the current website": Nova applies this clear across the selected profile.

`allProfile` adds profile categories such as cache, history, general autofill (including address and payment-form data), password autosave and browser-profile settings. WebView2 describes it as making the browser profile resemble a new profile. Account-scoped data is not itself deleted, but signing out can remove access to it. Both composite categories can include additional browser data types in future runtime versions. See [Microsoft's browsing-data category definitions](https://learn.microsoft.com/en-us/microsoft-edge/webview2/concepts/user-data-folder#what-kind-of-data-is-stored-in-the-udf).

Browser password-autosave data is distinct from [Nova's Vault](../../privacy/vault-and-secrets/README.md). `allProfile` is a browsing-data operation, not a command to delete a sandbox or remove downloaded files from disk. Choose explicit categories when their narrower scope matches the problem.

## Manual cleanup

Open the [Cookie Inspector](../cookie-inspector/README.md) and choose **Clear all site data for this profile...**. The dialog lets you select cookies, combined localStorage/sessionStorage/IndexedDB, cache data (including Cache Storage and service workers) and history. Read the profile scope before confirming.

**Clear cookies for this site** is a separate action in the inspector. It is narrower than the profile cleanup dialog and does not erase all other data types for that website.

## Agent cleanup and verification

Agent clears require `_meta.intent` and pass through the [site-data permission controls](../permissions-and-audit/README.md). After completion, reopen or reload the affected website and check the original symptom. Websites can recreate caches, cookies and storage during later visits; successful deletion does not mean those stores will stay empty.

Website camera, microphone and other [site permissions](../../../user-guide/settings/site-permissions.md) are managed separately.

[Cache clear tool reference](../../../mcp-reference/tools/site-data-and-identity/nova-cache-clear.md)

[Site Data Management](../README.md)
