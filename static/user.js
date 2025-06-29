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