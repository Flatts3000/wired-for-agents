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

        var copied = false;
        try {
          copied = document.execCommand("copy");
        } catch (e) {
          copied = false;
        }
        document.body.removeChild(ta);

        if (copied) {
          done();
          return;
        }

        // Select the real snippet in the page, so telling the user to press
        // Ctrl+C is actually true. The throwaway textarea above is already gone,
        // and its selection with it.
        btn.textContent = "Press Ctrl+C";
        try {
          var range = document.createRange();
          range.selectNodeContents(code);
          var sel = window.getSelection();
          sel.removeAllRanges();
          sel.addRange(range);
          announce("Copy failed. The " + label + " is now selected, press Control C to copy it.");
        } catch (e2) {
          announce("Copy failed. Select the " + label + " manually to copy it.");
        }
      }

      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, fallback);
      } else {
        fallback();
      }
    });
  });
})();
