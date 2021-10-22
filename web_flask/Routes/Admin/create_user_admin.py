#!/usr/bin/python3
from ...models import app
from ...models.forms.create_user import CreateUser
from ...models.user import Users
from flask_login import login_required
from flask import render_template
from flask_login import current_user

@app.route('/create_user', methods=['GET', 'POST'] )

def create_usr():
    form = CreateUser()
    return render_template('Administrador/crear_usuario.html', form=form, User_id=current_user.id)
