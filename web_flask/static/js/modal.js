// Para que el script funcione  primero añade la 
// clase "open_modal" al elemento que quiere que se seleccione
const thisWindow = document.querySelector('.open_modal');
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