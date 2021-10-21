const panels = document.querySelectorAll('.panel-tabs a');
// const panelContentBoxes = document.querySelectorAll('#tab-content > div');

panels.forEach((tab) => {
    tab.addEventListener('click', () => {
        panels.forEach(item => item.classList.remove('is-active'))
        tab.classList.add('is-active');
        
        const target = tab.dataset.target;
        // console.log(target);
    })
})

