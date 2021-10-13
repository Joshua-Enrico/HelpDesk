#!/usr/bin/python3
from flask import Flask, render_template, redirect, url_for
from ..models.Class import *
from ..app import *
from flask_wtf import FlaskForm

def login_validations():
    form = LoginForm()
    print(form.username.data)
    if form.validate_on_submit():
        print("hereee")
        user = Users.query.filter_by(Username=form.username.data).first()
        if user:
            if (user.Confirmed_mail != "yes"):
                return render_template('login1.html', predict_content='Correo No confirmado', form=form)
            if check_password_hash(user.Password, form.password.data):
                login_user(user, remember=form.remember.data)
                if (user.Admin == 'yes'):
                    return redirect(url_for('admin'))
                else:
                    return redirect(url_for('dashboard'))
        return render_template('login1.html', predict_content='Contraseña o usuario incorrecto', form=form)
    return render_template('login1.html', form=form)
