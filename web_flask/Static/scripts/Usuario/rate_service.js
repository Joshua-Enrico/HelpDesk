$(document).ready(function () {
    const ticketID = $('#ticket_id').val()

    $('#rate_service').submit(function (e) {
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
            url: `http://localhost:5001/api/v1/user/tickets/${ticketID}/rate_service`,
            headers: {'Authorization': 'Bearer ' + $('#token').val()},
            contentType: 'application/json; charset=utf-8',
            success: () => {
                window.location = `/dashboard_user`
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
