$(document).ready(function () {
    var Agent_id = ($(this).find('.agent_id').attr("data-id"))
    var User_id = ($(this).find('.user_id').attr("data-id"))
    var User_names = ($(this).find('.user_id').attr("nombre"))
    var Agent_names = ($(this).find('.agent_id').attr("nombre"))
    var ticket_id = ($(this).find('.ticket_id').attr("ticket_id"))
    const socket = io.connect('http://localhost:5000/private')
    socket.emit('ticket_agent', ticket_id)
    socket.on(ticket_id, function (msg) {
      $('#messages').append('<article class="message is-info"><div class="message-header"><p>'+ User_names + '</p></div><div class="message-body">' + msg + '</div></article>')
    });
    $('#send').on('click', function () {
      var msg = $('#myMessage').val();
      $('#messages').append('<article class="message is-info"><div class="message-header"><p>' + 'Tu' + '</p></div><div class="message-body">' + msg + '</div></article>')
      socket.emit('message_agent', { 'user_id': Agent_id, 'message': msg, 'message_to': User_id , 'ticket_id': ticket_id})
      $('#myMessage').val('')
    });
  });
