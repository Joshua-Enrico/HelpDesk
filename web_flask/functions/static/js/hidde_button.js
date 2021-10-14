console.log('hey')
var hidden = true;
function action() {
    hidden = !hidden;
    if(hidden) {
        document.getElementById('togglee').style.visibility = 'hidden';
    } else {
        document.getElementById('togglee').style.visibility = 'visible';
    }
}