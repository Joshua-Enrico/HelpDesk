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
                'Desde': $("input[name=From]").val(),
                'Hasta': $("input[name=To]").val()}
    console.log(form)
    $.ajax({
      type: 'POST',
      data: JSON.stringify(form),
      url: 'http://localhost:5001/api/endpoints/users',
      contentType: 'application/json; charset=utf-8',
      success: data => {
        result = data;
        console.log(result);
        $('#User_Exists').html(result.User_Exists);
        $('#Email_Exist').html(result.Email_Exist);
        $('#Not_equal').html(result.Not_equal);
        $('#rol_validation').html(result.Rol_validation);
        $('#Area_validation').html(result.Area_validation);
        $('#wrong_date').html(result.Wrong_date);
        $('#user_created').html(result.complete);
      }
    });
});
    $.ajax({
        type: 'GET',
        url: 'http://localhost:5001/api/endpoints/users',
        contentType: 'application/json',
        success: data => {
          result = data;
          console.log(result);

        }
    });
});