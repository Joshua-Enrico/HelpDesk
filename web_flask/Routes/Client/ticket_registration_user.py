#!/usr/bin/python3
from ...models import app
from flask_login import login_required
from flask import render_template
from flask_login import current_user



@app.route("/registra_ticket_usr")
@login_required
def ticket_register_usuario():
    return render_template('Usuario/registra_ticket_Usuario.html', user_id=current_user.id)
