#!/usr/bin/python3
from ...models import app
from flask_login import login_required
from flask import render_template, session, redirect, url_for, abort
from flask_login import current_user
from ...models.user import Users
from ...models.tickets import Tickets
from .Functions.access_validation import client_acces_val

@app.route('/user/rate_service/<ticket_id>', methods=['GET'])
@login_required
def user_rate_service(ticket_id):
    if (current_user.Rol != 'Usuario'):
        return redirect(url_for(client_acces_val(current_user.Rol)))
    token = session.get('token')
    ticket = Tickets.query.get(ticket_id)
    if ticket is None:
        abort(404)
    if ticket.User_ID != current_user.id:
        abort(403)
    owner = Users.query.get(ticket.User_ID)
    agent = Users.query.get(ticket.Agent_ID)
    return render_template('Usuario/rate_service.html', owner=owner, agent=agent, ticket=ticket, token=token)
