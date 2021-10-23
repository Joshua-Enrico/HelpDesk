const burger = document.getElementById('navbar-burger');
burger.addEventListener('click', () => {
    burger.classList.toggle('is-active');
    document.getElementById(burger.dataset.target).classList.toggle('is-active');
});