# Running Tests & Quality Gates

> [!NOTE]
> Nova AI Workspace enforces a rigorous testing regimen: unit tests, smoke tests, profile-isolated self-tests, and static code scans.

---

## 1. Test Profile Isolation (Mandatory)

> [!CAUTION]
> **NEVER run tests against the real `%LOCALAPPDATA%\NovaBrowser` profile.**
> The real user profile contains active logins, credentials, and persistent sandboxes. Running an un-isolated test will overwrite settings, rotate sandboxes, or purge session state.

All automated test scripts must redirect the profile root by setting the environment variable:

```powershell
$env:NOVA_TEST_LOCALAPPDATA_DIR = Join-Path $env:TEMP "nova-test-profile-[guid]"
```

* **`dotnet test`** is automatically protected: `NovaBrowser.Tests/TestProfileIsolation.cs` sets a disposable temporary profile directory before any storage path is resolved.
* **PowerShell tests** invoke `Enable-NovaIsolatedTestProfile` from `_nova-process-helper.ps1`.

---

## 2. Test Execution Commands

### 2.1 Unit Tests (xUnit)
Run the complete unit test suite with hang-dump tracking:

```powershell
.\.dotnet\dotnet.exe test .\NovaBrowser.Tests\NovaBrowser.Tests.csproj -c Release -p:Platform=x64 --blame-hang-timeout 5m --blame-hang-dump-type full
```

### 2.2 Smoke Tests (`smoke-test.ps1`)
Verifies that `dist\NovaAIWorkspace.exe` launches, initializes WebView2 runtimes, starts the MCP server, and shuts down cleanly within 20 seconds:

```powershell
powershell -ExecutionPolicy Bypass -File .\tests\smoke-test.ps1 -Seconds 20
```

### 2.3 Documentation Coverage & Link Gates
Validates that 100% of MCP tool schemas are cataloged and have active documentation pages:

```powershell
# Verify all active schemas appear in tool-catalog.md and dedicated files exist:
powershell -ExecutionPolicy Bypass -File .\tests\mcp-catalog-coverage-test.ps1

# Verify all links point to existing, matching markdown files:
powershell -ExecutionPolicy Bypass -File .\tests\mcp-catalog-link-test.ps1 -FailOnUnlinked
```

### 2.4 Code Scanner & Quality Report
Runs code health scanners, static analysis gates, and syntax smoke checks:

```powershell
powershell -ExecutionPolicy Bypass -File .\tools\scanner-report.ps1 -NoColor
```

---

## 3. Quality Metrics & Baselines

* **Warning Policy:** `TreatWarningsAsErrors` is enabled across all C# projects. Any build warning is treated as a fatal compilation failure.
* **Code Formatting:** Run `dotnet format` before committing any changes.
* **Coverage Floor:** Minimum allowable test coverage is **8.9% line coverage** and **4.7% branch coverage**.
