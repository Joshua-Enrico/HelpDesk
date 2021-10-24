#!/usr/bin/python3
from ...models import app
from flask_login import login_required
from ...models.forms.ticket import TicketForm
from .Functions.access_validation import client_acces_val
from flask import render_template, redirect, url_for, session
from flask_login import current_user

@app.route('/dashboard_user', methods=['GET', 'POST'])
@login_required
def dashboard_usuario():
    if (current_user.Rol != 'Usuario'):
        return redirect(url_for(client_acces_val(current_user.Rol)))
    ticket = TicketForm()
    token = session.get('token')
    return render_template('Usuario/dashboard_usuario.html', ticket=ticket, name=current_user.Nombre, User_id=current_user.id, token=token)
