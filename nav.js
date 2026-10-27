document.addEventListener("click", (event) => {
  const navbar = document.querySelector("#navbar");
  if (!navbar) return;

  const toggle = event.target.closest(".nav-toggle");
  if (toggle) {
    const open = navbar.classList.toggle("open");
    toggle.setAttribute("aria-expanded", open ? "true" : "false");
    toggle.setAttribute("aria-label", open ? "Fechar menu" : "Abrir menu");
    return;
  }

  if (event.target.closest(".nav-link")) {
    navbar.classList.remove("open");
    const button = navbar.querySelector(".nav-toggle");
    if (button) {
      button.setAttribute("aria-expanded", "false");
      button.setAttribute("aria-label", "Abrir menu");
    }
  }
});
