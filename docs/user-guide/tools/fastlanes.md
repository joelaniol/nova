# Fastlanes: Let Nova React for You

> [!NOTE]
> **Upcoming.** Fastlanes arrive with a coming release, which is not published yet.
>
> **Kommend.** Fastlanes kommen mit einem kommenden Release, das noch nicht veröffentlicht ist.

---

## 1. What it is

A fastlane is an automation you ask your agent to set up once. After you approve it, Nova does the rest on its own, without an agent having to keep watching. Nova reacts to one of three things:

* **A network monitor reports something**, for example a server that has been down for 30 seconds.
* **The clock**, for example every weekday at 07:30 or every 15 minutes.
* **A file arrives or changes in a folder.** Nova looks at names, sizes and change times only, never at the content.

Then Nova shows a notification, or sends a message to a web address. No AI is involved in that. If a case needs thought, the fastlane can additionally wake the agent session that proposed it, or start a Claude run in the background, without a window, with the task and tools you approved.

> Scheduled tasks were replaced by fastlanes. Existing scheduled tasks are not carried over; ask your agent to set the automation up again as a fastlane.

---

## 2. How to ask your agent

Type this in your agent conversation (Nova must be connected):

* "Tell me when my web-1 monitor has been down for 30 seconds."
* "Remind me every weekday at 07:30 to check the orders."
* "Notify me when a new CSV file lands in my Downloads folder."
* "Every time the server goes down, wake yourself and look into it."

The agent shows you what it plans. You do not have to write anything technical.

---

## 3. Where you approve

* A fastlane that only notifies you, wakes the session that proposed it, or calls an address on your PC or in your local network starts at once. Nova tells you, and you can pause or delete it any time.
* A fastlane that starts a run on your Claude account or calls an address on the internet asks you first. The question shows in plain words what happens when, and which tools a run may use. Tools Nova cannot limit to a fixed reach are named separately and are always asked.
* If you do not answer right away, the proposal waits in the agents panel and does nothing until you decide. Unanswered proposals expire after a week.

An agent can never approve its own fastlane.

---

## 4. Pause and delete

Open the agents panel to see your fastlanes, what they did lately and their state. There you can pause, resume and delete.

* Your agent may pause and delete a fastlane, too. Only you can resume one that you paused.
* A fastlane that hits its hourly limit three hours in a row is paused by Nova, and you are told. Only you resume it.
* The **Emergency stop** halts all automations. See [Emergency stop](../../getting-started/emergency-stop.md).
* Events that happen while a fastlane is paused are not caught up later.

The Settings card **Agent runs** now only holds the paths of the Claude and Codex programs.

---

## Related Documentation

* [Fastlanes (technical)](../../core-features/fastlanes/README.md)
* [Tools Overview](README.md)
* [Network Diagnostics & Discovery](network-and-diagnostics.md)
