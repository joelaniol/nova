# Audio & Video Transcription (Whisper)

> [!NOTE]
> Nova AI Workspace includes a built-in, fully offline speech-to-text engine powered by [Whisper](https://github.com/ggerganov/whisper.cpp). All audio processing and model inference run locally on your Windows computer inside Nova's sandboxed helper process (`NovaBrowser.Outrider.exe`). No audio files, recordings, or transcripts are ever transmitted to external cloud services or third-party APIs.

---

## 1. Overview & Capabilities

Whether you are capturing meeting notes, transcribing lecture recordings, generating subtitles for video files, or allowing AI agents to understand voice messages, Nova's transcription tool provides high-accuracy local transcription directly in the workspace.

* **100% Offline & Private:** Models run locally using CPU or GPU hardware acceleration.
* **Broad Media Format Support:** Transcribes MP3, WAV, M4A, AAC, OGG, FLAC, MP4, MKV, and WebM files.
* **Multi-Language Detection:** Automatic language identification or manual selection across dozens of spoken languages (German, English, Spanish, French, Japanese, etc.).
* **Multiple Export Formats:** Export completed transcripts as plain text (`.txt`), standard subtitle files (`.srt`), or web video subtitles (`.vtt`).
* **Human-Agent Parity:** Both you and your connected AI agents can initiate and inspect transcriptions using the same underlying engine.

---

## 2. Opening the Transcription Window

You can open the Transcription tool in several ways:

1. **Toolbar Button:** Click the **Transcription** button (`[CC]` icon) in the main window toolbar.
2. **Main Menu:** Select **Menu → Tools → Transcription**.
3. **Settings Navigation:** Open **Menu → Settings → Media & transcription**, and click **Open transcription window**.

```
+-----------------------------------------------------------------------------------+
|  [CC] Transcription                                                       [_][O][X]|
+-----------------------------------------------------------------------------------+
|  +-----------------------------------------------------------------------------+  |
|  |                [Drop audio or video files here to transcribe]               |  |
|  |                             [ Choose file... ]                              |  |
|  +-----------------------------------------------------------------------------+  |
|                                                                                   |
|  Spoken language: [ Automatic detection    v ]   Speech model: [ base       v ]   |
|                                                  [More models...] [ Transcribe ]  |
|                                                                                   |
|  [==========================              ] Transcribing... 01:15 of 03:40 (ETA 1m) |
|                                                                                   |
|  +-----------------------------------------------------------------------------+  |
|  | [00:00:04] Welcome to today's project review meeting.                       |  |
|  | [00:00:12] We will start by reviewing the latest release milestones...     |  |
|  +-----------------------------------------------------------------------------+  |
|                                                                                   |
|  [X] Show timestamps                   [ Copy ]  [ Save as v: .txt | .srt | .vtt ]|
+-----------------------------------------------------------------------------------+
```

---

## 3. Step-by-Step Transcription Workflow

### Step 1: Choose or Drop Media
* **Drag and Drop:** Drag any supported audio or video file from Windows File Explorer and drop it directly onto the large upload area.
* **File Picker:** Click **Choose file…** to browse and select a file from disk.
* Once a file is selected, the drop zone collapses into a compact row showing the file name, duration, and format. To select a different file, click **Start over**.

### Step 2: Configure Language & Speech Model
* **Spoken Language:**
  * Leave set to **Automatic detection** if the spoken language is unknown or mixed.
  * Alternatively, select the specific language (e.g. *German*, *English*) to improve accuracy and speed up initial recognition.
* **Speech Model:**
  * Select an installed local Whisper model from the dropdown:
    * **`tiny` / `tiny.en` (~75 MB):** Fastest execution, minimal RAM usage, ideal for quick dictation or low-power laptops.
    * **`base` / `base.en` (~142 MB):** Recommended default; balanced speed and solid accuracy for everyday audio.
    * **`small` (~466 MB):** Higher accuracy for technical jargon, accents, or background noise.
    * **`medium` (~1.5 GB):** Maximum accuracy for challenging recordings and complex multi-speaker audio.
  * If a model is not yet installed, click the **More models…** link to open Settings and download it with one click.

### Step 3: Run the Transcription
* Click the primary **Transcribe** button.
* Nova launches `NovaBrowser.Outrider.exe` to decode audio and run model inference.
* The progress bar displays elapsed time, total audio length, and estimated completion time (e.g. *"Transcribing… 00:45 of 02:30, about 00:30 left"*).
* Live recognized text segments stream directly into the transcript viewer in real time.
* **Need to stop early?** The button turns into **Cancel** while running. If canceled, all text transcribed up to that point is preserved in the viewer.

---

## 4. Working with the Transcript

Once processing completes (or while reviewing in progress):

* **Inline Timestamps:** Check the **Show timestamps** box to display segment time offsets (e.g. `[00:01:23]`) before each paragraph. Unchecking the box immediately switches the view back to clean, continuous prose.
* **Text Selection:** Click and drag to highlight any portion of the transcript, or press `Ctrl+A` inside the box to select everything.
* **Copy to Clipboard:** Click **Copy** to copy the full transcript text directly into your Windows clipboard.
* **Save as File:** Click **Save as** to export the result in your desired format:
  * **Text (`.txt`):** Plain text transcript without formatting codes.
  * **Subtitles (`.srt`):** Standard SubRip subtitle format with sequential numbering and millisecond timecodes, compatible with VLC, Premiere, and video players.
  * **Web Subtitles (`.vtt`):** WebVTT format for HTML5 video players and online media hosting.

---

## 5. Model Management & Settings

Open **Menu → Settings → Media & transcription** to manage offline models:

* **Download Models:** Click **Download** next to any model variant (`tiny`, `base`, `small`, `medium`). Downloads are verified via SHA-256 checksums and saved to `%LOCALAPPDATA%\NovaBrowser\models\`.
* **Remove Models:** Click **Remove** to free disk space when a large model is no longer needed.
* **Hardware Acceleration:** Outrider automatically detects CPU instruction sets (AVX2, AVX512, FMA) to optimize local inference performance.

---

## 6. AI Agent Integration

Connected AI coding agents (such as Claude Code, Codex, or Antigravity) can interact with Nova's transcription engine programmatically through MCP tools:

* [`nova.media_transcribe_start`](../../mcp-reference/tools/media-and-transcription/nova-media-transcribe-start.md): Launches a background transcription job on a local file.
* [`nova.media_transcribe_status`](../../mcp-reference/tools/media-and-transcription/nova-media-transcribe-status.md): Polls progress, status, and retrieves completed text segments.
* [`nova.media_transcribe_models`](../../mcp-reference/tools/media-and-transcription/nova-media-transcribe-models.md): Inspects installed models and installs missing variants.

When an agent transcribes media, the same safety guarantees apply: inference remains 100% local, and execution runs strictly inside the Outrider sandbox.

---

## Related Documentation

* **[Core Features: Media Intelligence](../../core-features/media-intelligence/README.md)** — Architectural deep-dive into Outrider, audio extraction, and crash isolation.
* **[Tools Overview](README.md)** — Other built-in tools including the Terminal Dock, Recordings, and Scheduled Tasks.
* **[Settings Guide](../settings/README.md)** — Managing workspace preferences and model downloads.
