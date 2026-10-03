# Workspace Layout & Visual Chrome

> [!NOTE]
> Nova AI Workspace combines the familiar simplicity of a modern Windows 11 browser with specialized instrumentation for monitoring background agent automation and developer workflows.

---

## 1. Visual Anatomy of Nova

Nova's main interface is built using native **WinUI 3** and **Windows App SDK**, providing Mica backdrop effects, rounded geometry, and fluid animations.

```
+-----------------------------------------------------------------------------------+
|  [Nova Icon]  [Tab 1: Work (Blue)]  [Tab 2: Scraping (Orange)]  [+]     [_] [O] [X] |
+-----------------------------------------------------------------------------------+
|  [<-] [->] [R] |  https://github.com/joelaniol/nova  [AAG Green] [MCP]  | [*] [D] [=] |
+-----------------------------------------------------------------------------------+
|                                                                                   |
|                                                                                   |
|                             Active Web Content                                    |
|                             (Microsoft WebView2)                                  |
|                                                                                   |
|                                                                                   |
+-----------------------------------------------------------------------------------+
|  >_ PowerShell 7 | C:\Users\...                                        [^] [v] [x] |
+-----------------------------------------------------------------------------------+
```

---

## 2. Key Interface Elements

### 2.1 Color-Coded Tab Strip
* **Sandbox Indicator Stripes:** Each tab features a colored bottom border and header tint matching its assigned Sandbox (e.g., Blue for Production/Work, Orange for Scraping, Green for Personal).
* **Agent Ownership Badge:** When an AI agent claims exclusive programmatic control over a tab, an animated glowing marker appears on the tab header.
* **Audio & Device Indicators:** Tabs actively playing sound or accessing microphones/cameras display interactive mute/block badges.

### 2.2 Omnibox & Address Bar
* **Navigation Field:** Standard URL navigation, local search engine queries, and custom internal scheme routing (`nova://settings`, `nova://downloads`).
* **MCP Status Pill:** Shows the live connection state of the local MCP Remote Control server:
  * 🟢 **Connected (Green):** MCP server active, agent connected through the stdio bridge or over HTTP.
  * 🟡 **Idle (Yellow):** MCP server listening; no active agent session.
  * 🔴 **Disabled (Red):** Remote control disabled in Settings.
* **AAG Security Badge:** Visual indicator of Agent Awareness Gates:
  * Displays current safety level (e.g., `Safe`, `Guarded`, `Restricted`).
  * Clicking the badge opens the live AAG permission inspector.

### 2.3 Quick Action Controls (Top Right)
* **Favorites / Bookmarks (`Ctrl+D`):** Access organized bookmark trees and folder structures.
* **Downloads Drawer (`Ctrl+J`):** Toggles the sliding flyout panel showing active and completed file downloads.
* **Settings Gear (`Ctrl+,`):** Opens the comprehensive Nova configuration overlay.
* **Terminal Dock Toggle (`Ctrl+``):** Instantly shows or hides the integrated bottom terminal dock.

---

## 3. Responsive Window Management

* **Snap Layouts Support:** Full native support for Windows 11 snap layouts, multi-monitor high-DPI scaling, and virtual desktops.
* **Spectator Border:** When an agent executes automated actions, an optional subtle purple or amber border illuminates the window perimeter, ensuring you always know when automation is running.
