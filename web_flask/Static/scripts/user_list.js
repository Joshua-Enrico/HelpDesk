

$(document).ready(function () {
  // $.ajax({
  //     type: 'GET',
  //     data: JSON.stringify({}),
  //     url: 'http://localhost:5001/api/v1/users',
  //     headers: {'Authorization': 'Bearer ' + $('#token').val()},
  //     contentType: 'application/json',
  //     success: data => {
  //         for (const user of data) {
  //             const template = `<tr>
  //             <th><input type="checkbox"></th>
  //             <th>001</th>
  //             <td>
  //               <div class="media-left">
  //                 <figure class="image is-64x64">
  //                   <img src="https://bulma.io/images/placeholders/128x128.png" alt="Image">
  //                 </figure>
  //               </div>
  //             </td>
  //             <td></td>
  //             <td>IT</td>
  //             <td>Administrador</td>
  //             <td>Activo</td>
  //             <td>
  //               <a class="button">
  //                 <span class="icon is-small">
  //                   <i class="fa fa-ellipsis-v "></i>
  //                 </span>
  //               </a>
  //             </td>
  //           </tr>`;
  //             $('tbody.User-info').append(template);
  //         }
  //     },
  // });

    $("div#wrapper").Grid({

        columns: [{ name: 'Selecciona'},
            'Nombre y Apellido',
            'Area', 'Rol',
            'Estado',
        { name: 'Acciones'}],
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
            url: 'http://localhost:5001/api/v1/users',
            headers: {'Authorization': 'Bearer ' + $('#token').val()},
            then: data => data.map(user =>
                [gridjs.html(`<input data-id=${ user.id } type="checkbox"></input>`), user.Nombre + ' ' + user.Apellido, user.Area, user.Rol, user.Estado,

                gridjs.html(`<div class="dropdown is-hoverable">
                <div class="dropdown-trigger">
                  <button class="button" aria-haspopup="true" aria-controls="dropdown-menu">
                    <span>🔘</span>
                    <span class="icon is-small">
                      <i class="fas fa-angle-down" aria-hidden="true"></i>
                    </span>
                  </button>
                </div>
                <div class="dropdown-menu" id="dropdown-menu" role="menu">
                  <div class="dropdown-content">
                    <a href="/user_edit/${user.id}" class="dropdown-item">
                      Editar Usuario
                    </a>
                    <a href="#" class="dropdown-item is-hoverable">
                      Chat con El usuario
                    </a>
                    <hr class="dropdown-divider">
                    <a href="#" class="dropdown-item">
                      Desactivar Usuario
                    </a>
                  </div>
                </div>
              </div>`)]
            )
        },
        className: {
            table: 'table is-striped'
        }
    });
});
