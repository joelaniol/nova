# Scheduled Tasks & Background Automation

> [!NOTE]
> Nova AI Workspace includes an enterprise-grade **Background Automation Engine** backed by local SQLite storage (`scheduled-tasks.db`). It allows AI coding agents (Claude Code, Codex CLI), PowerShell scripts, system binaries, and HTTP webhooks to execute on automated schedules, fixed intervals, or filesystem directory changes—even when browser windows are minimized or idle.

---

## 1. Overview & Key Capabilities

Traditional terminal loops (`while true; do ... sleep 300; done`) break whenever a terminal window is closed, lose history on reboot, cannot wake up gracefully after laptop sleep, and risk exposing plain-text API keys in shell scripts.

Nova's Scheduled Tasks engine provides a robust desktop automation platform:

* **Flexible Triggers:** Execute tasks on standard **Cron schedules** (e.g. every weekday at 09:00), **Fixed intervals** (e.g. every 15 minutes), or **Directory watch** triggers (when files are created or modified in a workspace).
* **Multi-Executor Support:** Run autonomous AI coding agents (**Claude Code**, **Codex CLI**), Windows **PowerShell** (`pwsh`), native executables, or HTTP REST webhooks.
* **Isolated Workspaces:** Each task operates within an isolated terminal workspace folder (`shared/`, `inbox/`, `outbox/`) preventing unintended file system side effects.
* **Encrypted Secrets:** Inject API tokens, database passwords, and credentials safely via the **Windows Data Protection API (DPAPI)**—no credentials stored in plaintext.
* **Circuit Breakers & Catch-Up:** Automatic catch-up window (up to 24 hours) after Windows wakes from sleep; circuit breakers automatically pause failing tasks to prevent token waste.

```
+-----------------------------------------------------------------------------------+
|  Scheduled Tasks                                                         [_][O][X]|
+-----------------------------------------------------------------------------------+
|  TASKS                    |  TASK CONFIGURATION: "Morning Site Health Check"      |
|  +---------------------+  |  --------------------------------------------------   |
|  | [v] Morning Health  |  |  Enabled: [X] Yes                                     |
|  |     Cron: 0 9 * * * |  |  Trigger:  [ Cron Expression             v ]          |
|  |     Status: OK (2m) |  |  Schedule: [ 0 9 * * 1-5                   ]          |
|  |---------------------|  |  Human:    "At 09:00 AM, Monday through Friday"       |
|  | [v] Price Scraper   |  |                                                       |
|  |     Every 30 min    |  |  Executor: [ Claude Code CLI (Safe Mode) v ]          |
|  |     Status: OK (14s)|  |  Prompt / Command:                                    |
|  |---------------------|  |  [ Check production API endpoints and alert on errors ]|
|  | [!] Backup Sync     |  |                                                       |
|  |     Status: Failed  |  |  Concurrency: [ Skip if already running   v ]          |
|  +---------------------+  |  Workspace:   [ prod-monitoring           v ]          |
|  [ + New Task ]           |                                                       |
|                           |  ACTIONS: [ Run Now ]  [ Save Changes ]  [ View Logs ]|
+-----------------------------------------------------------------------------------+
```

---

## 2. Accessing the Scheduled Tasks Manager

Open the Scheduled Tasks interface through:

1. **Main Menu:** Select **Menu → Scheduled tasks**.
2. **Toolbar Status Area:** Click the **Scheduled Tasks** status icon when background tasks are active.
3. **Settings Navigation:** Open **Menu → Settings → AI & agents → Scheduled tasks**.

---

## 3. Creating and Configuring a Task

Click **New Task** to open the task editor. A task consists of the following settings:

### 1. General Information
* **Task Name:** A descriptive label (e.g., *"Daily Competitor Pricing Monitor"*).
* **Description:** Optional notes explaining the goal and dependencies of the task.
* **Enabled Toggle:** Turn the schedule on or off without deleting the task definition.

### 2. Triggers & Schedules
* **Cron Expression:** Standard 5-field cron syntax (`minute hour day-of-month month day-of-week`). Nova renders a real-time, human-readable translation directly underneath the input box (e.g. `*/30 * * * *` translates to *"Every 30 minutes"*).
* **Fixed Interval:** Specify execution every $N$ seconds, minutes, or hours (e.g., *"Every 4 hours"*).
* **Directory Watch:** Automatically triggers when files are added, modified, or deleted within a watched workspace directory.

### 3. Choosing the Executor
Select how the task should run:

| Executor | Best For | Execution Context |
| :--- | :--- | :--- |
| **Claude Code CLI** | Multi-step agentic coding, repository analysis, web audits | Runs `claude` in an isolated terminal workspace; supports Safe Mode or Auto-Approve. |
| **Codex CLI** | Autonomous tasks using OpenAI models | Runs headless Codex agent sessions. |
| **PowerShell (`pwsh`)** | Local Windows administration, system maintenance, file processing | Native PowerShell script execution with full error trap logging. |
| **Custom Command** | Running Python scripts, Node.js jobs, or compiled binaries | Direct command-line invocation with arguments and working directory. |
| **HTTP Webhook** | Triggering external CI/CD pipelines, webhooks, or cloud services | Dispatches HTTP GET/POST requests with custom headers and payloads. |

### 4. Workspace & File Isolation
Every task can be bound to a dedicated **Terminal Workspace** located under `%LOCALAPPDATA%\NovaBrowser\workspaces\{workspace_id}\`:
* **`inbox/`**: Place input data files, URLs, or parameter manifests here for the task to process.
* **`outbox/`**: The task writes reports, exported CSVs, and artifacts here.
* **Shared root**: Preserves repository clones and cached data across runs.

### 5. Encrypted Secrets & Environment Variables
Never hardcode API keys or passwords in scripts:
* Add secrets in the **Secrets & Variables** tab.
* Secrets are encrypted with the Windows DPAPI for your local user account.
* During execution, secrets are injected as secure environment variables (e.g., `NOVA_TASK_SECRET_API_KEY`) accessible only to the running process and wiped immediately upon exit.

### 6. Concurrency & Catch-Up Policies
* **Overlap Policy:**
  * *Skip (Default):* If a previous run is still executing when the next schedule fires, the new run is safely skipped.
  * *Replace:* Terminates the existing run and begins a fresh execution.
* **Catch-Up Window:** If your computer was asleep or powered off when a scheduled run was due, Nova can automatically trigger a catch-up run within a 24-hour window upon system wake.

---

## 4. Monitoring Runs, Logs & Circuit Breakers

### Inspecting Run History
The bottom panel of the task editor maintains a comprehensive execution ledger:
* **Status Badges:** `Success` (green), `Failed` (red), `Running` (blue), or `Skipped` (gray).
* **Timing & Metrics:** Start time, duration, and AI token counts / estimated costs (for Claude and Codex runs).
* **Output Logs:** Click any past run to inspect `stdout.log` and `stderr.log` in real time.

### Manual Execution ("Run Now")
To test a newly configured task or force an immediate update outside its normal schedule, click the **Run Now** button. The task executes immediately, streaming output to the log viewer.

### Circuit Breakers (Runaway Prevention)
To protect your API budgets and prevent error loops, Nova includes an automatic **Circuit Breaker**:
* If a task fails repeatedly (default: 5 consecutive failures), the scheduler automatically transitions the task to the `CircuitBreaker` state.
* The task is paused until you inspect the error logs, fix the underlying issue, and click **Reset Circuit Breaker**.

---

## 5. Background Execution & System Tray

By default, scheduled tasks execute whenever Nova AI Workspace is open. To ensure background automations continue running even after closing the main browser window:

1. Open **Menu → Settings → General**.
2. Enable **Keep running in the background when window is closed**.
3. When closing Nova, the browser minimizes to the Windows System Tray (notification area), maintaining background timers, file watches, and scheduled tasks without cluttering your desktop.

---

## 6. AI Agent Integration

Connected AI agents can manage scheduled tasks autonomously via Nova's MCP tool suite:

* [`nova.scheduled_task_create`](../../mcp-reference/tools/scheduled-tasks/nova-scheduled-task-create.md): Programs a new scheduled task definition.
* [`nova.scheduled_task_list`](../../mcp-reference/tools/scheduled-tasks/nova-scheduled-task-list.md): Lists active background automations and next run times.
* [`nova.scheduled_task_trigger`](../../mcp-reference/tools/scheduled-tasks/nova-scheduled-task-trigger.md): Manually fires a task execution.
* [`nova.scheduled_task_run_output`](../../mcp-reference/tools/scheduled-tasks/nova-scheduled-task-run-output.md): Retrieves console output and execution logs.
* [`nova.scheduled_task_secret_set`](../../mcp-reference/tools/scheduled-tasks/nova-scheduled-task-secret-set.md): Securely provisions DPAPI credentials for a task.

---

## Related Documentation

* **[Core Features: Scheduled Tasks & Background Automation Engine](../../core-features/scheduled-tasks/README.md)** — Architectural design, database schema, and scheduler tick lifecycle.
* **[Tools Overview](README.md)** — Other workspace utilities including the Terminal Dock and Audio Transcription.
* **[Terminal Workspaces](../../core-features/terminal-workspaces/README.md)** — In-depth guide to ConPTY terminal workspaces and storage isolation.
