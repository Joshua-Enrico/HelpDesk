from datetime import datetime
from ....models import app, socketio, db
from ....models.chat_history import chathistory
from flask_socketio import SocketIO, send, emit
from flask import Flask, request
users = {}
ticket_agent = {}
ticket_user = {}

@socketio.on('ticket_user', namespace='/private')
def handleMessage(ticket_id):
    try:
        ticket_user[ticket_id].append(request.sid)
    except KeyError:
        ticket_user[ticket_id] = [request.sid]

@socketio.on('ticket_agent', namespace='/private')
def handleMessage(ticket_id):
    try:
        ticket_agent[ticket_id].append(request.sid)
    except KeyError:
        ticket_agent[ticket_id] = [request.sid]


@socketio.on('message', namespace='/private')
def handleMessage(msg):

    flag = 0
    message = chathistory(Ticket_id=msg['ticket_id'], User_ID=msg['user_id'], message=msg['message'])
    db.session.add(message)
    db.session.commit()
    try:
        user_id = msg['ticket_id']
        user_id = ticket_agent[user_id]
    except  KeyError:
        flag = 1
    if(flag == 0):
        emit(msg['ticket_id'], msg['message'], room=user_id)

@socketio.on('message_agent', namespace='/private')
def handleMessage_agent(msg):
    flag = 0
    message = chathistory(Ticket_id=msg['ticket_id'], Agent_ID=msg['user_id'], message=msg['message'])
    db.session.add(message)
    db.session.commit()
    try:
        user_id = msg['ticket_id']
        user_id = ticket_user[user_id]
    except  KeyError:
        flag = 1
    if(flag == 0):
        emit(msg['ticket_id'], msg['message'], room=user_id)

@socketio.on('disconnect', namespace='/private')
def disconnect():
    key_to_del = ''
    flag_user = 0
    flag_agent = 0
    flag = 0
    for key in ticket_user:
        for val in ticket_user[key]:
            if val == request.sid:
                ticket_user[key].remove(request.sid)
                if len(ticket_user[key]) == 0:
                    key_to_del = key
                    flag_user = 1
                flag = 1
    if flag_user == 1:
        del ticket_user[key_to_del]

    if flag == 0:
            for key in ticket_agent:
                for val in ticket_agent[key]:
                    if val == request.sid:
                        ticket_agent[key].remove(request.sid)
                        if len(ticket_agent[key]) == 0:
                            key_to_del = key
                            flag_agent = 1
    if flag_agent == 1:
        del ticket_agent[key_to_del]


