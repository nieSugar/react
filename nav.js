/* Floating lesson navigation injected into every lesson HTML.
 * - Detects current lesson by the leading 3-digit number in the filename.
 * - Renders Prev / counter / Next as real <a href> links so browser native
 *   navigation always wins (no framework / click-handler interception).
 * - Uses origin-absolute URLs (/<encoded>) to defeat any base-path quirks.
 * - Renders inside a Shadow DOM so the host page's CSS cannot affect it. */
(function () {
  if (window.__LESSON_NAV_INJECTED__) return;
  window.__LESSON_NAV_INJECTED__ = true;

  var LESSONS = [
    { n: "001", file: "001 - Getting Started - ui.dev.html" },
    { n: "002", file: "002 - Why React_ - ui.dev.html" },
    { n: "003", file: "003 - Imperative vs Declarative Programming - ui.dev.html" },
    { n: "004", file: "004 - Pure Functions - ui.dev.html" },
    { n: "005", file: "005 - Components - ui.dev.html" },
    { n: "006", file: "006 - JSX - ui.dev.html" },
    { n: "007", file: "007 - Props - ui.dev.html" },
    { n: "008", file: "008 - Elements vs Components - ui.dev.html" },
    { n: "009", file: "009 - Elements vs Components - ui.dev + styles.css.html" },
    { n: "010", file: "010 - Handling Events - ui.dev.html" },
    { n: "011", file: "011 - Preserving Values with useState - ui.dev.html" },
    { n: "012", file: "012 - Using useState - ui.dev.html" },
    { n: "013", file: "013 - Why React Renders - ui.dev.html" },
    { n: "014", file: "014 - Reality Check - ui.dev.html" },
    { n: "015", file: "015 - Managing Effects - ui.dev.html" },
    { n: "016", file: "016 - Managing Effects - Part 2 - ui.dev.html" },
    { n: "017", file: "017 - Preserving Values with useRef - ui.dev.html" },
    { n: "018", file: "018 - Teleportation with Context - ui.dev.html" },
    { n: "019", file: "019 - Complex State with useReducer - ui.dev.html" },
    { n: "020", file: "020 - Referential Equality and Why It Matters - ui.dev.html" },
    { n: "021", file: "021 - Managing Advanced Effects - ui.dev.html" },
    { n: "022", file: "022 - Abstracting Reactive Values with useEffectEvent - ui.dev.html" },
    { n: "023", file: "023 - Creating Custom Hooks - ui.dev.html" },
    { n: "024", file: "024 - Rebuilding useHooks - ui.dev.html" }
  ];

  function currentIndex() {
    try {
      var last = decodeURIComponent(location.pathname.split("/").pop() || "");
      var m = /^(\d{3})/.exec(last);
      if (!m) return -1;
      for (var i = 0; i < LESSONS.length; i++) {
        if (LESSONS[i].n === m[1]) return i;
      }
    } catch (e) {}
    return -1;
  }

  // Origin-absolute URL — immune to any base/path weirdness on the host page.
  function urlFor(lesson) {
    return location.origin + "/" + encodeURIComponent(lesson.file);
  }

  function buildStyles() {
    return (
      ":host{all:initial;}" +
      ".bar{" +
        "position:fixed;left:50%;bottom:20px;transform:translateX(-50%);" +
        "z-index:2147483647;display:flex;align-items:center;gap:8px;" +
        "padding:10px 12px;border-radius:14px;" +
        "background:rgba(17,24,39,0.92);" +
        "-webkit-backdrop-filter:blur(8px);backdrop-filter:blur(8px);" +
        "box-shadow:0 12px 36px rgba(0,0,0,0.35),0 0 0 1px rgba(255,255,255,0.06);" +
        "color:#fff;" +
        "font:600 13px/1.2 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;" +
      "}" +
      ".btn{" +
        "display:inline-flex;align-items:center;justify-content:center;" +
        "padding:8px 14px;border-radius:8px;color:#fff;background:#2563eb;" +
        "text-decoration:none;cursor:pointer;user-select:none;white-space:nowrap;" +
        "transition:background .15s ease, transform .15s ease, opacity .15s ease;" +
      "}" +
      ".btn:hover{background:#1d4ed8;transform:translateY(-1px);}" +
      ".btn[aria-disabled='true']{background:#4b5563;opacity:.5;cursor:not-allowed;pointer-events:none;}" +
      ".count{padding:0 8px;color:#cbd5e1;font:600 12px/1.2 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;letter-spacing:.03em;}"
    );
  }

  function render() {
    var idx = currentIndex();
    if (idx < 0) return;

    var prev = idx > 0 ? LESSONS[idx - 1] : null;
    var next = idx < LESSONS.length - 1 ? LESSONS[idx + 1] : null;

    // Host element attached to <html> (works even when <body> is missing/late).
    var host = document.createElement("div");
    host.id = "__lesson_nav_host__";
    host.style.cssText = "all:initial;";
    (document.body || document.documentElement).appendChild(host);

    // Shadow DOM to isolate from page CSS/JS.
    var root = host.attachShadow ? host.attachShadow({ mode: "open" }) : host;

    var style = document.createElement("style");
    style.textContent = buildStyles();
    root.appendChild(style);

    var bar = document.createElement("div");
    bar.className = "bar";

    function makeLink(label, lesson) {
      var a = document.createElement("a");
      a.className = "btn";
      a.textContent = label;
      if (lesson) {
        a.href = urlFor(lesson);
        a.setAttribute("data-lesson", lesson.n);
        // Defensive: if something prevents the default <a> nav, force it.
        a.addEventListener("click", function (ev) {
          if (ev.defaultPrevented) {
            location.assign(urlFor(lesson));
          }
        });
      } else {
        a.href = "javascript:void(0)";
        a.setAttribute("aria-disabled", "true");
      }
      return a;
    }

    bar.appendChild(makeLink("\u2190 Previous Lesson", prev));

    var counter = document.createElement("span");
    counter.className = "count";
    counter.textContent = (idx + 1) + " / " + LESSONS.length;
    bar.appendChild(counter);

    bar.appendChild(makeLink("Next Lesson \u2192", next));

    root.appendChild(bar);

    // Keyboard shortcuts: ArrowLeft / ArrowRight (capture phase so we win).
    window.addEventListener("keydown", function (e) {
      var t = e.target;
      if (t && /^(INPUT|TEXTAREA|SELECT)$/.test(t.tagName)) return;
      if (t && t.isContentEditable) return;
      if (e.altKey || e.ctrlKey || e.metaKey) return;
      if (e.key === "ArrowRight" && next) {
        e.preventDefault();
        location.assign(urlFor(next));
      } else if (e.key === "ArrowLeft" && prev) {
        e.preventDefault();
        location.assign(urlFor(prev));
      }
    }, true);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", render);
  } else {
    render();
  }
})();
