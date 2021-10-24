#!/usr/bin/python3
from ...models import app
from ...models.forms.create_user import CreateUser
from ...models.user import Users
from flask_login import login_required
from flask import render_template, redirect, url_for, session
from flask_login import current_user
from .Functions.access_validation import admins_acces_val

@app.route('/create_user', methods=['GET', 'POST'] )
def create_usr():
    if (current_user.Rol != 'Administrador'):
        return redirect(url_for(admins_acces_val(current_user.Rol)))
    token = session.get('token')
    form = CreateUser()
    return render_template('Administrador/crear_usuario.html', form=form, User_id=current_user.id, User_session_id=current_user.id, token=token)
