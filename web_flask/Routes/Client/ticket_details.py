#!/usr/bin/python3
from ...models import app
from flask_login import login_required
from flask import render_template, session, redirect, url_for
from flask_login import current_user
from ...models.user import Users
from ...models.tickets import Tickets
from .Functions.access_validation import client_acces_val

@app.route('/user/tickets/ver/<ticket_id>', methods=['GET'])
@login_required
def ver_ticket_user(ticket_id):
    if (current_user.Rol != 'Usuario'):
        return redirect(url_for(client_acces_val(current_user.Rol)))
    token = session.get('token')
    ticket = Tickets.query.get(ticket_id)
    owner = Users.query.get(ticket.User_ID)
    print('hola')
    print(ticket.to_dict())
    agent = Users.query.filter_by(id=ticket.Agent_ID).first()
    return render_template('Usuario/ticket_user.html', owner=owner, agent=agent, ticket=ticket, token=token)
