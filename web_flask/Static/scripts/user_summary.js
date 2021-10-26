$(document).ready(function () {
    console.log($('#token').val())
    const User_id = ($(this).find('.container').data("id"));
    $.ajax({
        type: 'GET',
        url: 'http://localhost:5001/api/v1/user_summary/' + User_id,
        headers: {'Authorization': 'Bearer ' + $('#token').val()},
        contentType: 'application/json',
        success: data => {
            for (const summary of data) {
                const template = `<ul class="nav nav-stacked">
                <li><a href="#">Todos <span class="pull-right badge bg-blue">${ summary.All_tickets }</span></a></li>
                <li><a href="#">Pendientes <span class="pull-right badge bg-aqua">${ summary.Pendings }</span></a></li>
                <li><a href="#">Asignados <span class="pull-right badge bg-green">${ summary.Assigned }</span></a></li>
                <li><a href="#">Resueltos <span class="pull-right badge bg-red">${ summary.Solved }</span></a></li>
              </ul>`;
                $('div.box-footer').append(template);
            }
        }
    });
});
