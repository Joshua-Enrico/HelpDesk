var hidden = false;
const thisButton = document.querySelector('.btn-hide');
const thisContent = document.querySelector('.card-content');
const iconUp = document.querySelector('.fa-angle-up');
const iconDown = document.querySelector('.fa-angle-down');

thisButton.addEventListener('click', () =>  {
    hidden = !hidden;
    if(hidden) {
        thisContent.classList.add('is-hidden');
        iconUp.classList.add('is-hidden');
        iconDown.classList.remove('is-hidden');
        console.log(hidden);
    } else {
        thisContent.classList.remove('is-hidden');
        iconUp.classList.remove('is-hidden');
        iconDown.classList.add('is-hidden');
        console.log(hidden)
    }
});