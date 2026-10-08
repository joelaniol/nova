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

## Preview Web Storage

Expandable localStorage and sessionStorage sections show keys and value previews for the current document. Long values can be shortened, and a bounded list can omit additional entries. These sections are previews rather than a complete storage export or an IndexedDB editor.

For targeted storage writes or key deletion through an agent, see [Web Storage](../web-storage/README.md).

## Clear site cookies or profile data

* **Clear cookies for this site** removes site cookies; it does not clear every kind of website storage.
* **Clear all site data for this profile...** opens a dialog with data-category checkboxes and a profile scope. It can affect other tabs sharing that profile.

[Cache & Cleanup](../cache-and-cleanup/README.md) explains the categories and their consequences. The inspector's visibility setting is separate from [agent cookie/storage permissions](../permissions-and-audit/README.md).

[Site Data Management](../README.md)
