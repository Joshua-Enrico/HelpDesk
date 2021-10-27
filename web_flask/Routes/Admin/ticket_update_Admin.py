#!/usr/bin/python3
from ...models import app
from flask_login import login_required
from flask import render_template, redirect, url_for
from flask_login import current_user
from .Functions.access_validation import admins_acces_val
from flask import render_template, session
from ...models.user import Users
from ...models.tickets import Tickets


@app.route("/admin/tickets/editar/<ticket_id>")
@login_required
def ticket_update_Administrador(ticket_id):
    if (current_user.Rol != 'Administrador'):
        return redirect(url_for(admins_acces_val(current_user.Rol)))
    token = session.get('token')
    users = Users.query.filter_by(Rol='Usuario')
    agents = Users.query.filter_by(Rol='Agente Helpdesk')
    ticket = Tickets.query.get(ticket_id)
    return render_template('Administrador/actualiza_ticket.html',
                           User_id=current_user.id,
                           token=token,
                           users=users,
                           agents=agents,
                           ticket=ticket)
