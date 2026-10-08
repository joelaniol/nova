# Site Data Troubleshooting

Start with the affected website in the intended tab or sandbox. Keep the symptom, current URL and profile clear before changing data. A login problem in one sandbox is not a reason to erase another sandbox or recreate its profile.

## A safe first request

> Investigate why this website keeps returning to login in my work sandbox. Start with cookie metadata and storage keys. Explain the likely cause and the smallest proposed change before deleting anything. Keep other websites and profiles intact, then re-check the original problem.

The [Cookie Inspector](../cookie-inspector/README.md) provides a manual starting point: enable it under **Settings → Tools → Cookie inspector**, open the website and inspect its cookies and storage previews.

## Login loops or an expired session

1. Confirm the tab's website and profile. Similar-looking tabs can use different sandbox sessions.
2. Inspect cookie metadata before revealing values. Check domain, path, expiry and security attributes; several cookies can have the same name.
3. Inspect current-origin storage keys separately. A website can keep application state in Web Storage as well as cookies.
4. If a specific stale entry is identified, preview the cookie deletion or propose a single storage-key deletion. Explain any remaining uncertainty before making the change.
5. Reload the website and try its normal login flow. If the problem persists, examine the website's visible error and the request/response evidence rather than repeatedly widening the deletion scope.

Cookie expiry is not the only cause: the server can revoke a session, reject credentials or fail during an authentication flow. Clearing site data cannot guarantee a successful login. [Network interception and replay](../../network/network-interception/README.md) can help investigate requests, but a separate replay request does not automatically reproduce the browser session or transport.

## Data reappears after deletion

A successful delete describes the operation at that moment. An open page may retain state in memory, write storage again or receive another cookie from its server. Cached resources can also be fetched again during a later visit.

Check whether the same cookie identity or storage key returned, when it returned and whether the page was reloaded. Avoid repeated bulk clears without finding the writer or the request that recreates the data. Metadata and a description of the sequence are usually a better first diagnostic than copying session tokens into a report.

## Stale content or offline application state

| Symptom | Narrow starting point |
|---|---|
| A saved preference or old application value is wrong | Inspect the current origin's [Web Storage](../web-storage/README.md); change or remove the identified key. |
| A resource appears stale | Consider the `diskCache` category and re-check the loaded resource. This clear is profile-wide. |
| An application still shows offline/cached state | Investigate Cache Storage and service-worker behavior before selecting those cleanup categories. |
| A cookie appears unchanged after deletion | Check name, domain and path, then whether the server or page recreated it. |

Nova's site-data tools do not provide an IndexedDB record editor or individual Cache Storage/service-worker inspection tools. Their supported cleanup is category-level. `allDomStorage`, including the accepted `localStorage` cleanup label, clears localStorage, sessionStorage and IndexedDB together across the selected profile. See [Cache & Cleanup](../cache-and-cleanup/README.md).

For a problem involving IndexedDB writes, [Web Storage: recorded database activity](../web-storage/README.md#observe-indexeddb-activity-through-session-recording) explains the separate Session Recording diagnostic path and its value-capture permission boundary.

## The agent cannot access or clear data

Read the reported reason and check [Permissions & Audit](../permissions-and-audit/README.md). A value-read grant is separate from a delete or clear grant. An explicit session denial remains effective even under a permissive global policy; cancelling a prompt is different from denying it. A cancelled, unavailable or timed-out prompt leaves the protected action unapproved.

## A sandbox or its login is missing

If the sandbox itself disappeared, follow [Sandbox & Session Recovery](../../../troubleshooting/sandbox-and-session-recovery.md#4-sandbox-profile-recovery). That is profile recovery, not cookie cleanup. Do not delete or recreate a profile as the first repair.

The site-data audit log is not a backup and offers no restore operation for deleted cookies or storage. If credentials remain valid, logging in again may establish a new session, but it does not recover all removed application data.

[Site Data Management](../README.md)
