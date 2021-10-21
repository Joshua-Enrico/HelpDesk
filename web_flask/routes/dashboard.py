#!/usr/bin/python3
from ..models import app
from flask_login import login_required
from ..models.forms.ticket import TicketForm
from flask import render_template
from flask_login import current_user
from ..models.tickets import Tickets
from ..models import db
from ..models.user_tickets_summary import User_Tickets_Summary
from ..models.tickets_summary import Tickets_Summary
from datetime import datetime

@app.route('/dashboard_user', methods=['GET', 'POST'])
@login_required
def dashboard_usuario():
    ticket = TicketForm()

    return render_template('Usuario/dashboard_usuario.html', ticket=ticket, name=current_user.Nombre, id=current_user.id)
