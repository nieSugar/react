/* Floating lesson navigation injected into every lesson HTML.
 * Determines the current lesson by the leading 3-digit number in the filename,
 * and renders Prev / Menu / Next buttons plus a counter (e.g. 7 / 24). */
(function () {
  if (window.__LESSON_NAV_INJECTED__) return;
  window.__LESSON_NAV_INJECTED__ = true;

  var LESSONS = [
    { n: "001", title: "Getting Started",                                 file: "001 - Getting Started - ui.dev.html" },
    { n: "002", title: "Why React?",                                      file: "002 - Why React_ - ui.dev.html" },
    { n: "003", title: "Imperative vs Declarative Programming",           file: "003 - Imperative vs Declarative Programming - ui.dev.html" },
    { n: "004", title: "Pure Functions",                                  file: "004 - Pure Functions - ui.dev.html" },
    { n: "005", title: "Components",                                      file: "005 - Components - ui.dev.html" },
    { n: "006", title: "JSX",                                             file: "006 - JSX - ui.dev.html" },
    { n: "007", title: "Props",                                           file: "007 - Props - ui.dev.html" },
    { n: "008", title: "Elements vs Components",                          file: "008 - Elements vs Components - ui.dev.html" },
    { n: "009", title: "Elements vs Components (styles.css)",             file: "009 - Elements vs Components - ui.dev + styles.css.html" },
    { n: "010", title: "Handling Events",                                 file: "010 - Handling Events - ui.dev.html" },
    { n: "011", title: "Preserving Values with useState",                 file: "011 - Preserving Values with useState - ui.dev.html" },
    { n: "012", title: "Using useState",                                  file: "012 - Using useState - ui.dev.html" },
    { n: "013", title: "Why React Renders",                               file: "013 - Why React Renders - ui.dev.html" },
    { n: "014", title: "Reality Check",                                   file: "014 - Reality Check - ui.dev.html" },
    { n: "015", title: "Managing Effects",                                file: "015 - Managing Effects - ui.dev.html" },
    { n: "016", title: "Managing Effects – Part 2",                       file: "016 - Managing Effects - Part 2 - ui.dev.html" },
    { n: "017", title: "Preserving Values with useRef",                   file: "017 - Preserving Values with useRef - ui.dev.html" },
    { n: "018", title: "Teleportation with Context",                      file: "018 - Teleportation with Context - ui.dev.html" },
    { n: "019", title: "Complex State with useReducer",                   file: "019 - Complex State with useReducer - ui.dev.html" },
    { n: "020", title: "Referential Equality and Why It Matters",         file: "020 - Referential Equality and Why It Matters - ui.dev.html" },
    { n: "021", title: "Managing Advanced Effects",                       file: "021 - Managing Advanced Effects - ui.dev.html" },
    { n: "022", title: "Abstracting Reactive Values with useEffectEvent", file: "022 - Abstracting Reactive Values with useEffectEvent - ui.dev.html" },
    { n: "023", title: "Creating Custom Hooks",                           file: "023 - Creating Custom Hooks - ui.dev.html" },
    { n: "024", title: "Rebuilding useHooks",                             file: "024 - Rebuilding useHooks - ui.dev.html" }
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

  function urlFor(lesson) {
    return encodeURIComponent(lesson.file);
  }

  function go(lesson) {
    if (!lesson) return;
    location.href = urlFor(lesson);
  }

  function makeButton(label, onClick, opts) {
    opts = opts || {};
    var b = document.createElement("button");
    b.type = "button";
    b.textContent = label;
    var bg = opts.bg || "#2563eb";
    var bgHover = opts.bgHover || "#1d4ed8";
    b.style.cssText =
      "all:unset;box-sizing:border-box;cursor:pointer;" +
      "padding:8px 14px;border-radius:8px;" +
      "font:600 13px/1.2 -apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;" +
      "color:#fff;background:" + bg + ";" +
      "transition:background .15s ease, transform .15s ease, opacity .15s ease;" +
      "user-select:none;white-space:nowrap;";
    if (opts.disabled) {
      b.style.background = "#4b5563";
      b.style.opacity = "0.5";
      b.style.cursor = "not-allowed";
      b.disabled = true;
    } else {
      b.addEventListener("mouseenter", function () {
        b.style.background = bgHover;
        b.style.transform = "translateY(-1px)";
      });
      b.addEventListener("mouseleave", function () {
        b.style.background = bg;
        b.style.transform = "none";
      });
      b.addEventListener("click", onClick);
    }
    return b;
  }

  function render() {
    var idx = currentIndex();
    if (idx < 0) return; // Filename did not start with a 3-digit lesson number — skip.
    var prev = idx > 0 ? LESSONS[idx - 1] : null;
    var next = idx < LESSONS.length - 1 ? LESSONS[idx + 1] : null;

    var bar = document.createElement("div");
    bar.id = "__lesson_nav_bar__";
    bar.style.cssText =
      "position:fixed;left:50%;bottom:20px;transform:translateX(-50%);" +
      "z-index:2147483647;display:flex;align-items:center;gap:8px;" +
      "padding:10px 12px;border-radius:14px;" +
      "background:rgba(17,24,39,0.92);backdrop-filter:blur(8px);-webkit-backdrop-filter:blur(8px);" +
      "box-shadow:0 12px 36px rgba(0,0,0,0.35),0 0 0 1px rgba(255,255,255,0.06);" +
      "color:#fff;font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;";

    bar.appendChild(
      makeButton("← Previous Lesson", function () { go(prev); }, { disabled: !prev })
    );

    var counter = document.createElement("span");
    counter.style.cssText =
      "padding:0 8px;color:#cbd5e1;font:600 12px/1.2 ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;letter-spacing:.03em;";
    counter.textContent =
      (idx >= 0 ? idx + 1 : "?") + " / " + LESSONS.length;
    bar.appendChild(counter);

    bar.appendChild(
      makeButton("Next Lesson →", function () { go(next); }, { disabled: !next })
    );

    (document.body || document.documentElement).appendChild(bar);

    // Keyboard shortcuts: ← / →
    document.addEventListener("keydown", function (e) {
      if (e.target && /^(INPUT|TEXTAREA|SELECT)$/.test(e.target.tagName)) return;
      if (e.target && e.target.isContentEditable) return;
      if (e.altKey || e.ctrlKey || e.metaKey) return;
      if (e.key === "ArrowRight" && next) go(next);
      if (e.key === "ArrowLeft"  && prev) go(prev);
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", render);
  } else {
    render();
  }
})();
