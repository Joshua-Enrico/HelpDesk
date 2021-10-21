$(document).ready(function () {
    $('#update_user').bootstrapValidator();
    const User_id = ($(this).find('.text-nowrap').data("id"));



    $('#update_user').submit(function (e) {
        e.preventDefault();
        var Nombre = $("input[name=name]").val()


        $("input[name=name]").removeClass("is-invalid");
        var form = {
            'Nombre': Nombre,
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
                $("p[name=User_exists]").text(result.User_Exists);
                if(result.User_Exists != ''){
                    $("input[name=username]").addClass("is-invalid");
                } else{
                    $("input[name=username]").removeClass("is-invalid");
                }
                $("p[name=Wrong_name]").text(result.Wrong_name);
                if(result.Wrong_name != ''){
                    $("input[name=name]").addClass("is-invalid");
                } else{
                    $("input[name=name]").removeClass("is-invalid");
                }
                $("p[name=Wrong_last]").text(result.wrong_last);
                if(result.wrong_last != ''){
                    $("input[name=Apellido_Usuario]").addClass("is-invalid");
                } else{
                    $("input[name=Apellido_Usuario]").removeClass("is-invalid");
                }
                $("p[name=Wrong_From]").text(result.Wrong_From);
                if(result.Wrong_From != ''){
                    $("input[name=start-date]").addClass("is-invalid");
                } else{
                    $("input[name=start-date]").removeClass("is-invalid");
                }
                $("p[name=Wrong_to]").text(result.Wrong_To);
                if(result.Wrong_To != ''){
                    $("input[name=end-date]").addClass("is-invalid");
                } else{
                    $("input[name=end-date]").removeClass("is-invalid");
                }
                $("p[name=Wrong_to]").text(result.Wrong_date);
                if(result.Wrong_date != '' && (result.Wrong_From === '' && result.Wrong_To === '')){
                    $("input[name=start-date]").addClass("is-invalid");
                    $("input[name=end-date]").addClass("is-invalid");
                }
                $("p[name=Email_Exists]").text(result.Email_Exist);
                if(result.Email_Exist != ''){
                    $("input[name=correo]").addClass("is-invalid");
                } else{
                    $("input[name=correo]").removeClass("is-invalid");
                }
                $("p[name=Not_equal]").text(result.Not_equal);
                if(result.Not_equal != ''){
                    $("input[name=new_pswrd]").addClass("is-invalid");
                    $("input[name=confirm_pswrd]").addClass("is-invalid");
                } else{
                    $("input[name=new_pswrd]").removeClass("is-invalid");
                    $("input[name=confirm_pswrd]").removeClass("is-invalid");
                }
                if(result.flag == 0){
                    location.reload();
                }
            }
        });
    });
});
