# Try Nova: Interactive Browser Demo

[Deutsche Anleitung](README.de.md)

Explore eight everyday browser tasks with Nova and your connected AI agent. Sign in, find an item in a long list, move a card, work with files and read information from a page. Each section lets you see the result directly.

Updated: 2026-10-05

## Get Started

1. Download this repository using **Code → Download ZIP**, then extract it. Keep the `demos` folder and its `assets` subfolder together.
2. Open the downloaded `demos/lab.html` in Nova. The demo runs locally and needs no web server.
3. Connect your agent using the [integration guide](../docs/integration/README.md), then give it one of the tasks below. You can also explore the controls yourself.

GitHub displays the HTML source; download the files to use the interactive page. The page itself makes no external network requests. Your connected agent uses its own configured service.

## Start with This Task

> Sign in with username **demo** and password **nova**. Find Build 8472 in the long list, then move the “Deploy release” card to Done. Tell me what changed on the page.

Look for the signed-in status, the highlighted build and the card in the Done column. Reload the page in the same browser profile to check whether the demo sign-in remains available.

This is a simulated sign-in stored locally, not a real account. Use the supplied demo credentials.

## Eight Things to Try

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
