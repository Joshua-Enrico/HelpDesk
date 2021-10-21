#!/usr/bin/python3
from flask import Flask, render_template, redirect, url_for
from flask_wtf import FlaskForm

def recover_account_func(token, Email, password):
    try:
        email = s.loads(token, salt='recover', max_age=3600)
        update_user = Users.query.filter_by(Email=Email).update({'Confirmed_mail':'yes', 'Password': password})
        db.session.commit()
        return render_template('confirmed.html',predict_content="Recuperacion de cuenta Realizado, ya puedes ingresar al Sistema")
    except (BadSignature, SignatureExpired):
        return render_template('confirmed.html',predict_content="El Link de confirmacion ya expiro")