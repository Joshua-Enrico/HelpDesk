#!/usr/bin/python3
from ...models import app
from ...models.forms.create_user import CreateUser
from .Functions.access_validation import admins_acces_val
from flask_login import login_required
from flask import render_template, session, redirect, url_for
from flask_login import current_user
import datetime
import uuid

@app.route("/administracion_usuario/", methods=['GET', 'POST'])
@login_required
def User_Administration():
    if (current_user.Rol != 'Administrador'):
        return redirect(url_for(admins_acces_val(current_user.Rol)))
    form = CreateUser()
    token = session.get('token')
    return render_template('Administrador/administracion_usuario.html', User_session_id=current_user.id,form=form, User_id=current_user.id, token=token)
