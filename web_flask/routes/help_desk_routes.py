#!/usr/bin/python3
from ..models import app
from ..functions.recover_account import recover_account_func
from ..functions.recover_pwd import recover_validations
from ..models.user import Users
from ..models.time_access import Time_Access
from ..models.forms.create_user import CreateUser
from ..models.forms.ticket import TicketForm
from flask import render_template
from flask_login import login_required
from flask_login import current_user


@app.route('/dashboard_HelpDesk', methods=['GET', 'POST'])
@login_required
def HelpDesk_Dashboard():
    ticket = TicketForm()

    return render_template('Agente_HelpDesk/dashboard_Agente_HelpDesk.html', ticket=ticket, name=current_user.Nombre, id=current_user.id)

@app.route('/user_list_HelpDesk', methods=['GET', 'POST'])
@login_required
def HelpDesk_User_list():
    form = CreateUser()
    return render_template('Agente_HelpDesk/administracion_usuario_HelpDesk.html', form=form)

@app.route("/registra_ticket_HelpDesk")
@login_required
def ticket_register_HeslpDesk():

    return render_template('Agente_HelpDesk/registra_ticket_HeslpDesk.html', user_id=current_user.id)

@app.route('/create_user_HelpDesk', methods=['GET', 'POST'] )
@login_required
def create_user_HelpDesk():
    form = CreateUser()
    return render_template('Agente_HelpDesk/crear_usuario_HelpkDesk.html', form=form)
