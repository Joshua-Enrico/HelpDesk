$(document).ready(function () {
    $('#create_ticket').submit(function (e) {
        e.preventDefault();
        var form = {
            'Subject': document.getElementById('Subject').value,
            'User_ID': document.getElementById('User_ID').value,
            'Problem_Type': document.getElementById('ProblemType').value,
            'Description': document.getElementById('Description').value,
        }

        Object.keys(form).forEach(key => {
            $(`#err-${key}`).html('')
        })

        $.ajax({
            type: 'POST',
            data: JSON.stringify(form),
            url: 'http://localhost:5001/api/v1/admin/tickets',
            headers: {'Authorization': 'Bearer ' + $('#token').val()},
            contentType: 'application/json; charset=utf-8',
            success: () => window.location = `/admin`,
            error: err => {
                resp = (err && err.responseJSON) || {}
                Object.entries(resp).forEach(([key, val]) => {
                    $(`#err-${key}`).html(val)
                })
            }
        });
    });
});
