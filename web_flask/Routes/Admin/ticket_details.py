#!/usr/bin/python3
from ...models import app
from flask_login import login_required
from sqlalchemy import desc, asc
from flask import render_template, session, redirect, url_for, abort
from flask_login import current_user
from ...models.user import Users
from ...models.chat_history import chathistory
from ...models.tickets import Tickets
from .Functions.access_validation import admins_acces_val

@app.route('/admin/tickets/ver/<ticket_id>', methods=['GET'])
@login_required
def editar_ticket(ticket_id):
    flag = 0
    if (current_user.Rol != 'Administrador'):
        return redirect(url_for(admins_acces_val(current_user.Rol)))
    token = session.get('token')
    ticket = Tickets.query.get(ticket_id)
    if ticket is None:
        abort(404)
    owner = Users.query.filter_by(id=ticket.User_ID).first()
    agent = Users.query.filter_by(id=ticket.Agent_ID).first()
    messages = chathistory.query.filter_by(Ticket_id=ticket_id).order_by(asc(chathistory.DateTime))
    return render_template('Administrador/ticket_detalle.html',flag=flag,messages=messages, owner=owner, agent=agent, ticket=ticket, token=token, User_session_id=current_user.id)
