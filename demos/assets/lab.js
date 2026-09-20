/* Nova Demo Lab — behaviour.
   Everything is deliberate: the list really is virtualised, the shadow root really is nested, the
   delays really are unknown in advance. A demo that fakes its difficulty proves nothing. */

(function () {
  "use strict";

  var $ = function (id) { return document.getElementById(id); };

  /* ---------------- activity log ---------------- */

  var logEl = $("log");

  function log(what, good) {
    var li = document.createElement("li");
    if (good) { li.className = "good"; }
    var t = document.createElement("time");
    var d = new Date();
    t.textContent = String(d.getHours()).padStart(2, "0") + ":" +
                    String(d.getMinutes()).padStart(2, "0") + ":" +
                    String(d.getSeconds()).padStart(2, "0");
    var s = document.createElement("span");
    s.className = "what";
    s.textContent = what;
    li.appendChild(t);
    li.appendChild(s);
    logEl.appendChild(li);
    logEl.scrollTop = logEl.scrollHeight;
    // Also on the page object, so an agent can read the whole run in one eval instead of
    // reconstructing it from the DOM.
    window.novaDemoLog = window.novaDemoLog || [];
    window.novaDemoLog.push({ at: d.toISOString(), what: what });
  }

  window.novaDemoLog = [];
  $("clearLog").addEventListener("click", function () {
    logEl.textContent = "";
    window.novaDemoLog = [];
    log("log cleared");
  });

  /* ---------------- tabs ---------------- */

  var tabs = Array.prototype.slice.call(document.querySelectorAll("nav.tabs button"));

  function selectTab(name, quiet) {
    tabs.forEach(function (b) {
      var on = b.dataset.panel === name;
      b.setAttribute("aria-selected", on ? "true" : "false");
      $("panel-" + b.dataset.panel).hidden = !on;
    });
    if (!quiet) { log("section: " + name); }
    try { localStorage.setItem("novaDemo.tab", name); } catch (e) { /* private window */ }
  }

  tabs.forEach(function (b) {
    b.addEventListener("click", function () { selectTab(b.dataset.panel); });
  });

  /* ---------------- 1. session ---------------- */

  var SESSION_KEY = "novaDemo.session";

  function readSession() {
    try { return JSON.parse(localStorage.getItem(SESSION_KEY) || "null"); }
    catch (e) { return null; }
  }

  function paintSession(quiet) {
    var s = readSession();
    var dot = $("sessionDot");
    if (s && s.user) {
      $("sessionState").textContent = "signed in as " + s.user + " (since " + s.since + ")";
      dot.style.background = "var(--accent)";
      $("loginOk").textContent = "Signed in as " + s.user + ". This survives a reload.";
      $("loginOk").hidden = false;
      $("loginErr").hidden = true;
      if (!quiet) { log("session restored: " + s.user, true); }
    } else {
      $("sessionState").textContent = "signed out";
      dot.style.background = "var(--text-faint)";
      $("loginOk").hidden = true;
    }
  }

  $("loginForm").addEventListener("submit", function (ev) {
    ev.preventDefault();
    var u = $("user").value.trim();
    var p = $("pass").value;
    if (u === "demo" && p === "nova") {
      var s = { user: u, since: new Date().toLocaleTimeString() };
      try { localStorage.setItem(SESSION_KEY, JSON.stringify(s)); } catch (e) { /* ignore */ }
      $("loginErr").hidden = true;
      paintSession(true);
      log("signed in as " + u, true);
    } else {
      $("loginErr").hidden = false;
      $("loginOk").hidden = true;
      log("sign-in rejected");
    }
  });

  $("logoutBtn").addEventListener("click", function () {
    try { localStorage.removeItem(SESSION_KEY); } catch (e) { /* ignore */ }
    paintSession(true);
    log("signed out");
  });

  $("reloadBtn").addEventListener("click", function () { location.reload(); });

  /* ---------------- 2. virtualised list ---------------- */

  var TOTAL = 10000;
  var ROW_H = 34;
  var TARGET = 8472;
  var vlist = $("vlist");
  var vinner = $("vinner");
  var found = false;

  vinner.style.height = (TOTAL * ROW_H) + "px";

  function renderRows() {
    var top = vlist.scrollTop;
    var first = Math.max(0, Math.floor(top / ROW_H) - 3);
    var last = Math.min(TOTAL - 1, Math.ceil((top + vlist.clientHeight) / ROW_H) + 3);

    var frag = document.createDocumentFragment();
    for (var i = first; i <= last; i++) {
      var row = document.createElement("div");
      row.className = "vrow" + (i === TARGET ? " target" : "");
      row.id = "row-" + i;
      row.style.top = (i * ROW_H) + "px";
      row.setAttribute("data-index", String(i));

      var idx = document.createElement("span");
      idx.className = "idx mono";
      idx.textContent = "#" + i;
      var label = document.createElement("span");
      label.textContent = i === TARGET
        ? "Build 8472 — the one you were looking for"
        : "Build " + i + " — routine";
      row.appendChild(idx);
      row.appendChild(label);
      frag.appendChild(row);
    }
    vinner.textContent = "";
    vinner.appendChild(frag);
    $("domCount").textContent = String(last - first + 1);

    if (!found && document.getElementById("row-" + TARGET)) {
      found = true;
      $("vstatus").textContent = "row " + TARGET + " is in the DOM";
      $("vstatus").style.color = "var(--accent)";
      log("row " + TARGET + " reached", true);
    }
  }

  vlist.addEventListener("scroll", renderRows, { passive: true });
  $("jumpTop").addEventListener("click", function () { vlist.scrollTop = 0; renderRows(); });

  // The first render happens while this panel is still hidden, so clientHeight is 0 and only a
  // handful of rows are produced. Re-render whenever the list actually has a size - that covers the
  // tab becoming visible and the window being resized, without the tab code having to know about
  // the list at all.
  if (typeof ResizeObserver === "function") {
    new ResizeObserver(function () {
      if (vlist.clientHeight > 0) { renderRows(); }
    }).observe(vlist);
  }

  renderRows();

  /* ---------------- 3. shadow roots + frame ---------------- */

  var outer = $("shadowHost").attachShadow({ mode: "open" });
  var mid = document.createElement("div");
  outer.appendChild(mid);
  var inner = mid.attachShadow({ mode: "open" });
  inner.innerHTML =
    '<style>' +
    'button{background:#1b2228;border:1px solid #2f3a42;color:#dce8ec;border-radius:8px;' +
    'padding:8px 14px;font:15px/1.5 "Segoe UI Variable","Segoe UI",system-ui,sans-serif;cursor:pointer}' +
    'button:hover{border-color:#3f8c62}' +
    'p{color:#5d6a72;font-size:13px;margin:0 0 10px}' +
    '</style>' +
    '<p>Two shadow roots above this button.</p>' +
    '<button id="deepBtn">Press the deep button</button>';

  inner.getElementById("deepBtn").addEventListener("click", function () {
    $("shadowState").textContent = "pressed at " + new Date().toLocaleTimeString();
    $("shadowState").style.color = "var(--accent)";
    log("deep shadow button pressed", true);
  });

  window.addEventListener("message", function (ev) {
    if (ev.data && ev.data.novaDemo === "frame-submit") {
      log("frame form submitted: " + ev.data.value, true);
    }
  });

  /* ---------------- 4. drag and drop ---------------- */

  var dragged = null;

  document.querySelectorAll(".chip").forEach(function (chip) {
    chip.addEventListener("dragstart", function (ev) {
      dragged = chip;
      ev.dataTransfer.effectAllowed = "move";
      ev.dataTransfer.setData("text/plain", chip.id);
    });
  });

  document.querySelectorAll(".col").forEach(function (col) {
    col.addEventListener("dragover", function (ev) { ev.preventDefault(); col.classList.add("over"); });
    col.addEventListener("dragleave", function () { col.classList.remove("over"); });
    col.addEventListener("drop", function (ev) {
      ev.preventDefault();
      col.classList.remove("over");
      var id = ev.dataTransfer.getData("text/plain");
      var chip = id ? document.getElementById(id) : dragged;
      if (!chip) { return; }
      col.appendChild(chip);
      if (chip.id === "chip-deploy") {
        $("boardState").textContent = "deploy: " + col.dataset.col;
        $("boardState").style.color = col.dataset.col === "done" ? "var(--accent)" : "var(--text-faint)";
      }
      log(chip.textContent + " moved to " + col.dataset.col, col.dataset.col === "done");
    });
  });

  /* ---------------- 5. files ---------------- */

  $("fileInput").addEventListener("change", function (ev) {
    var f = ev.target.files && ev.target.files[0];
    if (!f) { return; }
    $("fileState").textContent = f.name + " — " + f.size + " bytes";
    $("fileState").style.color = "var(--accent)";
    log("file chosen: " + f.name + " (" + f.size + " bytes)", true);
  });

  $("downloadBtn").addEventListener("click", function () {
    var rows = [["release", "date", "downloads", "crash_rate", "status"]];
    TABLE.forEach(function (r) { rows.push(r); });
    var csv = rows.map(function (r) { return r.join(","); }).join("\n");
    var blob = new Blob([csv], { type: "text/csv" });
    var url = URL.createObjectURL(blob);
    var a = document.createElement("a");
    a.href = url;
    a.download = "nova-demo-report.csv";
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    setTimeout(function () { URL.revokeObjectURL(url); }, 4000);
    $("dlState").textContent = "nova-demo-report.csv (" + csv.length + " bytes)";
    $("dlState").style.color = "var(--accent)";
    log("download started: nova-demo-report.csv", true);
  });

  /* ---------------- 6. dialogs and overlays ---------------- */

  $("alertBtn").addEventListener("click", function () {
    window.alert("The page thread is blocked until this is answered.");
    $("dialogState").textContent = "alert dismissed";
    log("alert dismissed", true);
  });

  $("confirmBtn").addEventListener("click", function () {
    var ok = window.confirm("Delete the selected build?");
    $("dialogState").textContent = "confirm: " + (ok ? "accepted" : "dismissed");
    log("confirm " + (ok ? "accepted" : "dismissed"), true);
  });

  $("promptBtn").addEventListener("click", function () {
    var v = window.prompt("Name for the new branch?", "release/next");
    $("dialogState").textContent = "prompt: " + (v === null ? "cancelled" : v);
    log("prompt answered: " + (v === null ? "cancelled" : v), true);
  });

  $("cmpBtn").addEventListener("click", function () {
    $("cmp").hidden = false;
    log("consent wall shown");
  });

  function cmpDecide(what) {
    $("cmp").hidden = true;
    $("cmpState").textContent = what;
    $("cmpState").style.color = what === "rejected" ? "var(--accent)" : "var(--text-faint)";
    log("consent " + what, what === "rejected");
  }

  $("cmpAccept").addEventListener("click", function () { cmpDecide("accepted all"); });
  $("cmpReject").addEventListener("click", function () { cmpDecide("rejected"); });
  $("cmpManage").addEventListener("click", function () { cmpDecide("opened options, then rejected"); });

  $("modalBtn").addEventListener("click", function () {
    $("modal").hidden = false;
    $("modalState").textContent = "open — page underneath is inert";
    log("modal opened");
  });

  function closeModal(how) {
    $("modal").hidden = true;
    $("modalState").textContent = "closed (" + how + ")";
    log("modal closed: " + how, true);
  }

  $("modalSave").addEventListener("click", function () { closeModal("saved"); });
  $("modalDiscard").addEventListener("click", function () { closeModal("discarded"); });

  /* ---------------- 7. timing ---------------- */

  $("startLate").addEventListener("click", function () {
    var slot = $("lateSlot");
    slot.textContent = "";
    var wait = 2000 + Math.floor(Math.random() * 4000);
    var p = document.createElement("p");
    p.className = "mono";
    p.style.color = "var(--text-faint)";
    p.textContent = "waiting…";
    slot.appendChild(p);
    log("delayed button will appear in " + Math.round(wait / 100) / 10 + "s");
    setTimeout(function () {
      slot.textContent = "";
      var b = document.createElement("button");
      b.className = "act primary";
      b.id = "lateBtn";
      b.type = "button";
      b.textContent = "I am here now";
      b.addEventListener("click", function () {
        b.disabled = true;
        b.textContent = "pressed";
        log("late button pressed", true);
      });
      slot.appendChild(b);
      log("#lateBtn appeared");
    }, wait);
  });

  $("startSettle").addEventListener("click", function () {
    var out = $("settleOut");
    out.style.color = "var(--text-faint)";
    out.textContent = "loading…";
    log("value loading");
    setTimeout(function () {
      out.textContent = "value: —";
      log("placeholder rendered (not the final value)");
      setTimeout(function () {
        out.textContent = "value: 42.7 MB/s";
        out.style.color = "var(--accent)";
        log("final value settled", true);
      }, 1500 + Math.floor(Math.random() * 1500));
    }, 700);
  });

  /* ---------------- 8. table + canvas ---------------- */

  var TABLE = [
    ["1.0.0-alpha.14", "2026-09-04", "312", "0.8%", "superseded"],
    ["1.0.0-alpha.15", "2026-09-08", "489", "0.6%", "superseded"],
    ["1.0.0-alpha.16", "2026-09-10", "540", "0.4%", "superseded"],
    ["1.0.0-alpha.17", "2026-09-10", "1204", "0.3%", "current"],
    ["1.0.0-beta.1", "2026-10-01", "0", "—", "planned"],
    ["1.0.0", "2026-11-15", "0", "—", "planned"]
  ];

  var tbody = document.querySelector("#dataTable tbody");
  TABLE.forEach(function (r) {
    var tr = document.createElement("tr");
    r.forEach(function (cell) {
      var td = document.createElement("td");
      td.textContent = cell;
      tr.appendChild(td);
    });
    tbody.appendChild(tr);
  });

  (function drawCanvas() {
    var c = $("pixelCanvas");
    var g = c.getContext("2d");
    g.fillStyle = "#070809";
    g.fillRect(0, 0, c.width, c.height);
    g.strokeStyle = "#2f3a42";
    g.strokeRect(0.5, 0.5, c.width - 1, c.height - 1);
    g.fillStyle = "#8b9aa3";
    g.font = "12px Consolas, monospace";
    g.fillText("verification code", 14, 26);
    g.fillStyle = "#7bf5ac";
    g.font = "bold 30px Consolas, monospace";
    g.fillText("NV-4831", 14, 64);
    // Noise, so the value cannot be guessed from the markup.
    g.strokeStyle = "rgba(123,245,172,0.18)";
    for (var i = 0; i < 14; i++) {
      g.beginPath();
      g.moveTo(Math.random() * c.width, Math.random() * c.height);
      g.lineTo(Math.random() * c.width, Math.random() * c.height);
      g.stroke();
    }
  })();

  /* ---------------- boot ---------------- */

  var startTab = "session";
  try { startTab = localStorage.getItem("novaDemo.tab") || "session"; } catch (e) { /* ignore */ }
  if (!document.getElementById("panel-" + startTab)) { startTab = "session"; }
  selectTab(startTab, true);
  paintSession();
  log("demo lab ready");
})();
