const menuIcon = document.querySelector('.menu-hamburger');
const profileIcon = document.querySelector('.profile-menu');
const navbar = document.querySelector('.menu-navbar');
const profileNavbar = document.querySelector('.menu-navbar-right');

menuIcon.addEventListener('click', () => {
  navbar.classList.toggle('change')
});

profileIcon.addEventListener('click', () => {
  profileNavbar.classList.toggle('change-right')
});