#!/usr/bin/python3
from ...models import app
from ...models.forms.ticket import TicketForm
from flask_login import login_required
from flask import render_template, session, redirect, url_for
from flask_login import current_user
from ...models.user import Users
from ...models.tickets import Tickets
from .Functions.access_validation import admins_acces_val

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    if (current_user.Rol != 'Administrador'):
        return redirect(url_for(admins_acces_val(current_user.Rol)))
    ticket = TicketForm()
    token = session.get('token')
    return render_template('Administrador/dashboard_Admin.html', ticket=ticket, name=current_user.Nombre, User_id=current_user.id, token=token, User_session_id=current_user.id)


@app.route('/admin/tickets/ver/<ticket_id>', methods=['GET'])
@login_required
def editar_ticket(ticket_id):
    if (current_user.Rol != 'Administrador'):
        return redirect(url_for(admins_acces_val(current_user.Rol)))
    token = session.get('token')
    ticket = Tickets.query.get(ticket_id)
    owner = Users.query.get(ticket.User_ID)
    agent = Users.query.get(ticket.Agent_ID)
    return render_template('Administrador/ticket_detalle.html', owner=owner, agent=agent, ticket=ticket, token=token, User_session_id=current_user.id)
