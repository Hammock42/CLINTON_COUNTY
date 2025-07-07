var navItems = document.querySelectorAll('.desktop-nav .nav-item');
var navEl = document.getElementById('main-navbar');

window.addEventListener('scroll', function() {
    if (window.scrollY > 100) {
        navEl.classList.add('bg-light');
        navEl.classList.remove('bg-grad');
        navItems.forEach(function(item) {
            item.classList.add('nav-item-scroll');
            item.classList.remove('nav-item-no-scroll');
        });
    } else {
        navEl.classList.add('bg-grad');
        navEl.classList.remove('bg-light');
        navItems.forEach(function(item) {
            item.classList.add('nav-item-no-scroll');
            item.classList.remove('nav-item-scroll');
        });
    }
});

document.addEventListener('DOMContentLoaded', function() {
    const navItems = document.querySelectorAll('.desktop-nav .nav-item.dropdown');
    const navElRect = navEl.getBoundingClientRect();

    navItems.forEach(item => {
        const dropdownMenu = item.querySelector('.dropdown-menu');
        const rect = item.getBoundingClientRect();
        const offsetLeft = navElRect.left - rect.left;
        const offsetTop = navElRect.bottom - rect.top - 10;

        dropdownMenu.style.left = `${offsetLeft}px`;
        dropdownMenu.style.top = `${offsetTop}px`;

        item.addEventListener('mouseover', function() {
            if (dropdownMenu) {
                dropdownMenu.classList.add('show');
            }
        });

        item.addEventListener('mouseout', function() {
            if (dropdownMenu) {
                dropdownMenu.classList.remove('show');
            }
        });

        const navLink = item.querySelector('.nav-link');
        navLink.addEventListener('click', function(event) {
            const href = this.getAttribute('href');
            if (href && href !== '#') {
                window.location.href = href;
            }
        });
    });
});