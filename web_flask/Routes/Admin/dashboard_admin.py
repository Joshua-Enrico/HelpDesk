#!/usr/bin/python3
from ...models import app
from ...models.forms.ticket import TicketForm
from flask_login import login_required
from flask import render_template, session
from flask_login import current_user
from ...models.user import Users
from ...models.tickets import Tickets


@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    ticket = TicketForm()
    token = session.get('token')
    return render_template('Administrador/dashboard_Admin.html', ticket=ticket, name=current_user.Nombre, id=current_user.id, token=token)


@app.route('/admin/tickets/editar/<ticket_id>', methods=['GET'])
@login_required
def editar_ticket(ticket_id):
    ticket = Tickets.query.get(ticket_id)
    owner = Users.query.get(ticket.User_ID)
    agent = Users.query.get(ticket.Agent_ID)
    return render_template('Administrador/ticket_admin_detalle.html', owner=owner, agent=agent, ticket=ticket)