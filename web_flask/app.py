#!/usr/bin/python3
from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_required, logout_user, current_user, login_user
import os
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
import pymysql
import smtplib
from .models.Class import *
from .functions.signup import *
from .functions.login import *
from .functions.recover_pwd import *
from .functions.confirmed import *
from .functions.recover_account import *
from .functions.admin_validations import Admin_validations
from .functions.user_administration import User_Administration
from datetime import datetime



@login_manager.user_loader
def load_user(User_id):
    return Users.query.get(str(User_id))



@app.route('/', methods=['GET', 'POST'])
def login():
    return login_validations()

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """ We call validation function where we have all render an validations to do"""
    return signup_validations()

@app.route('/recover', methods=['GET', 'POST'])
def recover_pwd():
    return recover_validations()

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    ticket = TicketForm()
    if ticket.validate_on_submit():
        New_Ticket = Tickets(User_ID=current_user.id, Subject=ticket.subject.data, Problem_Type=ticket.problemType.data, Company_Area=ticket.company_area.data, Description=ticket.description.data)
        db.session.add(New_Ticket)
        db.session.commit()
        summary = User_Tickets_Summary.query.filter_by(User_id=current_user.id).first()
        all_summary = Tickets_Summary.query.first()
        if (all_summary == None):
            obj = Tickets_Summary(All_tickets=0, Pendings=0, Solved=0, Assigned=0)
            db.session.add(obj)
            db.session.commit()


        if (summary == None):
            User_Summary =  User_Tickets_Summary(All_tickets=1, Pendings=1, Assigned=0, Solved=0, User_id=current_user.id)
            db.session.add(User_Summary)

            """ updating all summary """
            all_summary.All_tickets += 1
            all_summary.Pendings += 1
            all_summary.UpdateTime = datetime.now()

            db.session.commit()
        else:
            """ updating user summary table """
            summary.All_tickets +=  1
            summary.Pendings +=  1
            summary.UpdateTime = datetime.now()
            """ updating all summary table """
            all_summary.All_tickets += 1
            all_summary.Pendings += 1
            all_summary.UpdateTime = datetime.now()
            db.session.commit()

    return render_template('dashboard.html', ticket=ticket, name=current_user.Nombre, id=current_user.id)

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    return Admin_validations()

@app.route('/logout') 
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/confirm_email/<token>/<user_id>', methods=['GET', 'POST'] )
def confirmed(token, user_id):
    return  confirmed_func(token, user_id)


@app.route('/recover_acount/<token>/<Email>/<password>', methods=['GET', 'POST'] )
def recover_account(token, Email, password):
    return recover_account_func(token, Email, password)

@app.route("/registra_ticket")
@login_required
def ticket_registre():
    return render_template('registra_ticket.html')

@app.route("/administracion_usuario", methods=['GET', 'POST'])
def user_administration():

    return User_Administration()


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
    port = 5000
    app.run(host='0.0.0.0', port=port, threaded=True, debug=True)
