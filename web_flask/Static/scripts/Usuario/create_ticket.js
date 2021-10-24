$(document).ready(function () {
    $('#create_ticket').submit(function (e) {
        e.preventDefault();
        var form = {
            'Subject': document.getElementById('Subject').value,
            'Problem_Type': document.getElementById('Problem_Type').value || null,
            'Priority': document.getElementById('Priority').value,
            'Description': document.getElementById('Description').value,
        }

        Object.keys(form).forEach(key => {
            $(`#err-${key}`).html('')
        })

        $.ajax({
            type: 'POST',
            data: JSON.stringify(form),
            url: 'http://localhost:5001/api/v1/user/tickets',
            headers: {'Authorization': 'Bearer ' + $('#token').val()},
            contentType: 'application/json; charset=utf-8',
            success: data => {
                window.location = `/user/tickets/ver/${data.id}`
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
