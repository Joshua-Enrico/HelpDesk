#!/usr/bin/python3
from flask import render_template, redirect, url_for
from werkzeug.security import check_password_hash
from ....models.forms.login import LoginForm
from ....models.user import Users
from ....models.time_access import Time_Access
from flask_login import login_user
from datetime import datetime
import datetime as nowdate

def login_validations():
    form = LoginForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(Username=form.username.data).first()
        if user:
            check_acces = Time_Access.query.filter_by(User_id=user.id).first()
            now = datetime.now()
            if(user.Rol != 'Administrador'):
                if(now >= check_acces.To):
                    return render_template('login.html', predict_content='Acceso Al Sistema Denegado, contacte a un administrador', form=form)
            if check_password_hash(user.Password, form.password.data):
                login_user(user, remember=form.remember.data)
                if (user.Rol == 'Administrador'):
                    return redirect(url_for('admin'))
                elif(user.Rol == 'Agente Helpdesk'):
                    return redirect(url_for('HelpDesk_Dashboard'))
                else:
                    return redirect(url_for('dashboard_usuario'))
        return render_template('General/login.html', predict_content='Contraseña o usuario incorrecto', form=form)
    return render_template('General/login.html', form=form)
