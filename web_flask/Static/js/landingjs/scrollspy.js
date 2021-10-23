const navItems = document.getElementById('menubar').firstElementChild.children,
    navSections = new Array(navItems.length);
for (i = 0; i < navItems.length; i++)
    navSections[i] = document.getElementById(navItems[i].dataset.target);

const menuBarHeight = document.getElementById('menubar').offsetHeight;
function isVisible(ele) {
    const r = ele.getBoundingClientRect();
    const h = (window.innerHeight || document.documentElement.clientHeight);
    const w = (window.innerWidth || document.documentElement.clientWidth);
    return (r.top <= h) && 
        (r.top + r.height - menuBarHeight >= 0) && 
        (r.left <= h) && 
        (r.left + r.width >= 0);
}
function activateIfVisible() {
    for (b = true, i = 0; i < navItems.length; i++) {
        if (b && isVisible(navSections[i])) {
            navItems[i].classList.add('is-active');
            b = false;
        } else 
            navItems[i].classList.remove('is-active');
    }
}
var isTicking = null;
window.addEventListener('scroll', () => {
    if (!isTicking) {
        window.requestAnimationFrame(() => {
            activateIfVisible();
            isTicking = false;
        });
        isTicking = true;
    }
}, false);