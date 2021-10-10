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
from Class import *
from functions.signup import *
from functions.login import *
from functions.recover_pwd import *
from functions.confirmed import *
from functions.recover_account import *



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

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.nombre)

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
