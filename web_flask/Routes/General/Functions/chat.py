from datetime import datetime
from ....models import app, socketio, db
from ....models.chat_history import chathistory
from flask_socketio import SocketIO, send, emit
from flask import Flask, request
users = {}

@socketio.on('username', namespace='/private')
def handleMessage(username):
    users[username] = request.sid

@socketio.on('message', namespace='/private')
def handleMessage(msg):

    flag = 0
    message = chathistory(Ticket_id=msg['ticket_id'], User_ID=msg['user_id'], message=msg['message'])
    db.session.add(message)
    db.session.commit()
    try:
        user_id = msg['message_to']
        user_id = users[user_id]
    except  KeyError:
        flag = 1
    if(flag == 0):
        emit('private_chat', msg['message'], room=user_id)

@socketio.on('message_agent', namespace='/private')
def handleMessage_agent(msg):
    flag = 0
    message = chathistory(Ticket_id=msg['ticket_id'], Agent_ID=msg['user_id'], message=msg['message'])
    db.session.add(message)
    db.session.commit()
    try:
        user_id = msg['message_to']
        user_id = users[user_id]
    except  KeyError:
        flag = 1
    if(flag == 0):
        emit('private_chat', msg['message'], room=user_id)
