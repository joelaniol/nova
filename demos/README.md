# Try Nova: The Experience Loop

[Deutsche Anleitung](README.de.md)

Nova can carry verified experience from one visit into the next. This demo gives that idea a concrete test: a recurring notice, a changed interface, a save request with no saved result, and a step that belongs to you.

Updated: 2026-10-05

## Get Started

1. Download this repository using **Code → Download ZIP**, then extract it. Keep the `demos` folder and its `assets` subfolder together.
2. For persistent website knowledge, serve the demo on a **local HTTP address**. If Python is installed, run this from the extracted repository folder:

   ```sh
   python -m http.server 8765 --bind 127.0.0.1 --directory demos
   ```

3. Open `http://127.0.0.1:8765/lab.html` in Nova and connect your agent using the [integration guide](../docs/integration/README.md). Keep the same address and port for return visits. Stop the local server with Ctrl+C when finished.

Opening `demos/lab.html` directly also works for page interactions, but `file://` does not provide the website scope needed for this persistent-knowledge exercise. GitHub displays HTML source, so download the files first. The page makes no external network requests; your agent uses its configured service.

## One Task, Three Visits

### 1. Encounter: check the result, then keep the experience

Select **First visit** and ask:

> Clear the release notice and save the sample draft. Check the actual saved result rather than treating a successful click as completion. Ask me to confirm when needed; leave the confirmation control to me. After verifying that the notice is gone and the draft is usable, store the notice-handling experience in Nova. Use the observed dismissal control as a recognition signal. Show me what was stored and its current learning level.

The first save request deliberately leaves **Saved drafts** at **0**, even if you confirmed early. Your agent should notice that difference, request your confirmation, and continue with a checked save. Use **I confirm this demo draft** yourself when asked. Completion has a visible receipt and **Saved drafts: 1**.

The reusable experience concerns the notice: how to recognize it, dismiss it and verify that the draft becomes available. Your confirmation is not part of that recipe. The confirmation control is a handoff exercise, not an identity or permission security boundary.

### 2. Return: retrieve, do not just remember the conversation

Select **Return visit**. For a clearer demonstration, start a fresh conversation with the same Nova instance and browser profile:

> Retrieve Nova's stored experience for the release notice on this address. Show its ID and current learning level. Check whether it still applies, use it within its current trust limits, and verify that the notice is gone. Save the draft again, leaving confirmation to me.

A fresh conversation separates persistent Nova knowledge from the previous chat's context. A single successful encounter does **not** imply an active autonomous playbook. New knowledge may remain Shadow: retrievable, but still requiring deliberate checking and normal guarded actions. Active application is only appropriate if Nova actually reports that it is eligible. Do not force promotion for the demo.

### 3. Change: let the evidence challenge the recipe

Select **Site changed** and ask:

> Revalidate the stored notice recipe against the current page before using it. Show the result from Nova. If it no longer fits, inspect the changed interface, resolve the notice safely and verify the outcome. Explain what changed and what happened to the stored knowledge. Do not claim automatic recovery or demotion unless Nova reports it.

The dismissal control now has a different selector and label. Check the stored action's target as well as its recognition signals: a broad fingerprint can still match part of the page while its action is no longer usable. Look for the actual revalidation result and any reported health or trust change, followed by a checked recovery. The page changes the website; it does not alter Nova's knowledge itself.

## What Makes This a Nova Demonstration?

The individual clicks, form fields and simulated failures can also be automated with tools such as Playwright. The demonstration concerns the **integrated workflow**: procedural knowledge persists outside the conversation, has an explicit trust state, can be checked against a changed page, and is applied alongside outcome verification and a user handoff.

Ask the agent to show actual Nova responses for stored knowledge, revalidation and execution verification. Page counters and **Page activity** describe the sample website only. They cannot prove that Nova learned anything. If learning is unavailable or disabled, say so; the page remains an interaction exercise, but the learning demonstration is incomplete.

Compare the first and return visits using actual action evidence if you want to assess reuse. This fixture is not a benchmark and does not promise fewer calls or tokens. It does not simulate real authentication, cross-origin access or external publishing.

## More Browser Exercises

| Section | Ask your agent | What you can check |
| :--- | :--- | :--- |
| **Session** | “Sign in, reload the page and check whether I am still signed in.” | The sign-in status after reloading; the linked second page also displays the locally stored state. |
| **Long list** | “Find Build 8472.” | The highlighted build in a list of 10,000 items that renders only the nearby rows. |
| **Embedded controls** | “Press the nested button, then enter DEMO-123 in the embedded ticket form and submit it.” | A button confirmation and the submitted ticket in the embedded form. |
| **Drag and drop** | “Move ‘Deploy release’ to Done.” | The card's new column and its status below the board. No release is deployed. |
| **Files** | “Choose the sample file I provide, then download the report.” | The chosen file's name and size on the page; the CSV in Nova's downloads. |
| **Dialogs** | “Show the cookie banner and reject optional cookies. Then open the sample modal and close it without saving.” | The recorded demo cookie choice and modal status. JavaScript dialog examples are also available. |
| **Waiting** | “Start the delayed button and press it when it appears. Then load the value and report the final result.” | The button's pressed state and a value that replaces an initial placeholder. |
| **Reading data** | “Summarize the sample table and read the code drawn in the image.” | Structured table values and the code visible on the canvas. The table is fictional demo data. |

Choose a section before trying its task. You do not need to know tool names or selectors to describe the desired result to your agent.

## Understand the Results

The **Page activity** panel records events handled by this demo, such as a submitted form or a moved card. Use it alongside the visible result. It is a page-local activity list, not Nova's full action log or independent proof that an external task succeeded.

The examples are deliberately small and self-contained. They demonstrate interaction patterns rather than a performance benchmark or a guarantee that every website behaves the same way. Embedded forms use a local frame; the page does not demonstrate cross-origin access, real authentication, external uploads or network interception.

The simulated cookie banner records a demo choice. Choosing a file reads its name and size without uploading it. The download creates a CSV from the fictional table. Session persistence depends on the browser profile and available local storage; signing out clears the demo sign-in.

## Try Again

Use **Sign out**, **Back to top** or **Clear activity** for the relevant section. Reloading resets most page interactions, while the demo sign-in and last selected section can remain stored. Delayed content takes a few seconds to appear.

## Learn More

* [Get Nova](../README.md)
* [Connect an agent](../docs/integration/README.md)
* [Explore core features](../docs/core-features/README.md)
