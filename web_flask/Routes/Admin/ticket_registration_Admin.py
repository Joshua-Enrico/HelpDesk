#!/usr/bin/python3
from ...models import app
from flask_login import login_required
from flask import render_template, redirect, url_for
from flask_login import current_user
from .Functions.access_validation import admins_acces_val

@app.route("/registra_ticket_Amdin")
@login_required
def ticket_register_Administrador():
    if (current_user.Rol != 'Administrador'):
        return redirect(url_for(admins_acces_val(current_user.Rol)))
    return render_template('Administrador/registra_ticket_Administrador.html', User_id=current_user.id)