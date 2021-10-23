$(document).ready(function () {
    const User_id = ($(this).find('.hero-body').data("id"));

    $('#create_ticket').submit(function (e) {
        e.preventDefault();
        var form = {
            'Subject': document.getElementById('Subject').value,
            'User_ID': document.getElementById('User_ID').value,
            'Problem_Type': document.getElementById('ProblemType').value,
            'Company_Area': document.getElementById('CompanyArea').value,
            'Description': document.getElementById('Description').value,
        }

        $.ajax({
            type: 'POST',
            data: JSON.stringify(form),
            url: 'http://localhost:5001/api/v1/admin/tickets',
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
