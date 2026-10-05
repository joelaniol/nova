# Workspace Layout & Window Chrome

> [!NOTE]
> Nova AI Workspace looks and behaves like a familiar Windows browser, with extra indicators for agent activity and for the tools developers use alongside the browser.

---

## 1. Visual Anatomy of Nova

Use the top row to switch pages and accounts, the address bar to navigate, and the menu to open settings or stop an agent. From top to bottom:

```
+-----------------------------------------------------------------------------------+
|  [Sandbox pills: A  B  ...]  [Tab 1] [Tab 2] [+]                      [_] [O] [X] |
+-----------------------------------------------------------------------------------+
|  [<-] [->] [Reload] [Home] | [Site info] address bar [Star] | status buttons [Menu]|
+-----------------------------------------------------------------------------------+
|  Bookmark bar (optional)                                                          |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|                             Web page                                   |
|                                                                                   |
|                   [ terminal dock, when open, lies over the page ]                |
+-----------------------------------------------------------------------------------+
```

---

## 2. Key Interface Elements

### 2.1 Sandbox Pills & Tab Strip
* **Sandbox pills:** each visible sandbox has a pill in the title bar. A pill can show a colour or the site icon as its mark (**Mark** in the pill's context menu). See [Sandboxes & Profiles](sandboxes-and-profiles.md).
* **Tabs:** normal browser tabs. Right-click a tab to **Pin tab**, give it a **Color**, **Mute tab**, or close it, other tabs or all tabs. Private tabs and tabs that belong to a sandbox carry a small badge.
* **Agent markers:** a tab or sandbox pill that an agent is working in, or has reserved, shows a marker; its tooltip says *Agent active*, *Agent recently active* or *Agent reserved*. See [AI Visualization & Staying in Control](live-assist-and-spectator.md).
* **Media indicator:** a tab that uses the camera, microphone or screen sharing is marked.

### 2.2 Toolbar & Address Bar
* **Back**, **Forward**, **Reload** (with hard reload) and **Home**.
* **Address bar:** enter an address or a search; `Ctrl+L`, `Alt+D` or `F4` puts the cursor there. The site info button in front of it shows the connection and site permissions.
* **Star:** opens the favorite dialog for the current page (`Ctrl+D`), where you can save or manage its bookmark.
* **Status buttons** appear only when they have something to say, for example the pop-up blocker, the active proxy, device emulation, notifications, scheduled tasks, active recordings or intercepted requests.

### 2.3 Quick Actions
* **Terminal:** shows or hides the built-in terminal dock (when the terminal is enabled). See [Terminal Dock](terminal-dock.md).
* **Downloads:** opens the downloads panel (`Ctrl+J`); the button appears while downloads are active or recent. See [Downloads](downloads-manager.md).
* **Menu:** among others **New private tab**, **Reopen closed tab**, **Hard reload**, **Print**, **Find on page**, zoom, **Downloads**, **History**, **Scheduled tasks**, **Favorites**, **View** (bookmark bar, **AI visualization**), **Settings**, **Developer tools**, **About** and **Emergency stop**.
* **Bookmark bar:** shown or hidden with `Ctrl+Shift+B` or **Menu → View → Show bookmark bar**.

---

## 3. Window Behaviour

* **Full screen:** `F11`. Hold `Escape` for about one second to leave it.
* **Closing:** when you close the window, Nova can ask **Close Nova?** — **Keep running in the background** (so scheduled tasks keep running; Nova then sits in the notification area) or **Quit Nova**.

All keyboard shortcuts: [Keyboard Shortcuts](keyboard-shortcuts.md).
