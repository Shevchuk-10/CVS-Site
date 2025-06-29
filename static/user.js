function toggleMenu(btn) {
    const menu = document.getElementById('mobileMenu');
    const overlay = document.getElementById('overlay');
    menu.classList.toggle('active');
    btn.classList.toggle('active');
    overlay.classList.toggle('active');
}

function closeMenu() {
    const menu = document.getElementById('mobileMenu');
    const overlay = document.getElementById('overlay');
    const btn = document.getElementById('open-menu')

    menu.classList.remove('active');
    btn.classList.remove('active');
    overlay.classList.remove('active');
}

const scrollBtn = document.getElementById("scrollTopBtn");

window.addEventListener("scroll", () => {
    if (window.scrollY > 200) {
        scrollBtn.classList.add("show");
    } else {
        scrollBtn.classList.remove("show");
    }
});

scrollBtn.addEventListener("click", () => {
    window.scrollTo({
        top: 0,
        behavior: "smooth"
    });
});

const hireMeBtn = document.getElementById("hireMe");

hireMeBtn.addEventListener("click", () => {
    window.scrollTo({
        top: document.body.scrollHeight,
        behavior: "smooth"
    })
})