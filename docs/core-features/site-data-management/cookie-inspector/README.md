# Cookie Inspector

The Cookie Inspector is Nova's manual view of cookies and Web Storage for the current website. It also provides access to a separate profile cleanup dialog.

## Open the inspector

1. Open **Settings → Tools → Cookie inspector**.
2. Enable **Show cookie inspector in URL bar**.
3. Open the website in the intended tab or sandbox and click the cookie inspector icon in the address bar.
4. Check the website and profile shown in the panel before making changes.

The current site's cookie list is distinct from the profile's total cookie inventory. The panel can report additional cookies elsewhere in the profile; those are not all cookies belonging to the current page.

## Inspect and edit cookies

The cookie rows show individual cookies and their attributes. You can reveal values, edit cookies, delete a cookie or choose **Add cookie**. Cookies can carry authentication values, including HttpOnly cookies, so reveal or copy them only when needed.

Use the search field to filter the displayed cookies by name. The panel is a bounded view, not an unlimited profile export; the [cookie tools](../cookies/README.md) provide filtered and paginated inventories for agent workflows.

## Add a cookie

1. Open the inspector for the intended website and profile, then choose **Add cookie**.
2. Enter **Name** and **Value**. Check **Domain**, which is pre-filled with the current website's host, and **Path**, which initially uses `/`.
3. Under **Validity**, choose **session** or **Pick date**. For a dated cookie, enter the expiry in the displayed `yyyy-MM-dd HH:mm` format.
4. Set **SameSite**, **HttpOnly** and **Secure** to match the intended cookie. The [Cookies guide](../cookies/README.md) explains these attributes.
5. Choose **Add**. If a required field or date is highlighted, correct it before trying again. Reopen the inspector and check the saved cookie's identity and attributes.

An existing cookie with the same name, domain and path can be replaced by this operation. Check that identity before adding a cookie; creating a cookie does not create a valid server-side login by itself.

## Edit or delete an existing cookie

1. Find the cookie by name and check its domain and path, then choose the row's **Edit** action.
2. Change **Value**, **Validity**, **HttpOnly**, **Secure** or **SameSite** as needed. Choose **Save**, or **Cancel** to leave the edit form without saving.
3. Check the refreshed inspector and reload the website when you need to verify how the application reacts. Refreshing the inspector is not the same as reloading the page.

**Name, Domain and Path are read-only in the edit form.** To change the cookie's identity, delete the old cookie and add a new one with the intended identity. Use **Delete** on the cookie row or in its edit form and review any confirmation before proceeding. Deletion and recreation are separate operations, so consider the loss of the original session before deleting it.

These instructions describe manual controls in your browser. Agent cookie writes have their own domain-validation and [permission](../permissions-and-audit/README.md) rules; the manual editor's available fields are not an agent authorization.

## Preview Web Storage

Expandable localStorage and sessionStorage sections show keys and value previews for the current document. Long values can be shortened, and a bounded list can omit additional entries. These sections are previews rather than a complete storage export or an IndexedDB editor.

### What the copy button copies

The copy action on a storage row writes `key=preview` to the clipboard. It copies the stored preview, which can be shortened for long values; it does not fetch a complete value on demand or export the storage entry as JSON. A formatted preview on screen also does not change that clipboard format.

Use this copy action for a quick diagnostic excerpt, not as a complete backup or a replacement value to paste into another store. If a complete value is needed, ask your agent to inspect that specific key with the appropriate value-read permission and check the result limits. A bounded tool result is not automatically a complete export either.

For targeted storage reads, writes or key deletion through an agent, see [Web Storage](../web-storage/README.md).

## Clear site cookies or profile data

* **Clear cookies for this site** removes site cookies; it does not clear every kind of website storage.
* **Clear all site data for this profile...** opens a dialog with data-category checkboxes and a profile scope. It can affect other tabs sharing that profile.

[Cache & Cleanup](../cache-and-cleanup/README.md) explains the categories and their consequences. The inspector's visibility setting is separate from [agent cookie/storage permissions](../permissions-and-audit/README.md).

[Site Data Management](../README.md)
