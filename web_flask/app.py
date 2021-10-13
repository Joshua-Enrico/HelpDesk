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
from datetime import datetime   



@login_manager.user_loader
def load_user(User_id):
    return Users.query.get(int(User_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
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
    form = CreateID()
    if form.validate_on_submit():
        user_id = Workers_ids.query.filter_by(User_id=form.user_id.data).first()
        if (user_id):
            return render_template('admin.html', form=form, wrong_id='EL ID ya existe')
        else:
            new_user = Workers_ids(User_id=form.user_id.data, Used='false', Admin=form.admin.data)
            db.session.add(new_user)
            db.session.commit()
            return render_template('admin.html', form=form, complete='ID Creado Correctamente')
    return render_template('admin.html', form=form)

@app.route('/logout') 
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/confirm_email/<token>/<user_id>', methods=['GET', 'POST'] )
def confirmed(token, user_id):
    return  confirmed_func(token, user_id)


@app.route('/recover_acount/<token>/<user_id>/<password>', methods=['GET', 'POST'] )
def recover_account(token, user_id, password):
    return recover_account_func(token, user_id, password)


if __name__ == '__main__':
    app.run(debug=True)
