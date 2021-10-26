$(document).ready(function () {

    $.ajax({
        type: 'GET',
        url: 'http://localhost:5001/api/v1/admin/tickets/summary',
        headers: {'Authorization': 'Bearer ' + $('#token').val()},
        contentType: 'application/json',
        success: data => {
            $("a[name=Complete]").text('Todos tus tickets: ' + result.All_tickets);
            $("a[name=Pending]").text('Tickets Pendientes: ' + result.Pendings);
            $("a[name=Asigned]").text('Todos Asignados: ' + result.Assigned);
            $("a[name=Solved]").text('Tickets Resueltos: ' + result.Solved);
        }
    });
});
