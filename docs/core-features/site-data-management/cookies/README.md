# Cookies

To repair a login without wiping a whole profile, first inspect the website's cookie metadata. Delete a specific stale cookie only after identifying its domain and path; verify the website again afterward. A cookie change does not guarantee that the server will accept or renew a session.

## Browser-level inspection

Nova uses the target profile's browser cookie manager. This includes HttpOnly cookies that page JavaScript cannot read through `document.cookie`.

`nova.cookie_list` returns metadata by default. Filters can narrow results by URI, name or domain, and larger inventories are paginated. Reading values requires `includeValues=true` and a `domainFilter`; this is a sensitive read subject to [agent permissions](../permissions-and-audit/README.md).

A `cookieId` identifies a cookie within its profile using its name, domain and path. Cookies with the same name can therefore remain distinct. Use that ID, or the complete name/domain/path identity, when deleting one cookie.

## Session cookies, expiry and cookie scope

A session cookie has no persistent expiry time; it is distinct from a cookie with a future expiry. Do not use the session-cookie label as a promise about one tab closing or a particular session-restore workflow. The website can also invalidate a login on its server independently of the browser's cookie expiry.

For `nova.cookie_set`, `expires` is a Unix timestamp in seconds. Omit it or use `0` for a session cookie. A timestamp in the past creates an immediately expired cookie, effectively removing it. A future expiry does not guarantee that the server-side session remains valid until then.

| Attribute | Why it matters |
|---|---|
| Domain and path | Determine which requests a cookie can apply to, and distinguish otherwise identically named cookies. A path is not a separate browser profile. |
| Secure | Restricts cookie transmission to secure connections. |
| HttpOnly | Prevents page JavaScript from reading the cookie; Nova's browser cookie manager can still inspect it after the applicable permission check. |
| SameSite | Controls cookie use in cross-site request contexts. `None`, `Lax` and `Strict` are not interchangeable login fixes. |
| Expiry | Controls persistent lifetime; server-side revocation can still make a stored cookie unusable. |

## Create or replace a cookie

`nova.cookie_set` supports expiry, HttpOnly, Secure and SameSite attributes. `dryRun=true` validates a proposed cookie without writing it.

The domain must match the current host or an allowed parent domain. Nova blocks a built-in set of common public suffixes; this is not the complete Public Suffix List. `__Secure-` and `__Host-` cookies must satisfy their prefix constraints, and `SameSite=None` requires Secure. A rejected proposal must be corrected before writing.

## Delete one cookie or clear a domain

* `nova.cookie_delete` removes one identified cookie. With `dryRun=true`, it reports the matching cookies without deleting them; an unknown ID can return zero matches. Re-check the identity before performing the actual delete.
* `nova.cookie_clear` with `domain` clears cookies for that domain and its subdomains in the selected profile.
* Omitting `domain` clears every cookie in that profile, including cookies used by other tabs sharing it.

Cookie clearing does not also clear Web Storage, cached files or website permissions. See [Web Storage](../web-storage/README.md) and [Cache & Cleanup](../cache-and-cleanup/README.md) for those operations.

## Use a session in request replay

[Request replay session adoption](../../network/network-interception/README.md#adopt-a-browser-session-with-a-redacted-preview) can attach cookies applicable to a draft request's URL, including HttpOnly cookies, after permission to read session values. Adoption is explicit and subject to a destination check. Preparing the draft does not send it; the replay workflow documents the separate send step and redacted preview.

For login loops or data that returns after deletion, see [Site Data Troubleshooting](../troubleshooting/README.md).

## Tool reference

[Cookie list](../../../mcp-reference/tools/site-data-and-identity/nova-cookie-list.md) · [Set](../../../mcp-reference/tools/site-data-and-identity/nova-cookie-set.md) · [Delete](../../../mcp-reference/tools/site-data-and-identity/nova-cookie-delete.md) · [Clear](../../../mcp-reference/tools/site-data-and-identity/nova-cookie-clear.md)

[Site Data Management](../README.md)
