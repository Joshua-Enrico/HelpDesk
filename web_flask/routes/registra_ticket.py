#!/usr/bin/python3
from ..models import app
from flask_login import login_required
from flask import render_template
from flask_login import current_user

@app.route("/registra_ticket")
@login_required
def ticket_register():
    return render_template('registra_ticket.html')

@app.route("/registra_ticket_usr")
@login_required
def ticket_register_usuario():
    return render_template('Usuario/registra_ticket_Usuario.html', user_id=current_user.id)

@app.route("/registra_ticket_Amdin")
@login_required
def ticket_register_Administrador():

    return render_template('Administrador/registra_ticket_Administrador.html', user_id=current_user.id)