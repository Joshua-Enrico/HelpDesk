#!/usr/bin/python3
from ...models import app
from ...models.forms.create_user import CreateUser
from flask_login import login_required
from flask import render_template, session
from flask_login import current_user
import datetime
import uuid

@app.route("/administracion_usuario/", methods=['GET', 'POST'])
@login_required
def User_Administration():
    form = CreateUser()
    token = session.get('token')
    return render_template('Administrador/administracion_usuario.html', form=form, User_id=current_user.id, token=token)
