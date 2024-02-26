const hamburguer = document.querySelector(".hamburguer");
const menu = document.querySelector(".menu");

hamburguer.addEventListener("click", () => {
    if (hamburguer.classList.contains("open")) {
        hamburguer.classList.remove("open");
        menu.classList.add("invisible");
    } else {
        hamburguer.classList.add("open");
        menu.classList.remove("invisible")
    }
});
