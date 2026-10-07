# ReplayValidator — Recording Validation Tool

**Executable:** `NovaBrowser.ReplayValidator.exe`.

ReplayValidator is a headless diagnostic CLI for session-recording artifacts. Its current `--analyze` command reads and checks the unencrypted manifest and inventories the available JSONL sidecars. It does not decrypt and fully replay the encrypted recording streams.

## When It Runs

It runs when explicitly invoked for validation, rather than as an always-on browser service. Its commands include analysing a recording directory, listing fixtures and running a named fixture. It prints a report and exits; JSON, JUnit and SARIF report formats are supported.

## Why It Is Separate

Recording analysis can run independently of the interactive browser. The current CLI remains a limited validation surface: declared fixtures can report `skipped` with a warning, and an exit code of zero alone is not proof that replay occurred. Inspect the checks and warnings as well as the exit status.

Manifest validation does not establish that a server-side action succeeded or that every event was captured. It also does not restore the website's old live state.

## Checks Available Today

The recording-directory analysis checks that the directory and `manifest.json` exist, that the manifest parses and contains a recording identifier, and that its schema version is positive and supported. It then lists the JSONL sidecars present in that directory.

This is a manifest and artifact-inventory check. It does not parse every sidecar's event body, require a sidecar to exist, decrypt recorded streams, reconstruct a page or compare the recorded result with a live website. An empty sidecar inventory can therefore pass the current analysis.

## Commands and Reports

Run the tool from the installation directory, using a recording directory you intend to inspect:

```powershell
.\NovaBrowser.ReplayValidator.exe --analyze "<recording-directory>" --format json
.\NovaBrowser.ReplayValidator.exe --list-fixtures
.\NovaBrowser.ReplayValidator.exe --run-fixture "<category>/<name>" --format junit
```

Replace the angle-bracket placeholders with actual values. `--list-fixtures` supplies the declared fixture names. The format option accepts `json`, `junit` or `sarif`; JSON is the default. Reports describe individual checks, their status and warnings, allowing a diagnostic workflow to distinguish unsupported input from an actual failed check.

| Exit code | Meaning |
| :--- | :--- |
| `0` | The current command's checks passed; inspect warnings and skipped checks. |
| `2` | Validation failed. |
| `3` | Invalid recording input, such as a missing or malformed manifest. |
| `4` | Unsupported manifest schema. |
| `64` | Invalid command usage. |

## How to Interpret a Result

For example, a directory with a readable supported manifest can receive a passing analysis even when no JSONL files are present. The useful conclusion is that the manifest passed the implemented checks and the sidecars were inventoried. It is not evidence that a replay succeeded.

The fixture command currently includes declared cases that return skipped checks with warnings. Report formats make those outcomes machine-readable; they do not extend the implemented validation coverage. Use [session recording](../core-features/session-recording/README.md) for capture behaviour and [visual evidence](../core-features/evidence-verification-mode-evm/README.md) for outcome verification.

## Learn More

* [Session recording](../core-features/session-recording/README.md)
* [Visual evidence](../core-features/evidence-verification-mode-evm/README.md)
* [All components](README.md)
