#!/usr/bin/python3
from ...models import app
from flask_login import login_required
from sqlalchemy import desc, asc
from flask import render_template, session, redirect, url_for
from flask_login import current_user
from ...models.user import Users
from ...models.chat_history import chathistory
from ...models.tickets import Tickets
from .Functions.access_validation import client_acces_val

@app.route('/user/tickets/ver/<ticket_id>', methods=['GET'])
def ver_ticket_user(ticket_id):
    flag = 0
    if (current_user.Rol != 'Usuario'):
        return redirect(url_for(client_acces_val(current_user.Rol)))
    token = session.get('token')
    ticket = Tickets.query.get(ticket_id)
    owner = Users.query.get(ticket.User_ID)
    agent = Users.query.filter_by(id=ticket.Agent_ID).first()
    messages = chathistory.query.filter_by(Ticket_id=ticket_id).order_by(asc(chathistory.DateTime))
    try:
        print(messages[0])
    except  IndexError:
        flag = 1
    return render_template('Usuario/ticket_user.html',flag=flag, messages=messages, owner=owner, agent=agent, ticket=ticket, token=token, User_id=current_user.id)
