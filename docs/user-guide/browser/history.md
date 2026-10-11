# Browsing History & Chronological Search

> [!NOTE]
> Nova AI Workspace records your browsing navigation history locally in your profile storage (`history.db`). The History panel provides full-text search, chronological time groupings, per-sandbox origin indicators, and granular clearing controls for human operators and connected AI agents.

---

## 1. Overview & Key Capabilities

Browsing history in Nova is engineered for privacy, speed, and deep integration with sandbox profiles:

* **Chronological Groupings:** Automatically organizes visits into **Today**, **Yesterday**, **Last 7 days**, and **Older**.
* **Full-Text Search:** Instantly filters past visits by page title, URL path, or domain name.
* **Sandbox Origin Tagging:** Each entry shows which sandbox profile (e.g. *Default*, *Work*, or *Client B*) visited the page, preserving account context.
* **Scoped URL Bar Search (`@history`):** Search exclusively through your historical visits directly from the main address bar.
* **Private Browsing Protection:** Sites visited in **InPrivate** tabs are never recorded in history.
* **Granular Deletion:** Remove single visits, purge specific domains, or clear history across custom timeframes.

```
+-----------------------------------------------------------------------------------+
|  History (Ctrl+H)                                                         [_][O][X]|
+-----------------------------------------------------------------------------------+
|  Search history: [ pull request                              ] [ Clear Data... ]  |
|                                                                                   |
|  TODAY - October 11, 2026                                                         |
|  +-----------------------------------------------------------------------------+  |
|  | [16:20] Pull Request #142 - Feature Branch       [Sandbox: Work]    [X Del] |  |
|  |         https://github.com/company/repo/pull/142                            |  |
|  +-----------------------------------------------------------------------------+  |
|  | [14:45] Cloud Monitoring - Active Dashboards      [Sandbox: Default] [X Del] |  |
|  |         https://console.cloud.google.com/monitoring                         |  |
|  +-----------------------------------------------------------------------------+  |
|  | [11:10] .NET 8 Performance Documentation          [Sandbox: Work]    [X Del] |  |
|  |         https://learn.microsoft.com/dotnet/performance/                     |  |
|  +-----------------------------------------------------------------------------+  |
|                                                                                   |
|  YESTERDAY - October 10, 2026                                                     |
|  +-----------------------------------------------------------------------------+  |
|  | [18:30] Web Speech API Specification              [Sandbox: Default] [X Del] |  |
|  |         https://w3c.github.io/speech-api/                                   |  |
|  +-----------------------------------------------------------------------------+  |
+-----------------------------------------------------------------------------------+
```

---

## 2. Opening and Searching History

### Accessing the History Panel
1. **Keyboard Shortcut:** Press `Ctrl+H` from any active browser window.
2. **Main Menu:** Select **Menu → History**.
3. **Recently Closed Tabs:** Open **Menu → History → Recently closed tabs** to quickly restore accidentally closed pages (`Ctrl+Shift+T`).

### Searching Past Visits
* Click into the search box at the top of the History panel.
* Type any word from the page title or URL (e.g. `pull request` or `docs`).
* Results filter dynamically as you type, highlighting matching text across all time periods.

### Scoped Search in the Address Bar (`@history`)
You can search history without opening the separate History panel:
1. Focus the address bar (`Ctrl+L` or `Alt+D`).
2. Type `@history ` followed by your search query.
3. The address bar displays matching pages from your history with timestamps and sandbox badges. Press `Enter` to navigate to the highlighted item.

---

## 3. Navigating from History

Clicking any history entry opens the page:

* **Left Click:** Navigates the current active tab to the selected URL.
* **Middle Click (or `Ctrl+Click`):** Opens the URL in a new background tab.
* **Right-Click Context Menu:**
  * **Open in new tab:** Opens the visit in a new tab.
  * **Open in new window:** Launches a separate browser window.
  * **Open in original Sandbox:** Opens the visit within the exact sandbox profile where it was originally viewed (e.g. *Sandbox B*), restoring logged-in sessions.
  * **Copy link address:** Copies the URL to your clipboard.
  * **Delete from history:** Removes that specific visit.

---

## 4. Clearing Browsing History

Nova provides comprehensive controls for removing browsing data:

### Deleting Specific Entries
* **Single Visit:** In the History list, hover over any item and click the delete icon `[X]`, or right-click and select **Delete from history**.
* **Entire Domain:** Search for a domain (e.g. `example.com`), select multiple entries with checkboxes or `Shift+Click`, and click **Delete selected**.

### Clearing Browsing Data in Bulk (`Ctrl+Shift+Delete`)
To purge browsing traces across time ranges:
1. In the History panel, click **Clear browsing data…**, or press `Ctrl+Shift+Delete`.
2. Choose a **Time range**:
   * **Last hour**
   * **Last 24 hours**
   * **Last 7 days**
   * **Last 4 weeks**
   * **All time**
3. Select the data categories to remove:
   * **Browsing history:** Clears the chronological list of visited URLs.
   * **Download history:** Clears the list of downloaded files (downloaded files on disk are preserved).
   * **Cookies and site data:** Signs you out of websites across selected sandboxes.
   * **Cached images and files:** Frees disk space by removing temporary web assets.
4. Click **Clear data**.

---

## 5. Private Browsing Protection

Nova provides absolute privacy for InPrivate sessions:

* Open a private tab via `Ctrl+Shift+N` or **Menu → New private tab**.
* Private tabs use an ephemeral in-memory profile. **No navigation URLs, cookies, form data, or temporary caches are ever written to `history.db`.**
* Closing the private tab scrubs all session state immediately from memory. See [Private Browsing](private-browsing.md).

---

## 6. AI Agent Integration

Connected AI agents can interact with browsing history through Nova's Model Context Protocol (MCP) tools:

* [`nova.history_search`](../../mcp-reference/tools/app-shell-and-ui/nova-history-search.md): Searches historical visits with keyword and sandbox filters.
* [`nova.history_get`](../../mcp-reference/tools/browser-automation/nova-history-get.md): Retrieves the session navigation back/forward history for a specific tab.
* [`nova.history_go`](../../mcp-reference/tools/browser-automation/nova-history-go.md): Simulates browser back/forward navigation (`-1`, `+1`) within a tab.

---

## Related Documentation

* **[Favorites & Bookmarks](favorites.md)** — Organizing saved pages and New Tab speed dials.
* **[Workspace Layout & Window Chrome](tabs-and-windows.md)** — Tab management and quick actions.
* **[Private Browsing](private-browsing.md)** — Ephemeral sessions and history suppression.
* **[Keyboard Shortcuts Reference](keyboard-shortcuts.md)** — Browser navigation hotkeys (`Ctrl+H`, `Ctrl+Shift+T`, etc.).
