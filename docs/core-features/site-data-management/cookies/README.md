# Cookies

To repair a login without wiping a whole profile, first inspect the website's cookie metadata. Delete a specific stale cookie only after identifying its domain and path; verify the website again afterward. A cookie change does not guarantee that the server will accept or renew a session.

## Browser-level inspection

Nova uses the target profile's browser cookie manager. This includes HttpOnly cookies that page JavaScript cannot read through `document.cookie`.

`nova.cookie_list` returns metadata by default. Filters can narrow results by URI, name or domain, and larger inventories are paginated. Reading values requires `includeValues=true` and a `domainFilter`; this is a sensitive read subject to [agent permissions](../permissions-and-audit/README.md).

A `cookieId` identifies a cookie within its profile using its name, domain and path. Cookies with the same name can therefore remain distinct. Use that ID, or the complete name/domain/path identity, when deleting one cookie.

## Create or replace a cookie

`nova.cookie_set` supports expiry, HttpOnly, Secure and SameSite attributes. `dryRun=true` validates a proposed cookie without writing it.

The domain must match the current host or an allowed parent domain. Nova blocks a built-in set of common public suffixes; this is not the complete Public Suffix List. `__Secure-` and `__Host-` cookies must satisfy their prefix constraints, and `SameSite=None` requires Secure. A rejected proposal must be corrected before writing.

## Delete one cookie or clear a domain

* `nova.cookie_delete` removes one identified cookie.
* `nova.cookie_clear` with `domain` clears cookies for that domain and its subdomains in the selected profile.
* Omitting `domain` clears every cookie in that profile, including cookies used by other tabs sharing it.

Cookie clearing does not also clear Web Storage, cached files or website permissions. See [Web Storage](../web-storage/README.md) and [Cache & Cleanup](../cache-and-cleanup/README.md) for those operations.

## Use a session in request replay

[Request replay session adoption](../../network/network-interception/README.md#adopt-a-browser-session-with-a-redacted-preview) can attach cookies applicable to a draft request's URL, including HttpOnly cookies, after permission to read session values. Adoption is explicit and subject to a destination check. Preparing the draft does not send it; the replay workflow documents the separate send step and redacted preview.

## Tool reference

[Cookie list](../../../mcp-reference/tools/site-data-and-identity/nova-cookie-list.md) · [Set](../../../mcp-reference/tools/site-data-and-identity/nova-cookie-set.md) · [Delete](../../../mcp-reference/tools/site-data-and-identity/nova-cookie-delete.md) · [Clear](../../../mcp-reference/tools/site-data-and-identity/nova-cookie-clear.md)

[Site Data Management](../README.md)
