#!/usr/bin/python3
from flask import Flask, render_template, redirect, url_for
from ..models.Class import *
from ..app import *
from flask_wtf import FlaskForm

def recover_validations():
    form = recover()
    if form.validate_on_submit():
        user = Users.query.filter_by(Email=form.email.data).first()
        if (user == None):
            return render_template('recover_account.html', form=form, wrong_email='El Correo No Existe')
        if (user.User_id == None or user.User_id != form.user_id.data):
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