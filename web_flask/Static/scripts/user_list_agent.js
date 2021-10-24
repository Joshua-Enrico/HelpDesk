

$(document).ready(function () {

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
                    <a href="/user_edit_agent/${user.id}" class="dropdown-item">
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
