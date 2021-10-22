$(document).ready(function () {
  $('.box').submit(function(e) {
    e.preventDefault();
    var form = {'Username': $("input[name=id-name]").val(),
                'Email': $("input[name=user-email]").val(),
                'Nombre': $("input[name=nombre]").val(),
                'Apellido': $("input[name=apellido]").val(),
                'Password': $("input[name=pswrd]").val(),
                'Confirmed_Password': $("input[name=confirm-paswrd]").val(),
                'Area': $("select[name=Area]").val(),
                'Rol': $("select[name=ROL]").val(),
                'Desde': $("input[name=date-start]").val(),
                'Hasta': $("input[name=date-end]").val()}
    console.log(form)
    $.ajax({
      type: 'POST',
      data: JSON.stringify(form),
      url: 'http://localhost:5001/api/v1/users',
      contentType: 'application/json; charset=utf-8',
      success: data => {
        result = data;
        console.log(result);
        $("p[name=user_exists]").text(result.User_Exists);
        if(result.User_Exists !=''){
          $("input[name=id-name]").addClass("is-danger");
        } else{
          $("input[name=id-name]").removeClass("is-danger");
        }
        $("p[name=Email_Exist]").text(result.Email_Exist);
        if(result.Email_Exist !=''){
          $("input[name=user-email]").addClass('is-danger')
        } else {
          $("input[name=user-email]").removeClass('is-danger')
        }
        $("p[name=Not_equal]").text(result.Not_equal);
        if(result.Not_equal !=''){
          $("input[name=pswrd]").addClass('is-danger')
          $("input[name=confirm-paswrd]").addClass('is-danger')
        } else {
          $("input[name=pswrd]").removeClass('is-danger')
          $("input[name=confirm-paswrd]").removeClass('is-danger')
        }

        $("p[name=wrong_date]").text(result.Wrong_date);
        if(result.Wrong_date !='') {
          $("input[name=date-start]").addClass('is-danger')
          $("input[name=date-end]").addClass('is-danger')
        } else {
          $("input[name=date-start]").removeClass('is-danger')
          $("input[name=date-end]").removeClass('is-danger')
        }

        $("p[name=complete]").text(result.complete);
      }
    });
});

});