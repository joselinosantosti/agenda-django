var btnDark = document.getElementById("modo-dark")

btnDark.onclick = function() {modoDark()}

function modoDark() {
    let body = document.getElementsByTagName("body")[0]
    let nav = document.getElementsByTagName("nav")[0]
    if (body.classList.contains("bg-dark")) {
        body.classList.remove("bg-dark")
        body.classList.remove("text-white")
        nav.classList.add("gradient")
        nav.classList.remove("bg-dark")
    } else {
        body.classList.add("bg-dark")
        body.classList.add("text-white")
        nav.classList.remove("gradient")
        nav.classList.add("bg-dark")
    }
}