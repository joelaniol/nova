# `nova.screen_record_inspect`

> **Reads the evidence of a finished screen recording: summary, timeline, contact sheet and pictures.**

* **Core Feature Guide:** [Visual Evidence & Auditing](../../../research/evidence-verification-mode-evm/README.md)
* **Master Catalog:** [MCP Tool Catalog](../../tool-catalog.md)

---

## 1. Overview

> [!NOTE]
> **Upcoming.** This tool arrives with a coming release, which is not published yet.

Every recording made with [`nova.screen_record_start`](nova-screen-record-start.md) leaves an evidence folder next to the video (`<name>.evidence`): a timeline, lossless pictures, a contact sheet and a manifest with the video's SHA-256 and its self-check. `nova.screen_record_inspect` reads it, so an agent can check what a recording shows - or what another agent claims it shows - without decoding the video.

* `view="summary"` (default): whether the video is verified, how many marks, tool calls and observed changes the timeline holds, and the pictures.
* `view="timeline"`: the entries on the video's time axis - your marks ([`nova.screen_record_mark`](nova-screen-record-mark.md)), every MCP tool call (name, call id, started/completed/failed, duration; never arguments or results) and the changes Nova observed in the picture (start, strongest change, end, area, a picture before and after). Filter with `kinds`, `fromMs`, `toMs` and `limit`.
* `view="contact_sheet"`: one image with all evidence pictures and their times.
* `view="image"`: one picture named in the timeline.

Observed changes show what happened at the same time, not what caused it; a flicker shorter than about a tenth of a second can be missed.

By default the tool reads your most recent recording; `filePath` names another one (the video or its `.evidence` folder). Recordings outside Nova's Exports folder need the user's "Allow local files" setting; another agent's evidence is refused (`video.not_owner`).

---

## 2. Parameter Reference

<!-- generated:parameters (from the live tool catalog; do not edit by hand, regenerate with NOVA_UPDATE_PUBLIC_TOOL_DOCS=1) -->
| Parameter | Type | Required | Default | Allowed | Description |
| :--- | :--- | :---: | :--- | :--- | :--- |
| `filePath` | `string` | No | — | — | The recording (absolute path of the video or of its .evidence folder). Omit for your most recent recording. |
| `view` | `string` | No | `"summary"` | `summary`, `timeline`, `contact_sheet`, `image` | What to return. |
| `kinds` | `array` of `string` | No | — | — | view=timeline: only these kinds. |
| `fromMs` | `integer` | No | — | ≥ 0 | view=timeline: entries from this video time on. |
| `toMs` | `integer` | No | — | ≥ 0 | view=timeline: entries up to this video time. |
| `limit` | `integer` | No | `100` | 1–500 | view=timeline: at most this many entries. |
| `image` | `string` | No | — | — | view=image: a picture path from the timeline, e.g. evidence/mark-000.png. |
| `agentId` | `string` | No | — | — | The agentId you recorded with. |

Capability bundle: `visual_evidence` (load it with `nova.tools_bundle(bundle='visual_evidence')`).
Tool category: `normal` (standard risk class in Nova's agent permission settings).
<!-- /generated:parameters -->

---

## 3. Protocol Usage

### JSON-RPC Request
```json
{
  "name": "nova.screen_record_inspect",
  "arguments": {
    "view": "timeline",
    "kinds": ["mark", "change"],
    "limit": 50
  }
}
```

### JSON-RPC Response
```json
{
  "content": [
    {
      "type": "text",
      "text": "Evidence timeline retrieved: 6 marks, 4 UI change events."
    }
  ],
  "structuredContent": {
    "ok": true,
    "status": "ok",
    "view": "timeline",
    "totalEntries": 10,
    "entries": [
      {
        "timeMs": 0,
        "kind": "mark",
        "label": "initial page state",
        "role": "task"
      },
      {
        "timeMs": 1420,
        "kind": "change",
        "description": "table container hydrated"
      },
      {
        "timeMs": 3500,
        "kind": "mark",
        "label": "checkout button clicked",
        "role": "step"
      }
    ]
  }
}
```

---

## 4. Operational Best Practices

* **Audit Without Video Decoding:** Use `view: "summary"` to verify SHA-256 integrity and timeline marker counts without spending CPU cycles decoding the MP4 container.
* **Filter High-Frequency Events:** When analyzing long automation sessions with thousands of interaction events, set `kinds: ["mark"]` and specify `fromMs` / `toMs` windows to focus on specific verification phases.
* **Contact Sheet Extraction:** Use `view: "contact_sheet"` to produce an immediate visual collage of all milestone frames for PR reviews or customer documentation.

---

## 5. Related Tools

* [`nova.screen_record_start`](nova-screen-record-start.md) — Starts screen recording sessions.
* [`nova.screen_record_stop`](nova-screen-record-stop.md) — Stops active recording and yields verified video.
* [`nova.screen_record_mark`](nova-screen-record-mark.md) — Adds markers and checkpoints to the recording timeline.
* [`nova.screen_record_assert`](nova-screen-record-assert.md) — Asserts visual properties against timeline checkpoints.
* [`nova.video_render`](../video-editing/nova-video-render.md) — Renders the recording and contact sheet into styled clips.
