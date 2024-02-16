const menu = document.querySelector(".hamburguer")

menu.addEventListener("click", () => {
    if (menu.classList.contains("open")) {
        menu.classList.remove("open");
    } else {
        menu.classList.add("open");
    }
});
