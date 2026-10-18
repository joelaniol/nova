# Browsing History

> [!NOTE]
> **Upcoming in 1.0.0-alpha.21 (not published yet).** The History tab, the "Recently closed" view and the History menu described here come with 1.0.0-alpha.21. In 1.0.0-alpha.20 and earlier, history is listed under **Settings → History**.

Nova keeps your browsing history locally on your computer. You can search it, reopen pages, bring back tabs you closed by accident and delete what you no longer want to keep.

---

## 1. Opening History

* **Keyboard:** press `Ctrl+H`.
* **Main menu:** **Menu → History → Show history**.
* **Settings:** **Settings → History → Show history**.

History opens as an ordinary tab. If a History tab is already open, Nova switches to it instead of opening a second one. Back, Forward, Reload and `Ctrl+W` work as on any web page.

The page has two views in its left column:

* **Visited pages:** every recorded visit, newest first, grouped by day ("Today", "Yesterday", then the date).
* **Recently closed:** tabs and groups of tabs you closed, ready to be restored.

---

## 2. Finding a Page

* **Search:** type into the search box at the top. Nova searches page titles and addresses of your whole history, not only the visible part.
* **Show visits from:** the chips below the search box limit the list to **All**, **Normal tabs** or a single sandbox. Search and filter work together.
* **Badges:** a visit made inside a sandbox carries that sandbox's name; a visit opened by an AI agent carries an agent badge.
* **Address bar:** type `@history ` followed by a search term in the address bar to get suggestions from your history only.

---

## 3. Opening a Page from History

* **Click:** opens the page in a new tab right next to the History tab. Closing that tab brings you back to History.
* **Middle click or `Ctrl+Click`:** opens the page in a new background tab.
* **⋯ menu (or right-click):**
  * **Open in new tab**
  * **Copy address**
  * **More from this site:** searches your history for the same site.
  * **Remove from history**

---

## 4. Restoring Closed Tabs

* **`Ctrl+Shift+T`** reopens the most recently closed tab. The tab bar's context menu offers the same as **Reopen closed tab**.
* **Menu → History** lists the last closed tabs with their site icons. Tabs that were closed together (for example "Close tabs to the right") appear as one group; you can restore the whole group or a single tab from it.
* **History → Recently closed** shows the same list in the History tab.
* A tab that belonged to a sandbox reopens inside the same sandbox. If that sandbox no longer exists, Nova asks before opening the page in a normal tab.
* Tabs closed by an AI agent are marked with a bot icon. Tabs an agent opened and closed for itself are not listed.
* Private tabs are never listed.

### Previous session

If Nova was closed with tabs open, **Menu → History → Open last session** reopens them, even if you declined the restore question at startup. The New Tab page shows the same offer as a card.

---

## 5. Removing History

### Single pages

Use **Remove from history** in a row's ⋯ menu. The row disappears at once and **Undo** stays available for a few seconds. Removing a page removes all of its recorded visits.

### Clearing a time range

**History → Clear browsing data** opens **Settings → History**, which offers:

* **Clear last hour**
* **Clear last 24 hours**
* **Clear all history**

Clearing history also removes the matching entries from "Recently closed" and the kept last session, so nothing you deleted can be reopened from there.

### Keeping history for a limited time

**Settings → History → Keep history for** sets how long visits are kept: 30 days, 90 days, 180 days, 1 year or no time limit.

---

## 6. What Is Not Recorded

* Pages in **private tabs** are never written to history. See [Private Browsing](private-browsing.md).
* Reloading a page, or a page that reloads itself, does not add a new entry each time.
* Pages opened by an AI agent are recorded with an agent badge but never feed your address-bar suggestions. To stop recording them, turn off **Settings → Privacy & Security → Also save pages the AI assistant opens to history**.

---

## 7. AI Agent Integration

Connected AI agents can read history through Nova's MCP tools:

* [`nova.history_search`](../../mcp-reference/tools/app-shell-and-ui/nova-history-search.md): searches recorded visits.
* [`nova.history_get`](../../mcp-reference/tools/browser-automation/nova-history-get.md): reads a tab's back/forward list.
* [`nova.history_go`](../../mcp-reference/tools/browser-automation/nova-history-go.md): moves a tab back or forward.

---

## Related Documentation

* **[Favorites & Bookmarks](favorites.md)** — Organizing saved pages and New Tab speed dials.
* **[Workspace Layout & Window Chrome](tabs-and-windows.md)** — Tab management and quick actions.
* **[Private Browsing](private-browsing.md)** — Ephemeral sessions and history suppression.
* **[Keyboard Shortcuts Reference](keyboard-shortcuts.md)** — Browser navigation hotkeys (`Ctrl+H`, `Ctrl+Shift+T`, etc.).
