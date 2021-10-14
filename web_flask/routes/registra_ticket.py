#!/usr/bin/python3
from ..models import app
from flask_login import login_required
from flask import render_template

@app.route("/registra_ticket")
@login_required
def ticket_register():
    return render_template('registra_ticket.html')