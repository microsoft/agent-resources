// Accordion toggle
document.querySelectorAll(".section-header").forEach((btn) => {
  btn.addEventListener("click", () => {
    const card = btn.closest(".section-card");
    const isOpen = card.classList.toggle("open");
    btn.setAttribute("aria-expanded", isOpen);
  });
});

// Hash-based open
function openTarget() {
  const hash = location.hash.substring(1);
  if (hash) {
    const card = document.getElementById(hash);
    if (card && card.classList.contains("section-card")) {
      card.classList.add("open");
      card
        .querySelector(".section-header")
        .setAttribute("aria-expanded", "true");
      setTimeout(
        () => card.scrollIntoView({ behavior: "smooth", block: "start" }),
        100,
      );
    }
  }
}
window.addEventListener("hashchange", openTarget);
openTarget();

// Search / filter
const searchInput = document.getElementById("searchInput");
searchInput.addEventListener("input", () => {
  const q = searchInput.value.toLowerCase().trim();
  document.querySelectorAll(".section-card").forEach((card) => {
    if (!q) {
      card.style.display = "";
      card
        .querySelectorAll(".link-list li, .session-grid li")
        .forEach((li) => (li.style.display = ""));
      return;
    }
    let hasMatch = false;
    card
      .querySelectorAll(".link-list li, .session-grid li")
      .forEach((li) => {
        const match = li.textContent.toLowerCase().includes(q);
        li.style.display = match ? "" : "none";
        if (match) hasMatch = true;
      });
    card.style.display = hasMatch ? "" : "none";
    if (hasMatch && !card.classList.contains("open")) {
      card.classList.add("open");
      card
        .querySelector(".section-header")
        .setAttribute("aria-expanded", "true");
    }
  });
});

/* ── Hamburger Menu ── */
(function() {
  var btn = document.getElementById('menu-toggle');
  var menu = document.getElementById('site-menu');
  if (!btn || !menu) return;
  btn.addEventListener('click', function() {
    var open = btn.getAttribute('aria-expanded') === 'true';
    btn.setAttribute('aria-expanded', !open);
    menu.setAttribute('aria-hidden', open);
    menu.classList.toggle('open');
  });
  document.addEventListener('click', function(e) {
    if (!btn.contains(e.target) && !menu.contains(e.target)) {
      btn.setAttribute('aria-expanded', 'false');
      menu.setAttribute('aria-hidden', 'true');
      menu.classList.remove('open');
    }
  });
})();
