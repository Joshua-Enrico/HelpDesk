#!/usr/bin/python3
from ...models import app
from flask_login import login_required
from flask import render_template, session, redirect, url_for
from flask_login import current_user
from ...models.user import Users
from ...models.tickets import Tickets
from .Functions.access_validation import admins_acces_val

@app.route('/admin/tickets/ver/<ticket_id>', methods=['GET'])
@login_required
def editar_ticket(ticket_id):
    if (current_user.Rol != 'Administrador'):
        return redirect(url_for(admins_acces_val(current_user.Rol)))
    token = session.get('token')
    ticket = Tickets.query.get(ticket_id)
    owner = Users.query.get(ticket.User_ID)
    agent = Users.query.get(ticket.Agent_ID)
    return render_template('Administrador/ticket_detalle.html', owner=owner, agent=agent, ticket=ticket, token=token)
