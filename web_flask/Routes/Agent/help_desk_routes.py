#!/usr/bin/python3
from ...models import app
from ...models.user import Users
from ...models.time_access import Time_Access
from ...models.forms.create_user import CreateUser
from ...models.forms.ticket import TicketForm
from .Functions.access_validation import agent_acces_val
from flask import render_template, redirect, url_for, session
from flask_login import login_required
from flask_login import current_user


@app.route('/dashboard_HelpDesk', methods=['GET', 'POST'])
@login_required
def HelpDesk_Dashboard():
    if (current_user.Rol != 'Agente Helpdesk'):
        return redirect(url_for(agent_acces_val(current_user.Rol)))
    ticket = TicketForm()
    token = session.get('token')
    return render_template('Agente_HelpDesk/dashboard_Agente_HelpDesk.html',User_session_id=current_user.id, token=token, ticket=ticket, name=current_user.Nombre, User_id=current_user.id)

@app.route('/user_list_HelpDesk', methods=['GET', 'POST'])
@login_required
def HelpDesk_User_list():
    if (current_user.Rol != 'Agente Helpdesk'):
        return redirect(url_for(agent_acces_val(current_user.Rol)))
    form = CreateUser()
    token = session.get('token')
    return render_template('Agente_HelpDesk/administracion_usuario_HelpDesk.html',User_session_id=current_user.id, token=token, form=form, User_id=current_user.id)

@app.route("/registra_ticket_HelpDesk")
@login_required
def ticket_register_HeslpDesk():
    if (current_user.Rol != 'Agente Helpdesk'):
        return redirect(url_for(agent_acces_val(current_user.Rol)))
    token = session.get('token')
    return render_template('Agente_HelpDesk/registra_ticket_HeslpDesk.html',User_session_id=current_user.id, token=token, User_id=current_user.id)

@app.route('/create_user_HelpDesk', methods=['GET', 'POST'] )
@login_required
def create_user_HelpDesk():
    if (current_user.Rol != 'Agente Helpdesk'):
        return redirect(url_for(agent_acces_val(current_user.Rol)))
    form = CreateUser()
    token = session.get('token')
    return render_template('Agente_HelpDesk/crear_usuario_HelpkDesk.html',User_session_id=current_user.id, token=token, form=form, User_id=current_user.id)
