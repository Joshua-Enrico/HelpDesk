$(document).ready(function () {
  $('#create_user').submit(function(e) {
    e.preventDefault();
    var form = [];
    form.push(document.getElementById('Username').value);
    form.push(document.getElementById('Email').value);
    form.push(document.getElementById('Nombre').value);
    form.push(document.getElementById('Apellido').value);
    form.push(document.getElementById('Password').value);
    form.push(document.getElementById('Confirmed_Password').value);
    form.push(document.getElementById('Area').value);
    form.push(document.getElementById('Rol').value);
    form.push(document.getElementById('Desde').value);
    form.push(document.getElementById('Hasta').value);
    var form = {'Username': (document.getElementById('Username').value),
                'Email':(document.getElementById('Email').value),
                'Apellido':(document.getElementById('Apellido').value),
                'Password':(document.getElementById('Password').value),
                'Confirmed_Password':(document.getElementById('Confirmed_Password').value),
                'Area':(document.getElementById('Area').value),
                'Rol':(document.getElementById('Rol').value),
                'Desde':(document.getElementById('Desde').value),
                'Hasta':(document.getElementById('Hasta').value)}
    console.log(form)
    $.ajax({
      type: 'POST',
      data: JSON.stringify(form),
      url: 'http://localhost:5001/api/endpoints/users',
      contentType: 'application/json; charset=utf-8',
      success: data => {
        console.log(data);
      }
    });
});
    $.ajax({
        type: 'GET',
        url: 'http://localhost:5001/api/endpoints/users',
        contentType: 'application/json',
        success: data => {
            for (const user of data) {
                const template = `<tr>
                <th>001</th>
                <td>
                  <div class="media-left">
                    <figure class="image is-64x64">
                      <img src="https://bulma.io/images/placeholders/128x128.png" alt="Image">
                    </figure>
                  </div>
                </td>
                <td>${ user.Nombre } ${ user.Apellido }</td>
                <td>${ user.Area } IT</td>
                <td>${ user.Rol}</td>
                <td>${ user.Estado }</td>
                <td>
                  <a class="button">
                    <span class="icon is-small">
                      <i class="fa fa-ellipsis-v "></i>
                    </span>
                  </a>
                </td>
              </tr>`;
                $('tbody.users').append(template);
            }

        }
    });
});