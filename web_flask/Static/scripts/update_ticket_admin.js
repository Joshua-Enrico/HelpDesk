$(document).ready(function () {
    const ticketID = $('#ticket-id').val()

    $('#update_ticket').submit(function (e) {
        e.preventDefault();
        var form = {
            'Subject': document.getElementById('Subject').value,
            'User_ID': document.getElementById('User_ID').value,
            'Agent_ID': document.getElementById('Agent_ID').value || null,
            'Problem_Type': document.getElementById('ProblemType').value,
            'Company_Area': document.getElementById('CompanyArea').value,
            'Description': document.getElementById('Description').value
        }


        $.ajax({
            type: 'PUT',
            data: JSON.stringify(form),
            url: `http://localhost:5001/api/v1/admin/tickets/${ticketID}`,
            headers: {'Authorization': 'Bearer ' + $('#token').val()},
            contentType: 'application/json; charset=utf-8',
            success: data => {
                window.location = `/admin/tickets/ver/${data.id}`
            },
            error: err => {
                resp = (err && err.responseJSON) || {}
                Object.entries(resp).forEach(([key, val]) => {
                    $(`#err-${key}`).html(val)
                })
            }
        });
    });
});
