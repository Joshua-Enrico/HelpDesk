#!/usr/bin/python3
from ...models import app
from flask_login import login_required, current_user
from flask import render_template, redirect, url_for
from .Functions.access_validation import client_acces_val



@app.route("/registra_ticket_usr")
@login_required
def ticket_register_usuario():
    if (current_user.Rol != 'Usuario'):
        return redirect(url_for(client_acces_val(current_user.Rol)))
    return render_template('Usuario/registra_ticket_Usuario.html', User_id=current_user.id)
