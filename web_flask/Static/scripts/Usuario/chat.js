$(document).ready(function () {
    var User_id = ($(this).find('.chatbox').attr("data-id"))
    var Agent_id = ($(this).find('.agent_id').attr("data-id"))
    var User_names = ($(this).find('.user_id').attr("nombre"))
    var Agent_names = ($(this).find('.agent_id').attr("nombre"))
    var ticket_id = ($(this).find('.ticket_id').attr("ticket_id"))
    const socket = io.connect('http://localhost:5000/private');
    socket.emit('username', User_id)

    socket.on('private_chat', function (msg) {
      $('#messages').append('<article class="message is-info"><div class="message-header"><p>' + Agent_names + '</p></div><div class="message-body">' + msg + '</div></article>')
    });
    $('#send').on('click', function () {
      var msg = $('#myMessage').val();
      $('#messages').append('<article class="message is-info"><div class="message-header"><p>' + 'Tu' + '</p></div><div class="message-body">' + msg + '</div></article>')
      socket.emit('message', { 'user_id': User_id, 'message': msg, 'message_to': Agent_id , 'ticket_id':ticket_id})
      $('#myMessage').val('')
    });
  });