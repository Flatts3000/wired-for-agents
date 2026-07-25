// Copy-to-clipboard for the embed snippets.
// Kept in its own file so the Content-Security-Policy can use script-src 'self'
// instead of 'unsafe-inline'.
(function () {
  "use strict";

  var status = document.getElementById("copy-status");

  function announce(message) {
    if (!status) return;
    // Clear first so repeat presses of the same button still register as a change.
    status.textContent = "";
    window.setTimeout(function () { status.textContent = message; }, 60);
  }

  document.querySelectorAll("button.copy").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var code = btn.closest(".snippet").querySelector("code");
      var text = code.textContent;
      var label = btn.getAttribute("data-label") || "snippet";

      function done() {
        btn.textContent = "Copied";
        btn.dataset.done = "1";
        announce(label + " copied to clipboard");
        window.setTimeout(function () {
          btn.textContent = "Copy";
          delete btn.dataset.done;
        }, 1800);
      }

      function fallback() {
        var ta = document.createElement("textarea");
        ta.value = text;
        ta.setAttribute("readonly", "");
        ta.style.position = "fixed";
        ta.style.opacity = "0";
        document.body.appendChild(ta);
        ta.select();
        try {
          document.execCommand("copy");
          done();
        } catch (e) {
          btn.textContent = "Press Ctrl+C";
          announce("Copy failed. The snippet is selected, press Control C to copy it.");
        }
        document.body.removeChild(ta);
      }

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, fallback);
      } else {
        fallback();
      }
    });
  });
})();
