from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager, UserMixin, login_required, logout_user, current_user, login_user
import os
from itsdangerous import URLSafeTimedSerializer
import pymysql
import smtplib
from .Class import *

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if (user.confirmed_mail != "yes"):
                return render_template('login.html', predict_content='Correo No confirmado', form=form)
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                if (user.admin == 'yes'):
                    return redirect(url_for('admin'))
                else:
                    return redirect(url_for('dashboard'))
        return render_template('login.html', predict_content='Contraseña o usuario incorrecto', form=form)
    return render_template('login.html', form=form)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_paswrd = generate_password_hash(form.password.data, method='sha256')
        user = User.query.filter_by(username=form.username.data).first()
        email = User.query.filter_by(email=form.email.data).first()
        user_id = User_id.query.filter_by(user_id=form.user_id.data).first()
        if (user):
            return render_template('signup.html', form=form, user_in_use='El Usuario Ingresado Ya existe')
        if(email):
            return render_template('signup.html', form=form, email_in_use='El Correo Ingresado Ye exite')
        
        if(user_id):
            if (user_id.used != 'used'):
                unique_id = User_id(user_id=form.user_id.data, used='used')
            else:
                return render_template('signup.html', form=form, wrong_id='Este ID de trabajador ya esta en uso, verifique su ID')
        else:
            return render_template('signup.html', form=form, wrong_id='Id de trabajador incorrecto comuniquese con el administrador')

        token = s.dumps(form.email.data, salt='email-confirm')

        link = url_for('confirmed', token=token, user_id=form.user_id.data ,  _external=True)
        message = '\nTu link de confirmacion es: {}'.format(link) 
        print(message)
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login("helpdesk.notificacions@gmail.com", "vwwgjfvxxlwseqlz")
        server.sendmail("helpdesk.notificacions@gmail.com", form.email.data, message)

        new_user = User(username=form.username.data, nombre=form.nombre.data, apellido=form.apellido.data, email=form.email.data, password=hashed_paswrd, admin=user_id.admin, user_id=form.user_id.data, confirmed_mail='No')
        update_user = User_id.query.filter_by(user_id=form.user_id.data).update({'used':'used'})

        db.session.add(new_user)
        db.session.commit()
        return render_template('signup.html', form=form, complete='Solo Falta un paso mas, Confirme Su correo')
    return render_template('signup.html', form=form)

@app.route('/recover', methods=['GET', 'POST'])
def recover_pwd():
    form = recover()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if (user == None):
            return render_template('recover_account.html', form=form, wrong_email='El Correo No Existe')
        if (user.user_id == None or user.user_id != form.user_id.data):
            return render_template('recover_account.html', form=form, wrong_id='El ID de usuario no existe, o no concuerda con el suyo')
        hashed_paswrd = generate_password_hash(form.new_password.data, method='sha256')
        token = s.dumps(form.email.data, salt='recover')

        link = url_for('recover_account', token=token, user_id=form.user_id.data , password=hashed_paswrd,  _external=True)
        message = '\nTu link de confirmacion es:  {}'.format(link) 
        print(message)
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login("helpdesk.notificacions@gmail.com", "vwwgjfvxxlwseqlz")
        server.sendmail("helpdesk.notificacions@gmail.com", form.email.data, message)
        user.confirmed_mail = "Recovering"
        db.session.commit()
        return render_template('recover_account.html', form=form, complete='Ya casi listo, Solo necesita confirmar su correo')


    return render_template('recover_account.html', form=form)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.nombre)

@app.route('/admin', methods=['GET', 'POST'])
@login_required
def admin():
    form = CreateID()
    if form.validate_on_submit():
        user_id = User_id.query.filter_by(user_id=form.user_id.data).first()
        if (user_id):
            return render_template('admin.html', form=form, wrong_id='EL ID ya existe')
        else:
            new_user = User_id(user_id=form.user_id.data, used='false', admin=form.admin.data)
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
    print(user_id)
    try:
        email = s.loads(token, salt='email-confirm', max_age=3600)
        update_user = User.query.filter_by(user_id=user_id).update({'confirmed_mail':'yes'})
        print(update_user)
        db.session.commit()
        return render_template('confirmed.html',predict_content="Email Confirmado Ya puede ingresar al Sistema")
    except SignatureExpired:
        return render_template('confirmed.html',predict_content="El Link de confirmacion ya expiro")


@app.route('/recover_acount/<token>/<user_id>/<password>', methods=['GET', 'POST'] )
def recover_account(token, user_id, password):
    print(user_id)
    try:
        email = s.loads(token, salt='recover', max_age=3600)
        update_user = User.query.filter_by(user_id=user_id).update({'confirmed_mail':'yes', 'password': password})
        db.session.commit()
        return render_template('confirmed.html',predict_content="Recuperacion de cuenta Realizado, ya puedes ingresar al Sistema")
    except SignatureExpired as Error:
        return render_template('confirmed.html',predict_content="El Link de confirmacion ya expiro")

if __name__ == '__main__':
    app.run(debug=True)
