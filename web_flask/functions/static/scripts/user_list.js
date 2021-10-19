

$(document).ready(function () {
    $.ajax({
        type: 'GET',
        data: JSON.stringify({}),
        url: 'http://localhost:5001/api/endpoints/users',
        contentType: 'application/json',
        success: data => {
            for (const user of data) {
                const template = `<tr>
                <th><input type="checkbox"></th>
                <th>001</th>
                <td>
                  <div class="media-left">
                    <figure class="image is-64x64">
                      <img src="https://bulma.io/images/placeholders/128x128.png" alt="Image">
                    </figure>
                  </div>
                </td>
                <td></td>
                <td>IT</td>
                <td>Administrador</td>
                <td>Activo</td>
                <td>
                  <a class="button">
                    <span class="icon is-small">
                      <i class="fa fa-ellipsis-v "></i>
                    </span>
                  </a>
                </td>
              </tr>`;
                $('tbody.User-info').append(template);
            }
        },
    });

    $("div#wrapper").Grid({

        columns: [{ name: 'Selecciona'},
            'Nombre y Apellido',
            'Area', 'Rol',
            'Estado',
        { name: 'Acciones', formatter: (cell) => gridjs.html("<a class='button'><span class='icon is-small'><i class='fa fa-ellipsis-v'></i></span></a>")}],
        search: true,
        pagination: {
            limit: 10
        },
        language: {
            'search': {
                'placeholder': '🔍 Buscar...'
            },
            'pagination': {
                'previous': '⬅️',
                'next': '➡️',
                'results': () => 'Records'
            }
        },
        sort: true,
        resizable: true,
        server: {
            url: 'http://localhost:5001/api/endpoints/users',
            then: data => data.map(user =>
                [gridjs.html(`<input data-id=${ user.id } type="checkbox"></input>`), user.Nombre + ' ' + user.Apellido, user.Area, user.Rol, user.Estado,'']
            )
        },
        className: {
            table: 'table is-striped'

        }
    });

});