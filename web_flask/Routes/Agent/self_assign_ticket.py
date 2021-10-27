#!/usr/bin/python3
from ...models import app
from flask_login import login_required
from flask import render_template, session, redirect, url_for, abort
from flask_login import current_user
from ...models.user import Users
from ...models.tickets import Tickets
from .Functions.access_validation import agent_acces_val

@app.route('/agent/assign-ticket/<ticket_id>', methods=['GET'])
@login_required
def agent_assign_ticket(ticket_id):
    if (current_user.Rol != 'Agente Helpdesk'):
        return redirect(url_for(agent_acces_val(current_user.Rol)))
    token = session.get('token')
    ticket = Tickets.query.get(ticket_id)
    if ticket is None:
        abort(404)
    owner = Users.query.filter_by(id=ticket.User_ID).first()
    agent = Users.query.filter_by(id=ticket.Agent_ID).first()
    return render_template('Agente_HelpDesk/asignarse_ticket.html', owner=owner, agent=agent, ticket=ticket, token=token, User_session_id=current_user.id)
