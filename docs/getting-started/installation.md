# Installation & System Requirements

This guide outlines system requirements and step-by-step instructions for installing **Nova AI Workspace** on Windows.

Deutsch: [weiter unten](#nova-ai-workspace-installieren).

---

## 1. System Requirements

Nova AI Workspace is built natively for 64-bit Windows environments.

| Component | Minimum Requirement | Recommended |
| :--- | :--- | :--- |
| **Operating System** | Windows 10 (version 1809 / build 17763 or newer) | Windows 11 (23H2 or newer) |
| **Architecture** | 64-bit (x64) | 64-bit (x64) |
| **Processor** | 2-core x64 CPU | 4-core+ modern x64 CPU |
| **Memory (RAM)** | 4 GB RAM | 8 GB+ RAM (especially for multi-sandbox workflows) |
| **Disk Space** | 500 MB free space | 2 GB+ (for local Whisper models, caches, recordings) |
| **Microsoft Edge WebView2 Runtime** | Required | Usually already part of Windows 10/11; the setup installs it if it is missing |

You do not need to install .NET: Nova ships with its own runtime. The setup also installs the
Microsoft Visual C++ runtime if it is missing.

---

## 2. Download and Install

1. Open the [release list](https://github.com/joelaniol/nova/releases) and download the setup
   file ending in `-Setup-<version>.exe`, for example `NovaAIWorkspace-Setup-1.0.0-alpha.18.exe`.
   Older releases still carry the previous product name, `NovaBrowser-Setup-…`.
   Choose the setup under **Assets**. The `.mcpb` file is an MCP bridge bundle for compatible clients, and `.sha256` contains a checksum; neither installs Nova.
2. Run the setup. It asks for administrator rights because it installs for all users into
   `C:\Program Files\Nova AI Workspace`.
3. Follow the wizard. It creates a Start menu entry and, if you tick the box, a desktop shortcut.
   If WebView2 is missing, the setup downloads and installs it.

> [!TIP]
> **No internet on the target machine?** Some releases also offer a larger file ending in
> `-offline.exe`. It contains the WebView2 runtime, so the setup does not need to download anything.

Once installed, Nova checks for new versions by itself and offers the update.

> [!NOTE]
> **Windows SmartScreen.** Alpha builds are signed with a certificate Windows does not know yet, so
> SmartScreen may show *"Windows protected your PC"* and *"Unknown publisher"*. Click
> **More info** → **Run anyway** to continue.

---

## 3. What Gets Installed

```
Nova AI Workspace/
├── NovaAIWorkspace.exe            # Main application (window, browser tabs, local MCP server)
├── NovaBrowser.Outrider.exe       # Helper process for hardware and audio work
└── tools/
    └── NovaBrowser.McpProxy.exe   # Bridge for AI programs that talk to Nova over stdio
```

> [!IMPORTANT]
> Keep these files where the setup put them. Nova starts `NovaBrowser.Outrider.exe` from its own
> folder for risky native work (hardware diagnostics, local Whisper transcription, audio capture);
> if it is missing, those features stay off. Nova copies `tools\NovaBrowser.McpProxy.exe` into your
> profile folder (`%LOCALAPPDATA%\nova-cognitive\Nova\bin\`) and registers that copy with your AI
> programs, so updates never break their configuration.

---

## 4. Check That It Works

For the simplest first-use check, follow [Quickstart](quickstart.md). The server health check below is optional diagnostic detail.

1. **Start Nova** from the Start menu. The main window opens with a first tab.
2. **Check the MCP server.** While Nova is running, it listens for AI programs on
   `127.0.0.1`, port `27183` by default (you can change it in the settings under **Local port**). In
   PowerShell:
   ```powershell
   Invoke-RestMethod http://127.0.0.1:27183/health
   ```
   `status : ready` means the server is up.
3. **Connect your AI program** with the connection wizard; see
   [Settings & connection wizard](../user-guide/settings-and-connection-wizard.md) and the
   [integration guides](../integration/README.md).

---

## 5. Security Notes

* **Local only by default:** The MCP server binds to `127.0.0.1` and does not accept connections
  from other machines unless you explicitly allow remote clients in the settings.
* **Token-protected:** AI programs need Nova's access token, which the connection wizard sets up for
  you.

---

## Next Step

Continue with **[Quickstart](quickstart.md)** to connect your AI program and try your first task. For a short tour of the window and how to stop an agent, see [First run](first-run.md).

---

# Nova AI Workspace installieren

## Voraussetzungen

- Windows 10 ab Version 1809 oder Windows 11, 64 Bit (x64)
- mindestens 4 GB Arbeitsspeicher und 500 MB freier Speicherplatz; für lokale Spracherkennung,
  Aufnahmen und mehrere Sandboxes eher 8 GB und 2 GB
- Microsoft-Edge-WebView2-Laufzeit: ist bei Windows 10/11 meist schon da, sonst installiert sie
  das Setup mit

.NET musst du nicht installieren, Nova bringt seine Laufzeit selbst mit.

## Installation

1. Unter [Releases](https://github.com/joelaniol/nova/releases) die Datei herunterladen, die auf
   `-Setup-<version>.exe` endet, z. B. `NovaAIWorkspace-Setup-1.0.0-alpha.18.exe`. Ältere
   Versionen heißen noch `NovaBrowser-Setup-…`. Wähle das Setup unter **Assets**:
   `.mcpb` ist ein MCP-Verbindungspaket für kompatible Programme, `.sha256` eine Prüfsumme.
   Beide ersetzen das Setup nicht.
2. Setup starten. Es fragt nach Administratorrechten, weil es für alle Nutzer nach
   `C:\Program Files\Nova AI Workspace` installiert.
3. Dem Assistenten folgen. Er legt einen Startmenü-Eintrag an und auf Wunsch eine
   Desktop-Verknüpfung. Fehlt WebView2, lädt das Setup es nach.

Kein Internet auf dem Zielrechner? Manche Releases bieten zusätzlich eine größere Datei mit der
Endung `-offline.exe`, die WebView2 bereits enthält.

Meldet Windows SmartScreen „Der Computer wurde durch Windows geschützt“ bzw. „Unbekannter
Herausgeber“: auf **Weitere Informationen** → **Trotzdem ausführen** klicken. Das liegt am
Signaturzertifikat der Alpha-Versionen, das Windows noch nicht kennt.

Nach der Installation sucht Nova selbst nach neuen Versionen und bietet das Update an.

## Prüfen, ob alles läuft

1. Nova über das Startmenü starten.
2. In PowerShell prüfen, ob Nova für KI-Programme erreichbar ist:
   ```powershell
   Invoke-RestMethod http://127.0.0.1:27183/health
   ```
   `status : ready` heißt: läuft. (27183 ist der Standard-Port; ändern lässt er sich in den
   Einstellungen unter **Lokaler Port**.)
3. KI-Programm mit dem Verbindungsassistenten anbinden: [Integration](../integration/README.md).

Weiter geht es mit dem [ersten Start](first-run.md).
