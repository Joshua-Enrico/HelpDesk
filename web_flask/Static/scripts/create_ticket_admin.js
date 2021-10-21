$(document).ready(function () {
    const User_id = ($(this).find('.hero-body').data("id"));
    console.log(User_id)
    console.log('hola')
    $('#create_ticket').submit(function (e) {
        e.preventDefault();
        var form = {
            'subject': (document.getElementById('subject').value),
            'User_id': User_id,
            'problemType': (document.getElementById('problemType').value),
            'company_area': (document.getElementById('company_area').value),
            'description': (document.getElementById('description').value),
        }
        console.log(form)
        $.ajax({
            type: 'POST',
            data: JSON.stringify(form),
            url: 'http://localhost:5001/api/endpoints/admin/tickets',
            contentType: 'application/json; charset=utf-8',
            success: data => {
                result = data;
                console.log(result);
                $('#complete').html(result.complete);
            }
        });
    });
});
