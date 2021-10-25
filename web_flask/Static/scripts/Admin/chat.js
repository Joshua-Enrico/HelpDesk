$(document).ready(function () {
    const socket = io.connect('http://localhost:5000/private')
    socket.on('private_chat', function (msg) {
      $('#messages').append('<article class="message is-info"><div class="message-header"><p>'+ User_names + '</p></div><div class="message-body">' + msg + '</div></article>')
    });
  });