$(document).ready(function () {
    const User_id = ($(this).find('.panel-heading').data("id"));
    $.ajax({
        type: 'GET',
        url: 'http://localhost:5001/api/v1/agent_summary/' + User_id,
        headers: {'Authorization': 'Bearer ' + $('#token').val()},
        contentType: 'application/json',
        success: data => {
            let def = { All_tickets: 0,
                        Pendings: 0,
                        Assigned: 0,
                        Solved: 0}
            result = data[0] || def
            $("a[name=Complete]").text('Todos tus tickets: ' + result.All_tickets);
            $("a[name=Pending]").text('Tickets Pendientes: ' + result.Pendings);
            $("a[name=Asigned]").text('Todos Asignados: ' + result.Assigned);
            $("a[name=Solved]").text('Tickets Resueltos: ' + result.Solved);
        }
    });
});
