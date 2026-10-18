# ConPTY Setup, Win32 Lifecycle & Job Object Containment

Executing terminal commands in modern AI environments requires the full interactive capabilities of a real terminal: color escape sequences, cursor addressing, dynamic progress bars, and prompt interaction. Naive process spawning (`Process.Start`) cannot satisfy these requirements because Windows console applications behave differently when disconnected from a valid Windows Pseudo Console (**ConPTY**).

Nova AI Workspace's external runner process (`NovaBrowser.TerminalRunner.exe`) initializes native ConPTY instances and groups every spawned shell inside a Windows Job Object.

```mermaid
flowchart TD
    subgraph Runner["NovaBrowser.TerminalRunner.exe"]
        Alloc["1. Ensure Console Handle\n(AllocConsole / AttachConsole)"] --> CreatePipes["2. Create In/Out Pipe Pairs\n(CreatePipe for PTY Input/Output)"]
        CreatePipes --> ConPTY["3. Initialize ConPTY\n(CreatePseudoConsole with HPCON)"]
        ConPTY --> Job["4. Create Windows Job Object\n(KILL_ON_JOB_CLOSE limit)"]
        Job --> StartupEx["5. Configure STARTUPINFOEX\n(PROC_THREAD_ATTRIBUTE_PSEUDOCONSOLE)"]
        StartupEx --> Spawn["6. CreateProcessW\n(Spawn PowerShell / CLI in Job)"]
    end

    subgraph Tree["Contained Process Tree"]
        Spawn --> Shell["PowerShell.exe / pwsh.exe"]
        Shell --> Child1["git.exe"]
        Shell --> Child2["node.exe"]
        Shell --> Child3["compiler-worker.exe"]
    end

    Job -.->|Contains Entire Tree| Tree
```

---

## 1. ConPTY Setup & Win32 API Lifecycles

To provide complete virtual terminal fidelity, `TerminalRunner` invokes Windows pseudo console APIs:

```csharp
// 1. Create pipes for PTY input and output
CreatePipe(out IntPtr hPipeInRead, out IntPtr hPipeInWrite, IntPtr.Zero, 0);
CreatePipe(out IntPtr hPipeOutRead, out IntPtr hPipeOutWrite, IntPtr.Zero, 0);

// 2. Initialize the pseudo console with the requested window dimensions
COORD size = new COORD { X = (short)cols, Y = (short)rows };
int hr = CreatePseudoConsole(size, hPipeInRead, hPipeOutWrite, 0, out IntPtr hPC);
```

### The TTY Console Handle Requirement
A subtle, critical invariant of the Windows ConPTY subsystem:
* **The Invariant:** The calling process *must possess an active Win32 console handle* before calling `CreatePseudoConsole`. If a purely GUI or detached background process invokes `CreatePseudoConsole` without a console attached, the API fails with `ERROR_INVALID_HANDLE` (`0x6`).
* **Nova's Architecture:** `TerminalRunner` checks its console status on boot. If no console handle is present, it explicitly attaches via `AttachConsole(ATTACH_PARENT_PROCESS)` or allocates an invisible console buffer via `AllocConsole()`. This ensures consistent PTY creation whether launched from an interactive terminal, WinUI 3, or a background Windows service.

### Handle Inheritance and `STARTUPINFOEX`
When launching child processes, handle inheritance must be strictly limited:
* The shell process must inherit *only* the pseudo console reference, not arbitrary host pipe handles.
* Nova uses `InitializeProcThreadAttributeList` with `PROC_THREAD_ATTRIBUTE_PSEUDOCONSOLE`, passing `hPC`.
* The child process is created via `CreateProcessW` with `EXTENDED_STARTUPINFO_PRESENT`, attaching its standard input, output, and error streams directly to the ConPTY buffer.

---

## 2. Windows Job Object Tree Containment

In development automation, shells spawn complex trees of child processes: a PowerShell script runs `npm install`, which spawns `node.exe`, which spawns native C++ compiler tools (`cl.exe`).

If a terminal session is closed or times out, terminating only the top-level shell process (`powershell.exe`) leaves all child processes running as orphaned background zombies. These orphan processes consume memory, hold locks on files, and prevent clean test runs.

### The Job Object Shield
Nova encloses every runner session inside an isolated Windows Job Object:

```csharp
IntPtr hJob = CreateJobObject(IntPtr.Zero, null);
JOBOBJECT_EXTENDED_LIMIT_INFORMATION info = new JOBOBJECT_EXTENDED_LIMIT_INFORMATION
{
    BasicLimitInformation = new JOBOBJECT_BASIC_LIMIT_INFORMATION
    {
        LimitFlags = JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE | JOB_OBJECT_LIMIT_SILENT_BREAKAWAY_OK
    }
};
SetInformationJobObject(hJob, JobObjectExtendedLimitInformation, ref info, Marshal.SizeOf(info));
AssignProcessToJobObject(hJob, processHandle);
```

### Safety Invariants
1. **`JOB_OBJECT_LIMIT_KILL_ON_JOB_CLOSE`:**
   When the terminal session closes (or when `TerminalRunner` terminates), Windows automatically and unconditionally terminates every process assigned to the Job Object. No orphaned compiler, node, or python processes can survive.
2. **`JOB_OBJECT_LIMIT_SILENT_BREAKAWAY_OK`:**
   Allows designated processes (such as detached background daemons explicitly launched by the user) to break away if configured, while keeping ordinary build tools contained.

---

## 3. Sequence: Session Creation to Termination

```mermaid
sequenceDiagram
    autonumber
    participant Client as Nova Client (NovaAIWorkspace.exe)
    participant Runner as TerminalRunner Host
    participant ConPTY as Windows ConPTY Subsystem
    participant Job as Windows Job Object
    participant Shell as Child Shell Process

    Client->>Runner: SessionCreateReq(cols=120, rows=30, shell='powershell')
    Runner->>ConPTY: CreatePseudoConsole(size, inPipe, outPipe)
    Runner->>Job: CreateJobObject(KILL_ON_JOB_CLOSE)
    Runner->>Shell: CreateProcessW(STARTUPINFOEX with hPC)
    Runner->>Job: AssignProcessToJobObject(hShell)
    Runner-->>Client: SessionCreateResp(sessionId=1, status='created')

    Note over Client,Shell: Interactive PTY Streaming over Named Pipe

    Client->>Runner: SessionCloseReq(sessionId=1)
    Runner->>ConPTY: ClosePseudoConsole(hPC)
    Runner->>Job: CloseHandle(hJob)
    Note over Job,Shell: OS terminates Shell and all child processes immediately
    Runner-->>Client: SessionCloseResp(sessionId=1, status='closed')
```

---

## 4. Related Documentation

* [ConPTY & External Runner Host Overview](../README.md)
* [Identity Hashing, Lifecycle & Acceptance Testing](../identity-hashing-and-reconciliation/README.md)
* [IPC Named Pipe Wire Protocol](../../ipc-wire-protocol/README.md)
* [Agent Headless Sessions & Security](../../agent-sessions-and-security/README.md)
