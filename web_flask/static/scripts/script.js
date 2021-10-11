$(document).ready(function () {
    $.ajax({
        type: 'GET',
        url: 'http://172.18.201.15:5001/api/endpoints/users',
        contentType: 'application/json',
        success: data => {
            console.log(data);
            for (const user of data) {
                const template = `<tr>
            <td>
              <img src="https://bootdey.com/img/Content/user_1.jpg" alt="">
              <a href="#" class="user-link">Full name 1</a>
              <span class="user-subhead">Member</span>
            </td>
            <td>2013/08/12</td>
            <td class="text-center">
              <span class="label label-default">pending</span>
            </td>
            <td>
              <a href="#">${ user.Email }</a>
            </td>
            <td style="width: 20%;">
              <a href="#" class="table-link text-warning">
                <span class="fa-stack">
                  <i class="fa fa-square fa-stack-2x"></i>
                  <i class="fa fa-search-plus fa-stack-1x fa-inverse"></i>
                </span>
              </a>
              <a href="#" class="table-link text-info">
                <span class="fa-stack">
                  <i class="fa fa-square fa-stack-2x"></i>
                  <i class="fa fa-pencil fa-stack-1x fa-inverse"></i>
                </span>
              </a>
              <a href="#" class="table-link danger">
                <span class="fa-stack">
                  <i class="fa fa-square fa-stack-2x"></i>
                  <i class="fa fa-trash-o fa-stack-1x fa-inverse"></i>
                </span>
              </a>
            </td>
          </tr>`;
                $('section.users').append(template);
            }

        }
    });
});