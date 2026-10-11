# Favorites & Bookmarks

> [!NOTE]
> Nova AI Workspace provides a flexible **Favorites & Bookmarks** system designed for fast navigation, folder organization, New Tab Page speed dials, and scoped search. Favorites are stored locally in your profile settings and are fully accessible to both human operators and connected AI agents.

---

## 1. Overview & Key Features

Saving pages as favorites allows you to quickly return to important sites, organize development portals into folders, and launch pages directly into specific sandbox profiles:

* **Bookmark Bar:** Optional horizontal bar underneath the address bar for single-click access.
* **New Tab Page (NTP) Tiles:** Pin favorite sites as speed-dial cards on every new tab.
* **Scoped Address Bar Search (`@bookmarks`):** Search exclusively across your saved favorites by typing `@bookmarks ` in the address bar.
* **Multi-Sandbox Launching:** Open any bookmark directly in a specific sandbox profile (e.g. Sandbox A or Sandbox B) from the context menu.
* **Human-Agent Parity:** Connected AI agents can read, create, and organize favorites using [`nova.favorites_*`](../../mcp-reference/tools/app-shell-and-ui/README.md) tools.

```
+-----------------------------------------------------------------------------------+
|  [<-] [->] [Reload] | https://github.com/nova-workspace  [Star Active] | [Menu]  |
+-----------------------------------------------------------------------------------+
|  [Folder: Work]  [GitHub]  [AWS Console]  [Staging Portal]  [Documentation]  [>>] |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|  FAVORITE DIALOG (Ctrl+D)                                                         |
|  Name:   [ Nova AI Workspace - GitHub                                 ]          |
|  Folder: [ Bookmark bar                                             v ]          |
|  [X] Pin as speed dial on New Tab Page                                            |
|                                                                                   |
|  [ Remove ]                                              [ Cancel ]  [ Done ]     |
+-----------------------------------------------------------------------------------+
```

---

## 2. Adding and Editing Favorites

### Quick Add via Address Bar (`Ctrl+D`)
1. Navigate to the webpage you want to bookmark.
2. Click the **Star icon** at the right end of the address bar, or press `Ctrl+D`.
3. The favorite flyout dialog opens:
   * **Name:** Edit the bookmark title (defaults to the webpage title).
   * **Folder:** Choose where to store the favorite (**Bookmark bar**, **Other favorites**, or a custom folder).
   * **Pin to New Tab:** Check this box to feature the site as a quick-dial card on the New Tab Page.
4. Click **Done** to save, or click **Remove** to delete an existing bookmark.

### Adding from Tabs or Web Links
* **Active Tab:** Right-click any tab header and select **Add tab to favorites**.
* **Webpage Links:** Right-click any hyperlink on a webpage and select **Add link to favorites**.
* **Drag and Drop:** Drag the lock/info icon beside the address bar directly onto the visible Bookmark Bar to save it in one gesture.

---

## 3. The Bookmark Bar (Favorites Bar)

The Bookmark Bar sits directly below the main toolbar, providing instant access to your most frequently used links and folders:

* **Show / Hide Bar:** Press `Ctrl+Shift+B` or select **Menu → View → Show bookmark bar**.
* **Reorder Bookmarks:** Click and drag any bookmark or folder horizontally to change its position.
* **Create Folders:** Right-click an empty space on the bar and select **Add folder…**. Name the folder (e.g., *"Dev Portals"*, *"Client Projects"*) to group related bookmarks.
* **Overflow Menu (`>>`):** When you have more bookmarks than fit horizontally on your display, an overflow chevron appears at the right edge to access the remaining links.

### Bookmark Context Menu
Right-click any bookmark on the bar to access quick actions:
* **Open:** Navigates the current tab to the bookmark.
* **Open in new tab:** Opens the bookmark in a background tab (`Ctrl+Click`).
* **Open in new window:** Opens in a separate browser window.
* **Open in Sandbox…:** Opens the bookmark in a specific sandbox profile (e.g. *"Open in Client B"*), ensuring cookies and sessions remain isolated.
* **Edit…:** Modify the name, destination URL, or parent folder.
* **Delete:** Permanently removes the bookmark.

---

## 4. Scoped Search in the Address Bar (`@bookmarks`)

Nova's address bar includes intelligent frecency (frequency + recency) ranking:

* **Automatic Priority Boost:** Pages saved in your favorites automatically receive a 1.5× ranking boost when typing partial search terms into the address bar.
* **Scoped Search Mode:** Type `@bookmarks` or `@favorites` followed by a space in the address bar.
  * The address bar switches into **Search favorites** mode.
  * Suggestions are strictly filtered to matching titles and URLs in your favorites collection, ignoring generic search engine queries and broad browsing history.

---

## 5. New Tab Page (NTP) Speed Dial Tiles

Every time you open a new tab (`Ctrl+T`), Nova displays a clean New Tab Page with your top pinned favorites:

* **Pinning Tiles:** Any favorite marked with **Pin as speed dial on New Tab Page** appears as a visual card featuring the site's high-resolution favicon and title.
* **Reordering Tiles:** Drag and drop cards on the New Tab Page to arrange your preferred workspace layout.
* **Unpinning:** Hover over any card and click the ellipsis menu `(...)` $\rightarrow$ **Unpin from new tab** to remove it without deleting the underlying bookmark.

---

## 6. Importing & Exporting Bookmarks

Migrating bookmarks from or to another browser is seamless:

* **Importing:** Open **Menu → Settings → General** and click **Import favorites**. Select an exported standard `bookmarks.html` file from Chrome, Edge, Safari, or Firefox. Nova preserves your existing folder hierarchy.
* **Exporting:** In Settings, click **Export favorites** to generate a portable `bookmarks.html` backup file.

---

## 7. AI Agent Integration

AI coding agents can manage favorites autonomously via Nova's Model Context Protocol (MCP) tools:

* [`nova.favorites_list`](../../mcp-reference/tools/app-shell-and-ui/nova-favorites-list.md): Retrieves all saved favorites with URLs, titles, and folder structures.
* [`nova.favorites_add`](../../mcp-reference/tools/app-shell-and-ui/nova-favorites-add.md): Programmatically creates a new favorite.
* [`nova.favorites_remove`](../../mcp-reference/tools/app-shell-and-ui/nova-favorites-remove.md): Removes an obsolete bookmark by URL.
* [`nova.favorites_open`](../../mcp-reference/tools/app-shell-and-ui/nova-favorites-open.md): Navigates the active tab (or opens a new tab) to a saved bookmark.

---

## Related Documentation

* **[Browsing History](history.md)** — Searching and managing visited pages.
* **[Workspace Layout & Window Chrome](tabs-and-windows.md)** — Toolbar layout, sandbox pills, and tab strips.
* **[Keyboard Shortcuts Reference](keyboard-shortcuts.md)** — Complete shortcut reference (`Ctrl+D`, `Ctrl+Shift+B`, etc.).
* **[Sandboxes & Profiles](../identity-and-security/sandboxes-and-profiles.md)** — Multi-profile session isolation.
