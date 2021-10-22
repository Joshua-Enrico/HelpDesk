#!/usr/bin/python3
from ...models import app
from flask_login import login_required
from flask import render_template, session
from flask_login import current_user
from ...models.user import Users


@app.route("/registra_ticket_Amdin")
@login_required
def ticket_register_Administrador():
    token = session.get('token')
    users = Users.query.filter(Users.Rol == 'Usuario')
    return render_template('Administrador/registra_ticket_Administrador.html', User_id=current_user.id, token=token, users=users)
