const thisWindow = document.querySelector('#this_window');
const modalBg = document.querySelector('.modal-background')
const closeBtn = document.querySelector('.delete')
const modal = document.querySelector('.modal')

thisWindow.addEventListener('click', () =>  {
    modal.classList.add('is-active');
});

modalBg.addEventListener('click', () =>  {
    modal.classList.remove('is-active');
});

closeBtn.addEventListener('click', () =>  {
    modal.classList.remove('is-active');
});