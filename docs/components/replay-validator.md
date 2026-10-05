# ReplayValidator — Recording Validation Tool

**Executable:** `NovaBrowser.ReplayValidator.exe`.

ReplayValidator is a headless diagnostic CLI for session-recording artifacts. Its current `--analyze` command reads and checks the unencrypted manifest and inventories the available JSONL sidecars. It does not decrypt and fully replay the encrypted recording streams.

## When It Runs

It runs when explicitly invoked for validation, rather than as an always-on browser service. Its commands include analysing a recording directory, listing fixtures and running a named fixture. It prints a report and exits; JSON, JUnit and SARIF report formats are supported.

## Why It Is Separate

Recording analysis can run independently of the interactive browser. The current CLI remains a limited validation surface: declared fixtures can report `skipped` with a warning, and an exit code of zero alone is not proof that replay occurred. Inspect the checks and warnings as well as the exit status.

Manifest validation does not establish that a server-side action succeeded or that every event was captured. It also does not restore the website's old live state.

## Learn More

* [Session recording](../core-features/session-recording.md)
* [Visual evidence](../core-features/evm-and-visual-evidence.md)
* [All components](README.md)
