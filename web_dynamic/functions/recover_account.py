#!/usr/bin/python3
from flask import Flask, render_template, redirect, url_for
from Class import *
from app import *
from flask_wtf import FlaskForm

def recover_account_func():
    try:
        email = s.loads(token, salt='recover', max_age=3600)
        update_user = Users.query.filter_by(User_id=user_id).update({'Confirmed_mail':'yes', 'Password': password})
        db.session.commit()
        return render_template('confirmed.html',predict_content="Recuperacion de cuenta Realizado, ya puedes ingresar al Sistema")
    except (BadSignature, SignatureExpired):
        return render_template('confirmed.html',predict_content="El Link de confirmacion ya expiro")