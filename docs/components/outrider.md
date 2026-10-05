# Outrider — Native Work Helper

**Executable:** `NovaBrowser.Outrider.exe`.

Outrider handles native work that could hang or crash outside normal managed exception handling: device enumeration, GPU capability detection, local speech recognition and the Windows credential check used when Windows Hello is unavailable.

## When It Runs

Device inventory uses an on-demand hidden helper session. Speech recognition, GPU detection and credential verification use one-shot helper processes. More than one Outrider process can therefore be expected during concurrent native work.

Nova supervises deadlines and helper identity. Failed or timed-out work returns a degraded result rather than retrying the same failed probe in the browser process. The helper watches its parent and stops when Nova is gone.

## Why It Is Separate

A faulty camera driver should not close every tab. The process boundary makes failed native work disposable. It is fault isolation in the current user's Windows context, not an operating-system security sandbox or a source of agent permissions.

The installation includes an isolated Outrider folder as well as the helper at the installation root. These are deployment copies of the same component, not two different products.

## Learn More

* [Outrider boundary](../core-features/outrider-boundary.md) — Deadlines, transport and failure behaviour.
* [Media intelligence](../core-features/media-intelligence.md)
* [All components](README.md)
