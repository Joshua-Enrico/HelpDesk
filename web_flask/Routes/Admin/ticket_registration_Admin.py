#!/usr/bin/python3
from ...models import app
from flask_login import login_required
from flask import render_template, redirect, url_for
from flask_login import current_user
from .Functions.access_validation import admins_acces_val
from flask import render_template, session
from ...models.user import Users


@app.route("/registra_ticket_Admin")
@login_required
def ticket_register_Administrador():
    if (current_user.Rol != 'Administrador'):
        return redirect(url_for(admins_acces_val(current_user.Rol)))
    token = session.get('token')
    users = Users.query.filter(Users.Rol == 'Usuario')
    return render_template('Administrador/registra_ticket_Administrador.html', User_id=current_user.id, token=token, users=users)
