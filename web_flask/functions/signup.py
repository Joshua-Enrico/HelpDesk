#!/usr/bin/python3
from flask import Flask, render_template, redirect, url_for
from ..models.Class import *
from ..app import *
from flask_wtf import FlaskForm


def signup_validations():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_paswrd = generate_password_hash(form.password.data, method='sha256')
        user = Users.query.filter_by(Username=form.username.data).first()
        email = Users.query.filter_by(Email=form.email.data).first()
        user_id = Workers_ids.query.filter_by(User_id=form.user_id.data).first()
        if (user):
            return render_template('signup.html', form=form, user_in_use='El Usuario Ingresado Ya existe')
        if(email):
            return render_template('signup.html', form=form, email_in_use='El Correo Ingresado Ye exite')
        
        if(user_id):
            print(user_id)
            if (user_id.Used != 'used'):
                unique_id =  Workers_ids(User_id=form.user_id.data, Used='used')
            else:
                return render_template('signup.html', form=form, wrong_id='Este ID de trabajador ya esta en uso, verifique su ID')
        else:
            return render_template('signup.html', form=form, wrong_id='Id de trabajador incorrecto comuniquese con el administrador')

        token = s.dumps(form.email.data, salt='email-confirm')

        link = url_for('confirmed', token=token, user_id=form.user_id.data, _external=True)
        message = '\nTu link de confirmacion es: {}'.format(link) 
        print(message)
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login("helpdesk.notificacions@gmail.com", "vwwgjfvxxlwseqlz")
        server.sendmail("helpdesk.notificacions@gmail.com", form.email.data, message)

        new_user = Users(Username=form.username.data, Nombre=form.nombre.data, Apellido=form.apellido.data, Email=form.email.data, Password=hashed_paswrd, Admin=user_id.Admin, User_id=form.user_id.data, Confirmed_mail='No')
        update_user = Workers_ids.query.filter_by(User_id=form.user_id.data).update({'Used':'used'})

        db.session.add(new_user)
        db.session.commit()
        return render_template('signup.html', form=form, complete='Solo Falta un paso mas, Confirme Su correo')
    return render_template('signup.html', form=form)
