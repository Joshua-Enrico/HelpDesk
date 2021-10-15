$(document).ready(function () {
  $('#create_user').submit(function(e) {
    e.preventDefault();
    var form = {'Username': (document.getElementById('Username').value),
                'Email':(document.getElementById('Email').value),
                'Apellido':(document.getElementById('Apellido').value),
                'Password':(document.getElementById('Password').value),
                'Nombre':(document.getElementById('Nombre').value),
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
        result = data;
        console.log(result);
        $('#User_Exists').html(result.User_Exists);
        $('#Email_Exist').html(result.Email_Exist);
        $('#Not_equal').html(result.Not_equal);
        $('#rol_validation').html(result.Rol_validation);
        $('#Area_validation').html(result.Area_validation);
        $('#wrong_date').html(result.Wrong_date);
        $('#user_created').html(result.complete);
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