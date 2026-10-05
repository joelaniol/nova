/* Sample website state only. Knowledge, trust and verification verdicts belong to Nova. */
(function () {
  "use strict";
  var $ = function (id) { return document.getElementById(id); };
  var state;
  var receiptNumber = 0;

  function record(message) {
    var list = $("log");
    var item = document.createElement("li");
    var time = document.createElement("time");
    time.textContent = new Date().toLocaleTimeString("en-GB");
    var text = document.createElement("span");
    text.className = "what";
    text.textContent = message;
    item.append(time, text);
    list.appendChild(item);
    list.scrollTop = list.scrollHeight;
  }

  function paint() {
    $("experience-visit-state").textContent = state.visit;
    $("experience-notice-state").textContent = state.notice ? "Blocking the draft" : "Removed";
    $("experience-attempt-state").textContent = String(state.attempts);
    $("experience-saved-state").textContent = state.saved ? "1" : "0";
    $("experience-approval-state").textContent = state.approved ? "Confirmed on this page" : "Waiting for the user";
    $("experience-save").disabled = state.saved;
    $("experience-confirm").disabled = state.approved;
    $("experience-workspace").inert = state.notice;
  }

  function showNotice(changed) {
    var notice = document.createElement("div");
    notice.id = "experience-notice";
    notice.className = "experience-notice";
    notice.setAttribute("role", "dialog");
    notice.setAttribute("aria-labelledby", "experience-notice-title");
    var sheet = document.createElement("div");
    sheet.className = "experience-notice-sheet";
    var title = document.createElement("h3");
    title.id = "experience-notice-title";
    title.textContent = "Release desk notice";
    var copy = document.createElement("p");
    copy.textContent = changed
      ? "The workspace has a refreshed layout. Review the current controls before continuing."
      : "A recurring workspace notice. Close it to continue with the draft.";
    var button = document.createElement("button");
    button.className = "act primary";
    button.type = "button";
    button.id = changed ? "experience-dismiss-updated" : "experience-dismiss-original";
    button.textContent = changed ? "Continue to draft" : "Close notice";
    button.addEventListener("click", function () {
      notice.remove();
      state.notice = false;
      paint();
      $("experience-title").focus();
      record("Release notice closed on " + (changed ? "changed layout" : "original layout"));
    });
    sheet.append(title, copy, button);
    notice.appendChild(sheet);
    $("experience-notice-slot").appendChild(notice);
  }

  function visit(name, changed) {
    state = { visit: name, notice: true, attempts: 0, approved: false, saved: false };
    $("experience-notice-slot").textContent = "";
    $("experience-receipt-slot").textContent = "";
    $("experience-save-message").textContent = "Draft not saved.";
    $("experience-title").value = "Release desk update";
    $("experience-summary").value = "A small workspace update for the demo team.";
    $("experience-revision").textContent = changed ? "Changed layout" : "Original layout";
    showNotice(changed);
    paint();
    record(name + ": draft opened with a release notice");
  }

  $("experience-first").addEventListener("click", function () { visit("First visit", false); });
  $("experience-return").addEventListener("click", function () { visit("Return visit", false); });
  $("experience-change").addEventListener("click", function () { visit("Changed visit", true); });
  $("experience-reset").addEventListener("click", function () { visit("First visit", false); });
  $("experience-confirm").addEventListener("click", function () {
    state.approved = true;
    paint();
    record("Demo draft confirmation received on the page");
  });
  $("experience-save").addEventListener("click", function () {
    if (state.notice || state.saved) { return; }
    state.attempts += 1;
    // The first accepted click deliberately has no saved result: the demonstration needs an
    // observable difference between dispatch and outcome, even when confirmation arrived early.
    if (state.attempts === 1) {
      $("experience-save-message").textContent = "Request received. The draft is still unsaved; inspect the result before continuing.";
      record("Save request received; no draft saved");
    } else if (!state.approved) {
      $("experience-save-message").textContent = "Draft still unsaved. Waiting for the demo user's confirmation.";
      record("Save held: demo confirmation missing");
    } else if (!$("experience-title").value.trim() || !$("experience-summary").value.trim()) {
      $("experience-save-message").textContent = "Draft still unsaved. Add a title and summary.";
      record("Save held: draft fields incomplete");
    } else {
      state.saved = true;
      receiptNumber += 1;
      var receipt = document.createElement("p");
      receipt.id = "experience-saved-receipt";
      receipt.className = "experience-receipt";
      receipt.textContent = "Demo draft saved · DEMO-" + String(receiptNumber).padStart(4, "0");
      $("experience-receipt-slot").appendChild(receipt);
      $("experience-save-message").textContent = "Saved locally for this demo visit. Nothing was published.";
      record("Demo draft saved with a visible receipt");
    }
    paint();
  });
  $("experience-origin").textContent = location.protocol === "file:"
    ? "File preview: page interactions work. For Nova's persistent website knowledge, serve this folder on a local HTTP address; see the demo guide."
    : "Website scope: " + location.host + ". Keep this address and port for repeat visits. Nova stores its knowledge separately from this page.";
  visit("First visit", false);
})();
