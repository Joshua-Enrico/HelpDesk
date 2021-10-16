#!/usr/bin/python3
from ..models import app
from ..models.forms.ticket import TicketForm
from flask_login import login_required
from flask import render_template
from flask_login import current_user

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    ticket = TicketForm()

    return render_template('Administrador/dashboard_Admin.html', ticket=ticket, name=current_user.Nombre, id=current_user.id)
