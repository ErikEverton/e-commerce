const hamburguer = document.querySelector(".hamburguer")
const menu = document.querySelector(".menu")

menu.addEventListener("click", () => {
    if (menu.classList.contains("open")) {
        menu.classList.remove("open");
    } else {
        menu.classList.add("open");
    }
});
