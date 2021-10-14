$(document).ready(function () {
  var data = $("#create_user :input").serializeArray();
  console.log(data);
  $('#create_user').submit(function() {
    var data = $("#create_user :input").serializeArray();
    console.log(data);
});
    $.ajax({
        type: 'GET',
        url: 'http://localhost:5001/api/endpoints/users',
        contentType: 'application/json',
        success: data => {
            console.log(data);
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