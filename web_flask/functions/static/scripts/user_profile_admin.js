$(document).ready(function () {

    const User_id = ($(this).find('.text-nowrap').data("id"));



    $('#update_user').submit(function (e) {
        e.preventDefault();
        var form = {
            'Nombre': $("input[name=name]").val(),
            'Apellido': $("input[name=Apellido_Usuario]").val(),
            'Username': $("input[name=username]").val(),
            'From': $("input[name=start-date]").val(),
            'To': $("input[name=end-date]").val(),
            'Email': $("input[name=correo]").val(),
            'Password': $("input[name=new_pswrd]").val(),
            'Confirm_Pasword': $("input[name=confirm_pswrd]").val(),
            'User_id': User_id,
        }
        console.log(form)
        $.ajax({
            type: 'PUT',
            data: JSON.stringify(form),
            url: 'http://localhost:5001/api/endpoints/users_profile',
            contentType: 'application/json; charset=utf-8',
            success: data => {
                result = data;
                console.log(result);
                //$('#complete').html(result.complete);
            }
        });
    });
});