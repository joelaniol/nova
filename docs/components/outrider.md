# Outrider — Native Work Helper

**Executable:** `NovaBrowser.Outrider.exe`.

Outrider handles native work that could hang or crash outside normal managed exception handling: device enumeration, GPU capability detection, local speech recognition and the Windows credential check used when Windows Hello is unavailable.

## When It Runs

Device inventory uses an on-demand hidden helper session. Speech recognition, GPU detection and credential verification use one-shot helper processes. More than one Outrider process can therefore be expected during concurrent native work.

Nova supervises deadlines and helper identity. Failed or timed-out work returns a degraded result rather than retrying the same failed probe in the browser process. The shared inventory worker watches its parent and stops when Nova is gone; one-shot work has its own supervision.

## Why It Is Separate

A faulty camera driver should not close every tab. The process boundary makes failed native work disposable. It is fault isolation in the current user's Windows context, not an operating-system security sandbox or a source of agent permissions.

The installation includes an isolated Outrider folder as well as the helper at the installation root. These are deployment copies of the same component, not two different products.

## Capabilities

| Work | What Outrider supplies | How Nova uses it |
| :--- | :--- | :--- |
| DirectShow camera inventory | Video-input devices exposed through the driver stack. | Camera choices and device information. |
| Windows media-device inventory | Camera, microphone and speaker information available through Windows device APIs. | Permission and device-selection surfaces. |
| GPU capability detection | Information used to select a local transcription execution path. | Speech-recognition configuration. |
| Local speech recognition | A transcription result from an audio file and a local model. | Nova's transcription workflow. |
| Windows credential verification | The outcome of a Windows sign-in check. | Saved-password reveal or export when Windows Hello is unavailable. |

Outrider does not decide which device a website may access or whether a saved password may be delivered. Nova owns those decisions. Recognition also needs the appropriate local model; the presence of the helper alone does not mean transcription is configured.

## From Request to Result

For device inventory, Nova starts a hidden helper session on demand. A current-user named pipe carries framed requests and results. Nova checks the connecting helper's identity and handshake before using it. The session advertises its supported capabilities and can handle up to three jobs concurrently.

Speech recognition, GPU detection and credential verification use separate one-shot invocations. Each invocation performs its specific job and exits. The credential path is deliberately kept outside the shared inventory worker; an OS credential dialog and driver inventory have different failure characteristics.

For example, opening a camera list starts an inventory request. If the driver responds, Nova receives the device information. If it hangs, the deadline produces a degraded result. That result means the inventory was unavailable, rather than proving that the machine has no cameras.

## Failure and Recovery

Nova bounds native work and can terminate a helper that stops responding. Repeated inventory timeouts end the shared session and temporarily pause further probes before a fresh session is attempted. The inventory worker also monitors Nova's parent process. One-shot jobs have their own supervision and deadlines.

This boundary contains a native crash or hang; it cannot repair a broken driver or make unsupported hardware work. Ending Outrider in Task Manager interrupts the associated native work. It is preferable to inspect the feature's reported failure before repeatedly launching the same job.

## Learn More

* [Outrider boundary](../core-features/outrider-boundary/README.md) — Deadlines, transport and failure behaviour.
* [Media intelligence](../core-features/media-intelligence/README.md)
* [All components](README.md)
