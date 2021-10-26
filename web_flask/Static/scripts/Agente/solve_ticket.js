$(document).ready(function () {
    const ticketID = $('#ticket_id').val()

    $('#solve_ticket').submit(function (e) {
        e.preventDefault();
        let form = {
            'Service_Score': $('#Service_Score').val()
        }

        Object.keys(form).forEach(key => {
            $(`#err-${key}`).html('')
        })

        $.ajax({
            type: 'PUT',
            data: JSON.stringify(form),
            url: `http://localhost:5001/api/v1/agent/tickets/${ticketID}/solve`,
            headers: {'Authorization': 'Bearer ' + $('#token').val()},
            contentType: 'application/json; charset=utf-8',
            success: () => {
                window.location = `/dashboard_HelpDesk`
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
